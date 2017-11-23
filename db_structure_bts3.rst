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

This document starts out with an overview of all object types defined in the source, not their manifestation in the
database. Thus it includes super-types that are not directly present in the database.

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

    In the java domain these revisions are represented by eclipsey `BTSRevision`_ objects.

    .. ATTENTION::

        The CouchDB user ID in some cases is some random-looking string, but in some cases it is the user's login name.

    .. ATTENTION:
        
        Do not confuse this with CouchDB's ``_rev`` field, which is mapped by `BTSDBBaseObject`_. These two have nothing
        to do with each other. In particular, the revsion counter at the beginning of this field's revision strings may
        coincide with the revision counter at the beginning of couchdb's ``_rev`` field, but that is not guaranteed in
        any way. Just have a look at `addRevisionStatementInternal in GenericObjectServiceImpl.java`_.

.. _`addRevisionStatementInternal in GenericObjectServiceImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/core-services-impl/src/org/bbaw/bts/core/services/impl/generic/GenericObjectServiceImpl.java#L262
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
    ``repository`` in one of the obfuscated `embedded design documents in CouchDBManager.java`_.

    The code can't quite decide whether to check this at the database level (see the above reference) or `in the client`_.

.. _`embedded design documents in CouchDBManager.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/db/couch/src/org/bbaw/bts/db/couchdb/impl/CouchDBManager.java#L98
.. _`in the client`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/corpus-controller-impl/src/org/bbaw/bts/core/corpus/controller/impl/partController/CorpusNavigatorControllerImpl.java#L373

BTSComment
~~~~~~~~~~

A ``BTSComment`` describes a human-language comment on some object or text section. All comments on a project are stored in
the project's ``{project name}_admin`` database and link to their target object or text part by means of exactly one
``partOf`` relation. For details, see `PartOf relations`_.

A ``BTSComment`` is a `BTSObject`_ and has the following fields:

:``comment``:
    The comment's human-readable plain text

:``tags``:
    Unused.

BTSConfig
~~~~~~~~~

``BTSConfig`` is a super-type of `BTSConfigItem`_ and `BTSConfiguration`_ that provides their ``children`` attributes.

Config Graph
^^^^^^^^^^^^
.. figure:: graphs/config_graph_hybrid.png
    :width: 100%
    :target: graphs/config_graph_hybrid.pdf

    Graph of the unified hierarchical structure of both `BTSConfiguration`_ instances. Each `BTSConfigItem`_ is
    annotated with its ``type`` attribute.

:``children``:
    The logical children of this `BTSConfiguration`_ or `BTSConfigItem`_. On the top levels of a `BTSConfiguration`_
    this is used to categorize according to function of the config subtree. In the passport configuration this hierarchy
    is used to describe the hierarchy of passport fields and their groups. Have a look at the `Config Graph`_ for
    details.

BTSConfigItem
~~~~~~~~~~~~~

A ``BTSConfigItem`` is a single node in the configuration tree rooted in a single `BTSConfiguration`_ object. A
``BTSConfigItem`` is a `BTSIdentifiableItem`_, a `BTSConfig`_ and a `BTSObservableObject`_.  Have a look at the `Config
Graph`_ to see how this is actually used.

.. ATTENTION::
    Note that despite what it might initially seem like, ``BTSConfigItem`` does *not* inherit from either of
    `BTSNamedTypedObject`_, `BTSDBBaseObject`_, `AdministrativDataObject`_ or `BTSObject`_.

:``abbreviation``:
    This field is only used with some objects with ``.type == 'objectType'`` and contains a human-readable abbreviation
    of the described type.

:``description``: 
    This rarely used field is meant to contain human-readable comment on this node beyond what fits into ``label``. For
    good measure, its contents are wrapped into an array of `BTSTranslation`_ objects.

:``ignore``:
    This is a boolean field that can be used to "comment out" parts of the configuration. It seems setting this to
    ``true`` will also ignore any descendents of this node.

:``label``:
    This field is apparently meant to contain a human-readable label for the config node. It is similar to ``value``
    ``value`` except that the contents of ``label`` are wrapped into an array of `BTSTranslation`_ objects. Because why
    not.

:``ownerReferencedTypesStringList``:
    This field is relevant only(?) for a `BTSConfigItem`_ describing a passport field. In this case, this field
    points at an enumeration of the allowed values for the described passport field. See `BTSPassportEditorConfig`_.
    Example:
    
    .. code::

            [
                "objectTypes.CorpusObject>>74cb6b70ab6b58566bfadc664b001f0c.Custom-Entries.language,",
                "objectTypes.Text>>74cb6b70ab6b58566bfadc664b001f0c.Custom-Entries.language,",
                "objectTypes.Thesaurus Entry>>74cb6b70ab6b58566bfadc664b001f0c.Custom-Entries.language,",
            ]

    This field contains a list of strings, each describing one pointer from one thing to several other things. The
    format roughly is ``{source}>>{target}[,{target}...]``. with ``{source}`` generally being one of the strings
    described in `BASIC_OBJECT_TYPES in BTSConstants.java`_ and each ``{target}`` pointing either at a `BTSConfig`_ subtree
    with leaf nodes being possible values or pointing out specific values.

    In fact this filed contains its own little borked DSL, but considering overall there are only 393 instances of it a
    proper specification is hardly worth the effort. The intention can be accurately guessed in all instances. If you are so
    inclined you may have look at all its nasty innards in `BTSConfigurationServiceImpl.java`_

    .. ATTENTION::

        This field is generally accessed as ``ownerTypesMap``. See `fillOwnerTypesMap in BTSConfigItemImpl.java`_.

