# Traceroute Example

## Objective

Demonstrate controlled path discovery toward a destination.

## User Request

```text
Run a traceroute to 1.1.1.1.
```

## AI Tool Selection

The assistant selects:

```text
traceroute(hostname)
```

Example argument:

```text
hostname = 1.1.1.1
```

## Tool Execution

The diagnostic tool uses a restricted traceroute configuration.

Example:

```bash
traceroute -4 -n -m 15 -q 1 -w 2 1.1.1.1
```

The implementation limits:

* Address family
* Maximum hops
* Probes per hop
* Timeout
* Execution duration

## Example Result

A typical result might resemble:

```text
traceroute to 1.1.1.1

 1  192.0.2.1
 2  198.51.100.1
 3  203.0.113.1
 4  ...
```

The addresses above are documentation-only examples.

## AI Interpretation

Example:

```text
The destination path was traced successfully.

The first hop represents the local gateway or first routing device.
Subsequent hops represent routers encountered toward the destination.

Individual hops may not respond to traceroute probes even when the destination remains reachable.
```

## Troubleshooting Use

Traceroute is particularly useful when investigating:

* High latency
* Routing problems
* Unexpected paths
* Intermediate packet loss
* Connectivity differences between networks

## Safety

The diagnostic tool does not:

* Change routing
* Change BGP
* Modify interfaces
* Change firewall rules
* Modify VLANs
* Execute arbitrary commands

It only collects path information.
