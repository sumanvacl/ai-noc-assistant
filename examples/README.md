# Examples

This directory contains sanitized examples demonstrating how the AI-assisted NOC platform can be used for network diagnostics, troubleshooting, and knowledge-based support.

The examples are designed for demonstration, training, testing, and portfolio purposes.

> **Security notice:** All examples use public or documentation-safe targets. No production IP addresses, customer information, credentials, private topology, or confidential configuration should be committed to this repository.

## Examples

| Example                                                | Purpose                                        |
| ------------------------------------------------------ | ---------------------------------------------- |
| [Ping Diagnostic](ping-example.md)                     | Test IPv4 reachability and latency             |
| [DNS Lookup](dns-example.md)                           | Verify DNS resolution                          |
| [TCP Port Check](tcp-port-example.md)                  | Test whether a TCP service is reachable        |
| [Traceroute](traceroute-example.md)                    | Identify the network path toward a destination |
| [Troubleshooting Workflow](troubleshooting-example.md) | Demonstrate AI-assisted troubleshooting        |
| [RAG Knowledge Example](rag-knowledge-example.md)      | Demonstrate knowledge-base-assisted answers    |

## Architecture

The examples represent the following workflow:

```text
User
  |
  v
Open WebUI
  |
  v
Qwen LLM
  |
  +--------------------+
  |                    |
  v                    v
Knowledge Base       Diagnostic Tool
                       |
             +---------+---------+
             |         |         |
           Ping       DNS      TCP
                       |
                   Traceroute
```

## Design Principles

The diagnostic examples follow these principles:

* Read-only operations
* Explicit tool functions
* Input validation
* Execution timeouts
* No arbitrary shell execution
* No configuration changes
* No firewall changes
* No routing changes
* No customer-data access
* No unrestricted `run_command()` functionality

## Example Targets

The examples may use public targets such as:

```text
8.8.8.8
1.1.1.1
example.com
```

Actual results will vary depending on network conditions and the environment where the tools are executed.

## Intended Audience

These examples are useful for:

* IT engineers
* NOC engineers
* Network administrators
* AI/ML engineers
* DevOps engineers
* Students building AI-assisted infrastructure projects
* Recruiters reviewing the engineering implementation

## Important

The examples demonstrate the **engineering approach**, not a guarantee that every network environment will produce identical results.
