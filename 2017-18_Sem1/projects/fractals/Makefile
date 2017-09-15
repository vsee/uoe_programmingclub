export TEXINPUTS := $(TEXINPUTS):$(shell pwd)/latex-src

FINALTARGET := problem
TARGET := main
GENDIR := gen
PDFLATEXARGS := -halt-on-error -output-directory $(GENDIR)
PDFLATEX_CMD := pdflatex $(PDFLATEXARGS) $(TARGET) 2>/dev/null

.PHONY : clean

$(FINALTARGET).pdf $(TARGET).log: $(GENDIR) $(TARGET).pdf
		@echo " *** Final Build *** "
		$(PDFLATEX_CMD) >/dev/null
		cp $(GENDIR)/$(TARGET).pdf $(FINALTARGET).pdf

$(TARGET).pdf $(TARGET).aux: latex-src/$(TARGET).tex
		@echo " *** Initial Build *** "
		$(PDFLATEX_CMD)

$(GENDIR):
		mkdir -p $(GENDIR)

clean: 
		rm -fr $(GENDIR)
