#!/bin/sh

for N in 16 17 18 19 20 22 23 24 
do
    make ldomino-$N-winA-true-end.qcnf N=$N TF=true
    make ldomino-$N-winB-false-end.qcnf N=$N TF=false
    make ldomino-$N-winA-true-after.qcnf N=$N TF=true
    make ldomino-$N-winB-false-after.qcnf N=$N TF=false
done

for N in 15 21 25
do
    make ldomino-$N-winB-true-end.qcnf N=$N TF=true
    make ldomino-$N-winA-false-end.qcnf N=$N TF=false
    make ldomino-$N-winB-true-after.qcnf N=$N TF=true
    make ldomino-$N-winA-false-after.qcnf N=$N TF=false
done
