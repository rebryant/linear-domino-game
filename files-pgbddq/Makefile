INTERP = python3
GDIR = ../src
GEN = $(INTERP) $(GDIR)/gen_ldom.py

N =    20
VERB =
TF =   true



clean:
	rm -f *~

superclean: clean
	rm -f *.qcnf

ldomino-$(N)-winA-$(TF)-end.qcnf:
	$(GEN) -n $(N) $(VERB) -t e    -o ldomino-$(N)-winA-$(TF)-end.qcnf -O ldomino-$(N)-winA-$(TF)-end.order

ldomino-$(N)-winB-$(TF)-end.qcnf:
	$(GEN) -n $(N) $(VERB) -t e -i -o ldomino-$(N)-winB-$(TF)-end.qcnf -O ldomino-$(N)-winB-$(TF)-end.order

ldomino-$(N)-winA-$(TF)-after.qcnf:
	$(GEN) -n $(N) $(VERB) -t a    -o ldomino-$(N)-winA-$(TF)-after.qcnf -O ldomino-$(N)-winA-$(TF)-after.order

ldomino-$(N)-winB-$(TF)-after.qcnf:
	$(GEN) -n $(N) $(VERB) -t a -i -o ldomino-$(N)-winB-$(TF)-after.qcnf -O ldomino-$(N)-winB-$(TF)-after.order

.SUFFIXES: .qcnf .pgbddq-data

