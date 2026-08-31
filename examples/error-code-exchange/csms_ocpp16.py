"""A minimal mock CSMS backend speaking OCPP 1.6."""

from __future__ import annotations

import logging
from typing import Any

import websockets
from ocpp.routing import on
from ocpp.v16 import ChargePoint as ChargePointV16
from ocpp.v16 import call_result

logger = logging.getLogger("csms-ocpp1.6")

# What this backend last received. The relay reads it after its call returns,
# so the demo can log send/receive/acknowledge together and in order rather
# than printing from two concurrent tasks at once.
last_received: dict[str, Any] = {}


class MockCentralSystemV16(ChargePointV16):
    @on("StatusNotification")
    def on_status_notification(self, **kwargs: Any) -> call_result.StatusNotification:
        logger.info("received StatusNotification: %s", kwargs)
        last_received.clear()
        last_received.update(kwargs)
        return call_result.StatusNotification()


async def _handler(websocket: Any) -> None:
    if websocket.subprotocol != "ocpp1.6":
        await websocket.close()
        return
    charge_point_id = websocket.request.path.strip("/").rsplit("/", 1)[-1]
    cp = MockCentralSystemV16(charge_point_id, websocket)
    try:
        await cp.start()
    except websockets.ConnectionClosed:
        pass  # the EVSE disconnects once its single request is answered


def serve(host: str = "localhost", port: int = 9016) -> Any:
    """Return the `websockets.serve` awaitable for the OCPP 1.6 mock CSMS."""
    return websockets.serve(_handler, host, port, subprotocols=["ocpp1.6"])
