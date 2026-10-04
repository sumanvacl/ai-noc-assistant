# AI-Assisted Troubleshooting Example

## Scenario

A support engineer reports:

```text
A customer says that a website is not opening.
```

The AI assistant should not immediately assume the cause.

Instead, it follows a structured troubleshooting process.

## Step 1 — Clarify the Problem

Example:

```text
Is the problem affecting only one website or all websites?
```

Assume the answer is:

```text
Only one website.
```

## Step 2 — DNS Test

The assistant performs:

```text
dns_lookup(target)
```

Possible result:

```text
DNS resolution successful.
```

This indicates that the hostname can be resolved.

## Step 3 — TCP Test

The assistant checks HTTPS:

```text
check_tcp_port(target, 443)
```

Possible result:

```text
TCP port 443 reachable.
```

This indicates that a TCP connection can be established.

## Step 4 — Path Test

The assistant can perform:

```text
traceroute(target)
```

This provides additional routing information.

## Step 5 — Reasoning

The assistant now has several observations:

```text
DNS resolution       -> Successful
TCP 443 connectivity -> Successful
Network path         -> Available
```

Therefore, the assistant should avoid claiming:

```text
"The Internet connection is broken."
```

Instead, it should state something such as:

```text
Basic DNS and TCP connectivity to the destination are working.

The problem may be at the HTTP/application layer, destination server,
TLS negotiation, browser, or application-specific level.

Further application-layer testing is required.
```

## Troubleshooting Model

The general workflow is:

```text
User Complaint
      |
      v
Clarify Symptom
      |
      v
DNS
      |
      v
TCP Connectivity
      |
      v
Routing / Path
      |
      v
Application Layer
      |
      v
Evidence-Based Conclusion
```

## Engineering Principle

The AI should distinguish between:

```text
CONFIRMED
```

and:

```text
POSSIBLE
```

Example:

```text
CONFIRMED:
DNS resolution succeeded.

CONFIRMED:
TCP/443 connection succeeded.

POSSIBLE:
The problem may be application-layer related.

NOT CONFIRMED:
The remote web application is down.
```

This prevents the assistant from presenting assumptions as facts.
