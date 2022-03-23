TLIM = 1000
INTERP = /usr/bin/python3
SRCDIR = ../src
SOLVDIR = ~/repos/ghostq/bin
CONV =   $(SOLVDIR)/qcir-conv.py
SOLVER = $(SOLVDIR)/ghostq
WRAP = $(INTERP) $(SRCDIR)/wrap.py $(TLIM)
GRAB = $(INTERP) $(SRCDIR)/grab_data.py

FDIR = ../files

copy:
	cp -p $(FDIR)/*.qcnf .

.SUFFIXES: .qcnf .ghostq_data

.qcnf.ghostq_data:
	$(CONV) $< -write-gq -o $*.gq
	$(WRAP) $(SOLVER) $*.gq -s-cnf | tee $@

data:
	$(GRAB) "Total time" *-true-after.ghostq_data > ghostq-true-after.csv
	$(GRAB) "Total time" *-false-after.ghostq_data > ghostq-false-after.csv
	$(GRAB) "Total time" *-true-end.ghostq_data > ghostq-true-end.csv
	$(GRAB) "Total time" *-false-end.ghostq_data > ghostq-false-end.csv

clean:
	rm -f *~ *.ghostq_data

superclean: clean
	rm -f *.order *.qcnf
