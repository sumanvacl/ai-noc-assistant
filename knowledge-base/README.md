# Stargate AI NOC Knowledge Base

This directory contains the technical knowledge used by the
Stargate AI/NOC Engineering Assistant.

## Purpose

The knowledge base provides structured technical information for:

- ISP customer support
- Network troubleshooting
- NOC operations
- Router and switch troubleshooting
- OLT/ONU troubleshooting
- DNS troubleshooting
- Connectivity diagnostics
- Network monitoring
- Internal operational procedures

## Knowledge Priority

The AI should use information in the following order:

1. Current internal knowledge base
2. Live read-only diagnostic results
3. Approved authoritative external documentation
4. General technical knowledge

Production network information must not be guessed.

## Security

This repository must never contain:

- Passwords
- API keys
- SSH private keys
- Customer information
- VPN credentials
- Database files
- Production configuration backups
- Private certificates
- Confidential network diagrams

Production-specific information should be replaced with
sanitized examples before publication to GitHub.

## Document Format

Knowledge documents should use:

- Clear headings
- Problem descriptions
- Symptoms
- Diagnostic steps
- Expected results
- Possible causes
- Recommended actions
- Escalation conditions

## Example

A troubleshooting document should generally follow:

Problem
→ Symptoms
→ Initial checks
→ Diagnostics
→ Possible causes
→ Resolution
→ Escalation
