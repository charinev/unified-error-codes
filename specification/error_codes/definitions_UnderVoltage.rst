..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_undervoltage:

**************
 UnderVoltage
**************

Description
===========

A condition where the measured voltage at a defined electrical interface falls below the minimum threshold required for safe and effective operation, evaluated relative to the physical location within the EV–EVSE system.
Undervoltage shall be classified based on measurement location (“Side”), independent of energy direction or power type (AC or DC).

Side A - Supply Interface (EVSE Input)
Undervoltage at Side A is a voltage falling below limits at the EVSE terminals connected to the upstream power source (e.g., grid or local generation), such that the system's voltage supply is below its acceptable input range.

Side B  Vehicle Interface (EV-EVSE Connection)
Undervoltage at Side B is a voltage falling below limits at the physical connection between the EVSE and the vehicle (connector or socket outlet), as measured at the interface, such that the system's output voltage is lower than agreed between EV & EVSE.

This error code is applicable to and can be set by either the EV or EVSE. At Side A it is always reported by the EVSE; at Side B it may be reported by either side, depending on which system observes the shortfall at the connection.

Trigger Conditions
==================
Threshold Shortfall
   Measured voltage < allowable minimum limit (per applicable standard or manufacturer-defined value)

Measurement Location
   Side A (supply interface), or
   Side B (vehicle interface)

Time Qualification
   Falls below threshold for a defined minimum duration (to filter transients), or
   Instantaneous shortfall where explicitly required (e.g., protection limits)

Criteria
========

Reference criteria from IEC 61851-23, Appendix.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_undervoltage_location`
-  :ref:`telemetry_undervoltage_system`
-  :ref:`telemetry_undervoltage_actual`
-  :ref:`telemetry_undervoltage_threshold`

