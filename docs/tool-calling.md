
---

# `docs/tool-calling.md`

This should explain the **AI/tool integration**, which is a major selling point of your project.

```markdown
# AI Tool Calling

## 1. Overview

The Stargate AI/NOC platform uses controlled tool calling to allow
the language model to request specific network diagnostics.

The model does not receive unrestricted operating-system access.

---

# 2. Available Tools

The diagnostic framework provides:

```text
ping()
dns_lookup()
check_tcp_port()
traceroute()