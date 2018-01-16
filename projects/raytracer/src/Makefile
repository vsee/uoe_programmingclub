Q := @
SVG := ${shell ls | grep '\.svg$$'}
OUT := $(SVG:%.svg=%.pdf)

all: $(OUT)

%.pdf: %.svg
	@echo "  INKSCAPE $@"
	$(Q)$(INKSCAPE) -C -z --file=$< --export-pdf=$@ --export-dpi=600

clean:
	rm -f $(OUT)