.. _`fillOwnerTypesMap in BTSConfigItemImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/db/model/src/org/bbaw/bts/btsmodel/impl/BTSConfigItemImpl.java#L693-L711
.. _`BASIC_OBJECT_TYPES in BTSConstants.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/global-commons/src/org/bbaw/bts/commons/BTSConstants.java#L83-L97
.. _`BTSConfigurationServiceImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/core-services-impl/src/org/bbaw/bts/core/services/impl/services/BTSConfigurationServiceImpl.java#L535

:``passportEditorConfig``:
    This field is only used for config items describing the passport structure and points to a
    `BTSPassportEditorConfig`_ object describing the way the UI should behave for this field.

:``sortKey``:
    An integer field that in several places is used instead of ``name`` to sort things.

:``subtype``:
    This is only used when ``.type == "objectType"`` to express some sort of icon to use somewhere. The values are all
    like ``IMG_SOMETHING_OR_OTHER``.

:``type``:
    This describes the type *of the config node itself*. One might think that this would be redundant given the
    ``value`` attribute and the hierarchical structure of the config, but come on, we're not in the ``.ini`` days
    anymore, are we? So, we end up with the following ``type`` values:
    * ``<none>``
    * ``Passport-Category``
    * ``Passport-Entry-GroupCategories``
    * ``Passport-Entry-Item Passport``
    * ``Relation``
    * ``objectType``
    * ``objectTypes``

:``value``:
    This is the textual value of the config node. For top-level nodes this is generally the same as the Type, for
    lower-level nodes this contains e.g. the type names in an enumeration or the passport field names. This field's
    value is supposed to be used as an identifier, and thus generally ``looks_like_this``.

:``rules``:
    Unused.

:``showWidget``:
    Unused.

BTSConfiguration
~~~~~~~~~~~~~~~~

Every project has exactly one ``BTSConfiguration`` stored in its ``{project name}_admin`` database. A
``BTSConfiguration`` is a `BTSObject`_ and a `BTSConfig`_. This ``BTSConfiguration`` describes everything and the
kitchen sink, from UI defaults through the ACL to the database schema.  The top-level ``BTSConfiguration`` object is the
root of the config tree. Its descendants are all `BTSConfigItem`_. They are stored in the ``children`` attribute
inherited from `BTSConfig`_. Have a look at the `Config Graph`_ to see how this is actually used.

:``provider``:
    A symbolic name of the config. This is only used to find the configuration object specified in the application
    preferences. There is no reason the ``_id`` could not be used there.

    Following is a table of all two values this field may take.

    ======================================= =============== ================================
    ``_id``                                 ``provider``    ``name``
    ======================================= =============== ================================
    ``74cb6b70ab6b58566bfadc664b001f0c``    ``aaew``        Altägyptisches Wörterbuch (AAEW)
    ``WTJMUMGNKBGYDMYAYFRNGFNBDQ``          ``aemconfig``   AEM Configuration
    ======================================= =============== ================================

    Generated with 
    ``for f in *_admin.json; jq -C '.docs[] | select(.eClass == "http://btsmodel/1.0#//BTSConfiguration") | .name, .provider' $f; end``

BTSDBBaseObject
~~~~~~~~~~~~~~~

``BTSDBBaseObject`` is another of those base types of just about half of everything. 

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

This type describes a per-project "role". A role seems to be just a set of permissions such as "r" for a "reader" or
"rw" for an updater.

:``roleName``:
    This field contains the name of the role, such as ``"guests"`` or ``"editors"``.

:``userNames``:
    This field is a list of (human-readable) user names that have this role.

:``userRoles``:
    Contrary to its name, this field contains a list of couchDB ids of `BTSUserGroup`_ objects. I'm not sure what the
    meaning of this is, but I suppose that all members of these groups kinda also get to have this role??

BTSDBConnection
~~~~~~~~~~~~~~~

This type describes on a per-project basis where to sync to. In practice, all corpora have the same target. There are
three fields to it of which only ``masterServer`` seems to be relevant at all.

:``type``:
    This field is either ``couchdb``, ``Couchdb`` or absent. It does not seem to matter which of those.

:``masterServer``:
    This field is always the same value, It contains an HTTP URL where the couchDB is to be found.

:``dbPath``:
    Unused.

BTSDate
~~~~~~~

.. ATTENTION::
     This seems to be unused.

BTSExternalReference
~~~~~~~~~~~~~~~~~~~~

Below is a table of which types use ``BTSExternalReference`` objects in their ``externalReferences`` fields.

================ ===== =========
Type             count frequency
================ ===== =========
`BTSLemmaEntry`_ 63391    92.66%
`BTSThsEntry`_    3459     5.06%
`BTSTCObject`_    1377     2.01%
`BTSText`_         111     0.16%
`BTSUser`_          55     0.08%
`BTSUserGroup`_     11     0.02%
`BTSAnnotation`_     3     0.00%
`BTSTextCorpus`_     2     0.00%
================ ===== =========

:``type``:
    The ``type`` of an external reference describes roughly the target domain of the reference. The most common ``type``
    is ``aaew_wcn`` which stands for ``Altägyptisches Wörterbuch: Wortcorpusnummer``. This is simply the index number
    (and thus in this database couchdb object id) of the target entry. ``aaew_1`` are references to row IDs in an older
    version of the AÄW. Note that anything besides these two is perfectly irrelevant in practice.
    
    ======== ===== =========
    type     count frequency
    ======== ===== =========
    aaew_wcn 63391    92.66%
    aaew_1    3525     5.15%
    <none>    1487     2.17%
    URI          2     0.00%
    text         2     0.00%
    Text         1     0.00%
    geo          1     0.00%
    ======== ===== =========

:``reference``:

:``provider``:

BTSIDReservationObject
~~~~~~~~~~~~~~~~~~~~~~

``BTSIDReservationObject`` is meant to allow an user to pre-commit an object ID. Since in some cases the objects couchDB
id is actually the lemma number this is actually mission-critical and collisions would actually produce a lot of
problems. The logic surrounding this is quite brittle and lacks proper error handling or locking.

A single ``BTSIDReservationObject`` represents a reservation of a single ID. The application always tries to keep a
fixed number of reservations in cache. If the application can't find a reservation, it will just make up an ID in a
totally different format (mangled UUID) instead.

Since in different places different ID formats are used (see `BTSIdentifiableItem`_), ``BTSIDReservationObject`` allows
prefixes. There is no further scoping or proper namespacing.

.. ATTENTION:: The details of the reservation logic are controlled by the ``propertyStrings`` field on the
    `BTSProjectDBCollection`_ belonging to the active (dictionary) object.

``BTSIDReservationObject`` is a subtype of `BTSDBBaseObject`_. From there it inherits its useless `_rev` field.

:``_id``:
    This is the actual ID being reserved. This is a couchDB id, but it also carries a semantic value. This is always
    something human-readable, some arbitrary prefix (generally ``""`` or ``"d"``) followed by a 4-6 digit number.
:``updaters``:
    This field has a totally different meaning than elsewhere, though I suspect that that might only be the java side
    and the javascript view functions might not actually care. Here, this is always an array of one element, which
    always is the ID (which is also sometimes the human-readable name) of the user that created this reservation.
:``btsUUID``:
    This is an ID meant to identify a single BTS installation. It is set to a string of the decimal timestamp
    of the first time that BTS installation was started. Example: ``"1447396852251"``.  Be careful in that generally
    within the BTS the name "uuid" does not always refer to what is commonly known as an `UUID`_. In fact, it may
    neither be guaranteed to be universal nor unique as you can see in one case in `applicationStartup in
    ApplicationStartupControllerImpl.java`_.  Also, have a look at `createId in IDServiceImpl.java`_.

.. _`UUID`: https://en.wikipedia.org/wiki/Universally_unique_identifier
.. _`createId in IDServiceImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/core-services-impl/src/org/bbaw/bts/core/services/impl/services/IDServiceImpl.java#L68 
.. _`applicationStartup in ApplicationStartupControllerImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/controller-impl/src/org/bbaw/bts/core/controller/impl/generalController/ApplicationStartupControllerImpl.java#L162

BTSIdentifiableItem
~~~~~~~~~~~~~~~~~~~

``BTSIdentifiableItem`` is a base interface of most everything in the database. Its purpose is to describe anything that
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

``beginId`` and ``endId`` may be set. If that is the case, the target is a
range of the content of a ``BTSText`` and ``beginId`` and ``endId`` both refer to objects such as `BTSWord`_.

Following is an exhaustive table of the object types ``beginId`` and ``endId`` refer to in the live data.

=================== ======= ==========
Type                Count   Frequency
=================== ======= ==========
`BTSWord`_          44727   72.2%
`BTSMarker`_        17212   27.8%
`BTSAmbivalence`_   10      0.0%
=================== ======= ==========


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
from ``BTSNamedTypedObject`` and in turn ``BTSIdentifiableItem``. Also brings in ``revisions, state, revisionState,
visibility`` from AdministrativDataObject.

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

.. ATTENTION::
     This seems to be unused.

BTSPassportEditorConfig
~~~~~~~~~~~~~~~~~~~~~~~

This is a rather hairy one. An instance of this type describes 
``BTSPassportEditorConfig`` is a subtype of `BTSIdentifiableItem`_.

:``widgetType``:
    This indicates what type of input field is desired. These widget types are the following:

    .. code::

        jq -c '.docs[] | recurse(.children[]?) | .passportEditorConfig? | select(. != null) | .widgetType' aem_admin.json aaew_admin.json | sort | uniq -c | sort -rn

    =========================== ========= ==============
    ``widgetType``              ``count`` ``percentage``
    =========================== ========= ==============
    null                              558 69%
    "Text"                             81 10%
    "Boolean Select"                   62  8%
    "Text Field"                       46  6%
    "Select from Thesaurus"            32  4%
    "Select from Configuration"        26  3%
    =========================== ========= ==============

    :``Text``: is a single-line text field.
    :``Text Field``: is a multi-line text field
    :``Boolean Select``: is a simple checkbox
    :``Select from Thesaurus``: This is a text field that can be used to enter a dictionary entry's ``_id`` or ``name``.
        There is a keyboard shortcut on this that will trigger an extremely slow lookup of the object in the database and
        present substring matches to choose for the current input. There is a button that opens a tree viewer for the
        target objects instead.
    :``Select from Configuration``: This results in a drop-down list containing entries that are themselves read from
        "the configuration". The values this drop-down list allows are pointed at in the
        ``ownerReferencedTypesStringList`` field of `BTSConfigItem`_.

    The ``null`` values are there since many `BTSConfigItem`_ instances that don't actually need a
    ``BTSPassportEditorConfig`` for some reason still have an empty one.

:``horizontalWidth``:
    This sets the width of this input field in the UI as a number of layout grid cells. This has nothing to do with the
    data contained within the field which still may be of arbitrary length.
:``allowMultiple``:
    This indicates whether this entry may hold a list of values instead of a single value. In the UI this is solved
    using the "add row" input field pattern.
:``required``:
    This is never used in practice. The idea is that when this is set, the corresponding passport entry must be set
    before submitting changes.
:``regex``:
    This is never used in practice. The idea is that when this is set, the corresponding passport entry must conform to
    this regex before submitting changes.
:``predicateList``:
    This is never used in practice. No idea what the idea was with this.

BTSProject
~~~~~~~~~~

A "Project" is a single administrative entity. It has its own database configuration, access control rules and set of
corpora. ``BTSProject`` is a subtype of `BTSObject`_. As in any good data model, there is no direct link between a
``BTSProject`` and its constituent `BTSTextCorpus`_ instances. Both are only linked through the ``corpusPrefix`` field
in `BTSCorpusObject`_ pointing at one of the `BTSProjectDBCollection`_ instances of the `BTSProject`_. Every time the
``BTSProject`` side of the database has to be accessed from the `BTSCorpusObject`_ side, the
`BTSProject`_/`BTSProjectDBCollection`_/whatever is simply looked up by ``corpusPrefix``. A good starting point for
looking into this is `getDBCollection in PermissionsAndExpressionsEvaluationControllerImpl.java`_.

The BTSProject is not exposed much in the user interface. The main contact area with this type is the installer, where
one can select one or multiple projects to download.

:``prefix``:
    "key" of this project, such as ``"aaew"`` in case of the Altägyptisches Wörterbuch. Among others, this is used in
    the database name of this project's personal database.
:``name``:
    Inherited from `BTSNamedTypedObject`_ via `BTSObject`_ this contains the project's human-readable name, such as
    ``"Altägyptisches Wörterbuch BBAW"``.
:``description``:
    Does not contain much if anything at all, such as "Höhlenbuch (Unterweltsbuch)" for the "Höhlenbuch".
:``dbConnection``:
    `BTSDBConnection`_ of this project. This describes which database this project is supposed to sync to.
:``dbCollections``:
    This field contains a list of `BTSProjectDBCollection`_ objects. Though from the code it seems higher ambitions were
    had there is always exactly one database collection per text corpus.

.. _`getDBCollection in PermissionsAndExpressionsEvaluationControllerImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/controller-impl/src/org/bbaw/bts/core/controller/impl/generalController/PermissionsAndExpressionsEvaluationControllerImpl.java#L691-L704

