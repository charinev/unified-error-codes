..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_hightemperature:

*****************
 HighTemperature
*****************

Description
===========

An overtemperature fault occurs when the measured temperature of a system or
component within the EV or EVSE exceeds its calibrated safety or performance
threshold during charging. The fault is reported against the subsystem
(Location) that observed the overtemperature condition.

This error code is applicable to and can be set by either the EV or EVSE,
depending on which side owns the affected component and its thermal
monitoring. This allows the same definition and criteria to be used for both
EV and EVSE.

Trigger Conditions
==================

- Measured temperature at the reporting Location exceeds the calibrated safety
  or performance threshold defined by the applicable standard or manufacturer.

Criteria
========

Reference criteria from IEC 61851-23:

-  101.2.2.1 — Temperature of the DC contact assembly of the vehicle
   connector.
-  101.2.3.2 — Overtemperature handling.
-  101.2.3.3 — Check of the plausibility of the values provided by the thermal
   sensing devices.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_hightemperature_actual`
-  :ref:`telemetry_hightemperature_threshold`
-  :ref:`telemetry_hightemperature_location`
