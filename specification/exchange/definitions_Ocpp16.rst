..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _ocpp16_exchange:

*******************************
 EVSE and CSMS (OCPP 1.6)
*******************************

An EVSE reports error codes to the charging management system (CSMS)
over OCPP 1.6 JSON with two messages: a ``StatusNotification.req`` that
names the error code, and a ``DataTransfer.req`` that carries the
details.

.. list-table:: Error code exchange over OCPP 1.6
   :widths: 25 75

   -  -  **vendorId**
      -  ``urn:uec:0.1.0``
   -  -  **Messages**
      -  ``StatusNotification.req``, ``DataTransfer.req``
   -  -  **messageId**
      -  ``ErrorCodeExtension``
   -  -  **Details**
      -  ``ErrorCodeExtension``, in the ``data`` field of the
         ``DataTransfer.req``
   -  -  **ASN.1 module**
      -  :download:`UnifiedErrorCodeExchange.asn1`
   -  -  **Encoding**
      -  JSON Encoding Rules (JER, ITU-T X.697)

The ``vendorId`` is ``urn:uec:`` followed by the version of this
specification. It is the ``vendorId`` of both messages, and it
identifies them as carrying error codes from this specification.

OCPP 1.6 limits ``info`` and ``vendorErrorCode`` of a
``StatusNotification.req`` to 50 characters each, which is too little
for telemetry. The ``DataTransfer.req`` carries what does not fit.

UnifiedErrorCodes configuration key
===================================

The configuration key ``UnifiedErrorCodes`` controls whether the EVSE
sends the ``DataTransfer.req`` messages described here.

Its purpose is to switch them off for a backend that cannot handle them
and would reject every one of them. When it is false, the EVSE shall not
send them. The EVSE sends the ``StatusNotification.req`` messages as
described below whatever its value.

.. list-table:: UnifiedErrorCodes configuration key
   :widths: 30 70

   -  -  **Key**
      -  ``UnifiedErrorCodes``
   -  -  **Type**
      -  boolean
   -  -  **Accessibility**
      -  RW
   -  -  **Default**
      -  true
   -  -  **Applicability**
      -  Required for an EVSE that implements this specification

StatusNotification.req
======================

An error code is always reported in a ``StatusNotification.req``, as is
usual in OCPP 1.6, one for each report. The complete message, with the
telemetry, additionally comprises a ``DataTransfer.req``.

The ``StatusNotification.req`` carries the ``eventId`` of the report in
``info``. The report in the ``DataTransfer.req`` has the same
``eventId``, so that the two messages can be correlated: they describe
the same event. Only the ``StatusNotification.req`` identifies the
connector.

.. list-table:: StatusNotification.req fields
   :header-rows: 1
   :widths: 22 24 54

   -  -  Data field
      -  Field type
      -  Description

   -  -  ``connectorId``
      -  integer, at least 0
      -  Required. The connector the error was detected on. ``0`` is used
         if the error is for the charging station main controller.

   -  -  ``errorCode``
      -  ``ChargePointErrorCode``
      -  Required. The value given for the error code in
         :numref:`ocpp16_error_code_mapping`, or ``OtherError`` for an
         error code that it does not list. The error code is identified
         by ``vendorErrorCode``.

   -  -  ``status``
      -  ``ChargePointStatus``
      -  Required. The current status of the connector.

   -  -  ``timestamp``
      -  dateTime
      -  Required. The ``timestamp`` of the report, in UTC, as an ISO 8601
         date and time.

   -  -  ``vendorId``
      -  ``CiString255Type``
      -  Required. ``urn:uec:0.1.0``. It identifies
         ``vendorErrorCode`` as an error code from this
         specification.

   -  -  ``vendorErrorCode``
      -  ``CiString50Type``
      -  Required. The ``code`` of the report, as a string: the name of
         the error code in the ``ErrorCodeId`` type of the ASN.1
         module, for example ``ConnectorLockFailure``.

   -  -  ``info``
      -  ``CiString50Type``
      -  Required. The ``eventId`` of the report, as it is written in
         JER: 32 hexadecimal digits.

.. _ocpp16_error_code_mapping:

.. list-table:: ChargePointErrorCode of an error code
   :header-rows: 1
   :widths: 50 50

   -  -  Error code
      -  ``errorCode``

   -  -  ``ConnectorLockFailure``
      -  ``ConnectorLockFailure``

   -  -  ``HighTemperature``
      -  ``HighTemperature``

   -  -  ``Overvoltage``
      -  ``OverVoltage``

   -  -  ``SideBOverCurrentFailure``
      -  ``OverCurrentFailure``

This specification does not report the end of an error. The EVSE sends a
``StatusNotification.req`` for later status changes as OCPP 1.6 requires,
with ``errorCode`` ``NoError`` when no error remains.

DataTransfer.req
================

.. list-table:: DataTransfer.req fields
   :header-rows: 1
   :widths: 22 24 54

   -  -  Data field
      -  Field type
      -  Description

   -  -  ``vendorId``
      -  ``CiString255Type``
      -  Required. ``urn:uec:0.1.0``.

   -  -  ``messageId``
      -  ``CiString50Type``
      -  Required. ``ErrorCodeExtension``.

   -  -  ``data``
      -  text, unlimited length
      -  Required. An ``ErrorCodeExtension`` encoded with JER. It is a
         JSON array of one or more reports.

If the CSMS answers with a ``DataTransfer.conf`` whose ``status`` is not
``Accepted``, the EVSE shall not send that ``DataTransfer.req`` again.

Forwarding error codes from the EV
==================================

An EVSE shall forward the error codes it received from the EV to the CSMS.
For each message with error codes that it receives from the EV, the EVSE
shall:

-  Decode the ``ErrorCodeExtension`` received over ISO 15118-202.

-  Send each report of it in a ``StatusNotification.req``, as described
   above. The ``connectorId`` is the connector the EV is connected to.

-  Encode the ``ErrorCodeExtension`` again as JSON, with JER, and send it
   in the ``data`` field of one ``DataTransfer.req``.

The ``eventId`` in ``info`` is what lets the CSMS correlate the
``StatusNotification.req`` messages with the reports of the
``DataTransfer.req``. The reports keep their fields, including
``eventId`` and ``origin``, which stays ``EV`` for an error that the EV
detected.

The EVSE does not send the ``DataTransfer.req`` if the
``UnifiedErrorCodes`` configuration key is false.

Example
=======

A connector lock failure in the EV, detected on connector 1. First the
``StatusNotification.req``:

.. code-block:: json

   {
     "connectorId": 1,
     "errorCode": "ConnectorLockFailure",
     "status": "Faulted",
     "info": "3f0c2b7e5d1a4c8e9b647a2e1d90c5f3",
     "timestamp": "2026-10-06T14:32:10Z",
     "vendorId": "urn:uec:0.1.0",
     "vendorErrorCode": "ConnectorLockFailure"
   }

Then the ``DataTransfer.req``. Its ``data`` is a string that holds the
JSON text of the reports:

.. code-block:: json

   {
     "vendorId": "urn:uec:0.1.0",
     "messageId": "ErrorCodeExtension",
     "data": "[{\"eventId\":\"3f0c2b7e5d1a4c8e9b647a2e1d90c5f3\",\"timestamp\":\"20261006143210Z\",\"origin\":\"EV\",\"code\":\"ConnectorLockFailure\",\"telemetry\":{\"position\":\"Unlocked\",\"command\":\"Lock\"}}]"
   }
