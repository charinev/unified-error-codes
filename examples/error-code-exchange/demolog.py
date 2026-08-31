"""Small logging helpers so the demo reads as an ordered sequence of steps."""

from __future__ import annotations

import datetime
import itertools
import json
from typing import Any

_step_numbers = itertools.count(1)


def step(title: str) -> None:
    """Start a new numbered step."""
    print(f"\n[{next(_step_numbers)}] {title}")


def line(actor: str, message: str) -> None:
    """Log one message attributed to an actor."""
    print(f"    {actor:<18} {message}")


def block(lines: list[str]) -> None:
    """Emit already-formatted lines as one atomic write.

    The two OCPP relays run concurrently, so each builds its lines and
    emits them together; otherwise their output interleaves and the
    send/receive/acknowledge sequence becomes impossible to follow.
    """
    print("\n".join(lines))


def format_line(actor: str, message: str) -> str:
    """Format a line for later emission via `block`."""
    return f"    {actor:<18} {message}"


def _plain(value: Any) -> Any:
    if isinstance(value, (bytes, bytearray)):
        return value.hex()
    if isinstance(value, datetime.datetime):
        return value.isoformat()
    return str(value)


def as_json(value: Any, indent: int = 8) -> str:
    """Render a decoded ASN.1 or OCPP payload as indented JSON.

    Bytes render as hex and timestamps as ISO 8601, rather than leaking
    Python reprs into the transcript.
    """
    text = json.dumps(value, indent=2, default=_plain)
    pad = " " * indent
    return "\n".join(pad + row for row in text.splitlines())


def as_hex(data: bytes, indent: int = 8, width: int = 64) -> str:
    """Render wire bytes as indented, wrapped hex."""
    text = data.hex()
    pad = " " * indent
    return "\n".join(pad + text[i : i + width] for i in range(0, len(text), width))
