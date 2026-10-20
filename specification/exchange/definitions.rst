..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

####################
 Exchange protocols
####################

This chapter defines how a Unified Error Code and its related telemetry
are exchanged between the parties of a charging system.

*****************************
 EV and EVSE (ISO 15118-202)
*****************************

Unified Error Codes are exchanged between an EV and an EVSE using the
Event Notification Protocol (ENP) of ISO 15118-202, through an ENP
extension.

An ENP message carries a list of extensions. Each extension is an
``extensionID``, a 16-octet identifier, followed by an ``extensionValue``
of the ASN.1 type that identifier selects.

This specification defines one more extension in the same way.

.. list-table:: Error code extension
   :widths: 25 75

   -  -  **extensionID**
      -  ``0F9FA02C-B967-40FF-AF1D-50BF09A1D8DC``
   -  -  **extensionValue**
      -  ``ErrorCodeExtension``
   -  -  **ASN.1 module**
      -  :download:`UnifiedErrorCodeExchange.asn1`
   -  -  **Encoding**
      -  Canonical Octet Encoding Rules (COER, ISO/IEC 8825-7, also
         published as ITU-T X.696)
   -  -  **Status**
      -  Proposed, not yet registered with ISO 15118-202 (`issue #65
         <https://github.com/charinev/unified-error-codes/issues/65>`_).

The ASN.1 module is the normative definition of the extension and is
maintained as a separate document. The ``extensionValue`` is the
``ErrorCodeExtension`` type defined in it, a list of one or more error
code reports, so that several errors can be reported in one message.

A given report has exactly one valid COER encoding.

Each report has the following fields:

.. list-table:: Fields of an error code report
   :header-rows: 1
   :widths: 20 15 65

   -  -  Field
      -  Presence
      -  Description

   -  -  ``eventId``
      -  Required
      -  A UUID that identifies the report. The side that detects the
         error creates it, and it stays the same when the report is
         forwarded.

   -  -  ``timestamp``
      -  Required
      -  When the error was detected, in UTC and to the second, in the
         form ``YYYYMMDDhhmmssZ``.

   -  -  ``origin``
      -  Required
      -  The side that detected the error, ``EV`` or ``EVSE``.

   -  -  ``code``
      -  Required
      -  The name of one error code.

   -  -  ``telemetry``
      -  Optional
      -  The signals specific to that code.

The ``telemetry`` type is selected by ``code``. It is absent for a code
without related telemetry.

A value from a fixed list, such as ``origin``, is a string limited to the
values of that list, written with the capitalization of this
specification.

COER encoding example
=====================

A connector lock failure that the EV detected: the lock stayed unlocked
after a lock command. The report, shown in JER for readability:

.. code-block:: json

   [
     {
       "eventId": "3f0c2b7e5d1a4c8e9b647a2e1d90c5f3",
       "timestamp": "20261006143210Z",
       "origin": "EV",
       "code": "ConnectorLockFailure",
       "telemetry": { "position": "Unlocked", "command": "Lock" }
     }
   ]

Its COER encoding, which is the ``extensionValue``, is 75 octets:

.. code-block:: none

   01 01                       one report
   40                          preamble: telemetry present
   3F 0C 2B 7E 5D 1A 4C 8E     eventId
   9B 64 7A 2E 1D 90 C5 F3
   0F 32 30 32 36 31 30 30 36  timestamp, "20261006143210Z"
      31 34 33 32 31 30 5A
   02 45 56                    origin, "EV"
   14 43 6F 6E 6E 65 63 74 6F  code, "ConnectorLockFailure"
      72 4C 6F 63 6B 46 61 69
      6C 75 72 65
   0F                          telemetry, 15 octets
   00                          preamble: no extensions
   08 55 6E 6C 6F 63 6B 65 64  position, "Unlocked"
   04 4C 6F 63 6B              command, "Lock"

.. include:: definitions_Ocpp16.rst