BTSProjectDBCollection
~~~~~~~~~~~~~~~~~~~~~~

A ``BTSProjectDBCollection`` describes one couchDB database belonging to the project. This database contains the objects
of a single `BTSTextCorpus`_.  ``BTSProjectDBCollection`` is a subtype of `BTSIdentifiableItem`_.

:``collectionName``:
    The name of the couchDB database, such as ``aaew_corpus_bbawfelsinschriften``.
:``propertyStrings``:
    This field contains a (json) list of ``"key=value"`` (json) strings. In practice, these are solely used on the
    dictionaries to configure the ID reservation logic.
:``roleDescriptions``:
:``indexed``:
    This boolean flag sets whether this database is supposed to be indexed by elasticsearch. See `CouchDBManager.java`_
    for details.
:``synchronized``:
    This boolean flag sets whether this database is supposed to be synchronized to remote described in this
    `BTSProjectDBCollection`_'s owner `BTSProject`_'s `BTSDBConnection`_.

.. _`CouchDBManager.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/db/couch/src/org/bbaw/bts/db/couchdb/impl/CouchDBManager.java

BTSReferencableItem
~~~~~~~~~~~~~~~~~~~

.. ATTENTION::
     This seems to be unused.

BTSRelation
~~~~~~~~~~~

Since CouchDB is a document oriented database what more natural way is there to describe the tree-like hierarchy of
objects than by kludging an ersatz relational layer on it?

A ``BTSRelation`` represents a single item in a relation (and not as the name implies the relation itself). An
implementation detail is that these relations are inherently directional, and the ``BTSRelation`` object is always
stored in the *head* object. So, a ``partOf`` relation describing that object ``A`` is a part of object ``B`` would be
stored in object ``A``. Read: ``A is partOf B``.

Every relation contains the couchDB ``_id`` of its target object in its ``objectId`` field. 

Relations come in many flavors. The important one is ``partOf``, which is used to express hierarchical structure in the
object browser. It can be used on most anything. The other relation type flavors are only used on ``BTSLemmaEntry``
objects. Below are some nice stats on these.

Due to the inherently asymmetric nature of this representation, most "relation types" need a reciprocal type to be put
at the far end of the relation. Such pairs are e.g. ``successor`` and ``predecessor`` or ``composes`` and
``composedOf``. Note that these are sometimes not named very well.

.. ATTENTION:: ``partOf`` relations do not have a reciprocal element.

.. WARNING:: reciprocal relations are maintained by hand, this does in practice lead to inconsistencies as are evident
    for example from the untyped relations shown in the data below.

Relation type statistics
^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html
    :file: relation_types.html
    
Relation target type statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html
    :file: relation_child_types.html

PartOf relations
^^^^^^^^^^^^^^^^

In certain cases such as when used with a `BTSComment`_ a ``partOf`` relation may contain ``parts``. Each "part" is a
`BTSInterTextReference`_ pointing to part of some text. The statistics of the number of parts as extracted from a
database backup are as follows.

``jq '.docs[].relations[]?.parts | length' *.json | sort | uniq -c | sort -bnk2``

======= ======= ==========
length  count   percentage
======= ======= ==========
      0   92685      66.26
      1   46892      33.52
      2     206       0.15
      3      53       0.04
      4      28       0.02
      5      11       0.01
      6       6       0.00
      7       2       0.00
      8       1       0.00
      9       1       0.00
     12       1       0.00
     13       1       0.00
     16       1       0.00
======= ======= ==========

.. ATTENTION::
    Technically, the ``partOf`` graph is only directed. In practice, it seems it is also acyclic and something would
    probably crash if it wasn't. It is, however, *not* a vanilla tree as objects can have several parents.

.. ATTENTION::
    TODO: Right now I can't make any statements on the equivalency of two ``partOf`` relations using the same target
    ``objectId`` but each containing different ``parts`` and only one ``partOf`` relation using the same target
    ``objectId`` but containing the union of both partses .

BTSRevision
~~~~~~~~~~~

Internal object used to represent the entries of the ``_rev`` field in a `BTSDBBaseObject`_. This type incorrectly
inherits from `BTSIdentifiableItem`_.

BTSTimespan
~~~~~~~~~~~

.. ATTENTION::
     This seems to be unused.

BTSTranslation
~~~~~~~~~~~~~~

This type describes a string along with its language. It inherits ``_id`` from `BTSIdentifiableItem`_ and has its own
two properties. Several ``BTSTranslation`` instances are aggregated into one `BTSTranslations`_ instance. Don't confuse
the two!

:``lang``:
    The language of this string. This is a ISO 639-1 two-letter language code from the hardcoded `language list in
    BTSCoreConstants.java`_.
:``value``: The string proper

.. _`language list in BTSCoreConstants.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/core-commons/src/org/bbaw/bts/core/commons/BTSCoreConstants.java#L111-L143

