INPUTS := $(wildcard svgs/[0-9]*.svg)
PATHS := $(INPUTS:svg=path)
PNGS := $(INPUTS:svg=png)


all: $(PATHS)

%.path: %.svg
	cat $< | xpath -q -e //g > $@

%.png: %.svg
	convert -density 200 $< $@
