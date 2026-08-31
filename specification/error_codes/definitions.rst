..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

#############
 Error Codes
#############

This section defines the error codes.

.. _terminology_side_a_side_b:

Terminology: Side A and Side B
===============================

Several error codes and telemetry signals reference measurement location
using the terms **Side A** and **Side B**, per IEC 61851-23:2023 sections
3.7.102 and 3.7.103:

Side A
   The supply interface — the EVSE terminals connected to the upstream
   power source (e.g., grid or local generation).

Side B
   The vehicle interface — the physical connection between the EVSE and
   the vehicle (connector or socket outlet).

.. _error_gridpowerloss:

**************
 GridPowerLoss
**************

Description
===========

This error is raised when the charging station experiences a partial or
complete loss of grid power supply.

Trigger Conditions
==================

-  The power supply voltage at Side A or Side B of the EVSE drops below a
   critical threshold as described by the manufacturer.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_communication_state`
-  :ref:`telemetry_supply_voltage_l1`
-  :ref:`telemetry_supply_voltage_l2`
-  :ref:`telemetry_supply_voltage_l3`

.. include:: definitions_EVShiftPosition.rst
.. include:: definitions_ContactorPosition.rst
.. include:: definitions_ConnectorLockFailure.rst
.. include:: definitions_HighTemperature.rst
.. include:: definitions_PowerModuleFault.rst
.. include:: definitions_UnderVoltage.rst
