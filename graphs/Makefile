
GRAPHER = python3 ../tools/grapher.py
DATABASE = ../data/bts.sqlite3
OUTDIR = ../docs/graphs

DOT_GRAPHS = basemodel_type_graph basemodel_interface_graph corpusmodel_type_graph corpusmodel_interface_graph

all: $(DOT_GRAPHS)

$(DOT_GRAPHS): %: $(OUTDIR)/%.pdf $(OUTDIR)/%.png

$(addprefix $(OUTDIR)/,$(addsuffix .pdf,$(DOT_GRAPHS))): $(OUTDIR)/%.pdf: %.dot
	dot -x -Goverlap=prism100 -Tpdf $^ > $@

$(addprefix $(OUTDIR)/,$(addsuffix .png,$(DOT_GRAPHS))): $(OUTDIR)/%.png: %.dot
	dot -x -Goverlap=prism100 -Tpng $^ > $@

basemodel_type_graph.dot: $(DATABASE)
	$(GRAPHER) $(DATABASE) $@ -s org.bbaw.bts. -i org.bbaw.bts.btsmodel.,org.bbaw.bts.model. -e org.bbaw.bts.btsmodel.provider.

basemodel_interface_graph.dot: $(DATABASE)
	$(GRAPHER) $(DATABASE) $@ -s org.bbaw.bts. -i org.bbaw.bts.btsmodel.,org.bbaw.bts.model. -e org.bbaw.bts.btsmodel.provider. --only-interfaces

corpusmodel_type_graph.dot: $(DATABASE)
	$(GRAPHER) $(DATABASE) $@ -s org.bbaw.bts. -i org.bbaw.bts.btsmodel.BTSObject,org.bbaw.bts.corpus.btsCorpusModel. -e org.bbaw.bts.corpus.btsCorpusModel.provider.

corpusmodel_interface_graph.dot: $(DATABASE)
	$(GRAPHER) $(DATABASE) $@ -s org.bbaw.bts. -g org.bbaw.bts.btsmodel.BTSIdentifiableItem,org.bbaw.bts.btsmodel.BTSNamedTypedObject,org.bbaw.bts.btsmodel.AdministrativDataObject,org.bbaw.bts.btsmodel.BTSObject -i org.bbaw.bts.corpus.btsCorpusModel. -e org.bbaw.bts.corpus.btsCorpusModel.provider. --only-interfaces
	