BTSTranslations
~~~~~~~~~~~~~~~

This type describes a string possibly translated into several languages. In contrast to `BTSTranslation`_ it is *not* a
subclass of `BTSIdentifiableItem`_.

Objects of this type are used in the translation of texts and their constituent words in `BTSSenctence`_ and `BTSWord`_,
in the translation of dictionary entries in `BTSLemmaEntry`_ and in `BTSConfigItem`_ as a means of internationalization
of small parts of the UI.

:``translations``:
    Array of `BTSTranslation`_ objects, one for each language present. Note that there is no way to specify the original
    string in a set of translations.

BTSUser
~~~~~~~

This type describes an user account for the BTS. This account is synchronized and used both locally and remote. A
`BTSUser`_ is a `BTSObject`_.

In addition to the specific fields below, some `BTSUser`_ objects have their inherited ``externalReferences`` field set
to a list containing one `BTSExternalReference`_ of type ``aaew_1`` with a string-formatted small number that apparently
is this user's ID in a previous incarnation of the BTS.

:``comment``:
    Not used.
:``dbAdmin``:
    Flag only used during user creation and not manifested in database.
:``description``:
    Miscellaneous comments. Very rarely used.
:``groupIds``:
    This is a list of `BTSUserGroup`_ object couchDB ids of groups this user is a member of.
