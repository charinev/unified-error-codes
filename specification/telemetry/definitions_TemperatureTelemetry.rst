..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _telemetry_temperature_actual:

********************
 Actual Temperature
********************

-  **Description**: The measured temperature of the EVSE or EV component
   reported as the source of the temperature fault.
-  **Unit**: Degrees Celsius (°C)
-  **Resolution**: `1 °C`

.. _telemetry_temperature_threshold:

***********************
 Temperature Threshold
***********************

-  **Description**: The calibrated safety or performance temperature
   threshold for the reporting component, defined by the applicable standard
   or the manufacturer. For an overtemperature fault this is the maximum
   temperature above which the fault is raised; for an under-temperature
   fault this is the minimum operating temperature below which the fault is
   raised.
-  **Unit**: Degrees Celsius (°C)
-  **Resolution**: `1 °C`

.. _telemetry_temperature_location:

**********************
 Temperature Location
**********************

-  **Description**: The subsystem or device component against which the
   temperature is reported.
-  **Values**:

   -  ``Cable`` — Charging cable.
   -  ``CablePositive`` — Charging cable positive line.
   -  ``CableNegative`` — Charging cable negative line.
   -  ``CableHousingPositive`` — Cable housing positive line.
   -  ``CableHousingNegative`` — Cable housing negative line.
   -  ``ConnectorPositive`` — Connector/Plug positive pin.
   -  ``ConnectorNegative`` — Connector/Plug negative pin.
   -  ``PowerModulesSideA`` — Power modules Side A.
   -  ``PowerModulesSideB`` — Power modules Side B.
   -  ``Electronics`` — Electronic/control components.
   -  ``Socket`` — Charging socket.
   -  ``SocketPositive`` — Charging socket positive pin.
   -  ``SocketNegative`` — Charging socket negative pin.
   -  ``Battery`` — EV Battery.
   -  ``Body`` — EVSE/EV body.
