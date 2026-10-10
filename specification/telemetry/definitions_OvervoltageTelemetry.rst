..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _telemetry_overvoltage_actual:

*****************
 Actual Voltage
*****************

-  **Description**: The measured voltage at the reporting site at the time the
   overvoltage condition was detected.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_overvoltage_threshold:

********************
 Threshold Voltage
********************

-  **Description**: The allowable voltage limit for the reporting site, above
   which the overvoltage fault is raised, as defined by the applicable standard
   or the manufacturer.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_overvoltage_site:

**********************
 Overvoltage Site
**********************

-  **Description**: The measurement location at which the overvoltage was
   observed.
-  **Values**:

   -  ``SiteA`` — Supply interface, at the EVSE terminals connected to the
      upstream power source.
   -  ``SiteB`` — Vehicle interface, at the physical connection between the
      EVSE and the vehicle.

.. _telemetry_overvoltage_duration:

**************************
 Exceedance Duration
**************************

-  **Description**: How long the measured voltage stayed above the threshold
   before the fault was raised. Zero for an instantaneous exceedance reported
   without time qualification.
-  **Unit**: Milliseconds (ms)
-  **Resolution**: `1 ms`