:``loggedIn``:
    Not used.
:``mail``:
    This is the email address of this user. This is not always present!
:``password``:
    This contains the very insecurely encrypted (sic!) password of this user.
:``sigle``:
    This is a short identifier for this user such as ``SDS/AAEW/BBAW``. This field is not always present.
:``status``:
    Not used.
:``userName``:
    login name of this user. Often this is also the user objects couchDB ``_id``.
:``foreName``:
    given name
:``sureName``:
    surname
:``webDescription``:
    This contains a human-readable description of this persons's position. This is rarely present.
:``webURL``:
    This contains an URL to some website where this person may be found. This is rarely present.

BTSUserGroup
~~~~~~~~~~~~

This type describes a group of users. The group membership is managed in the individual `BTSUser`_ objects via their
``groupIds`` field. `BTSUserGroup`_ is a subtype of `BTSObject`_.

:``name``:
    This field contains the human-readable long-form name of this group, such as ``"Totenbuch-Projekt, Ägyptologisches Seminar der Universität Bonn"``.
    This field is not present in ``terminated`` groups.
:``state``:
    Either ``active`` or ``terminated``.

BTSWorkflowRule
~~~~~~~~~~~~~~~

.. ATTENTION::
     This seems to be unused.

BTSWorkflowRuleItem
~~~~~~~~~~~~~~~~~~~

.. ATTENTION::
     This seems to be unused.

DBLease
~~~~~~~

This type is part of the borked locking infrastructure. The basic idea is that a `DBLease`_ instance is automatically
created for every object that is opened in the BTS. This is done via the selection mechanism centered around
`setSelection in PermissionsAndExpressionsEvaluationController.java`_.

