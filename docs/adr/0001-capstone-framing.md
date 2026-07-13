# ADR-0001: Capstone Framing - Python Knowledge Assistant

- **Status:** Draft v1
- **Date:** 2026-07-13
- **Author:** Sethuraman Kannan

## Context

Many beginner and intermediate Python learners struggle to find precise answers inside the official Python documentation because the documentation is accurate but broad and dense. This capstone will build a grounded Q&A assistant over 20 selected official Python documentation pages, so users can ask Python learning questions and receive concise answers with source-grounded citations.

## Decision - Solution Framing Canvas

| Box | My Answer |
|-----|-------------|
| **Inputs** | The user sends a question related to Python in Plain English. Eg: "What is the use of `finally` in a `try-catch` block?" |
| **Outputs** | The system returns a concise answer in plain English, plus citations from the corpus |
| **Tools** | In v1, the system uses the OpenAI API for generation, and later weeks will add a vector store over the corpus. |
| **Memory** | The system has no memory across sessions in v1; each question is treated independently. |
| **Autonomy level** | The system is a grounded Q&A assistant, not an autonomous agent. |
| **Decision boundaries** | The system will explain Python concepts from the selected documentation, but it should say it is unsure when the question is outside the corpus. |

## Consequences

- **Positive:** The corpus is official, public, stable, HTML-based and easy to chunk without OCR.
- **Positive:** The assistant can help users navigate Python concepts faster while staying grounded in trusted documentation.
- **Positive:** The framework is simple and explanatory for W1, and also naturally capable of scaling to RAG / Agentic tooling later |

- **Negative / risks:** No memory implies context is lost between question sessions.
- **Negative / risks:** The assistant may over-answer from general model knowledge unless citations and retrieval boundaries are enforced.

- **Things we'll re-visit:** Chunking strategy and citation quality will be revisited when retrieval is introduced.
- **Things we'll re-visit:** Multi-turn memory and agentic behavior will be revisited after the basic Q&A system is reliable.