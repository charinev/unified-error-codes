..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_undercurrent:

**************
 UnderCurrent
**************

Description
===========

This error is raised by the EVSE when the current it delivers to the EV
falls below the current it has committed to supply for the active
charging schedule.

Out of Scope
============

-  An EV drawing less current than the EVSE offers, which is normal
   behavior in unidirectional charging.
-  EV deviations from its committed power profile under ISO 15118-20
   power tolerance.
-  Bi-directional charging (V2G/V2H) under-current conditions.

Trigger Conditions
==================

-  The measured output current at the supply or transmission interface
   falls below the current level committed for the active schedule, for
   longer than a defined qualification time, as specified by the
   applicable standard or the manufacturer-defined schedule commitment.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_undercurrent_location`
-  :ref:`telemetry_undercurrent_expected`
-  :ref:`telemetry_undercurrent_actual`
