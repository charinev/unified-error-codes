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

.. _telemetry_unified_error_code_basic_metadata:

**********************************
 Unified Error Code Basic Metadata
**********************************

.. code-block:: text

   UnifiedErrorCodeBasicMetadata DEFINITIONS AUTOMATIC TAGS ::= BEGIN

   EXPORTS ALL;

   BasicMetadata ::= SEQUENCE {
       reportingSource ReportingSource,
       evseId EVSEIdentifier OPTIONAL,
       evccId EVCCIdentifier OPTIONAL,
       evseMacAddress MACAddress OPTIONAL,
       evccMacAddress MACAddress OPTIONAL,
       communicationProtocol CommunicationProtocol OPTIONAL,
       sessionContext SessionContext,
       ...
   }

   ReportingSource ::= UTF8String ("EV" | "EVSE", ...)
   EVSEIdentifier ::= UTF8String (SIZE (1..MAX))
   EVCCIdentifier ::= OCTET STRING (SIZE (68))
   MACAddress ::= OCTET STRING (SIZE (6))

   CommunicationProtocol ::= SEQUENCE {
       hlcProtocol HLCProtocol,
       versionMajor VersionNumber,
       versionMinor VersionNumber,
       ...
   }

   HLCProtocol ::= UTF8String (
       "DIN SPEC 70121" | "ISO 15118-2" | "ISO 15118-20", ...
   )
   VersionNumber ::= INTEGER (0..65535)

   SessionContext ::= SEQUENCE {
       timestamp UTCDateTime,
       sessionId SessionIdentifier OPTIONAL,
       energyTransferMode EnergyTransferMode OPTIONAL,
       controlMode ControlMode OPTIONAL,
       messageName MessageName OPTIONAL,
       ...
   }
   UTCDateTime ::= GeneralizedTime
   SessionIdentifier ::= OCTET STRING (SIZE (1..MAX))

   EnergyTransferMode ::= UTF8String (
       "AC" | "AC_BPT" | "AC_DER_IEC" | "AC_DER_SAE" | "DC" | "DC_BPT" |
       "DC_ACDP" | "DC_ACDP_BPT" | "WPT" | "MCS" | "MCS_BPT", ...
   )
   ControlMode ::= UTF8String ("Scheduled" | "Dynamic", ...)
   MessageName ::= CHOICE {
       slac SLACMessageName,
       v2g V2GMessageName,
       ...
   }
   SLACMessageName ::= UTF8String ("CM_SLAC_PARM" | "CM_SLAC_MATCH", ...)
   V2GMessageName ::= UTF8String (
       "SessionSetup" | "PaymentServiceSelection" | "PreCharge", ...
   )

   END

.. include:: definitions_ConnectorLockTelemetry.rst
.. include:: definitions_TemperatureTelemetry.rst
.. include:: definitions_PowerModuleTelemetry.rst
.. include:: definitions_OverCurrentTelemetry.rst
.. include:: definitions_OvervoltageTelemetry.rst
.. include:: definitions_UnderCurrentTelemetry.rst
