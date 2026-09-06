..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _ocpp16_error_code_delivery:

*******************************
 Reporting an Error Code
*******************************

Message
=======

An error code is reported in a ``StatusNotification.req`` message.

OCPP 1.6 caps ``info`` and ``vendorErrorCode`` at 50 characters each, which is
why DIN DKE SPEC 99003 pairs every ``StatusNotification.req`` with a
``DataTransfer.req`` carrying the detail that does not fit. An error code name
fits, so this edition needs no second message. ``DataTransfer.req`` is left
unused and available to a future edition that carries telemetry.

Field usage
===========

.. list-table::
   :header-rows: 1
   :widths: 22 20 58

   -  -  Field
      -  Value
      -  Description

   -  -  ``connectorId``
      -  integer
      -  Required. The connector the condition was detected on, or ``0`` when
         the condition belongs to the charging station as a whole rather than
         to one connector. OCPP 1.6 admits only ``Available``, ``Unavailable``
         and ``Faulted`` as the status of connector ``0``.

   -  -  ``errorCode``
      -  ``ChargePointErrorCode``
      -  Required by OCPP 1.6, whose enumeration is closed and cannot carry an
         error code name. It shall be set to the value that
         :ref:`ocpp16_error_code_mapping` gives for the reported error code.

   -  -  ``status``
      -  ``ChargePointStatus``
      -  Required. ``Faulted`` when the condition prevents energy delivery. Any
         other status means, in OCPP 1.6, that charging operations remain
         possible and the condition is a warning.

   -  -  ``timestamp``
      -  dateTime
      -  Optional in OCPP 1.6; required by this document. The time the
         condition was detected, in UTC.

   -  -  ``vendorId``
      -  ``CiString255Type``
      -  Required. Shall be ``org.charin.uec.v1``, which identifies
         ``vendorErrorCode`` as an error code name from this document. OCPP 1.6
         recommends a reversed DNS name for this field.

   -  -  ``vendorErrorCode``
      -  ``CiString50Type``
      -  Required. Shall be the error code name, spelled exactly as
         :doc:`../error_codes/definitions` spells it. Error code names are
         therefore at most 50 characters long.

   -  -  ``info``
      -  ``CiString50Type``
      -  Not used by this document. Reserved.

A charging management system that does not recognise ``vendorId`` ignores
``vendorId`` and ``vendorErrorCode``, and is left with the ``errorCode``,
``status`` and ``timestamp`` it would have received anyway. Reporting error
codes this way therefore does not break an existing OCPP 1.6 deployment, and no
configuration key is needed to switch it off.

Raising and clearing an error
=============================

An error code in OCPP 1.6 is a state and not an event: each
``StatusNotification.req`` replaces whatever the charging management system last
recorded for that connector, and OCPP 1.6 defines no message that ends an error.

When the reported condition ends, the EVSE shall send a further
``StatusNotification.req`` for the same ``connectorId`` with ``errorCode`` set
to ``NoError``, omitting ``vendorId`` and ``vendorErrorCode``, and with
``status`` set to the status the connector has returned to.

A connector therefore has at most one error code at a time. Where several
conditions hold at once, the EVSE shall report the one it considers the root
cause. Reporting several error codes as a correlated group is out of scope in
this edition.

Example
=======

A contactor that failed to reach its commanded state, reported against
connector 1:

.. code-block:: json

   {
     "connectorId": 1,
     "errorCode": "PowerSwitchFailure",
     "status": "Faulted",
     "timestamp": "2026-09-06T14:32:10Z",
     "vendorId": "org.charin.uec.v1",
     "vendorErrorCode": "ContactorPosition"
   }

The same connector once the condition has ended:

.. code-block:: json

   {
     "connectorId": 1,
     "errorCode": "NoError",
     "status": "Available",
     "timestamp": "2026-09-06T14:41:02Z"
   }
