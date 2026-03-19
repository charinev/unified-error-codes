..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

#############
 Error Codes
#############

This section defines the error codes.

.. _error_powerloss:

***********
 PowerLoss
***********

Description
===========

This error is raised when the charging station experiences a partial or
complete loss of its main power supply.

Trigger Conditions
==================

-  The main power supply voltage drops below a threshold that prevents the charging station from operating.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_communication_state`
-  :ref:`telemetry_supply_voltage_l1`
-  :ref:`telemetry_supply_voltage_l2`
-  :ref:`telemetry_supply_voltage_l3`

.. _error_connectorlockfailure:

**********************
 ConnectorLockFailure
**********************

Description
===========

This error is raised when the CCS connector lock mechanism fails to reach
the expected locked or unlocked position. The latch is mechanically engaged
by the EV, but lock state is observable from the EVSE via position feedback.

Trigger Conditions
==================

-  The lock position feedback does not reach the locked threshold within the
   expected time after a lock command is issued.
-  The lock position feedback does not reach the unlocked threshold within the
   expected time after an unlock command is issued.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_connector_lock_position`
-  :ref:`telemetry_connector_lock_command`
