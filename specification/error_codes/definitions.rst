..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

#############
 Error Codes
#############

This section defines the error codes.

.. _error_powerloss:

***********
 PowerLoss
***********

**Identifier**: `PowerLoss`

Description
===========

This error is raised when the charging station experiences a partial or
complete loss of its main power supply.

Trigger Conditions
==================

-  The main power supply voltage drops below a critical threshold.
-  A complete outage of the external power grid is detected.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_inlet_voltage_l1`
-  :ref:`telemetry_inlet_voltage_l2`
-  :ref:`telemetry_inlet_voltage_l3`
