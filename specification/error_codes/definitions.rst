..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

#############
 Error Codes
#############

This section defines the error codes.

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
.. include:: definitions_UnderCurrent.rst
