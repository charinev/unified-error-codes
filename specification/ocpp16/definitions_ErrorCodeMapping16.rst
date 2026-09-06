..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _ocpp16_error_code_mapping:

***********************************
 Mapping to ChargePointErrorCode
***********************************

``StatusNotification.req`` requires an ``errorCode`` from a closed enumeration of
sixteen values, so every error code needs a value to send there while its own
name travels in ``vendorErrorCode``.

The value is the closest match in meaning, so that a charging management system
which knows nothing of this document still classifies the report roughly
correctly. It is a lossy summary and not an identifier: the error code name in
``vendorErrorCode`` is what identifies the condition.

.. list-table::
   :header-rows: 1
   :widths: 34 30 36

   -  -  Error code
      -  ``ChargePointErrorCode``
      -  Basis

   -  -  ``ConnectorLockFailure``
      -  ``ConnectorLockFailure``
      -  "Failure to lock or unlock connector."

   -  -  ``HighTemperature``
      -  ``HighTemperature``
      -  "Temperature inside Charge Point is too high."

   -  -  ``Overvoltage``
      -  ``OverVoltage``
      -  "Voltage has risen above an acceptable level."

   -  -  ``OverCurrent``
      -  ``OverCurrentFailure``
      -  "Over current protection device has tripped."

   -  -  ``ContactorPosition``
      -  ``PowerSwitchFailure``
      -  "Failure to control power switch."

   -  -  ``PowerModuleFault``
      -  ``InternalError``
      -  "Error in internal hard- or software component." A power module is a
         component of the EVSE or the EV, and its failure is internal to the
         reporting side.

   -  -  ``GridPowerLoss``
      -  ``OtherError``
      -  The enumeration has no value for a loss of supply at the grid
         connection.

   -  -  ``EVShiftPosition``
      -  ``OtherError``
      -  The enumeration has no value for a condition detected in the vehicle.
         ``EVCommunicationError`` is deliberately not used: OCPP 1.6 restricts
         it to communication problems and to statuses other than ``Faulted``.

An error code that this table does not list shall be reported with ``errorCode``
set to ``OtherError``.

Four of the eight values above are the ones DIN DKE SPEC 99003 chose for the
same conditions, so an implementation following both documents reports them
identically.

.. note::

   This table uses the error code names as normalized by GitHub issue #76.
   Until that change lands, the catalogue spells ``HighTemperature`` as
   "High Temperature" and ``OverCurrent`` as ``SideB_OverCurrentFailure``.
