..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_undercurrent:

**************
 UnderCurrent
**************

Description
===========

This error is raised by the EVSE when the :ref:`Side B <term_side_b>`
current it delivers to the EV falls below the current it has agreed
with the EV to supply.

Out of Scope
============

-  An EV drawing less current than the EVSE offers, which is normal
   behavior in unidirectional charging.
-  EV deviations from its committed power profile under ISO 15118-20
   power tolerance.
-  Bi-directional charging (V2G/V2H) under-current conditions.

Trigger Conditions
==================

-  The measured output current at :ref:`Side B <term_side_b>` falls
   below the current agreed with the EV, for
   longer than a qualification time defined by the applicable standard
   or the manufacturer.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_undercurrent_expected`
-  :ref:`telemetry_undercurrent_actual`
-  :ref:`telemetry_undercurrent_duration`