The logic behind lock creation (e.g. `acquireLockOptimistic in BTSEvaluationServiceImpl.java`_) is very racy. Also,
there is no good guarantee that things that are locked are also unlocked in time. And locks expire at some point, and
AFAICT there is noone actively checking when exactly that happens.

.. _`setSelection in PermissionsAndExpressionsEvaluationController.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/controller-impl/src/org/bbaw/bts/core/controller/impl/generalController/PermissionsAndExpressionsEvaluationControllerImpl.java#L150-L198
.. _`acquireLockOptimistic in BTSEvaluationServiceImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/core-services-impl/src/org/bbaw/bts/core/services/impl/services/BTSEvaluationServiceImpl.java#L416-L468

UserActionCounter
~~~~~~~~~~~~~~~~~

.. ATTENTION::
    This is a purely internal type. It seems to be meant to allow for some history-dependent scheduling of
    completions(?) but despite fragments of database infrastructure code it has never been manifested into the database.

StringToStringListMap
~~~~~~~~~~~~~~~~~~~~~

.. ATTENTION::
    This is a purely internal type.

StringToStringMap
~~~~~~~~~~~~~~~~~

.. ATTENTION::
    This is a purely internal type.

Object Types of the Corpus Model
--------------------------------

The corpus model is the second EMF model and the one that contains most of the things an user can actually *see* and
edit in the UI.

BTSAbstractParagraph
~~~~~~~~~~~~~~~~~~~~

.. ATTENTION::
     This seems to be unused.

BTSAbstractText
~~~~~~~~~~~~~~~

.. ATTENTION::
    There is a lot of code around this, but it does not seem to be used anywhere.

BTSAmbivalence
~~~~~~~~~~~~~~

`BTSAmbivalence`_ may be part of a `BTSSenctence`_ and describes the case when a transliteration is ambiguous. It
contains nothing but an array of `BTSLemmaCase`_ objects in its ``cases`` attribute, each being one of the possible
transliterations of this part of the sentence.

`BTSAmbivalence`_ is a subtype of `BTSTextSentenceItem`_.

:``cases``: 
    One `BTSLemmaCase`_ for each possible transliteration

    .. ATTENTION::
        Despite its name this field contains `BTSLemmaCase`_ objects, not `BTSAmbivalenceItem`_ objects.

BTSAmbivalenceItem
~~~~~~~~~~~~~~~~~~

.. ATTENTION::
    Despite the name suggesting that this is what is found in the ``cases`` field of a `BTSAmbivalence`_, this in fact
    seems to be unused, `BTSLemmaCase`_ being used there instead.

BTSAnnotation
~~~~~~~~~~~~~

.. TODO BTSAnnotation

BTSCorpusHeader
~~~~~~~~~~~~~~~

.. ATTENTION::
     This seems to be unused.

BTSCorpusObject
~~~~~~~~~~~~~~~

This is the base class for objects that can be shown in one of the tree viewers. This is a subtype of BTSObject, and as
such also includes everything of `BTSNamedTypedObject`_, `AdministrativDataObject`_ and `BTSIdentifiableItem`_:

.. code::

    _id, name, type, subtype, sortKey, code, relations, externalReferences, revisions, state, revisionState, visibility

.. ATTENTION::
    Do not confuse this with the similarly named ``BTSTCObject`` (from "Text Corpus Object") or ``BTSTextCorpus``. Both
    are subclasses of ``BTSCorpusObject``. The later is an individual corpus such as the ``bbawfelsinschriften`` while
    the former is something like an annotated folder that is part of a corpus or another folder.

:``passport``:
    The BTSPassport of the object. This contains a more-or-less arbitrary, loosely schematized collection of keys and
    values describing this object.

:``corpusPrefix``:
    This field contains the name of the corpus this object is stored in, which corresponds to the couchDB database name.
    For example, ``bbawfelsinschriften`` for ``aaew_corpus_bbawfelsinschriften``. Obviously, maintaining a local copy of
    the database name inside every single object is of the highest priority for purposes of data security.

:``workPhase``:
    Never used.

BTSGraphic
~~~~~~~~~~

This type generally describes a single hieroglyph. Generally, a word is rendered as a sequence of several `BTSGraphic`_
objects, each containing one component of the word's `MdC`_ encoding. Note that since a word's `MdC`_ encoding sometimes
contains elements that don't directly map to hieroglyphs such as the `cartouche`_ markers ``<>`` not every `BTSGraphic`_
directly maps to a graphical representation. Also note that `MdC`_ control characters such as ``:`` or ``*`` are
prepended to the affected `BTSGraphic`_ instance's ``code``.

Hieroglyphs are rendered by `JSesh`_. There is some transformation logic that feeds `MdC`_ into `JSesh`_ given e.g.
`BTSWord`_ or `BTSSenctence`_. Note that the `MdC`_ variant BTS uses in `BTSGraphic`_ is slightly different to the one
`JSesh`_ parses. Due to the one-way nature (`MdC`_ always goes from the BTS into `JSesh`_) and the particular
implementation the BTS grammar is more lenient than the one of `JSesh`_. A good starting point to understand this is
`transformTextToJSeshMdCString in BTSTextEditorControllerImpl.java`_.

:``code``:
    This hieroglyph's `MdC`_ string.
