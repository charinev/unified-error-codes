..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_lowtemperature:

*****************
 Low Temperature
*****************

Description
===========

The temperature of an EVSE or EV high-voltage component has fallen below the
minimum operating threshold required for safe charging. The error is reported
against the subsystem (Location) that observed the under-temperature
condition. This condition will typically result in a derated (reduced-power)
charging capability rather than a complete shutdown until the temperature
returns within the allowable range.

Trigger Conditions
==================

- Measured temperature at the reporting Location drops below the minimum
  operating threshold defined by the manufacturer.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_temperature_actual`
-  :ref:`telemetry_temperature_threshold`
-  :ref:`telemetry_temperature_location`
