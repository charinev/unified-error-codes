..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _telemetry_undervoltage_location:

**********************
 UnderVoltage Location
**********************

-  **Description**: The measurement location at which the undervoltage
   condition was detected.
-  **Values**: SiteA, SiteB
-  **Unit**: N/A
-  **Resolution**: N/A

.. _telemetry_undervoltage_system:

********************
 UnderVoltage System
********************

-  **Description**: The system, EV or EVSE, responsible for or reporting the
   undervoltage condition. At Side A this is always the EVSE; at Side B
   either the EV or the EVSE may be the reporting system, since both sides
   observe the same physical interface.
-  **Values**: EV, EVSE
-  **Unit**: N/A
-  **Resolution**: N/A

.. _telemetry_undervoltage_actual:

*****************
 Actual Voltage
*****************

-  **Description**: The actual voltage measured at the reporting location at
   the time of the undervoltage condition.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_undervoltage_threshold:

********************
 Threshold Voltage
********************

-  **Description**: The minimum allowable voltage defined by the applicable
   standard or manufacturer for the reporting location, below which the
   undervoltage fault is raised.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`
