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

.. figure:: graphs/model_interface_graph.png
   :width: 50%
   :target: graphs/model_interface_graph.pdf

   Graph aller Interfaces der Modelle.

http://btsmodel/1.0#//AdministrativDataObject
http://btsmodel/1.0#//BTSComment *
http://btsmodel/1.0#//BTSConfig
http://btsmodel/1.0#//BTSConfigItem *
http://btsmodel/1.0#//BTSConfiguration *
http://btsmodel/1.0#//BTSDBBaseObject
http://btsmodel/1.0#//BTSDBCollectionRoleDesc *
http://btsmodel/1.0#//BTSDBConnection *
http://btsmodel/1.0#//BTSDate
http://btsmodel/1.0#//BTSExternalReference *
http://btsmodel/1.0#//BTSIDReservationObject *
http://btsmodel/1.0#//BTSIdentifiableItem
http://btsmodel/1.0#//BTSInterTextReference *
http://btsmodel/1.0#//BTSNamedTypedObject
http://btsmodel/1.0#//BTSObject
http://btsmodel/1.0#//BTSObservableObject
http://btsmodel/1.0#//BTSOperator
http://btsmodel/1.0#//BTSPassportEditorConfig *
http://btsmodel/1.0#//BTSProject *
http://btsmodel/1.0#//BTSProjectDBCollection *
http://btsmodel/1.0#//BTSReferencableItem
http://btsmodel/1.0#//BTSRelation *
http://btsmodel/1.0#//BTSRevision
http://btsmodel/1.0#//BTSTimespan
http://btsmodel/1.0#//BTSTranslation *
http://btsmodel/1.0#//BTSTranslations *
http://btsmodel/1.0#//BTSUser *
http://btsmodel/1.0#//BTSUserGroup *
http://btsmodel/1.0#//BTSWorkflowRule
http://btsmodel/1.0#//BTSWorkflowRuleItem
http://btsmodel/1.0#//DBLease *
http://btsmodel/1.0#//StringToStringListMap
http://btsmodel/1.0#//StringToStringMap
http://btsmodel/1.0#//UserActionCounter

http://btsCorpusModel/1.0#//BTSAbstractParagraph
http://btsCorpusModel/1.0#//BTSAbstractText
http://btsCorpusModel/1.0#//BTSAmbivalence *
http://btsCorpusModel/1.0#//BTSAmbivalenceItem
http://btsCorpusModel/1.0#//BTSAnnotation *
http://btsCorpusModel/1.0#//BTSCorpusHeader
http://btsCorpusModel/1.0#//BTSCorpusObject
http://btsCorpusModel/1.0#//BTSGraphic *
http://btsCorpusModel/1.0#//BTSImage
http://btsCorpusModel/1.0#//BTSLemmaCase *
http://btsCorpusModel/1.0#//BTSLemmaEntry *
http://btsCorpusModel/1.0#//BTSMarker *
http://btsCorpusModel/1.0#//BTSPassport *
http://btsCorpusModel/1.0#//BTSPassportEntry
http://btsCorpusModel/1.0#//BTSPassportEntryGroup *
http://btsCorpusModel/1.0#//BTSPassportEntryItem *
http://btsCorpusModel/1.0#//BTSSenctence *
http://btsCorpusModel/1.0#//BTSSentenceItem
http://btsCorpusModel/1.0#//BTSTCObject *
http://btsCorpusModel/1.0#//BTSText *
http://btsCorpusModel/1.0#//BTSTextContent *
http://btsCorpusModel/1.0#//BTSTextCorpus *
http://btsCorpusModel/1.0#//BTSTextItems
http://btsCorpusModel/1.0#//BTSTextSentenceItem
http://btsCorpusModel/1.0#//BTSThsEntry *
http://btsCorpusModel/1.0#//BTSWord *

In db but not in model:
http://btsmodel/1.0#//BTSText !!!

Fundamentale Objekttypen
------------------------


