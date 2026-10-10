..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_overvoltage:

*************
 Overvoltage
*************

Description
===========

A condition where the measured voltage at a defined electrical interface exceeds the allowable threshold specified by applicable standards and/or manufacturer-defined limits, evaluated relative to the physical location within the EV–EVSE system.
Overvoltage shall be classified based on measurement location (“Site”), independent of energy direction or power type (AC or DC).

Site A - Supply Interface (EVSE Input)
Overvoltage at Site A is a voltage exceeding limits at the EVSE terminals connected to the upstream power source (e.g., grid or local generation).

Site B  Vehicle Interface (EV-EVSE Connection)
Overvoltage at Site B is a voltage exceeding limits at the physical connection between the EVSE and the vehicle (connector or socket outlet), as measured at the interface.

Trigger Conditions
==================
Threshold Exceedance
   Measured voltage > allowable limit (per applicable standard or manufacturer-defined value)

Measurement Location
   Site A (supply interface), or
   Site B (vehicle interface)

Time Qualification
   Exceeds threshold for a defined minimum duration (to filter transients), or
   Instantaneous exceedance where explicitly required (e.g., protection limits)

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_overvoltage_site`
-  :ref:`telemetry_overvoltage_actual`
-  :ref:`telemetry_overvoltage_threshold`
-  :ref:`telemetry_overvoltage_duration`
