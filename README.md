# unified-error-codes

## Project overview

Unified Error Codes is a CharIN-led effort to create a standardized, consistent approach to error codes across the EV charging ecosystem (EV, EVSE, CSO/CPO). The project addresses issues such as inconsistent definitions, limited diagnostic detail, proprietary/undefined error exchange mechanisms, and complex interconnectivity that can contribute to delayed repairs, lower reliability, and reduced user trust in public charging infrastructure.

## Scope and deliverables

The project structures error codes into three categories:
Hardware, Communication, Software.

Planned milestones:
Hardware error codes: definition and coverage refined
Communication error code coverage
Software error codes: definition
Community feedback: setting up a Git page

Standardization links and references:
Connection work with IEC/ISO 61851-23 work group (IEC/TC69/MT5), with error code definitions pointing to applicable IEC 61851-23 appendix content.
EVSE to back office pathway based on OCPP 2.0.1 (with evaluation of OCPP 2.1 noted). 
Diagnostic frameworks and naming/data structure work referencing ISO 14229 and SAE J2012 DTC concept

## Repository licensing

This repository uses a mixed open-source licensing model:

Software code and tools: Apache License 2.0 (Apache-2.0).
Documentation and specifications: Creative Commons Attribution 4.0 International (CC BY 4.0).
SPDX short identifiers used in file headers follow the SPDX License List.

Repository layout (intended):
- LICENSE_CODE: Apache-2.0 (full text)
- LICENSE_DOCS: CC-BY-4.0 (legal code)
- NOTICE: Apache-2.0 notices/attributions
- docs/ and specs/: CC-BY-4.0
- tools/: Apache-2.0

Required file headers:
Code files:
SPDX-License-Identifier: Apache-2.0
Copyright CharIN e.V. and Contributors

Documentation and specification files:
SPDX-License-Identifier: CC-BY-4.0
Copyright CharIN e.V. and Contributors

## Contributing

This project uses a Developer Certificate of Origin (DCO) process. Every contribution must be accompanied by a “Signed-off-by:” line in the commit message (commonly added via `git commit -s`).

When contributing:
- Code/tools contributions are submitted under Apache-2.0.
- Documentation/specification contributions are submitted under CC-BY-4.0.
