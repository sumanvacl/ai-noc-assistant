# RAG Knowledge Base Example

## Objective

Demonstrate how the AI assistant can combine a knowledge base with live diagnostic information.

## Example Knowledge

A sanitized knowledge-base entry might contain:

```text
Topic: PPPoE Authentication Failure

Common symptoms:
- PPPoE session does not establish
- Username/password authentication fails
- ONU may remain online
- Customer may report "no Internet"

Initial checks:
1. Verify the customer account status.
2. Check ONU/router status.
3. Verify PPPoE credentials.
4. Check whether the authentication server is reachable.
5. Review relevant logs if available.
```

## User Request

```text
A customer cannot connect using PPPoE.
What should I check?
```

## Knowledge Retrieval

The RAG system retrieves the relevant knowledge-base entry.

The assistant can then produce a structured response:

```text
Start with these checks:

1. Confirm the customer account is active.
2. Check ONU/router status.
3. Verify the PPPoE username and password.
4. Check whether the authentication service is reachable.
5. Review authentication logs if available.

Do not immediately assume the password is incorrect.
```

## Combining RAG and Tools

The architecture can combine:

```text
Knowledge Base
      |
      v
Expected troubleshooting procedure
      |
      +
      |
      v
Diagnostic Tool
      |
      v
Live network evidence
      |
      v
AI-generated conclusion
```

For example:

```text
RAG says:
"Check reachability of the authentication service."

Tool reports:
"TCP connection successful."

AI conclusion:
"The authentication service is reachable, so investigate
credentials, account status, authentication logs, or session state."
```

## Knowledge Priority

The intended priority is:

```text
1. Internal knowledge base
2. Live read-only diagnostic results
3. Approved authoritative external documentation
4. General technical knowledge
```

The assistant should not invent organization-specific information when the knowledge base does not contain it.

## Production vs GitHub

The public repository should contain:

* Sanitized procedures
* Generic examples
* Documentation
* Example configurations
* Test data

It should not contain:

* Production customer records
* Passwords
* API tokens
* SSH keys
* Private certificates
* Production database files
* Private network topology
* Confidential IP allocation information
* Production backups

The public examples are intended to demonstrate the engineering architecture without exposing operational secrets.
