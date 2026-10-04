# System Architecture

## 1. Overview

The Stargate AI/NOC Engineering Platform is an on-premises AI-assisted
IT and Network Operations platform.

The system combines:

- Local Large Language Model inference
- Open WebUI
- Retrieval-Augmented Generation (RAG)
- Technical knowledge bases
- Controlled network diagnostic tools
- Linux and Docker infrastructure
- Backup and recovery procedures

The objective is to provide technical support personnel with an AI
assistant capable of retrieving approved technical knowledge and
performing controlled read-only network diagnostics.

---

## 2. High-Level Architecture

```text
                         NOC / IT Users
                               |
                               v
                     +-------------------+
                     |    Open WebUI     |
                     |     TCP/8080      |
                     +---------+---------+
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
        +----------------+          +----------------+
        | Knowledge Base |          |  AI Tool Calls |
        |      / RAG     |          +-------+--------+
        +--------+-------+                  |
                 |                          |
                 +------------+-------------+
                              |
                              v
                     +----------------+
                     |     Ollama     |
                     |    TCP/11434   |
                     +-------+--------+
                             |
                             v
                       Qwen LLM Model
                             |
                             v
                   AI-generated response