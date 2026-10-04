# Network Troubleshooting Methodology

## Objective

Use a structured troubleshooting process to identify the
most likely cause of a network problem.

## Principle

Do not immediately change configuration.

First:

1. Understand the problem.
2. Collect facts.
3. Perform read-only diagnostics.
4. Compare observed results with expected behavior.
5. Identify likely causes.
6. Recommend the safest next action.

## Standard Workflow

```text
Problem
   |
   v
Collect Symptoms
   |
   v
Check Physical Layer
   |
   v
Check Local Connectivity
   |
   v
Check IP Configuration
   |
   v
Check DNS
   |
   v
Check TCP Connectivity
   |
   v
Check Latency / Packet Loss
   |
   v
Check Route
   |
   v
Determine Likely Cause
   |
   v
Recommend Action
