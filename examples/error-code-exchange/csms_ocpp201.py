"""A minimal mock CSMS backend speaking OCPP 2.0.1."""

from __future__ import annotations

import logging
from typing import Any

import websockets
from ocpp.routing import on
from ocpp.v201 import ChargePoint as ChargePointV201
from ocpp.v201 import call_result

logger = logging.getLogger("csms-ocpp2.0.1")

# What this backend last received. The relay reads it after its call returns,
# so the demo can log send/receive/acknowledge together and in order rather
# than printing from two concurrent tasks at once.
last_received: dict[str, Any] = {}


class MockCentralSystemV201(ChargePointV201):
    @on("NotifyEvent")
    def on_notify_event(self, **kwargs: Any) -> call_result.NotifyEvent:
        logger.info("received NotifyEvent: %s", kwargs)
        last_received.clear()
        last_received.update(kwargs)
        return call_result.NotifyEvent()


async def _handler(websocket: Any) -> None:
    if websocket.subprotocol != "ocpp2.0.1":
        await websocket.close()
        return
    charge_point_id = websocket.request.path.strip("/").rsplit("/", 1)[-1]
    cp = MockCentralSystemV201(charge_point_id, websocket)
    try:
        await cp.start()
    except websockets.ConnectionClosed:
        pass  # the EVSE disconnects once its single request is answered


def serve(host: str = "localhost", port: int = 9201) -> Any:
    """Return the `websockets.serve` awaitable for the OCPP 2.0.1 mock CSMS."""
    return websockets.serve(_handler, host, port, subprotocols=["ocpp2.0.1"])
