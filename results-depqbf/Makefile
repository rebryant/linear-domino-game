TLIM = 1000
INTERP = /usr/bin/python3
SRCDIR = ../src
SOLVDIR = ~/repos/depqbf
WRAP = $(INTERP) $(SRCDIR)/wrap.py $(TLIM)
SOLVER = $(SOLVDIR)/depqbf
GRAB = $(INTERP) $(SRCDIR)/grab_data.py

FDIR = ../files

copy:
	cp -p $(FDIR)/*.qcnf .

.SUFFIXES: .qcnf .depqbf_data

.qcnf.depqbf_data:
	$(WRAP) $(SOLVER) $< | tee $@

data:
	$(GRAB) "Total time" *-true-after.depqbf_data > depqbf-true-after.csv
	$(GRAB) "Total time" *-false-after.depqbf_data > depqbf-false-after.csv
	$(GRAB) "Total time" *-true-end.depqbf_data > depqbf-true-end.csv
	$(GRAB) "Total time" *-false-end.depqbf_data > depqbf-false-end.csv

clean:
	rm -f *~ *.depqbf_data

superclean: clean
	rm -f *.order *.qcnf
