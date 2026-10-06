..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _telemetry_undercurrent_location:

************************
 UnderCurrent Location
************************

-  **Description**: The location at which the under-current condition
   was measured.
-  **Values**:

   -  ``Supply`` — EVSE input / Site A.
   -  ``Transmission`` — EVSE-to-EV path / Site B.

.. _telemetry_undercurrent_expected:

***************************
 Expected Current Output
***************************

-  **Description**: The current committed for the active charging
   schedule at the reported location.
-  **Unit**: Amperes (A)
-  **Resolution**: `0.1 A`

.. _telemetry_undercurrent_actual:

*************************
 Actual Current Output
*************************

-  **Description**: The current measured at the reported location at
   the time of the under-current condition.
-  **Unit**: Amperes (A)
-  **Resolution**: `0.1 A`
