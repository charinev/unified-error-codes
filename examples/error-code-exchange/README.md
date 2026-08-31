# Error Code Exchange Demo

Runnable, end-to-end demonstration of the `ErrorCodeReport` message
defined in
[`specification/protocol/definitions_ErrorCodeExchangeMessage.rst`](../../specification/protocol/definitions_ErrorCodeExchangeMessage.rst),
implementing [GitHub issue #61](https://github.com/charinev/unified-error-codes/issues/61)
and the ENP extension registration proposed in
[GitHub issue #65](https://github.com/charinev/unified-error-codes/issues/65).

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for the full design.

## What it shows

The complete path **EV → EVSE → CSMS**:

1. An EV builds an `ErrorCodeReport` for a `SideB_OverCurrentFailure`,
   carrying the three telemetry signals that error code lists as
   required for analysing it — including where the over-current was
   measured, which is telemetry rather than something the code name
   encodes — using the canonical ASN.1 module at
   [`specification/protocol/UnifiedErrorCodeExchange.asn1`](../../specification/protocol/UnifiedErrorCodeExchange.asn1)
   directly, so the demo can never drift from the published schema, and
   wraps it as an ISO 15118-202 ENP extension — see `ARCHITECTURE.md`'s
   "ENP extension wrapping" section for what is real here and what is
   scaffolding.
   (The specification requires the canonical Octet Encoding Rules,
   COER; the demo uses asn1tools' `oer` codec as the closest supported
   stand-in — see the comment in `demo.py`.)
2. An EVSE unwraps and decodes it, then relays the *same* detected
   error to **two** mock CSMS backends **in parallel**: one speaking
   **OCPP 1.6** (`StatusNotification`), one speaking **OCPP 2.0.1**
   (`NotifyEventRequest`) — simulating a station that has not yet
   fully migrated off the older protocol.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python demo.py
```

## Files

| File | Role |
|---|---|
| `DemoEnpExtension.asn1` | Demo-only ENP extension wrapper (scaffolding, not spec) |
| `common.py` | Shared sample data and ASN.1 codec setup |
| `demolog.py` | Step-numbered transcript formatting |
| `ev.py` | EV: builds and encodes the `ErrorCodeReport` |
| `evse.py` | EVSE: decodes it, relays to both OCPP backends |
| `csms_ocpp16.py` | Minimal mock CSMS speaking OCPP 1.6 |
| `csms_ocpp201.py` | Minimal mock CSMS speaking OCPP 2.0.1 |
| `demo.py` | Orchestrates the full EV → EVSE → CSMS run |
