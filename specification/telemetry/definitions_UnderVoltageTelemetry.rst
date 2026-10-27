..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _telemetry_undervoltage_system:

********************
 UnderVoltage System
********************

-  **Description**: The system, EV or EVSE, responsible for or reporting the
   undervoltage condition. Either may be the reporting system, since both
   observe the same physical interface at Side B.
-  **Values**: EV, EVSE

.. _telemetry_undervoltage_actual:

*****************
 Actual Voltage
*****************

-  **Description**: The actual voltage measured at Side B at the time of the
   undervoltage condition.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_undervoltage_threshold:

********************
 Threshold Voltage
********************

-  **Description**: The minimum allowable voltage defined by the applicable
   standard or manufacturer for Side B, below which the undervoltage fault is
   raised.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`
