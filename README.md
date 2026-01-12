<p align="center">
  <img src="https://github.com/charinev/opnc/assets/83767351/1688cfe1-97de-46c7-9b97-65bcec242193" alt="CharIN Logo" width="200"/>
</p>

# Unified Error Codes

This repository contains the draft specification for Unified Error Codes. It represents a joint effort to standardize error codes and diagnostics across the entire EV charging ecosystem.

Here you can find the project materials related to **Unified Error Codes**, developed in the CharIN FG Charging Communication Subgroup - Error Codes. 

## The Problem

The EV charging industry faces significant operational challenges due to a lack of standardization in diagnostics. This fragmentation creates costs, hinders reliability, and frustrates drivers. It can contribute to **delayed repairs, poor reliability, and reduced user trust** in public charging infrastructure.

* **Lack of a Standardized, Comprehensive Definition**

    As a result, each Charging Station vendor implements its own proprietary set of error codes. This creates a major integration and operational problem for CPOs (Charge Point Operators) and CSMS (Charging Station Management System) providers, who must manage and map custom error sets from multiple vendors. This fragmentation significantly increases the effort and cost required to ensure network reliability.

* **Ambiguous Reporting Protocols between Charging Station and CSMS**

    While OCPP is the common protocol between Charging Station and CSMS (Charging Station Management System), it does not precisely define *how* specific error codes must be reported. This ambiguity leads to different interpretations and implementations, creating uncertainty around:
    - How to report transient errors.
    - Which standard OCPP components should report which errors.
    - How to handle errors for non-standard components.
    - How to include additional diagnostic telemetry data.
    As a result, vendors often implement error reporting in different ways or create separate, proprietary channels for diagnostics, further complicating integration.

* **Undefined Charger Response to Faults**

    Current standards (e.g., IEC) primarily focus on the minimum electrical safety requirements for shutting down a charging session. They do not, however, define a complete, required response to a fault. This includes a critical omission: there are almost no requirements for informing the EV driver about the problem. This lack of clear, standardized behavior — a famous example being the "connector lock failure" — leaves the driver with a failed session without explanation or guidance.

* **No Defined Bidirectional Error Exchange between Charing Station and EV**

    ISO 15118-202 opens a pathway for data exchange between the Charging Station and the EV. However, it only defines the *transport* layer, not the *schema* or *content* of the error codes to be exchanged. Furthermore, there is no standard way to exchange critical diagnostic data *before* high-level communication is established.

* **Lack of Synchronization with Vehicle Diagnostics (DTCs)**

    The EV already has a well-defined set of Diagnostic Trouble Codes (DTCs). During charging, the EV and Charging Station share critical system components (e.g., PLC network, Control Pilot, V2G communication). Synchronizing error codes and telemetry from both the vehicle and the charger would provide a complete, unified view of system health, enabling a much more powerful and accurate root-cause analysis.

* **No actionable outcomes for customers or service technicians**

## Foundations and reference publications

The subgroup’s work builds on existing error-code initiatives and publications, including earlier specifications and industry references:

* [DIN DKE SPEC 99003](https://www.dinmedia.de/en/technical-rule/din-dke-spec-99003/383541627)
* [Korea Smart Grid Association: Fault Identification Numbers](https://ksga.org/sgstandard/Board/7260/detailView.do)
* [MREC (Managed Recharging Error Codes)](https://inl.gov/chargex/mrec)

A large majority of the error codes defined in each of these specifications overlap. This signals a clear consensus in the market and a prime opportunity for a common, unified definition. These references provide a baseline for harmonized error-code definitions, improved interpretability, and more consistent diagnostics across the charging ecosystem.

<img width="400" height="130" alt="image" src="https://github.com/user-attachments/assets/34526e65-e78d-4a28-a176-d00f181143b1" />

As DIN DKE SPEC 99003 is the outcome of a CharIN Working Group, we are using it as a baseline. However, the principle of this project is to cover the requirements and use cases from all of these documents.

## Scope

### Error Codes Data Model

Defining the semantics of error codes: **when** an error should be raised, **what** it means, and **what** associated telemetry and measurement data is required for enhanced root-cause analysis. This data model is protocol-agnostic, meaning it can be transported over multiple protocols (each requiring its own specific encoding definition).

The goal is to streamline diagnostics and improve the uptime of the charging network. Domains include, but are not limited to:

* **Hardware:** e.g., cable resistance degradation, power module faults, Control Pilot voltage issues.
* **Software:** e.g., memory faults, application crashes.
* **Communication:** e.g., PLC signal quality, EXI decoding errors, TLS handshake failures, OCPP message timeouts.

The expected benefits of this work include:
- Enhanced user experience through more transparent and user-friendly charging processes
- Improved operational efficiency for CPOs through better service, maintenance, and troubleshooting
- Better product quality assurance for charging station developers and manufacturers through detailed debugging insights

### Error and Diagnostic Exchange Protocol between Charging Station and CSMS

Defining how the Charging Station should deliver this reliability-essential data to the CSMS backend. This includes specifying how the data model should be encoded within the OCPP protocol. 

### Error and Diagnostic Exchange Protocol between Charging Station and EV

Defining how error and diagnostic data should be encoded between the (Charging Station) and EV either through ISO 15118-202 or another redudant pathway. This also includes defining a potential pathway to exchange critical diagnostic data *before* high-level communication is established.

### Alignment with Vehicle Diagnostics (DTC/DTS)

Defining how these new Charging Station error codes relate to and integrate with the existing EV diagnostic system (Diagnostic Trouble Codes / Diagnostic Trouble Service).

### Link criteria using existing standards

* The project notes an ongoing connection with the **IEC/ISO 61851-23** work group (IEC/TC69/MT5), with error code definitions pointing to the applicable 61851-23 appendix.
* IEC 61851 Appendix M includes a table defining EVSE error codes for error and emergency shutdown conditions.

### Focus Group Project Plan
<img width="1187" height="677" alt="image" src="https://github.com/user-attachments/assets/74665d5a-d62d-4763-89d8-58997291e9f1" />


## Contribute

We believe that collaborative work can make error code unification an effective reality for the e-mobility industry.
All contributions are welcome. Please check the [contribution guidelines](NOTICE.md).

This project uses a DCO-style sign-off process. Every contribution must be accompanied by a `Signed-off-by:` line in the commit message (commonly added via `git commit -s`).

When contributing:

* Code/tools contributions are submitted under **Apache-2.0**.
* Documentation/specification contributions are submitted under **CC-BY-4.0**.

## Governance

This project is an open initiative led by the CharIN e.V. Working Group.
We welcome contributions from the entire e-mobility community. All discussions, proposals, and changes will be managed transparently through GitHub Issues and Pull Requests.

## Disclaimer

This specification should be seen as an addition to available industry standards and best practices.
It is developed by the community, and everyone is free and invited to contribute.

## Licensing

This repository uses a **mixed open-source licensing model**:

* **Apache License 2.0 (Apache-2.0)** for software code and tools
* **Creative Commons Attribution 4.0 International (CC-BY-4.0)** for documentation and specifications

Required file headers:

For software code files:

* `SPDX-License-Identifier: Apache-2.0`
* `Copyright CharIN e.V. and Contributors`

For documentation and specification files:

* `SPDX-License-Identifier: CC-BY-4.0`
* `Copyright CharIN e.V. and Contributors`
