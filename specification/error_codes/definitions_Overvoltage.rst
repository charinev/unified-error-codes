..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_overvoltage:

*************
 Overvoltage
*************

Description
===========

A condition where the measured voltage at a defined electrical interface exceeds the allowable threshold specified by applicable standards and/or manufacturer-defined limits, evaluated relative to the physical location within the EV–EVSE system.
Overvoltage shall be classified based on measurement location (“Side”), independent of energy direction or power type (AC or DC).

Side A - Supply Interface (EVSE Input)
Overvoltage at Side A is a voltage exceeding limits at the EVSE terminals connected to the upstream power source (e.g., grid or local generation).

Side B  Vehicle Interface (EV-EVSE Connection)
Overvoltage at Side B is a voltage exceeding limits at the physical connection between the EVSE and the vehicle (connector or socket outlet), as measured at the interface.

Trigger Conditions
==================
Threshold Exceedance
   Measured voltage > allowable limit (per applicable standard or manufacturer-defined value)

Measurement Location
   Side A (supply interface), or
   Side B (vehicle interface)

Time Qualification
   Exceeds threshold for a defined minimum duration (to filter transients), or
   Instantaneous exceedance where explicitly required (e.g., protection limits)

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

{
  "basicMetadata": {
    "eventId": 10234567,
    "timestamp": "2026-05-18T14:32:10Z",
    "identifiers": {
      "evId": "EV_9F3A21",
      "evseId": "EVSE_DC_FAST_4021",
      "sessionId": "SESSION_778899"
    },
    "faultAttribution": {
      "suspectedPrimary": "EVSE",
      "evaluationBasis": "AggregatedEvidence"
    },
    "severity": "FAILED"
  },
  "coreError": {
    "error": {
      "errorCode": "OV_DC_SITEB_DIFF",
      "errorDomain": "Hardware",
      "errorCategory": "Overvoltage",
      "errorSubType": "DC+ to DC-",
      "isFatal": true
    },
    "rootCause": {
      "primary": "EVSE Power Module Regulation Failure",
      "secondary": "Voltage Control Loop Instability",
      "failureMode": "Output voltage exceeded commanded setpoint"
    },
    "chargingContext": {
      "phase": "Charging",
      "subPhase": "CurrentRamp",
      "protocolLayer": "ISO15118",
      "message": "CurrentDemand"
    },
    "failureCriteria": {
      "iec61851_23": {
        "requirement": "8.2.2",
        "requirementName": "DC Output Voltage Limits",
        "failureCondition": "Measured voltage exceeded maximum allowable DC output voltage",
        "evaluationMethod": "Direct measurement at Side B connector"
      },
      "manufacturerSpecific": [
        {
          "manufacturer": "OEM_X",
          "requirementId": "MSP-DC-OV-001",
          "failureCondition": "Voltage > 520 V for > 100 ms"
        }
      ]
    },
    "associatedErrorEvidence": {
      "location": {
        "system": "EVSE",
        "subsystem": "PowerModule",
        "component": "DC Output Stage"
      },
      "expectedVsActual": [
        {
          "parameter": "Voltage_SiteB_DC+_to_DC-",
          "expected": "<= 500 V",
          "actual": "542 V",
          "evaluation": "Exceeded threshold"
        },
        {
          "parameter": "Voltage_SiteB_DC+_to_PE",
          "expected": "<= 250 V",
          "actual": "248 V",
          "evaluation": "Within limit"
        },
        {
          "parameter": "Voltage_SiteA_AC_L-L",
          "expected": "480 V ±10%",
          "actual": "477 V",
          "evaluation": "Within limit"
        }
      ]
    }
  },
  "extensions": {
    "overvoltageContext": {
      "site": "SiteB",
      "measurementReference": {
        "evse": "Connector",
        "ev": "Inlet"
      },
      "powerType": "DC",
      "conductorPair": "DC+ to DC-",
      "thresholdSource": "IEC61851-23",
      "thresholdValue": "500 V",
      "measuredValue": "542 V",
      "durationMs": 120,
      "violationType": "Sustained",
      "dvdt": "14 V/ms",
      "sampleWindow": {
        "samples": 12,
        "maxVoltage": "542 V",
        "avgVoltage": "512 V"
      },
      "connectionState": "Plugged"
    },
    "operationalContext": {
      "shutdownType": "Emergency",
      "triggerCondition": "Voltage exceeded threshold for >100 ms during active charging",
      "chargeStateAtFailure": "Active Charging"
    },
    "iso15118": {
      "lastMessage": "CurrentDemand",
      "sessionState": "EnergyTransfer"
    },
    "dtc": {
      "vehicleDTC": "P0C1A",
      "evseDTC": "EVSE_OV_004"
    },
    "errorCodeTuple": {
      "site": "B",
      "system": "EVSE",
      "type": "DC",
      "failureMode": "Overvoltage_Differential"
    }
  }
}



