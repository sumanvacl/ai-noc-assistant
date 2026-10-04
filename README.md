# Stargate AI NOC Engineering Platform

An on-premises AI-assisted Network Operations and IT Support platform
developed and deployed for real-world NOC/IT operations.

## Overview

This project integrates:

- Ollama
- Qwen 3.5 9B
- Open WebUI
- Retrieval-Augmented Generation (RAG)
- Internal technical knowledge bases
- Controlled AI tool calling
- Network diagnostics
- DNS troubleshooting
- TCP connectivity testing
- Traceroute
- Backup and disaster recovery
- Role-based operational workflow

## Architecture

```text
                    Users
                      |
                      v
               +--------------+
               |  Open WebUI  |
               +--------------+
                      |
              +-------+-------+
              |               |
              v               v
        Knowledge Base     AI Tools
              |               |
              v               v
             RAG          Diagnostics
              |               |
              +-------+-------+
                      |
                      v
                Ollama
                      |
                      v
                 Qwen 3.5 9B