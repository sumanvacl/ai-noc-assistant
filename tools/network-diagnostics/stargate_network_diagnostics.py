"""
Stargate AI NOC - Network Diagnostics

Read-only network diagnostic tools intended for integration with
an AI/NOC assistant such as Open WebUI + Ollama.

Supported diagnostics:
    - IPv4 ping
    - DNS A-record lookup
    - TCP port connectivity test
    - IPv4 traceroute

Security principles:
    - No arbitrary shell execution
    - Explicit command allowlists
    - Target validation
    - Restricted command parameters
    - Execution timeouts
    - Read-only network operations

This project is intended for controlled NOC/IT troubleshooting.
"""

from __future__ import annotations

import ipaddress
import re
import socket
import subprocess
from typing import Any


class NetworkDiagnostics:
    """Read-only network diagnostic functions."""

    # Conservative hostname validation.
    HOSTNAME_RE = re.compile(
        r"^(?=.{1,253}$)"
        r"(?:[A-Za-z0-9]"
        r"(?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
        r"\.)*"
        r"[A-Za-z0-9]"
        r"(?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$"
    )

    MAX_HOSTNAME_LENGTH = 253

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    @classmethod
    def validate_target(cls, target: str) -> tuple[bool, str]:
        """
        Validate an IPv4 address or DNS hostname.

        Returns:
            (True, "") when valid.
            (False, reason) when invalid.
        """

        if not target:
            return False, "Target is required."

        target = target.strip()

        if not target:
            return False, "Target is empty."

        if len(target) > cls.MAX_HOSTNAME_LENGTH:
            return False, "Target name is too long."

        # Prevent command-line option injection.
        if target.startswith("-"):
            return False, "Invalid target."

        # IPv4 validation.
        try:
            ipaddress.IPv4Address(target)
            return True, ""
        except ValueError:
            pass

        # Hostname validation.
        if cls.HOSTNAME_RE.fullmatch(target):
            return True, ""

        return False, "Target must be a valid IPv4 address or hostname."

    # ---------------------------------------------------------
    # Ping
    # ---------------------------------------------------------

    @classmethod
    def ping(
        cls,
        target: str,
        count: int = 4,
    ) -> str:
        """
        Perform a read-only IPv4 ping.

        Args:
            target:
                IPv4 address or hostname.

            count:
                Number of ICMP packets.
                Allowed range: 1-10.
        """

        valid, reason = cls.validate_target(target)

        if not valid:
            return f"ERROR: {reason}"

        try:
            count = int(count)
        except (TypeError, ValueError):
            return "ERROR: count must be an integer."

        if not 1 <= count <= 10:
            return "ERROR: count must be between 1 and 10."

        command = [
            "ping",
            "-4",
            "-c",
            str(count),
            "-W",
            "5",
            target,
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=25,
                check=False,
            )

        except subprocess.TimeoutExpired:
            return "ERROR: ping operation timed out."

        except FileNotFoundError:
            return "ERROR: ping utility is not installed."

        except Exception as exc:
            return (
                "ERROR: ping execution failed: "
                f"{type(exc).__name__}: {exc}"
            )

        output = result.stdout.strip()

        if result.stderr.strip():
            output += "\n" + result.stderr.strip()

        if not output:
            return (
                "ERROR: ping returned no output "
                f"(exit code {result.returncode})."
            )

        return output

    # ---------------------------------------------------------
    # DNS
    # ---------------------------------------------------------

    @classmethod
    def dns_lookup(cls, hostname: str) -> str:
        """
        Perform a read-only DNS A-record lookup.

        Args:
            hostname:
                DNS hostname to resolve.
        """

        valid, reason = cls.validate_target(hostname)

        if not valid:
            return f"ERROR: {reason}"

        command = [
            "nslookup",
            "-type=A",
            "-timeout=5",
            "-retry=1",
            hostname,
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=15,
                check=False,
            )

        except subprocess.TimeoutExpired:
            return "ERROR: DNS lookup timed out."

        except FileNotFoundError:
            return "ERROR: nslookup utility is not installed."

        except Exception as exc:
            return (
                "ERROR: DNS lookup failed: "
                f"{type(exc).__name__}: {exc}"
            )

        output = result.stdout.strip()

        if result.stderr.strip():
            output += "\n" + result.stderr.strip()

        if not output:
            return (
                "ERROR: DNS lookup returned no output "
                f"(exit code {result.returncode})."
            )

        return output

    # ---------------------------------------------------------
    # TCP port test
    # ---------------------------------------------------------

    @classmethod
    def check_tcp_port(
        cls,
        target: str,
        port: int,
    ) -> str:
        """
        Check whether a TCP connection can be established.

        Args:
            target:
                IPv4 address or hostname.

            port:
                TCP port from 1-65535.
        """

        valid, reason = cls.validate_target(target)

        if not valid:
            return f"ERROR: {reason}"

        try:
            port = int(port)
        except (TypeError, ValueError):
            return "ERROR: port must be an integer."

        if not 1 <= port <= 65535:
            return "ERROR: port must be between 1 and 65535."

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )

        sock.settimeout(5)

        try:
            result = sock.connect_ex((target, port))

            if result == 0:
                return (
                    f"TCP CONNECTED: {target}:{port} "
                    "is reachable."
                )

            return (
                f"TCP NOT CONNECTED: {target}:{port} "
                f"(socket error {result})."
            )

        except socket.gaierror as exc:
            return f"ERROR: DNS resolution failed: {exc}"

        except socket.timeout:
            return f"TCP TIMEOUT: {target}:{port}"

        except Exception as exc:
            return (
                "ERROR: TCP test failed: "
                f"{type(exc).__name__}: {exc}"
            )

        finally:
            sock.close()

    # ---------------------------------------------------------
    # Traceroute
    # ---------------------------------------------------------

    @classmethod
    def traceroute(cls, target: str) -> str:
        """
        Perform a controlled IPv4 traceroute.

        Maximum:
            15 hops
            1 probe per hop
            2 second wait per probe
        """

        valid, reason = cls.validate_target(target)

        if not valid:
            return f"ERROR: {reason}"

        command = [
            "traceroute",
            "-4",
            "-n",
            "-m",
            "15",
            "-q",
            "1",
            "-w",
            "2",
            target,
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=45,
                check=False,
            )

        except subprocess.TimeoutExpired:
            return "ERROR: traceroute operation timed out."

        except FileNotFoundError:
            return "ERROR: traceroute utility is not installed."

        except Exception as exc:
            return (
                "ERROR: traceroute failed: "
                f"{type(exc).__name__}: {exc}"
            )

        output = result.stdout.strip()

        if result.stderr.strip():
            output += "\n" + result.stderr.strip()

        if not output:
            return (
                "ERROR: traceroute returned no output "
                f"(exit code {result.returncode})."
            )

        return output


# -------------------------------------------------------------
# Simple local test interface
# -------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Stargate read-only network diagnostics"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # ping
    ping_parser = subparsers.add_parser("ping")
    ping_parser.add_argument("target")
    ping_parser.add_argument(
        "--count",
        type=int,
        default=4,
    )

    # DNS
    dns_parser = subparsers.add_parser("dns")
    dns_parser.add_argument("target")

    # TCP
    tcp_parser = subparsers.add_parser("tcp")
    tcp_parser.add_argument("target")
    tcp_parser.add_argument("port", type=int)

    # traceroute
    trace_parser = subparsers.add_parser("traceroute")
    trace_parser.add_argument("target")

    args = parser.parse_args()

    if args.command == "ping":
        print(
            NetworkDiagnostics.ping(
                args.target,
                args.count,
            )
        )

    elif args.command == "dns":
        print(
            NetworkDiagnostics.dns_lookup(
                args.target
            )
        )

    elif args.command == "tcp":
        print(
            NetworkDiagnostics.check_tcp_port(
                args.target,
                args.port,
            )
        )

    elif args.command == "traceroute":
        print(
            NetworkDiagnostics.traceroute(
                args.target
            )
        )
