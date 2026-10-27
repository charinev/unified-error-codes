..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_undervoltage:

**************
 UnderVoltage
**************

Description
===========

An undervoltage fault occurs when the measured voltage at
:ref:`Side B <term_side_b>` falls below the minimum threshold required for
safe and effective operation during charging, independent of energy direction
or power type (AC or DC).

This error code is applicable to and can be set by either the EV or EVSE,
since both observe the same physical interface. This allows the same
definition and criteria to be used for both EV and EVSE.

Trigger Conditions
==================

- Measured voltage at :ref:`Side B <term_side_b>` falls below the minimum
  safety or performance threshold defined by the applicable standard or
  manufacturer.
- The measured voltage stays below that threshold for the defined minimum
  duration, or falls below it instantaneously where required by protection
  limits.

Criteria
========

Reference criteria from IEC 61851-23:

-  CC.5.5.11 — Minimum voltage at Side B.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_undervoltage_system`
-  :ref:`telemetry_undervoltage_actual`
-  :ref:`telemetry_undervoltage_threshold`
-  :ref:`telemetry_communication_state`