:``ignored``:
:``innerSentenceOrder``:
    This is an integer field that in rare cases is used to reorder ``graphics`` within a word. When the sentence is
    translated into `MdC`_ for display, each word's ``graphics`` are passed through a stable sort keyed on
    ``innerSentenceOrder``. This results in the intermediate `MdC`_ representation of the word passed to `JSesh`_ being
    in a different order.

.. TODO exactly explain what ``innerSentenceOrder`` does.

.. _`MdC`: https://en.wikipedia.org/wiki/Manuel_de_Codage
.. _`cartouche`: https://en.wikipedia.org/wiki/Cartouche
.. _`JSesh`: https://jsesh.qenherkhopeshef.org/
.. _`transformTextToJSeshMdCString in BTSTextEditorControllerImpl.java`: https://github.com/telota/bts/blob/7f7933ae338cbb22553156658823f42e3464dac5/core/corpus-controller-impl/src/org/bbaw/bts/core/corpus/controller/impl/partController/BTSTextEditorControllerImpl.java#L1036-L1115

BTSImage
~~~~~~~~

.. ATTENTION::
     This seems to be unused.

BTSLemmaCase
~~~~~~~~~~~~

This type describes one of several alternative transliterations in a `BTSAmbivalence`_. It is a `BTSNamedTypedObject`_
and thus also a `BTSIdentifiableItem`_.

.. ATTENTION::
    Do not confuse this with `BTSLemmaEntry`_. These two a totally diferrent. `BTSLemmaEntry`_ describes a single
    dictionary entry. `BTSLemmaCase`_ one of several alternative transliterations in a `BTSSenctence`_ via
    `BTSAmbivalence`_.

:``name``:
    This field contains a string with a number identifying this alternative transliteration, e.g. ``"1"`` or ``"2"``.
    This string is entered by a human. There is some inconsistencies, but almost always this string is equal to the
    index (starting from 1) of this `BTSLemmaCase`_ instance in the containing `BTSAmbivalence`_ instance's ``cases``
    array.
:``scenario``:
    This field contains the actual transliteration content of this alternative. This field behaves just like
    ``sentenceItems`` in `BTSSenctence`_ with the exception that in practice, a `BTSAmbivalence`_ instance does not
    contain other `BTSAmbivalence`_ instances.

BTSLemmaEntry
~~~~~~~~~~~~~

.. ATTENTION::
    Do not confuse this with `BTSLemmaCase`_. These two a totally diferrent. `BTSLemmaEntry`_ describes a single
    dictionary entry. `BTSLemmaCase`_ one of several alternative transliterations in a `BTSSenctence`_ via
    `BTSAmbivalence`_.

BTSMarker
~~~~~~~~~

This type describes a marker such as "begin of sentence" or "this is line number $foo". It is a possible element in the
``sentenceItems`` array of a `BTSSenctence`_ or the ``scenario`` array of a `BTSLemmaCase`_. `BTSMarker`_ is a subtype
of `AdministrativDataObject`_ and `BTSNamedTypedObject`_ and thus in turn `BTSIdentifiableItem`_. Note that the ``type``
and ``name`` fields of `BTSMarker`_ is used totally differently than the ``type`` and ``name`` fields of
`BTSNamedTypedObject`_.

:``type``:
:``name``:
    Both these fields are used to contain human-readable, non-standardized comment on this marker's function

.. TODO properly understand how both of these are used in practice.

:``value``:
    Almost never used.

BTSPassport
~~~~~~~~~~~

`BTSPassport`_ is a type describing attributes on a `BTSCorpusObject`_. The attributes in a `BTSPassport`_ instance are
of form key➜value and may be categorized into nested named groups. A loose schema of this (which keys are allowed, in
which groups they may occur) is described in the `BTSConfig`_. 95.61% of roughly 1M attributes conform to this schema,
4.39% or roughly 40k do not. Below is a list of all attribute paths that do not conform to the schema in the
`BTSConfig`_.

=========================================== ======= ==========
Attribute path                              count   percentage
=========================================== ======= ==========
√.object.description_of_object→copy             169 0.02
√.object.description_of_object→agent           3165 0.34
√.object.description_of_object→<none>          2016 0.21
√.thesaurus.main_group→old_id                  3442 0.37
√.thesaurus.main_group→old_thesaurus_number    3442 0.37
√.thesaurus.main_group→termsort                3442 0.37
√.text.textual_metadata→egyTextName           25676 2.73
=========================================== ======= ==========

Passport Key Graph
^^^^^^^^^^^^^^^^^^
.. figure:: graphs/passport_graph_mapped.png
    :width: 100%
    :target: graphs/passport_graph_mapped.pdf

    A Graph of passport attribute paths found in actual live data.


:``children``:
    A list of `BTSPassportEntryGroup`_ instances

BTSPassportEntry
~~~~~~~~~~~~~~~~

This type is a simple superclass of `BTSPassportEntryItem`_ and `BTSPassportEntryGroup`_. It is a subtype of
`BTSIdentifiableItem`_.

.. ATTENTION: Do not confuse `BTSPassportEntry`_ and its subtype `BTSPassportEntryItem`_.

BTSPassportEntryGroup
~~~~~~~~~~~~~~~~~~~~~

This type describes a group of `BTSPassportEntry`_ objects in a `BTSPassport`_ or nested in another
`BTSPassportEntryGroup`_. `BTSPassportEntryGroup`_ is a subtype of `BTSPassportEntry`_ and in turn
`BTSIdentifiableItem`_.

