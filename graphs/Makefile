
GRAPHER = python3 ../tools/grapher.py
DATABASE = ../data/bts.sqlite3
OUTDIR = ../docs/graphs

DOT_GRAPHS = model_type_graph model_interface_graph

all: $(DOT_GRAPHS)

$(DOT_GRAPHS): %: $(OUTDIR)/%.pdf $(OUTDIR)/%.png

$(addprefix $(OUTDIR)/,$(addsuffix .pdf,$(DOT_GRAPHS))): $(OUTDIR)/%.pdf: %.dot
	dot -x -Goverlap=prism100 -Tpdf $^ > $@

$(addprefix $(OUTDIR)/,$(addsuffix .png,$(DOT_GRAPHS))): $(OUTDIR)/%.png: %.dot
	dot -x -Goverlap=prism100 -Tpng $^ > $@

model_type_graph.dot: $(DATABASE)
	$(GRAPHER) $(DATABASE) $@ -s org.bbaw.bts. -i org.bbaw.bts.btsmodel.,org.bbaw.bts.model. -e org.bbaw.bts.btsmodel.provider.

model_interface_graph.dot: $(DATABASE)
	$(GRAPHER) $(DATABASE) $@ -s org.bbaw.bts. -i org.bbaw.bts.btsmodel.,org.bbaw.bts.model. -e org.bbaw.bts.btsmodel.provider. --only-interfaces

