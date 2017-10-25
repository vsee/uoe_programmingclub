export TEXINPUTS := $(TEXINPUTS):$(shell pwd)/latex-src

export INKSCAPE=`which inkscape`

FINALTARGET := problem
TARGET := main
GENDIR := gen
PDFLATEXARGS := -halt-on-error -output-directory $(GENDIR)
PDFLATEX_CMD := pdflatex $(PDFLATEXARGS) $(TARGET) 2>/dev/null

.PHONY : clean figures figures-clean

$(FINALTARGET).pdf $(TARGET).log: $(GENDIR) $(TARGET).pdf
		@echo " *** Final Build *** "
		$(PDFLATEX_CMD) >/dev/null
		cp $(GENDIR)/$(TARGET).pdf $(FINALTARGET).pdf

$(TARGET).pdf $(TARGET).aux: figures latex-src/$(TARGET).tex
		@echo " *** Initial Build *** "
		$(PDFLATEX_CMD)

$(GENDIR):
		mkdir -p $(GENDIR)

figures:
	+make -C latex-src/

figures-clean:
	make -C latex-src clean

clean: figures-clean
		rm -fr $(GENDIR)
