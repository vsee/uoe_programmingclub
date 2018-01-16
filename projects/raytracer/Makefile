export TEXINPUTS := $(TEXINPUTS):$(shell pwd)/src

export INKSCAPE=`which inkscape`

FINALTARGET := problem
TARGET := main
GENDIR := gen
PDFLATEXARGS := -halt-on-error -shell-escape 
PDFLATEX_CMD := pdflatex $(PDFLATEXARGS) ../src/$(TARGET) 2>/dev/null

.PHONY : clean figures figures-clean

$(FINALTARGET).pdf $(TARGET).log: $(GENDIR) $(TARGET).pdf
		@echo " *** Final Build *** "
		cd $(GENDIR) ; $(PDFLATEX_CMD) >/dev/null
		cp $(GENDIR)/$(TARGET).pdf $(FINALTARGET).pdf

$(TARGET).pdf $(TARGET).aux $(TARGET).pyg: figures src/$(TARGET).tex
		@echo " *** Initial Build *** "
		cd $(GENDIR) ; $(PDFLATEX_CMD)

$(GENDIR):
		mkdir -p $(GENDIR)

figures:
	+make -C src/

figures-clean:
	make -C src clean

clean: figures-clean
		rm -fr $(GENDIR)
