
SOURCES = index.rst db_structure_bts3.rst
OUTDIR = docs

all: $(addprefix $(OUTDIR)/,$(SOURCES:%.rst=%.html))

$(OUTDIR)/%.html: %.rst
	rst2html5 --link-stylesheet --stylesheet=bootstrap.css,style.css $< $@
