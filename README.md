# ShopAssist – LLM Cost Optimization

**An optimization project focused on reducing Large Language Model (LLM) inference costs in a customer support automation system.**

## Overview

ShopAssist is a customer support assistant that processes customer tickets and determines the most appropriate support action based on customer messages, order information, and knowledge-base articles.

The system classifies tickets into four possible actions:

- `REFUND`
- `REPLACE`
- `SEND_ARTICLE`
- `ESCALATE_TIER2`

The objective of this project is to optimize LLM usage by reducing unnecessary prompt tokens, minimizing redundant processing, and improving the efficiency of the support workflow.

## Project Objectives

- Reduce token consumption and LLM processing costs.
- Optimize prompts without losing essential instructions.
- Generate structured JSON responses.
- Reduce redundant LLM calls and unnecessary context.
- Evaluate token usage and cost using the provided billing simulator.

## Problem Statements

### Question 1 – Single-Call Optimization

Optimize the customer support assistant to process each ticket using a single LLM call while keeping the output within the specified cost budget.

**Optimization approach:**
- Simplify system instructions.
- Remove unnecessary prompt content.
- Avoid redundant information.
- Use structured JSON output.
- Preserve the required order snapshot in the prompt.

**Target:** 3,000 points or less per ticket.

### Question 2 – Multi-Stage Workflow Optimization

Optimize the original four-stage support workflow:

1. **Triage:** Understand the customer's issue.
2. **Retrieve:** Identify relevant knowledge-base information.
3. **Compose:** Prepare the support decision and response.
4. **Audit:** Verify the final decision.

The optimization focuses on reducing repeated context, unnecessary processing, and redundant LLM calls.

**Target:** 2,500 points or less per ticket.

## Cost Model

The project uses a simulated LLM billing system with the following pricing:

| Token Type | Cost |
|---|---:|
| Normal input token | 3 points |
| Cached input token | 0.3 points |
| Output token | 15 points |

Output tokens are five times more expensive than normal input tokens, making prompt and response optimization important.

## Tech Stack

- **Language:** Python
- **LLM:** Local LLM simulator
- **Tokenization:** tiktoken
- **Testing:** pytest
- **Version Control:** Git and GitHub

## Project Structure

```text
shopassist-llm-cost-optimization/
│
├── data/
│   ├── kb/                 # Knowledge-base articles
│   ├── orders/             # Order information
│   └── tickets/            # Customer support tickets
│
├── question1/
│   ├── agent.py            # Single-call optimized agent
│   ├── run.py              # Execution script
│   └── README.md
│
├── question2/
│   ├── agent.py            # Multi-stage workflow optimization
│   ├── run.py              # Execution script
│   └── README.md
│
├── shared/
│   ├── billing.py          # Cost calculation
│   ├── kb.py               # Knowledge-base utilities
│   ├── llm.py              # LLM simulator
│   ├── tokens.py           # Token counting utilities
│   └── tools.py            # Shared tools
│
├── tests/                  # Automated tests
├── questions/              # Assignment problem statements
├── eval/                   # Evaluation utilities
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Riya-negi02/shopassist-llm-cost-optimization.git
```

### 2. Navigate to the project directory

```bash
cd shopassist-llm-cost-optimization
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run Question 1

```bash
python question1/run.py
```

### 5. Run Question 2

```bash
python question2/run.py
```

## Testing

Run the test suite using:

```bash
python -m pytest -q
```

The baseline-cost tests are designed to check that the original implementation has high costs. After optimization, these particular baseline assertions may fail because the optimized cost is below the expected baseline threshold. Review the remaining tests and actual cost measurements separately.

## Key Learning Outcomes

Through this project, the following concepts are explored:

- LLM prompt engineering and optimization
- Tokenization and token-cost calculation
- Structured model outputs
- Efficient context management
- Multi-stage LLM workflow optimization
- Automated testing and performance evaluation
- Git-based project management

## Future Improvements

- Implement and verify prompt caching.
- Compare token usage before and after optimization.
- Improve knowledge-base retrieval.
- Evaluate decision accuracy across different ticket types.
- Further reduce unnecessary output tokens.

## Acknowledgement

This project was developed as part of an LLM cost optimization internship assignment. The implementation is based on the provided assignment materials and starter project.
