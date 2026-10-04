# Troubleshooting Case Studies

## Case 1 — Ollama Context Overflow

### Symptom

Tool calls failed with:

5677 tokens > 4096 context

### Investigation

Open WebUI logs were inspected.

### Root Cause

The configured Ollama context was insufficient for
the Open WebUI prompt + tool schema + conversation.

### Resolution

The context configuration was increased to 8192.

### Result

Native tool calling successfully executed.

---

## Case 2 — Open WebUI Memory/Title Generation

### Symptom

Background title generation generated:

KeyError: 'model'

### Investigation

Open WebUI middleware and memory capability handling
were inspected.

### Root Cause

The background task could provide the model as a string
rather than the expected metadata dictionary.

### Resolution

The model capability handling was made compatible with
string model identifiers.

### Result

Title generation completed without the previous exception.