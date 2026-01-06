# unified-error-codes by CharIN

Here you can find the project materials related to **Unified Error Codes**, developed in the CharIN FG Charging Communication Subgroup - Error Codes.

<img width="295" height="251" alt="image" src="https://github.com/user-attachments/assets/2c4efdfd-8829-4631-a5da-1160f2d6c60e" />

As interoperability in the EV charging market depends on consistent fault reporting across stakeholders, the project addresses the lack of a standardized and consistent approach to error codes across **EV, EVSE, CSO/CPO**, which can contribute to **delayed repairs, poor reliability, and reduced user trust** in public charging infrastructure.

### Why this project exists

The materials highlight recurring issues in today’s ecosystem:

* Inconsistent definitions
* Limited diagnostic detail
* Undefined or proprietary error exchange mechanisms
* Complex system interconnectivity
* No actionable outcomes for customers or service technicians

### Foundations and reference publications

The subgroup’s work builds on existing error-code initiatives and publications, including earlier specifications and industry references such as the **MREC (Minimum Required Error Codes)** mission statement and **DIN DKE SPEC 99003**. These references provide a baseline for harmonized error-code definitions, improved interpretability, and more consistent diagnostics across the charging ecosystem.

**MREC (Minimum Required Error Codes)**  
The MREC mission statement promotes implementing a uniform set of error codes to streamline error reporting, interpretability, and diagnostics.

**DIN DKE SPEC 99003**  
CharIN announced the publication of **DIN DKE SPEC 99003**, titled **“Unified Error Codes for a Reliable Electric Vehicle Charging Ecosystem”**. The document was officially released by DIN on **October 1, 2024** and aims to address the lack of clarity and consistency in error reporting during charging failures by establishing a comprehensive and unified set of error codes.

<img width="400" height="130" alt="image" src="https://github.com/user-attachments/assets/34526e65-e78d-4a28-a176-d00f181143b1" />

According to CharIN, the expected benefits include:
- Enhanced user experience through more transparent and user-friendly charging processes
- Improved operational efficiency for CPOs through better service, maintenance, and troubleshooting
- Better product quality assurance for charging station developers and manufacturers through detailed debugging insights

The specification is available as a complimentary PDF download via DIN Media (registration required).

References:
- CharIN news: https://www.charin.global/news/din-dke-spec-99003-unified-error-codes/
- DIN Media listing: https://www.dinmedia.de/en/technical-rule/din-dke-spec-99003/383541627

### What CharIN Error Codes group covers

**1) Error codes definition and coverage**

* Error codes are structured into three categories: **Hardware, Communication, Software**.
* Hardware error codes definition and coverage refined.
* Communication error code coverage including metadata accompanying hardware/software related faults.
* Software error codes definition.
* Clarification of fault/status/parameter definitions and setting up a Git page for community feedback.

**2) EVSE to back office communication pathway**

* Uses **OCPP 2.0.1** for EVSE to back office communication, with an evaluation of **OCPP 2.1** noted.
* OCPP 2.0.1 adds optional JSON fields such as **TechCode** and **TechInfo**. The work group plans recommendations for a common data structure and naming scheme.

**3) EVSE to EV diagnostic communication pathway (DTC sharing)**

* The work describes establishing a redundant pathway for EVSE and EV to share error codes through a diagnostic framework (DTCs), referencing **SAE J2012**, with transport options noted as TBD (Wi-Fi, Bluetooth, Ethernet).
* It also proposes using **DoIP** either through the physical plug or via Wi-Fi between EV and EVSE-capable controllers, and starting with a common presentation layer (J2012) while being flexible at the application layer (UDS vs SOVD).

**4) Link criteria using existing standards**

* The project notes an ongoing connection with the **IEC/ISO 61851-23** work group (IEC/TC69/MT5), with error code definitions pointing to the applicable 61851-23 appendix.
* IEC 61851 Appendix M includes a table defining EVSE error codes for error and emergency shutdown conditions.

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

## Contributing

This project uses a DCO-style sign-off process. Every contribution must be accompanied by a `Signed-off-by:` line in the commit message (commonly added via `git commit -s`).

When contributing:

* Code/tools contributions are submitted under **Apache-2.0**.
* Documentation/specification contributions are submitted under **CC-BY-4.0**.
