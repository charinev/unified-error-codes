..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

#######
 Scope
#######

This document specifies a unified set of error codes for electric vehicle
charging, and how an EVSE delivers them to a charging management system.

An error code identifies a condition that an EV or an EVSE has detected, by a
name that both sides and the charging management system understand the same
way. The purpose is diagnostic: a charge point operator, a vehicle manufacturer
and an EVSE manufacturer looking at the same failed charging session should be
able to name its cause identically without a bilateral agreement between them.

Normative and informative parts
===============================

The following clauses are normative:

-  :doc:`Scope <../scope/definitions>`
-  :doc:`Conventions <../conventions/definitions>`
-  :doc:`Error Codes <../error_codes/definitions>`
-  The clauses specifying delivery of error codes to a charging management
   system.

:doc:`Annex A <../telemetry/definitions>` is informative. It is published for
early feedback and states no requirements. Where an error code lists the
telemetry related to it, that list is a pointer into Annex A and is likewise
informative.

Out of scope in this edition
============================

-  Delivery of telemetry to a charging management system. The telemetry signals
   in Annex A are given so that the error codes can be discussed with the
   measurements that make them diagnosable, but how those measurements travel
   over OCPP is not settled and is therefore not specified here.
-  Exchange of error codes between the EV and the EVSE.
-  Severity classification of error codes.
-  Reporting several error codes as a single correlated group.
