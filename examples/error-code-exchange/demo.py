#!/usr/bin/env python3
"""End-to-end demo: EV -> EVSE -> CSMS (OCPP 1.6 and OCPP 2.0.1 in parallel).

See ARCHITECTURE.md for the full design. In short:

1. The EV builds a Unified Error Code ErrorCodeReport and wraps it as an
   ENP extension (the proposed Error Code Extension from GitHub issue
   #65), as it would be sent over the Event Notification Protocol (ENP)
   specified by ISO 15118-202.
2. The EVSE unwraps and decodes it, then relays the same detected error
   to two mock CSMS backends at once: one speaking OCPP 1.6, one
   speaking OCPP 2.0.1.

Requires: pip install -r requirements.txt
Run: python demo.py
"""

from __future__ import annotations

import asyncio

import csms_ocpp16
import csms_ocpp201
import demolog
from common import ERROR_CODE_EXTENSION_ID, compile_asn1_codec
from ev import raise_error_over_iso15118
from evse import decode_from_iso15118, relay_to_both_backends

OCPP16_URI = "ws://localhost:9016/EVSE-DE-ABC-E1234-1"
OCPP201_URI = "ws://localhost:9201/EVSE-DE-ABC-E1234-1"


async def main() -> None:
    # asn1tools has no 'coer' codec name in the installed release ('coer'
    # isn't a recognized asn1tools codec at all as of 0.168); 'oer' is the
    # closest supported ITU-T X.696-family encoding, and this message has
    # no SET types or unconstrained CHOICE alternatives that would make its
    # OER encoding differ from a canonical (COER) one.
    coer = compile_asn1_codec("oer")

    demolog.step("EV detects a fault and builds an ErrorCodeReport")
    wire_bytes = raise_error_over_iso15118(coer)
    demolog.line("EV", "detected SideB_OverCurrentFailure")
    demolog.line("EV", "attached the 3 telemetry signals that code requires")
    demolog.line("", "location=EV, actual=150.3 A, threshold=125.0 A")
    demolog.line("EV", "wrapped the report as an ENP extension")
    demolog.line("", f"extensionID     {ERROR_CODE_EXTENSION_ID}")
    demolog.line("", "extensionValue  COER-encoded ErrorCodeReport")

    demolog.step(
        f"EV --> EVSE over ISO 15118-202 ENP (OER, {len(wire_bytes)} bytes)"
    )
    print(demolog.as_hex(wire_bytes))

    demolog.step("EVSE unwraps the extension and decodes the report")
    report = decode_from_iso15118(coer, wire_bytes)
    demolog.line("EVSE", "extensionID recognised, payload decoded")
    demolog.line("EVSE", "arrived on the EV's ENP channel, so the EV reported it")
    demolog.line("", "(the report itself carries no 'which side' field)")
    print(demolog.as_json(report))

    demolog.step("Starting mock CSMS backends")
    async with csms_ocpp16.serve(), csms_ocpp201.serve():
        demolog.line("CSMS (OCPP 1.6)", f"listening on {OCPP16_URI}")
        demolog.line("CSMS (OCPP 2.0.1)", f"listening on {OCPP201_URI}")

        demolog.step("EVSE relays the same error to both backends, concurrently")
        await relay_to_both_backends(
            report, OCPP16_URI, OCPP201_URI, reported_by="ev"
        )

    demolog.step("Done")
    demolog.line("", "the same Unified Error Code reached both backends")


if __name__ == "__main__":
    asyncio.run(main())
