Database Structure of the BTSv3
===============================

Introduction
------------

BTS version 3 is running on a CouchDB. There is a single central instance as well as one local instance per BTS3
installation. The local instances are kept in sync with the central instance using the synchronization feature built
into CouchDB. The java process of a BTS3 instance talks to its local CouchDB instance using HTTP against localhost.
Embedded into the BTS3 java process is an Elasticsearch instance that is fed from the local couchdb. This
synchronization being only half working is the reason one frequently must manually kick of "indexing" actions from a
complaining BTS3 dialog.

This document starts out with an overview of all object types defined in the source, not their manifestation in the
database. Thus it includes super-types that are not directly present in the database.

General Object Layout inside the Database
-----------------------------------------

All object types listed here map 1:1 to Java classes. Each of these classes is mapped to Eclipse's eObject system. Every
object in the database contains an attribute ``eClass`` that uniquely identifies the type of this object. This attribute
looks like a HTTP URL but isn't: ``http://{"btsmodel" or "btsCorpusModel"}/1.0#//{eClass name}``.  There is two groups
of eClass definitions, called models: The ``btsmodel`` or base model and the ``btsCorpusModel`` (sic!) or corpus model.
The base model mainly contains internal management types. The corpus model contains types for the actual payload of the
BTS.

Following are two graphs that describe the relationship between all types, one for each model.

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

Tables of Defined eClass Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following is a table per model of all defined eClasses including information on whether they are to be found in the
database.

