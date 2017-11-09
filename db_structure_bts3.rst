Datenbankstruktur des BTS Version 3
===================================

Einleitung
----------

Das BTS3 läuft auf einer CouchDB. Es gibt eine zentrale Instanz sowie als Teil jeder BTS3-Installation eine lokale
Instanz. Die lokale Instanz wird über die CouchDB-eigene Synchronisationsfunktion bidirektional mit der zentralen
Instanz synchronisiert. Lokal redet der BTS3-Java-Prozess über HTTP an localhost mit der lokalen CouchDB. Im
BTS3-Java-prozess läuft eingebettet eine Elasticsearch-Instanz, die mit Daten aus der lokalen CouchDB gefüttert wird.
Deshalb ist die auch ständig nicht mehr synchron und muss ständig von Hand über den BTS3-Datenbankmanager neu
synchronisiert werden.

In diesem Dokument werden alle Objekttypen *wie sie in der CouchDB vorkommen* beschrieben. Das bedeutet, dass dieses
Dokument all die Dinge außenvor lässt, die zwar irgendwo im Code zu finden sind, aber in der Praxis entweder nicht
funktionieren oder nicht benutzt werden.

Allgemeines Objektlayout in der Datenbank
-----------------------------------------

Alle hier aufgelisteten Objekte bilden 1:1 auf Java-Klassen ab. All diese Klassen sind Teil des Eclipse eObject-Systems.
Jedes Objekt enthält ein Attribut ``eClass``, das eine Pseudo-URL enthält, die den Typen dieses Objektes eindeutig
identifiziert. Diese URL folgt immer dem Schema ``http://{"btsmodel" oder "btsCorpusModel"}/1.0#//{Name der eClass}``.
Es gibt zwei Gruppen von eClass-Definitionen, oder *Modelle*: Das ``btsmodel`` sowie das ``btsCorpusModel`` (sic!).
Ersteres enthält hauptsächlich interne Verwaltungsklassen, letzteres die Klassen für die eigentlichen Nutzdaten. Im
folgenden eine Auflistung aller definierten ``eClass``-Pseudo-URLs mit der Angabe, ob diese auch tatsächlich irgendwo in
der Datenbank zu finden sind.

.. figure:: graphs/basemodel_interface_graph.png
    :width: 100%
    :target: graphs/basemodel_interface_graph.pdf

    Graph of all interfaces of the base model. For one including the impls, see `basemodel_type_graph.pdf`_.

.. figure:: graphs/corpusmodel_interface_graph.png
    :width: 100%
    :target: graphs/corpusmodel_interface_graph.pdf

    Graph of all interfaces of the corpus model. For one including the impls, see `corpusmodel_type_graph.pdf`_.

.. _`basemodel_type_graph.pdf`: graphs/basemodel_type_graph.pdf
.. _`corpusmodel_type_graph.pdf`: graphs/corpusmodel_type_graph.pdf

