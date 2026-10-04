# DNS Lookup Example

## Objective

Demonstrate DNS troubleshooting using the AI assistant's controlled DNS diagnostic function.

## User Request

```text
Check the DNS records for example.com.
```

## AI Tool Selection

The assistant selects:

```text
dns_lookup(hostname)
```

Example argument:

```text
hostname = example.com
```

## Tool Execution

The diagnostic tool performs an A-record lookup.

Example command:

```bash
nslookup -type=A -timeout=5 -retry=1 example.com
```

## Example Result

A result may look similar to:

```text
Name:    example.com
Address: 93.184.216.34
```

The exact result can change and should always be treated as live information.

## AI Interpretation

Example:

```text
DNS resolution is working.

example.com successfully returned an IPv4 address.

This indicates that the configured DNS resolver was able to resolve the hostname.
```

## Troubleshooting Use

DNS testing can help distinguish between:

```text
Application problem
        |
        +-- DNS resolution failure
        |
        +-- TCP connectivity failure
        |
        +-- HTTP/application failure
```

For example:

```text
Hostname does not resolve
        |
        v
Investigate DNS

Hostname resolves
        |
        v
Check TCP connectivity
```

## Safety

The DNS diagnostic:

* Accepts a hostname
* Validates the input
* Uses a fixed DNS query type
* Uses a timeout
* Does not modify DNS configuration
* Does not execute arbitrary commands
