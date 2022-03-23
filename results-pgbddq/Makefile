TLIM = 1000
INTERP = /usr/bin/python3
SRCDIR = ../src
SOLVDIR = ../pgbddq
WRAP = $(INTERP) $(SRCDIR)/wrap.py $(TLIM)
SOLVER = $(INTERP) $(SOLVDIR)/pgbddq.py
GRAB = $(INTERP) $(SRCDIR)/grab_data.py

FDIR = ../files-pgbddq

copy:
	cp -p $(FDIR)/*.{qcnf,order} .

.SUFFIXES: .qcnf .pgbddq_data

.qcnf.pgbddq_data:
	$(WRAP) $(SOLVER) -i $< -p $*.order -m n | tee $@

data:
	$(GRAB) "Total time" *-true-after.pgbddq_data > pgbddq-true-after.csv
	$(GRAB) "Total time" *-false-after.pgbddq_data > pgbddq-false-after.csv

clean:
	rm -f *~ *.pgbddq_data

superclean: clean
	rm -f *.order *.qcnf
