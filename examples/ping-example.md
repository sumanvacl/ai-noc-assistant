# Ping Diagnostic Example

## Objective

Demonstrate how the AI assistant can use a controlled diagnostic tool to perform an IPv4 ping test.

## User Request

Example user request:

```text
Ping 8.8.8.8 and tell me whether it is reachable.
```

## AI Tool Selection

The AI identifies that a network reachability test is required and selects:

```text
ping(hostname)
```

The tool receives:

```text
hostname = 8.8.8.8
```

## Tool Execution

The diagnostic tool executes an IPv4 ping using controlled parameters.

Example command:

```bash
ping -4 -c 4 -W 5 8.8.8.8
```

The tool does not accept arbitrary shell commands from the user.

## Example Result

A successful result may look similar to:

```text
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=28.3 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=28.0 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=116 time=28.6 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=116 time=30.0 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss
```

## AI Interpretation

Example response:

```text
8.8.8.8 is reachable.

Packets transmitted: 4
Packets received: 4
Packet loss: 0%

The destination is responding normally to ICMP echo requests.
```

## Engineering Value

This demonstrates:

* Native LLM tool calling
* Controlled network diagnostics
* Real-time information gathering
* Structured tool arguments
* Separation between AI reasoning and command execution
* Read-only infrastructure interaction

## Safety

The implementation should enforce:

* IPv4-only execution
* Maximum packet count
* Execution timeout
* Target validation
* No arbitrary command execution
* `shell=False` for subprocess execution

## Important

Latency and packet-loss values shown above are examples. They should not be interpreted as permanent network measurements.