Definierte eClasses des Basis-Modells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. table::

    ======================================================= =================== =============
    eClass                                                  In Datenbank [#db]_ Anmerkungen
    ======================================================= =================== =============
    ``http://btsmodel/1.0#//AdministrativDataObject``       ✘
    ``http://btsmodel/1.0#//BTSComment``                    ✔
    ``http://btsmodel/1.0#//BTSConfig``                     ✘
    ``http://btsmodel/1.0#//BTSConfigItem``                 ✔
    ``http://btsmodel/1.0#//BTSConfiguration``              ✔
    ``http://btsmodel/1.0#//BTSDBBaseObject``               ✘
    ``http://btsmodel/1.0#//BTSDBCollectionRoleDesc``       ✔
    ``http://btsmodel/1.0#//BTSDBConnection``               ✔
    ``http://btsmodel/1.0#//BTSDate``                       ✘
    ``http://btsmodel/1.0#//BTSExternalReference``          ✔
    ``http://btsmodel/1.0#//BTSIDReservationObject``        ✔
    ``http://btsmodel/1.0#//BTSIdentifiableItem``           ✘
    ``http://btsmodel/1.0#//BTSInterTextReference``         ✔
    ``http://btsmodel/1.0#//BTSNamedTypedObject``           ✘
    ``http://btsmodel/1.0#//BTSObject``                     ✘
    ``http://btsmodel/1.0#//BTSObservableObject``           ✘
    ``http://btsmodel/1.0#//BTSOperator``                   ✘
    ``http://btsmodel/1.0#//BTSPassportEditorConfig``       ✔
    ``http://btsmodel/1.0#//BTSProject``                    ✔
    ``http://btsmodel/1.0#//BTSProjectDBCollection``        ✔
    ``http://btsmodel/1.0#//BTSReferencableItem``           ✘
    ``http://btsmodel/1.0#//BTSRelation``                   ✔
    ``http://btsmodel/1.0#//BTSRevision``                   ✘
    ``http://btsmodel/1.0#//BTSTimespan``                   ✘
    ``http://btsmodel/1.0#//BTSTranslation``                ✔
    ``http://btsmodel/1.0#//BTSTranslations``               ✔
    ``http://btsmodel/1.0#//BTSUser``                       ✔
    ``http://btsmodel/1.0#//BTSUserGroup``                  ✔
    ``http://btsmodel/1.0#//BTSWorkflowRule``               ✘
    ``http://btsmodel/1.0#//BTSWorkflowRuleItem``           ✘
    ``http://btsmodel/1.0#//DBLease``                       ✔
    ``http://btsmodel/1.0#//UserActionCounter``             ✘
    ``http://btsmodel/1.0#//StringToStringListMap``         ✘                   [#implonly]_
    ``http://btsmodel/1.0#//StringToStringMap``             ✘                   [#implonly]_
    ======================================================= =================== =============

Definierte eClasses des Corpus-Modells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. table::

    ======================================================= =================== =============
    eClass                                                  In Datenbank [#db]_ Anmerkungen
    ======================================================= =================== =============
    ``http://btsCorpusModel/1.0#//BTSAbstractParagraph``    ✘
    ``http://btsCorpusModel/1.0#//BTSAbstractText``         ✘
    ``http://btsCorpusModel/1.0#//BTSAmbivalence``          ✔
    ``http://btsCorpusModel/1.0#//BTSAmbivalenceItem``      ✘
    ``http://btsCorpusModel/1.0#//BTSAnnotation``           ✔
    ``http://btsCorpusModel/1.0#//BTSCorpusHeader``         ✘
    ``http://btsCorpusModel/1.0#//BTSCorpusObject``         ✘
    ``http://btsCorpusModel/1.0#//BTSGraphic``              ✔
    ``http://btsCorpusModel/1.0#//BTSImage``                ✘
    ``http://btsCorpusModel/1.0#//BTSLemmaCase``            ✔
    ``http://btsCorpusModel/1.0#//BTSLemmaEntry``           ✔
    ``http://btsCorpusModel/1.0#//BTSMarker``               ✔
    ``http://btsCorpusModel/1.0#//BTSPassport``             ✔
    ``http://btsCorpusModel/1.0#//BTSPassportEntry``        ✘
    ``http://btsCorpusModel/1.0#//BTSPassportEntryGroup``   ✔
    ``http://btsCorpusModel/1.0#//BTSPassportEntryItem``    ✔
    ``http://btsCorpusModel/1.0#//BTSSenctence``            ✔
    ``http://btsCorpusModel/1.0#//BTSSentenceItem``         ✘
    ``http://btsCorpusModel/1.0#//BTSTCObject``             ✔
    ``http://btsCorpusModel/1.0#//BTSText``                 ✔
    ``http://btsCorpusModel/1.0#//BTSTextContent``          ✔
    ``http://btsCorpusModel/1.0#//BTSTextCorpus``           ✔
    ``http://btsCorpusModel/1.0#//BTSTextItems``            ✘
    ``http://btsCorpusModel/1.0#//BTSTextSentenceItem``     ✘
    ``http://btsCorpusModel/1.0#//BTSThsEntry``             ✔
    ``http://btsCorpusModel/1.0#//BTSWord``                 ✔
    ======================================================= =================== =============

.. [#db] Ist die jeweilige eClass zwar im Modell vorhanden, aber nirgendwo in der Datenbank zu finden? Das ist z.B. bei
    rein abstrakten Basisklassen der Fall.
.. [#implonly] Es ist kein separates Interface vorhanden. Die zugehörige Impl-Klasse benutzt ein generisches
    Eclipse-Interface.

Objekttypen des Basis-Modells
-----------------------------

AdministrativDataObject
~~~~~~~~~~~~~~~~~~~~~~~
AdministrativDataObject is a base class of BTSObject meant to bring in object versioning functionality. Its fields are
the following.

:``revisions``:
    A list of revisions of this object. In the database json, this is mapped to an array of strings. This usually looks
    like this:

    .. code::

        [ "0@2015-06-26T16:13:16@74cb6b70ab6b58566bfadc664b00282d",
          "1@2015-06-26T16:18:09@74cb6b70ab6b58566bfadc664b00282d",
          "2@2015-08-06T10:56:12@IHYWLODR3RDGHIAJRRNREH7MIQ" ]

    The first element is an incrementing revision number, the second one is a timestamp in some random timezone and the
    third one is the couchdb object id of the user to blame. As usual, don't expect these to *always* actually follow
    that format as `the parsing code in BtsmodelFactoryImpl.java`_ made to fail silently.

.. _`the parsing code in BtsmodelFactoryImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/db/model/src/org/bbaw/bts/btsmodel/impl/BtsmodelFactoryImpl.java#L491

:``state``:
    This field is part of an improvised tombstone implementation. It may assume the values ``active`` or ``terminated``.
    Absence of this field seems to be considered equivalent with its value being ``active``.

    The semantics of this are similar to a "is_deleted" field. To "delete" an object, you set its ``state`` from
    ``active`` to ``terminated``, but leave the object in the database. This means you never delete an object's history
    and an user can't mess up *too* bad.

    This field seems to be only ever checked in a smattering of UI classes, namely `CorpusNavigatorPart.java`_, `AnnotationsPart.java`_, `SignTextComposite.java`_ and `EgyTextEditorPart.java`_.

.. _`CorpusNavigatorPart.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/ui/corpus/src/org/bbaw/bts/ui/corpus/parts/CorpusNavigatorPart.java#L434
.. _`AnnotationsPart.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/ui/corpus/src/org/bbaw/bts/ui/corpus/parts/AnnotationsPart.java#L809
.. _`SignTextComposite.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/ui/egy/src/org/bbaw/bts/ui/egy/textSign/SignTextComposite.java#L1776
.. _`EgyTextEditorPart.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/ui/egy/src/org/bbaw/bts/ui/egy/parts/EgyTextEditorPart.java#L2135

:``revisionState``:
    This field is also called ``reviewState``, it is an enum string.  The possible values of this field are enumerated
    under the ``Revision-Status`` meta model entry.  There is a convoluted system in place to restrict which states can
    be applied to which object types, however in practice luckily this remains mostly unused.

    The meaning of this field is something along the lines of "has this object been reviewed for publication?"

    This field is used in the code in a somewhat inconsistent manner. Most object types do not have any code referring
    to it even though all objects carry it. It seems the only place it *is* in fact used is with lemmata, and there `the
    code`_ looks like this:

    .. code::

        entry.getRevisionState().contains("obsolete")

.. _`the code`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/corpus-services-impl/src/org/bbaw/bts/core/services/corpus/impl/services/BTSLemmaEntryServiceImpl.java#L244

:``visibility``:
    This field is supposed to provide basic read/list access control on objects. Its possible values seem to be supposed
    to be described in the ``Visibility`` meta model entry, which contains ``group``, ``project``, ``public``,
    ``Reader`` and ``all_authenticated``. The code however contains at least one reference to one additional value
    ``repository`` in one of the obfuscated embedded design documents in `CouchDBManager.java`_.

    The code can't quite decide whether to check this at the database level (see the above reference) or `in the client`_.

.. _`CouchDBManager.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/db/couch/src/org/bbaw/bts/db/couchdb/impl/CouchDBManager.java#L98
.. _`in the client`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/corpus-controller-impl/src/org/bbaw/bts/core/corpus/controller/impl/partController/CorpusNavigatorControllerImpl.java#L373

BTSComment
~~~~~~~~~~
BTSConfig
~~~~~~~~~
BTSConfigItem
~~~~~~~~~~~~~
BTSConfiguration
~~~~~~~~~~~~~~~~
BTSDBBaseObject
~~~~~~~~~~~~~~~
BTSDBBaseObject is another of those base types of just about half of everything. 

:``_rev``:
    Current couchDB MVCC revision of this object. This is a string such as ``1-37221aa74fd85dcb3286a87fadb9cee3``, with
    the digit upfront being an incrementing (but not necessarily unique) counter and the value behind it being a
    hex-encoded random value to distinguish concurrent revisions.

Access control fields
^^^^^^^^^^^^^^^^^^^^^

These fields are part of a half-finished implementation of a limited form of `ACLs`_. The idea is that on a per-object
basis, a list of users or groups with read permission and a list of users or groups with update permission may be added.
There does not seem to be any code to propagate permissions from parent to child objects and in the database most
objects do not seem to contain sensible ACLs.

:``updaters``:
:``readers``:
    Both of these properties are lists of strings. Each entry is either a user name (which is used as the user
    object's couchDB ``_id``) or a group name. Groups are simply implemented by their constituent users each having their
    name as part of a ``groupIds`` array in their own user object. Access is only enforced client-side, if at all.

.. _`ACLs`: https://en.wikipedia.org/wiki/Access_control_list

Fields for local caching of values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:``conflictingRevs``:
    This field is a pseudo-attribute that is not written to db. Under certain circumstances it is populated by
    `CouchDBDao.java`__ with the ids of conflicting revisions of the document containing the field as couchDB sees them.

__ https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/db/dao-couch/src/org/bbaw/bts/dao/couchDB/CouchDBDao.java#L590
    
:``DBCollectionKey``:
    Not written to db. This field is populated in `CouchDBDao.java`__ and caches the name of the local elasticsearch
    index that contains the object this field belongs to.

__ https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/db/dao-couch/src/org/bbaw/bts/dao/couchDB/CouchDBDao.java

(Mostly) unused fields
^^^^^^^^^^^^^^^^^^^^^^

:``locked``:
    This field is not written to db. This is a flag that seems to be only used to change the image that is displayed for
    a particular obejct.  Has no functional value.

:``deleted``:
    Not written to db. Flag; does not seem to be used anywhere

:``project``:
    Not written to db. Seems to be unused.

BTSDBCollectionRoleDesc
~~~~~~~~~~~~~~~~~~~~~~~
BTSDBConnection
~~~~~~~~~~~~~~~
BTSDate
~~~~~~~
BTSExternalReference
~~~~~~~~~~~~~~~~~~~~
BTSIDReservationObject
~~~~~~~~~~~~~~~~~~~~~~
BTSIdentifiableItem
~~~~~~~~~~~~~~~~~~~
BTSIdentifiableItem is a base interface of most everything in the database. Its purpose is to describe anything that
holds an ``_id`` attribute, which in couchdb is every top-level document (i.e. that is not embedded into some other
document). Its sole field is:

:``_id``:
    The raw couchdb object ID. Do not make any assumptions about the contents of this field. Treat it as couchdb treats
    it: As an arbitrary string. Fun fact: There is both an object with the ``_id`` ``-1`` and one with the ``_id``
    ``-2``. 

    Using the following code we can get some statistics about these ids.

    .. code::

        set count (wc -l ids|cut -d' ' -f1); for re in '^"[0-9]+"$' '^"[0-9a-f]{32}"$' '^"[a-zA-Z0-9]{27}"$' '^"[A-Z0-9]{26}"$' '^"dm[0-9]*"$'; set num (egrep $re ids|wc -l); echo $re $num (echo $num/$count|bc -l); end

    The total number of objects is slightly over 4.4 million.

    .. table::

        =================== ======= ==========
        regex               count   percentage
        =================== ======= ==========
        ``[a-zA-Z0-9]{27}`` 4282726 96.86%
        ``[A-Z0-9]{26}``    70761    1.60%
        ``[0-9]+``          52185    1.18%
        ``dm[0-9]*``        7971     0.18%
        ``[0-9a-f]{32}``    3        0.00%
        other               7932     0.18%
        =================== ======= ==========
        
    For some database objects inherited from previous BTS versions, short numeric strings such as ``100120`` are used.

BTSInterTextReference
~~~~~~~~~~~~~~~~~~~~~
BTSNamedTypedObject
~~~~~~~~~~~~~~~~~~~
BTSNamedTypedObject is an interface that through ``BTSObject`` and other inheritance paths is implemented by a large
number of types. It describes an object that may have a ``name``, a ``type``, a ``subtype`` and a ``sortKey``. ``type``
and ``subtype`` are used somewhat inconsistently. For some object types, their range of values is described in the meta
model entries under ``/objectTypes``. Not every object type uses ``type`` as well as ``subtype`` and not every ``type``
also has one or more ``subtype``.

:``name``:
    This field generally describes a human-readable name of the object. The ``name`` is generally used as a label when
    displaying objects (e.g. in the tree viewer, or in an input mask). Sample values for this are e.g. ``Hammamat C-M 265``
    and ``〈Wadi Allaqi 3〉`` for some TCObjects or ``ḫnd (ḥr) (mw)`` and ``mꜣꜣ.t-Ḥr.w`` for some lemmata.

    .. ATTENTION::
        In case of lemmata the name often is a simple concatenation of transliterations of the lemma's constituent
        words, but **this is no rule**.

:``type``:
    This field describes the logical type of the object. Its semantics vary by object type/eclass. Following are some
    example values found in the live database.

    =========================== ============================================================================
    Type                        List of possible of values in JSON
    =========================== ============================================================================
    ``Corpus:Text``             ``"Text", "Subtext", "subtext", "undefined", "", null``
    ``Corpus:Senctence``        ``"HS", null``
    ``Base:Comment``            No type, no subtype.
    ``Corpus:LemmaEntry``       ``null, "undefined", "numeral", "particle", "preposition", "verb", ... ~15``
    ``Corpus:Annotation``       ``"undefined", null, "conceptual" "ConceptualGroup2", "Annotation-Leipzig", ... ~10``
    ``Corpus:TCObject``         ``null, "", "undefined", "Arrangement", "TCSuperText", "TCObject", "Group", "Scene", ... ~10``
    ``Corpus:TextCorpus``       ``null, "undefined"``
    ``Corpus:ThsEntry``         ``null, "objectType", "objecttype", "actor", "grouping", "miniature", "model", "material", "copy", ... ~25``
    =========================== ============================================================================

    ``BTSMarker`` is a ``BTSNamedTypedObject``, but its type field seems to be free text provided by the user.

:``subtype``:
    This field is sometimes used to describe a subtype of an object. It is used only in the following object types:

    =========================== ============================================================================
    Type                        List of possible of values in JSON
    =========================== ============================================================================
    ``Base:ConfigItem``         ``"IMG_THS", "IMG_ANNOTATION", "IMG_OVR_OBSOLETE", ... ~30``
    ``Corpus:LemmaEntry``       ``"person_name", "substantive_masc", "gods_name", "title", "verb_2-lit", ... ~50``
    ``Corpus:Annotation``       ``"MetaphorRelatedWord", "Metonym", "subtype", "left-to-right", ... ~10``. Only used very infrequently.
    ``Corpus:TCObject``         Only four overall usages, with values ``"undefined"`` (thrice) and ``"subcaption"`` (once)
    =========================== ============================================================================

:``sortKey``:
    An integer field that in several places is used instead of ``name`` to sort things. Following is an exhaustive table
    of occurences.

    =================== ======= =========
    Type                Count   Frequency
    =================== ======= =========
    Corpus:Text         14196   46.38%
    Corpus:TCObject     1403    8.76%
    Corpus:ThsEntry     4       0.115% 
    Corpus:Annotation   2       0.014%
    Corpus:TextCorpus   1       2.00% 
    Base:ConfigItem     297     36.89%
    =================== ======= =========

BTSObject
~~~~~~~~~
Base type for a large part of database objects. Brings in ``_id, name, type, subtype, sortKey`` by means of inheritance
from ``BTSNamedTypedObject`` and in turn ``BTSIdentifiableItem``.

.. ATTENTION::
    Despite its name only about half of the database object types inherit from this. Also, do not trust even the meager
    amounts of documentation in its source code.

The model for BTSObject includes a field ``tempSortKey`` that is used in some places, but this field never makes it to
the database. It is instead used as some kind of object-global variable.

:``code``:
    Never used.

:``relations``:
    Array field of ``Relation`` objects describing relations between the containing object and other objects. This is
    used to describe complex relations such as ``rootOf`` or ``composedOf`` for lemmata. *Everywhere* else it is only
    ever used with ``partOf`` to express the hierarchical structure of the object tree. Below is an exhaustive table of
    occurences.

    =================== ======= =========
    Type                Count   Frequency
    =================== ======= =========
    Corpus:Annotation   13862   100%
    Corpus:TCObject     16008   100%
    Corpus:Text         30605   99.99%
    Base:Comment        33312   99.99%
    Corpus:ThsEntry     3457    99.34%
    Corpus:LemmaEntry   20195   30.11%!
    Corpus:TextCorpus   1       2%
    =================== ======= =========

:``externalReferences``:
    This field is an array of ``ExternalReference`` objects. The idea here seems to be to store alternative ways to
    refer to the entry containing the field. In practice, it only used a handful (<50) times outside the dictionary
    proper with the notable exception of the TLA demotic corpus. In the TLA demotic corpus it is used to store malformed
    URLs pointing to an external database. In the dictionary it is used to store reference numbers of the entries. In
    the user database it is used to store what seems to be user IDs of a previous BTS version.

    Below is a listing of occurrences by object type in the database.

    =================== ======= =========
    Type                Count   Frequency
    =================== ======= =========
    Corpus:LemmaEntry   63391   94.52%
    Corpus:ThsEntry     3459    99.40%
    Base:User           55      47%
    Corpus:TCObject     1370    8.56%
    Corpus:Text         109     0.36%
    Base:UserGroup      11      0.45%
    Corpus:Annotation   3       0.00%
    Corpus:TextCorpus   1       2%
    =================== ======= =========

BTSObservableObject
~~~~~~~~~~~~~~~~~~~
BTSObservableObject is purely internal. It extends EObject and adds an interface for third parties to track
modifications of this object's eclipsey properties.

BTSOperator
~~~~~~~~~~~
BTSPassportEditorConfig
~~~~~~~~~~~~~~~~~~~~~~~
BTSProject
~~~~~~~~~~
BTSProjectDBCollection
~~~~~~~~~~~~~~~~~~~~~~
BTSReferencableItem
~~~~~~~~~~~~~~~~~~~
BTSRelation
~~~~~~~~~~~
.. ATTENTION::
    Technically, the ``partOf`` graph is only directed. In practice, it seems it is also acyclic and something would
    probably crash if it wasn't. It is, however, *not* a vanilla tree as objects can have several parents.

BTSRevision
~~~~~~~~~~~
BTSTimespan
~~~~~~~~~~~
BTSTranslation
~~~~~~~~~~~~~~
BTSTranslations
~~~~~~~~~~~~~~~
BTSUser
~~~~~~~
BTSUserGroup
~~~~~~~~~~~~
BTSWorkflowRule
~~~~~~~~~~~~~~~
BTSWorkflowRuleItem
~~~~~~~~~~~~~~~~~~~
DBLease
~~~~~~~
UserActionCounter
~~~~~~~~~~~~~~~~~
StringToStringListMap
~~~~~~~~~~~~~~~~~~~~~
StringToStringMap
~~~~~~~~~~~~~~~~~

Objekttypen des Corpus-Modells
------------------------------

BTSAbstractParagraph
~~~~~~~~~~~~~~~~~~~~
BTSAbstractText
~~~~~~~~~~~~~~~
BTSAmbivalence
~~~~~~~~~~~~~~
BTSAmbivalenceItem
~~~~~~~~~~~~~~~~~~
BTSAnnotation
~~~~~~~~~~~~~
BTSCorpusHeader
~~~~~~~~~~~~~~~
BTSCorpusObject
~~~~~~~~~~~~~~~
BTSGraphic
~~~~~~~~~~
BTSImage
~~~~~~~~
BTSLemmaCase
~~~~~~~~~~~~
BTSLemmaEntry
~~~~~~~~~~~~~
BTSMarker
~~~~~~~~~
BTSPassport
~~~~~~~~~~~
BTSPassportEntry
~~~~~~~~~~~~~~~~
BTSPassportEntryGroup
~~~~~~~~~~~~~~~~~~~~~
BTSPassportEntryItem
~~~~~~~~~~~~~~~~~~~~
BTSSenctence
~~~~~~~~~~~~
BTSSentenceItem
~~~~~~~~~~~~~~~
BTSTCObject
~~~~~~~~~~~
BTSText
~~~~~~~
BTSTextContent
~~~~~~~~~~~~~~
BTSTextCorpus
~~~~~~~~~~~~~
BTSTextItems
~~~~~~~~~~~~
BTSTextSentenceItem
~~~~~~~~~~~~~~~~~~~
BTSThsEntry
~~~~~~~~~~~
BTSWord
~~~~~~~