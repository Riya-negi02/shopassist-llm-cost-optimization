from __future__ import annotations

import json
from dataclasses import dataclass

from shared.billing import CostSession
from shared.kb import title_index
from shared.llm import ChatMessage, LlmClient
from shared.tools import format_thread, get_order, get_ticket

from question1.agent import parse_resolution


@dataclass
class TicketResolution:
    action: str
    kb_article: str


class SupportPipeline:
    """Optimized pipeline for Question 2 — collapsed to a single node."""

    def __init__(self, session: CostSession | None = None):
        self.session = session or CostSession()
        self.llm = LlmClient(self.session)
        # We only load the titles. This avoids the 200,000-token bloated help center.
        self.titles = title_index(500)

    def handle_ticket(self, ticket_id: str) -> TicketResolution:
        ticket = get_ticket(ticket_id)
        order = get_order(ticket["order_id"])
        thread = format_thread(ticket)
        snapshot = json.dumps(order, indent=2)

        # The system prompt is 100% static across all runs to enable caching.
        # title_index(500) is long enough to hit the >1024 token minimum for the cache discount.
        messages = [
            ChatMessage(
                "system",
                "\n\n".join(
                    [
                        "You are ShopAssist, the Tier-1 customer support copilot.",
                        "ARTICLE TITLES:",
                        self.titles,
                        "Instructions: Output JSON only with exactly three keys: action, kb_article, and customer_reply. Do not include any other text."
                    ]
                ),
            ),
            ChatMessage(
                "user",
                f"TICKET_ID: {ticket_id}\nTHREAD:\n{thread}\nORDER_SNAPSHOT:\n{snapshot}\nEND_SNAPSHOT",
            ),
        ]
        
        # A single LLM call replaces the 4-node pipeline
        completion = self.llm.chat("handle_ticket", messages)
        parsed = parse_resolution(completion)
        return TicketResolution(parsed.action, parsed.kb_article)