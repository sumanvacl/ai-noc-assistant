# Security Policy

This project is designed around least-privilege,
read-only network diagnostics.

The AI diagnostic tools must not provide arbitrary
shell execution.

Production credentials, private keys, customer data,
and confidential network configuration are excluded
from this repository.

Diagnostic tools use:

- input validation
- command allowlists
- execution timeouts
- restricted parameters
- read-only operations