..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _ocpp2x_error_code_delivery:

*******************************
 Reporting an Error Code
*******************************

Message
=========

An error code is reported in a ``NotifyEventRequest`` message.

OCPP 2.x has no equivalent of the OCPP 1.6 ``ChargePointErrorCode``
enumeration. ``StatusNotificationRequest`` carries no error information at all
in OCPP 2.x, and OCPP 2.1 deprecates it. A fault is instead reported against the
device model, as a component, a variable and the value that variable took.

Reporting an error code over OCPP 2.x therefore takes two things, and this
section specifies both: which component and variable a given error code is
reported against, in :ref:`ocpp2x_device_model_mapping`; and where the error
code name itself travels, so that a charging management system can identify the
condition without having to infer it from the device model.

Field usage
===========

The fields below are those of ``EventDataType``, one element of the
``eventData`` list of ``NotifyEventRequest``.

.. list-table::
   :header-rows: 1
   :widths: 24 18 58

   -  -  Field
      -  Value
      -  Description

   -  -  ``component``
      -  ``ComponentType``
      -  Required. Shall be the component that
         :ref:`ocpp2x_device_model_mapping` gives for the reported error code.
         ``evse.id`` and ``evse.connectorId`` shall be set when the condition
         belongs to one EVSE or one connector rather than to the charging
         station as a whole. Where a charging station has several instances of
         a component, ``component.instance`` identifies the affected one.

   -  -  ``variable``
      -  ``VariableType``
      -  Required. Shall be the variable that
         :ref:`ocpp2x_device_model_mapping` gives for the reported error code.

   -  -  ``actualValue``
      -  string[0..2500]
      -  Required. The value the variable took, as
         :ref:`ocpp2x_device_model_mapping` gives it.

   -  -  ``techCode``
      -  string[0..50]
      -  Required by this document, optional in OCPP 2.x. Shall be the error
         code name, spelled exactly as :doc:`../error_codes/definitions` spells
         it. Error code names are therefore at most 50 characters long.

   -  -  ``techInfo``
      -  string[0..500]
      -  Not used by this document. Reserved.

   -  -  ``eventId``
      -  integer
      -  Required. Identifies this event so that another event can name it as
         its cause.

   -  -  ``timestamp``
      -  dateTime
      -  Required. The time the condition was detected, in UTC.

   -  -  ``trigger``
      -  ``EventTriggerEnumType``
      -  Required. ``Alerting`` for a condition the firmware detects itself and
         for a threshold that has been passed. ``Delta`` where the report is
         driven by a configured monitor watching a value change.

   -  -  ``eventNotificationType``
      -  ``EventNotificationEnumType``
      -  Required. ``HardWiredNotification`` where the firmware raises the
         condition itself rather than a configured monitor doing so.

   -  -  ``cleared``
      -  boolean
      -  Set to ``true`` on the event that ends a condition. See below.

   -  -  ``cause``
      -  integer
      -  Optional. The ``eventId`` of the event considered to be the cause of
         this one.

   -  -  ``severity``
      -  integer
      -  Not used by this document. This field exists only in OCPP 2.1, and
         severity classification of error codes is out of scope in this
         edition.

A charging management system that does not recognise the error code name in
``techCode`` is left with the component, variable and value it would have
received anyway. Reporting error codes this way therefore adds no message and
no device model entry that an OCPP 2.x deployment does not already have.

Raising and clearing an error
=============================

A condition that lasts is reported against a boolean state variable such as
``Problem``, ``Active`` or ``Overload``. The EVSE shall report it with
``actualValue`` set to ``"true"`` when the condition begins, and shall report
the same component and variable again with ``actualValue`` set to ``"false"``
and ``cleared`` set to ``true`` when it ends.

A condition that is instantaneous or self-resetting is reported once, against
the ``Operated`` or ``Complete`` variable of the component. OCPP 2.x defines
those two variables as appearing only in event notifications, where they are
always true, so no clearing event follows.

A condition detected by crossing a threshold is reported with ``actualValue``
set to the measured value rather than to a boolean, and is cleared by a further
event with ``cleared`` set to ``true`` once the value has returned within the
threshold.

Where several conditions hold at once, the EVSE should report the one it
considers the root cause first, and may report the others with ``cause`` set to
the ``eventId`` of that first event. Defining how a charging management system
is to treat such a group is out of scope in this edition.

Differences between OCPP 2.0.1 and OCPP 2.1
===========================================

``NotifyEventRequest`` and ``EventDataType`` are otherwise identical in the two
versions, and this section applies unchanged to both. The one difference that
touches it is ``EventDataType.severity``, which OCPP 2.1 adds and this document
does not use.

Example
=========

A contactor that failed to reach its commanded state, reported against
connector 1 of EVSE 1:

.. code-block:: json

   {
     "generatedAt": "2026-09-06T14:32:10Z",
     "seqNo": 0,
     "eventData": [
       {
         "eventId": 1,
         "timestamp": "2026-09-06T14:32:10Z",
         "trigger": "Alerting",
         "eventNotificationType": "HardWiredNotification",
         "component": {
           "name": "PowerContactor",
           "evse": { "id": 1, "connectorId": 1 }
         },
         "variable": { "name": "Problem" },
         "actualValue": "true",
         "techCode": "ContactorPosition"
       }
     ]
   }

The same condition once it has ended:

.. code-block:: json

   {
     "generatedAt": "2026-09-06T14:41:02Z",
     "seqNo": 0,
     "eventData": [
       {
         "eventId": 2,
         "timestamp": "2026-09-06T14:41:02Z",
         "trigger": "Alerting",
         "eventNotificationType": "HardWiredNotification",
         "component": {
           "name": "PowerContactor",
           "evse": { "id": 1, "connectorId": 1 }
         },
         "variable": { "name": "Problem" },
         "actualValue": "false",
         "cleared": true,
         "techCode": "ContactorPosition"
       }
     ]
   }
