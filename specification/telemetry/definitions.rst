..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

###########
 Telemetry
###########

This section defines the telemetry signals that shall be monitored by
the charging station.

.. _telemetry_supply_voltage_l1:

*******************
 Supply Voltage L1
*******************

-  **Description**: The continuous measurement of AC voltage for L1
   phase. Measured at the AC supply input to the charging station.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_supply_voltage_l2:

*******************
 Supply Voltage L2
*******************

-  **Description**: The continuous measurement of AC voltage for L2
   phase. Measured at the AC supply input to the charging station.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_supply_voltage_l3:

*******************
 Supply Voltage L3
*******************

-  **Description**: The continuous measurement of AC voltage for L3
   phase. Measured at the AC supply input to the charging station.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_communication_state:

********************
 Communication State
********************

-  **Description**: The state of the communication between EV and charging station.
-  **Unit**: N/A
-  **Resolution**: N/A

.. _telemetry_connector_lock_position:

************************
 Connector Lock Position
************************

-  **Description**: The position feedback state of the CCS connector lock
   mechanism as reported by the EVSE. Determined by a threshold-based
   evaluation of the lock actuator feedback signal, which may be a continuous
   analog measurement.
-  **Unit**: N/A (enumerated: ``locked``, ``unlocked``, ``unknown``)
-  **Resolution**: N/A

.. _telemetry_connector_lock_command:

***********************
 Connector Lock Command
***********************

-  **Description**: The last command issued to the connector lock actuator
   by the EVSE. Used to correlate commanded state against reported position
   feedback during failure analysis.
-  **Unit**: N/A (enumerated: ``lock``, ``unlock``)
-  **Resolution**: N/A
