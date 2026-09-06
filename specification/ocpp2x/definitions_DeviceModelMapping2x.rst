..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _ocpp2x_device_model_mapping:

***************************************
 Mapping to the OCPP 2.x Device Model
***************************************

OCPP 2.x reports a fault against the device model rather than as an error code,
so each error code needs a component and a variable to be reported against.
OCPP 2.x requires a standardized component name to be used wherever one matches
the physical component being described, which is what makes such a mapping
possible at all.

The table below gives that mapping. Every component and variable name in it is a
standardized OCPP 2.x name.

.. list-table::
   :header-rows: 1
   :widths: 24 22 14 16 24

   -  -  Error code
      -  Component
      -  Variable
      -  ``actualValue``
      -  Basis

   -  -  ``ConnectorLockFailure`` (EVSE)
      -  ``ConnectorPlugRetentionLock``
      -  ``Problem``
      -  ``"true"`` / ``"false"``
      -  OCPP 2.x describes this variable as "Locking Failed" and itself
         requires this component and variable for a lock failure.

   -  -  ``ConnectorLockFailure`` (EV)
      -  ``EVRetentionLock``
      -  ``Problem``
      -  ``"true"`` / ``"false"``
      -  "Lock Problem (e.g. failed to lock/unlock)".

   -  -  ``ContactorPosition``
      -  ``PowerContactor``
      -  ``Problem``
      -  ``"true"`` / ``"false"``
      -  "Close/Open failed".

   -  -  ``HighTemperature``
      -  ``TemperatureSensor``
      -  ``Active``
      -  ``"true"`` / ``"false"``
      -  ``Active`` on this component means "High temperature (over MaxSet)".
         ``Problem`` is deliberately not used: on this component it means a
         fault in the sensor, not an overtemperature.

   -  -  ``PowerModuleFault``
      -  ``AcDcConverter``
      -  ``Problem``
      -  ``"true"`` / ``"false"``
      -  "some problem/fault exists". Which module failed is carried by
         ``component.instance``.

   -  -  ``GridPowerLoss``
      -  ``ElectricalFeed``
      -  ``Problem``
      -  ``"true"`` / ``"false"``
      -  This component "represents an incoming electrical connection to a
         Charging Station, that may be a grid/distribution network connection".

   -  -  ``OverCurrent``
      -  ``OverCurrentProtection``
      -  ``Active``
      -  ``"true"`` / ``"false"``
      -  ``Active`` on this component means "Tripped. Trip when over
         MaxSet/MaxLimit."

   -  -  ``Overvoltage`` (Site A)
      -  ``ElectricalFeed``
      -  ``ACVoltage``
      -  measured voltage
      -  OCPP 2.x has no overvoltage protection component, so an overvoltage at
         the supply interface is reported as the measured voltage of the
         incoming feed.

   -  -  ``Overvoltage`` (Site B)
      -  ``EVSE``
      -  ``DCVoltage``
      -  measured voltage
      -  The same, at the vehicle interface. ``ACVoltage`` is used instead where
         the vehicle interface is AC.

   -  -  ``EVShiftPosition``
      -  ``ConnectedEV``
      -  ``ChargingState``
      -  ``"VehicleShiftPosition"``
      -  ``VehicleShiftPosition`` is a member of the ``ChargingState`` value
         list, which OCPP 2.x itself maps to ``FAILED_EVShiftPosition`` of
         ISO 15118-2.

Notes on individual rows
========================

``ConnectorLockFailure`` has two rows because the error code applies to whichever
side owns the lock. Which row applies is decided by which side owns the
mechanism, not by which side reported the condition. Where the EVSE relays a lock
failure the vehicle reported to it over ISO 15118, the ``ConnectedEV`` component
with ``ChargingState`` set to ``"ChargerConnectorLockFault"`` may be used
instead.

``OverCurrent`` is reported against ``OverCurrentProtection`` where the charging
station models a discrete protection device. Where it does not, the ``EVSE``
component with the ``Overload`` variable, which OCPP 2.x describes as "Excessive
current/power consumption", may be used instead.

``Overvoltage`` is the one error code in this table reported as a measured value
rather than as a boolean state, because OCPP 2.x offers no component whose state
means "voltage too high". Reporting the voltage itself lets a charging management
system apply its own monitor to the same variable and reach the same conclusion.

DIN DKE SPEC 99003 states that defining this mapping is outside its scope, so
there is no earlier mapping to align with. The rows above are derived from the
descriptions OCPP 2.x gives its own standardized components and variables.
