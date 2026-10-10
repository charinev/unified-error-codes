..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_overcurrent:

*************
 OverCurrent
*************

Description
===========

EVSE definition : This error code is set when the EVSE detects the Side B current exceeds the maximum allowed Side B current threshold of the EVSE. 

EV definition : This error code is set when the DC current during DC charging has risen above an acceptable level measured within the EV system.

This error code is applicable to and can be set by either the EV or EVSE,
depending on which side satisfies and detects the over current condition. 

Trigger Conditions
==================

-  The EVSE trigger conditions and thresholds are as defined in the IEC 61851-23 standard, section CC.6.4.
-  The EV trigger conditions and thresholds are as defined by the manufacturer

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`Telemetry_OverCurrent_Location`
-  :ref:`Telemetry_OverCurrent_ActualCurrent`
-  :ref:`Telemetry_OverCurrent_ThresholdCurrent`

