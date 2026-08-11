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
   phase. Measured at Side A of the EVSE as defined in IEC 61851-23:2023
   sections 3.7.102 and 3.7.103.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_supply_voltage_l2:

*******************
 Supply Voltage L2
*******************

-  **Description**: The continuous measurement of AC voltage for L2
   phase. Measured at Side A of the EVSE as defined in IEC 61851-23:2023
   sections 3.7.102 and 3.7.103.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_supply_voltage_l3:

*******************
 Supply Voltage L3
*******************

-  **Description**: The continuous measurement of AC voltage for L3
   phase. Measured at Side A of the EVSE as defined in IEC 61851-23:2023
   sections 3.7.102 and 3.7.103.
-  **Unit**: Volts (V)
-  **Resolution**: `1 V`

.. _telemetry_communication_state:

********************
 Communication State
********************

-  **Description**: The state of the communication between EV and charging station.
-  **Unit**: N/A
-  **Resolution**: N/A
-  **Source**: DIN DKE SPEC 99003:2024-10, Table 17 — CommunicationStateType parameter
-  **Values**:

   -  ``SLAC`` — Error occurred during SLAC.
   -  ``SDP`` — Error occurred during SDP.
   -  ``CommunicationSetup`` — Error occurred during CommunicationSetup.
   -  ``ServiceDiscovery`` — Error occurred during ServiceDiscovery.
   -  ``PaymentSelection`` — Error occurred during PaymentSelection.
   -  ``CertificateInstallation`` — Error occurred during CertificateInstallation.
   -  ``CertificateUpdate`` — Error occurred during CertificateUpdate.
   -  ``Authorization`` — Error occurred during Authorization.
   -  ``ChargeParameterDiscovery`` — Error occurred during ChargeParameterDiscovery.
   -  ``CableCheck`` — Error occurred during CableCheck.
   -  ``PreCharge`` — Error occurred during PreCharge.
   -  ``CurrentDemand`` — Error occurred during CurrentDemand.
   -  ``WeldingDetection`` — Error occurred during WeldingDetection.
   -  ``SessionStop`` — Error occurred during SessionStop.

.. include:: definitions_ConnectorLockTelemetry.rst
.. include:: definitions_HighTemperatureTelemetry.rst
.. include:: definitions_PowerModuleTelemetry.rst
.. include:: definitions_UnderCurrentTelemetry.rst