.. table::

    ======================================================= =================== =============
    eClass                                                  In database [#db]_  Notes
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

.. table::

    ======================================================= =================== =============
    eClass                                                  In database [#db]_  Notes
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

.. [#db] This eClass is present only in the model, not in the database. This is the case e.g. for abstract base types.
.. [#implonly] There is no custom implementation of this eClass. The corresponding interface uses a generic
    implementation from eclipse.

Database types
--------------

There are several different database types that are used by the BTS.

.. NOTE::
    A single CouchDB instance may contain several "databases", each of which may contain a whole bunch of disparate
    "documents".

Global
~~~~~~

These global databases are present exactly once and are common to all projects and corpora.

.. _`Global admin database`:

:``admin``:
    This database contains miscellaneous global data. It contains all `BTSProject`_ instances as well as the
    `BTSUser`_ and `BTSUserGroup`_ instances used for access control.

.. _`Global notification database`:

:``notification``:
    This database is used for a homebrewn locking scheme. See `DBLease`_.
:``users``:
    This is a couchdb-internal database.
:``replicator``:
    This is a couchdb-internal database.

Project
~~~~~~~

The project databases exist up to once per project. Sometimes, a project does not have all possible project
databases.

.. _`project corpus index database`:

:``{project name}_corpus``:
    This database is basically an index of all corpora that are part of this project through their respective
    `BTSTextCorpus`_ objects.

.. _`project admin database`:

:``{project name}_admin``:
    This database contains the project's configuration, as in `BTSConfig`_. For some reason, it also contains all
    `BTSComment`_ objects that belong to this project.

.. _`project word list database`:

:``{project name}_wlist``:
    This is the project's word list. It contains all `BTSLemmaEntry`_ objects of this project. The texts in the
    project have their words linked into this database. Objects are keyed by their ~6-digit decimal lemma keys.

.. _`project thesaurus database`:

:``{project name}_ths``:
    This is the project's thesaurus database. It contains all `BTSThsEntry`_ objects belonging to this project.
    Basically you can consider this database a project-specific grand enum table.

.. _`project atext database`:

:``{project name}_atext``:
    This database type is almost entirely unused. This seems to be part of some unfinished feature.

Corpora
~~~~~~~

The private corpus database exists once per corpus. These contain the bulk of the data in the BTS.

.. _`private corpus database`:

:``{project name}_corpus_{corpus name}``:
    This database contains all `BTSCorpusObject`_ instances that belong to this project. This is mostly
    `BTSTCObject`_ and `BTSText`_ instances.

.. to generate data type-database statistics:
    for infix in corpus.; begin echo $infix; jq -c '.docs[].eClass' *$infix*json | sort | uniq -c | sort -h; echo; end | tee typestats; end
    for infix in admin.json; begin echo $infix; jq -c '.docs[].eClass' admin.json | sort | uniq -c | sort -h; echo; end | tee -a typestats; end
    for infix in users replicator notification _admin wlist ths corpus_ atext; begin echo $infix; jq -c '.docs[].eClass' *$infix*.json | sort | uniq -c | sort -h; echo; end | tee -a typestats; end


Object types of the base model
------------------------------

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
`partOf`_ `BTSRelation`_.

.. NOTE::
    All `BTSComment`_ instances are stored in the `project admin database`_.

.. ATTENTION::
    Do not confuse this with `BTSAnnotation`_, which describes a highlighted part of a text.

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

.. _ownerReferencedTypesStringList:

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
    format roughly is ``{source}>>{target}[,{target}...]``. ``{source}`` generally is one of the strings described in
    `BASIC_OBJECT_TYPES in BTSConstants.java`_ and describes which object types this entry applies to. This means if this ORTS list is set on a passport entry config and the corresponding input widget is loaded as part of a corpus object's passport editor the tarets given in this line will be applied.
    
    Each ``{target}`` entry points either at a `BTSConfig`_ subtree with leaf nodes being possible values or points at a
    particular ``type`` of `BTSThsEntry`_ objects in the global thesaurus. The input fields use this type to filter the
    `BTSThsEntry`_ instances they display in their browsers.

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

    .. ATTENTION::
        Please do not attempt to put anything but ``[a-zA-Z0-9_]`` in there as the whole
        `ownerReferencedTypesStringList`_ logic would probably break as soon as there's dots or angle brackets or
        commas anywhere.

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

.. NOTE::
    All `BTSConfiguration`_ instances are stored in the `project admin database`_.

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
    
.. _`DBCollectionKey`:

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

.. NOTE::
    All `BTSIDReservationObject`_ instances are stored in the `project word list database`_.

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
    ever used with `partOf`_ to express the hierarchical structure of the object tree. Below is an exhaustive table of
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

    .. _`Select from Thesaurus`:

    :``Select from Thesaurus``: This results in a text field and a button. Usage is a bit different to regular text
        fields. You can directly input an object's ID or name here, but you have to press a key combination to "resolve"
        this into a proper reference to the object via the autocompletion. If this is not done, the input value is not
        persisted.

        Next to this weird text field is two buttons that are actually labels. One opens an object browser on the
        currently referenced object. The other opens another object browser, but one that only displays objects matched
        by `ownerReferencedTypesStringList`_.
    :``Select from Configuration``: This results in a drop-down list containing entries that are themselves read from
        "the configuration". The values this drop-down list allows are pointed at in the
        `ownerReferencedTypesStringList`_ field of `BTSConfigItem`_.

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

.. NOTE::
    All `BTSProject`_ instances are stored in the `global admin database`_.

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
stored in the *head* object. So, a `partOf`_ relation describing that object ``A`` is a part of object ``B`` would be
stored in object ``A``. Read: ``A is partOf B``.

Every relation contains the couchDB ``_id`` of its target object in its ``objectId`` field. 

Relations come in many flavors. The important one is `partOf`_, which is used to express hierarchical structure in the
object browser. It can be used on most anything. The other relation type flavors are only used on ``BTSLemmaEntry``
objects. Below are some nice stats on these.

Due to the inherently asymmetric nature of this representation, most "relation types" need a reciprocal type to be put
at the far end of the relation. Such pairs are e.g. ``successor`` and ``predecessor`` or ``composes`` and
``composedOf``. Note that these are sometimes not named very well.

.. ATTENTION:: `partOf`_ relations do not have a reciprocal element.

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

.. _partOf:

PartOf relations
^^^^^^^^^^^^^^^^

In certain cases such as when used with a `BTSComment`_ a `partOf`_ relation may contain ``parts``. Each "part" is a
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
    Technically, the `partOf`_ graph is only directed. In practice, it seems it is also acyclic and something would
    probably crash if it wasn't. It is, however, *not* a vanilla tree as objects can have several parents.

.. ATTENTION::
    TODO: Right now I can't make any statements on the equivalency of two `partOf`_ relations using the same target
    ``objectId`` but each containing different ``parts`` and only one `partOf`_ relation using the same target
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

.. NOTE::
    All `BTSUser`_ instances are stored in the `global admin database`_.

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

.. NOTE::
    All `BTSUserGroup`_ instances are stored in the `global admin database`_.

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

.. NOTE::
    All `DBLease`_ instances are stored in the `global notification database`_.

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
    seems to be unused, `BTSLemmaCase`_ being used there instead. For type information hava a look at the table under
    `BTSTextSentenceItem`_.

BTSAnnotation
~~~~~~~~~~~~~

`BTSAnnotation`_ is a type describing a highlighted part of a text. `BTSAnnotation`_ is a `BTSCorpusObject`_ and as such
inheriting a whole slew of miscellaneous fields. The usage of `BTSAnnotation`_ is a bit patchy.  Following is a list of
all nontrivial fields that are used with `BTSAnnotation`_. The two semantically most relevant fields are ``type`` and
``name``, as well as the one `partOf`_ `BTSRelation`_.

.. NOTE::
    A `BTSAnnotation`_ on some object is stored in the same database as the target object. This means an annotation
    on e.g. a `BTSCorpusObject`_ will be stored in the corpuses `private corpus database`_ while an annotation on a
    `BTSLemmaEntry`_ will be stored in the project's `project word list database`.

.. TODO verify this storage association

.. ATTENTION::
    Do not confuse this with `BTSComment`_, which describes a human-readable comment on some object *or* part of text.

Fields used with BTSAnnotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
======================= ===== =========
Field                   Count Frequency
======================= ===== =========
<total>                 13862
state                   13862   100.00%
type                    10090    72.79%
name                     8016    57.83%
corpusPrefix             5148    37.14%
passport                  696     5.02%
subtype                    54     0.39%
externalReferences[]        3     0.02%
sortKey                     2     0.01%
======================= ===== =========

Type values used with BTSAnnotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
======================= ===== =========
Type                    Count Frequency
======================= ===== =========
<total>                 13862
rubrum                   9927  71.61%
lexical                    48   0.35%
textual                    30   0.22%
conceptual                 29   0.21%
Annotation-Leipzig         20   0.14%
undefined                  13   0.09%
Layout                      8   0.06%
<empty>                     7   0.05%
ConceptualGroup2            6   0.04%
ConceptualGroup3            2   0.01%
======================= ===== =========

Type values used with named BTSAnnotations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
======================= ===== =========
Type                    Count Frequency
======================= ===== =========
rubrum                   4352     54.3%
<null>                   3513     43.8%
lexical                    44      0.5%
textual                    28      0.3%
conceptual                 25      0.3%
Annotation-Leipzig         19      0.2%
undefined                  13      0.2%
Layout                      8      0.1%
ConceptualGroup2            6      0.1%
<empty string>              6      0.1%
ConceptualGroup3            2      0.0%
======================= ===== =========

The most common names of BTSAnnotations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``name`` of a `BTSAnnotation`_ by default contains ``"Rubrum"``. Otherwise, it is mostly a human-readable comment.
Many a `BTSAnnotation`_ does not have a name. Note that ``name`` has a long-tail distribution with very many rarely used
values.

.. To extract name statistics: jq -c '.docs[] | select(.eClass == "http://btsCorpusModel/1.0#//BTSAnnotation") | .name | select(. != null)' *.json|sort|uniq -c|sort -rn|head -n 20

================= ===== =========
                  Count Frequency
================= ===== =========
<name not null>    8016
"Rubrum"           4348    54.24%
"supralinear"       177     2.21%
"Osiris"            177     2.21%
"Chiffrenschrift"   113     1.41%
"Ptol VIII"         104     1.30%
"Textfeld"          101     1.26%
"titre"              75     0.94%
"Bildfeld"           63     0.79%
"griechisch"         57     0.71%
"Pehou"              41     0.51%
"paroles Osiris"     39     0.49%
"Sekhet"             35     0.44%
"Kolophon"           34     0.42%
"lexical"            33     0.41%
"hieratisch"         31     0.39%
"Nil"                30     0.37%
"nome"               27     0.34%
"Isis"               24     0.30%
"textual"            23     0.29%
"Giebelfeld"         23     0.29%
================= ===== =========

Mapping between BTSAnnotation and BTSText parts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Almost always, a `BTSAnnotation`_ has a single `partOf`_ `BTSRelation`_ pointing at a `BTSText`_. There is only two
exceptions in the entire database of which each has two `partOf`_ relations. See the following table for the frequency
of `BTSText`_ as a relation target compared to other types.

.. To count annotation relations with parts field: jq -c '.docs[] | select(.eClass == "http://btsCorpusModel/1.0#//BTSAnnotation") | .relations[0] | select(has("parts"))' *.json|wc -l

======================================= ======= =========
Type                                    Count   Frequency
======================================= ======= =========
BTSText (total)                         13830   99.77%
BTSText (Relation has ``parts`` field)  13796   99.52%
<unknown>                               15       0.10%
BTSLemmaEntry                           8        0.06%
BTSTextCorpus                           5        0.04%
BTSTCObject                             4        0.03%
<parts only>                            1        0.01%
BTSThsEntry                             1        0.01% 
======================================= ======= =========


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

.. NOTE::
    All instances of `BTSCorpusObject`_ is stored in the `private corpus database`_.

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
    in a different order. The reason for this is that there are cases of words which are written in hieroglyphs in a
    different order than they are pronounced. In the BTS, the oder of words in the database always follows the
    pronunciation and transliteration. To allow for the hieroglyph rendering assuming a different order,
    ``innerSentenceOrder`` may be set.

.. TODO Add an example to ``innerSentenceOrder``

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

This type describes a single lemma in the project's dictionary. It is a direct subtype of `BTSCorpusObject`_ and as
such uses many of its fields including the passport.

.. NOTE::
    All `BTSLemmaEntry`_ instances are stored in the `project word list database`_.

.. ATTENTION::
    Do not confuse this with `BTSLemmaCase`_. These two a totally diferrent. `BTSLemmaEntry`_ describes a single
    dictionary entry. `BTSLemmaCase`_ one of several alternative transliterations in a `BTSSenctence`_ via
    `BTSAmbivalence`_.

Notable inherited fields
^^^^^^^^^^^^^^^^^^^^^^^^

:``type``:
:``subtype``:
    These are used to express the word type of this entry such as ``substantive`` or ``aadjective`` for ``type`` and
    ``verb_4-inf`` or ``kings_name`` for ``subtype``.  Possible values are enumerated in the `BTSConfig`_ under
    ``√.objectTypes.Lemma``.

:``name``:
    This field contains the unicode transliteration of the lemma's egyptian pronunciation.

:``revisionState``:
    This field contains a lifecycle state for this entry.

    =========================== ===== =========
                                Count Frequency
    =========================== ===== =========
    null                           10     0.02%
    "new"                          12     0.02%
    "obsolete"                    752     1.44%
    "published-obsolete"         3723     7.13%
    "published-awaiting-review" 14250    27.30%
    "published"                 33451    64.08%
    =========================== ===== =========

:``relations``:
    While the rest of the BTS exclusively uses partOf_ relations_, lemmata heavily use all sorts of relations. Below is
    a list detailing how many BTSLemmaEntry_ there are with a given number of relations_.

    ============== ===== =========
    # of relations Count Frequency
    ============== ===== =========
    0              47070    69.97%
    1              12498    18.58%
    2               4221     6.27%
    3               1379     2.05%
    4                704     1.05%
    5                369     0.55%
    6                240     0.36%
    7                137     0.20%
    8                129     0.19%
    9                 69     0.10%
    ...
    71                 1     0.00%
    73                 1     0.00%
    75                 1     0.00%
    77                 1     0.00%
    91                 1     0.00%
    ============== ===== =========

.. _relations: BTSRelation_

Specific fields
^^^^^^^^^^^^^^^

:``translations``:
    This field contains a BTSTranslations_ object containing all the translations of this entry into several languages.

:``words``:
    This field contains the words of this entry. A BTSLemmaEntry_ of a compound word should ideally consist of several
    words, however there is no mechanism that guarantees this.
    
    In many cases, the latter entries of ``words`` have their ``wChar`` field surrounded by parentheses as in ``(foo)``.
    This is to mark collocations in specializations of a verb. That is, a verb ``have`` that has a broad meaning is
    present in the word list with one generic entry for the verb and with a number of specialized entries, one for each
    collocation and meaning ``have (kittens)``. These cases are also expressed through partOf_ and ``contains``
    relations_.

    Below is a table of how many entries there are with a given length of ``words``.

    ====== ===== =========
    Length Count Frequency
    ====== ===== =========
    1      50689    97.11%
    2       1223     2.34%
    3        185     0.35%
    4         45     0.09%
    0         24     0.05%
    5         19     0.04%
    6          7     0.01%
    7          6     0.01%
    ====== ===== =========

    .. ATTENTION::
        Note that there are many cases of entries that have several words where all hieroglyphs are bunched into the
        first word, and the later words only contain MdC_. This is an artifact of the initial data import.

:``ignore``:
    This field is unused.

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

This is an interface meant to bundle a bunch of stuff that could theoretically be put into a `BTSSenctence`_. It
directly inherits from `BTSNamedTypedObject`_. For details see `BTSTextSentenceItem`_.

BTSTCObject
~~~~~~~~~~~

.. ATTENTION::
    Try to not confuse this with `BTSTextCorpus`_, `BTSCorpusObject`_, `BTSTextContent`_ or `BTSObject`_.

`BTSTCObject`_ ("Berlin Text System Text Corpus Object") is a `BTSCorpusObject`_ describing what is in effect a folder
with other computer things. The general convention is that a `BTSTCObject`_ maps to some physical place or thing and its
`BTSTCObject`_ descendants are parts of it. Example: ``〈Pyramidentexte〉`` contains ``Pyramide Pepis I.`` contains
``〈Sargkammer〉`` contains ``〈"Wartesaal"/vestibule〉`` contains ``〈Westwand〉`` contains 26 `BTSText`_ instances. As
you can see there is no particular schema to these names, and ever representing them in some sort of path language will
be quite challenging due to their liberal use of weird characters.

A `BTSTCObject`_ notably may possess a `BTSPassport`_ describing what effects to extended object metadata. It does not
have any fields beyond what it inherits from `BTSCorpusObject`_.

As usual, hierarchy is expressed using a `partOf`_ `BTSRelation`_. As follows there are rare cases of multiple ancestors
that make this graph not be a tree.

===================== ===== =========
# of partOf Relations Count Frequency
===================== ===== =========
<total>               16008   100.00%
1                     15988    99.88%
2                        19     0.12%
3                         1     0.01%
===================== ===== =========

Types values used with BTSTCObject
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=========== ===== =========
Type        Count Frequency
=========== ===== =========
<total>     16008
TCObject     8239    51.47%
ObjectPart   4175    26.08%
Caption      1445     9.03%
Scene        1281     8.00%
Group         327     2.04%
Arrangement   166     1.04%
TCSuperText    34     0.21%
<empty>         2     0.01%
undefined       1     0.01%
=========== ===== =========

A `BTSTCObject`_'s type manifests itself in the icon displayed for this object in the tree viewer.

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

A `BTSTextCorpus`_ is sort of a top-level folder for `BTSCorpusObject`_ instances. A `BTSTextCorpus`_ belongs to exactly
one `BTSProject`_. It is a basic `BTSCorpusObject`_ with two quirks: It may contain a `BTSCorpusHeader`_ (which in
practice it never does) and it has a flag ``active`` that is not persisted in the database. The list of active corpora
is stored in the app's preferences.

Each `BTSTextCorpus`_ has its own CouchDB database (i.e. database within the same CouchDB instance). The association
between a `BTSProject`_ and its corpora is done via the names of these databases. The format is ``{project
name}_corpus_{corpus name}``, e.g. ``aaew_corpus_bbawgrabinschriften``. When anything is loaded from a corpuses
database, the non-persisted `DBCollectionKey`_ field inherited from `BTSDBBaseObject`_ is set to the database name. The
content of this field is later used to access the project.

.. NOTE::
    A corpuses `BTSTextCorpus`_ instance is stored in the `project corpus index database`_.

BTSTextItems
~~~~~~~~~~~~

This is an interface meant to bundle a bunch of stuff that could theoretically be put into a text. It directly inherits
from `AdministrativDataObject`_ and `BTSNamedTypedObject`_ and thus only *nearly* is a `BTSObject`_. For details see
`BTSTextSentenceItem`_

BTSTextSentenceItem
~~~~~~~~~~~~~~~~~~~

This is an interface combining `BTSTextItems`_ and `BTSSentenceItem`_, supposedly meant to describe types implementing
both. In practice it is not really used as all two usages also directly implement its super-interfaces. Following is a
table of types and which of this group of interfaces they implement

=============================== ======================== ===================== ============================ ===========================
Type                            Is a `BTSSentenceItem`_? Is a `BTSTextItems`_? Is a `BTSTextSentenceItem`_? Is a `BTSAmbivalenceItem`_?
=============================== ======================== ===================== ============================ ===========================
`BTSMarker`_                    ✔                        ✔                     ✔                            ✔
`BTSAmbivalence`_               ✔                        ✔                     ✔                            ✘
`BTSWord`_                      ✔                        ✘                     ✘                            ✔
`BTSSenctence`_                 ✘                        ✔                     ✘                            ✘
=============================== ======================== ===================== ============================ ===========================

BTSThsEntry
~~~~~~~~~~~

`BTSThsEntry`_ (Berlin Text System Thesaurus Entry) is a subtype of `BTSCorpusObject`_ not containing any fields of its
own that describes a semantically sensible value that can be put into some particular passport field. See
`ownerReferencedTypesStringList`_ in `BTSConfigItem`_ and `Select from Thesaurus`_ in `BTSPassportEditorConfig`_ for
details on how the corpus side of things looks.

In practice, all instances `BTSThsEntry`_ are organized into subtrees via `partOf`_ relations. All entries in one
subtree share one ``type`` and describe all the possible values that a particular type of passport field may assume.
Within subtrees the entries are organized into some semantically sensible hierarchy. For example, the ``findSpot``
entries in ``3 = Fundstellen`` are organized according to their geographical hierarchy. ``3 = Funstellen`` contains
``Wüste östlich des Niltals und Küste des Roten Meeres (Staatsgebiet Ägypten und Sudan)`` contains ``Routen zum Roten
Meer`` contains ``Wadi Abbad``.

.. WARNING::
    There may be BTSThsEntry objects without parents. Also there might be some with several parents. Just keep that in
    mind.

.. NOTE::
    All `BTSThsEntry`_ instances are stored in the `project thesaurus database`_.

BTSWord
~~~~~~~

`BTSWord`_ is a type describing a single transliteration of a single egyptian word.  It is a possible element in the
``sentenceItems`` array of a `BTSSenctence`_ or the ``scenario`` array of a `BTSLemmaCase`_ (transliteration
alternative), and it can be in ``words`` of a `BTSLemmaEntry`_ (dictionary entry).

`BTSWord`_ is a subtype of `BTSIdentifiableItem`_ and `BTSNamedTypedObject`_. Despite this, ``name`` or ``type`` are
never used with it.

.. TODO check the definition of this with Jakob and Simon

:``lKey``:
    This field is mostly used when this `BTSWord`_ is part of a transliteration in a `BTSText`_. If this `BTSWord`_ is
    part of a BTSLemmaEntry_, this field is null most of the time but may point to other entries in case of a compound
    word.

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

