
---

# `docs/backup-and-recovery.md`

```markdown
# Backup and Recovery

## 1. Objective

The AI/NOC platform must be recoverable after:

- Container failure
- Configuration error
- Host failure
- Accidental deletion
- Software upgrade problems
- Database corruption

---

# 2. What Should Be Backed Up

Important components include:

```text
Open WebUI persistent data
Docker configuration
Open WebUI image definition
Ollama configuration
Deployment files
Knowledge-base source files
Diagnostic tools
Operational scripts
Documentation