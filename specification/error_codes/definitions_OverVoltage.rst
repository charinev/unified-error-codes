..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_overvoltage:

*************
 OverVoltage
*************

Description
===========

A condition where the measured voltage at :ref:`Side B <term_side_b>` exceeds the allowable threshold specified by applicable standards and/or manufacturer-defined limits, independent of energy direction or power type (AC or DC).

Trigger Conditions
==================
Threshold Exceedance
   Measured voltage at :ref:`Side B <term_side_b>` > allowable limit (per applicable standard or manufacturer-defined value)

Time Qualification
   Exceeds threshold for a defined minimum duration (to filter transients), or
   Instantaneous exceedance where explicitly required (e.g., protection limits)

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_overvoltage_actual`
-  :ref:`telemetry_overvoltage_threshold`
-  :ref:`telemetry_overvoltage_duration`