:``type``:
    The key of this group. This is the same as the ``value`` attribute of the `BTSConfigItem`_ instance corresponding to
    the node of this attribute in the schema in the `BTSConfig`_.
:``children``:
    A list of `BTSPassportEntryGroup`_ and further nested `BTSPassportEntryGroup` instances (possibly both types). This
    hierarchy seems to be mostly just 2-3 levels deep.

.. ATTENTION: The ``type`` attribute is used differently than in `BTSNamedTypedObject`_ here.

BTSPassportEntryItem
~~~~~~~~~~~~~~~~~~~~

This type describes a single key→value attribute in a `BTSPassport`_. `BTSPassportEntryItem`_ is a subtype of
`BTSPassportEntry`_ and in turn `BTSIdentifiableItem`_.

.. ATTENTION: Do not confuse `BTSPassportEntry`_ and its subtype `BTSPassportEntryItem`_.

:``type``:
    The key of this attribute. This is the same as the ``value`` attribute of the `BTSConfigItem`_ instance
    corresponding to the node of this attribute in the schema in the `BTSConfig`_.
:``value``:
    The actual string value of this attribute.

.. ATTENTION: The ``type`` attribute is used differently than in `BTSNamedTypedObject`_ here.

BTSSenctence
~~~~~~~~~~~~

.. WARNING:: This is actually written BTSSen*c*tence.

A `BTSSenctence`_ (sic!) is the basic element of a `BTSText`_. It consists of a list of `BTSSentenceItem`_ objects along
translations into a number of languages. `BTSSenctence`_ is a subtype of `BTSTextItems`_.

:``sentenceItems``:
:``translation``:
    The multilingual translations of this sentence as a `BTSTranslations`_ object.

BTSSentenceItem
~~~~~~~~~~~~~~~

.. WARNING:: Despite the misspelling in the name of `BTSSenctence`_, `BTSSentenceItem`_ is not misspelled.

.. TODO BTSSentenceItem

BTSTCObject
~~~~~~~~~~~

.. TODO BTSTCObject

BTSText
~~~~~~~

This type describes a single text. It is a subtype of `BTSCorpusObject`_ and uses most of the fields defined there. The
actual text content is contained as a list of sentences in the ``textItems`` field of the `BTSTextContent`_ instance in
this object's ``textContent`` field.

Note that as `BTSText`_ inherits from `BTSCorpusObject`_ it can have its own passport filled with information and it is
displayed in the object browser. Everything below `BTSText`_ such as `BTSSenctence`_ or `BTSWord`_ objects is not a
`BTSCorpusObject`_ and thus cannot be navigated to in the object browser and cannot hold its own passport.

:``textContent``: 
    A `BTSTextContent`_ object. Technically, this is a list of `BTSTextItems`_ objects each of which could be either a
    `BTSSenctence`_, a `BTSAmbivalence`_ or a `BTSMarker`_. Luckily, in practice the immediate contents of this are
    exclusively `BTSSenctence`_ instances.

BTSTextContent
~~~~~~~~~~~~~~

This type is a simple container for a list of `BTSSenctence`_ objects. It is a very basic EObject.

BTSTextCorpus
~~~~~~~~~~~~~

.. TODO BTSTextCorpus

BTSTextItems
~~~~~~~~~~~~

This is an interface meant to bundle a bunch of stuff that could theoretically be put into a text. It directly inherits
from `AdministrativDataObject`_ and `BTSNamedTypedObject`_ and thus only *nearly* is a `BTSObject`_.

BTSTextSentenceItem
~~~~~~~~~~~~~~~~~~~

This is an interface combining `BTSTextItems`_ and `BTSSentenceItem`_.

BTSThsEntry
~~~~~~~~~~~

.. TODO BTSThsEntry

BTSWord
~~~~~~~

`BTSWord`_ is a type describing a single transliteration of a single egyptian word.  It is a possible element in the
``sentenceItems`` array of a `BTSSenctence`_ or the ``scenario`` array of a `BTSLemmaCase`_ (transliteration
alternative), and it can be in ``words`` of a `BTSLemmaEntry`_ (dictionary entry).

`BTSWord`_ is a subtype of `BTSIdentifiableItem`_ and `BTSNamedTypedObject`_. Despite this, ``name`` or ``type`` are
never used with it.

.. TODO check the definition of this with Jakob and Simon

:``lKey``:
    This field is only used when this `BTSWord`_ is part of a transliteration in a `BTSText`_. If this `BTSWord`_ is
    part of a `BTSLemmaEntry`_, this field is always null.

    This field contains the couchDB object ``_id`` of the `BTSLemmaEntry`_ this word can be found in. Note that
    `BTSLemmaEntry`_ object ids are human-readable short numbers (5-6 digit) that also serve as human-readable
    dictionary keys.

:``flexCode``:
    This field is only used when this `BTSWord`_ is part of a transliteration in a `BTSText`_. If this `BTSWord`_ is
    part of a `BTSLemmaEntry`_, this field is always null.

.. TODO explain this, and where it comes from

:``wChar``:
    This field contains this word's unicode transliteration, such as ``"pꜣy=j-nb-n-ꜥḏdjw"``. The grammar of this is
    rather complex and differs depending on whether this is part of a text transliteration or a dictionary entry.

:``translation``:
    This field contains a `BTSTranslations`_ instance with all translations of this word.

:``graphics``:
    This field contains a list `BTSGraphic`_ objects that when concatenated make up this word.

