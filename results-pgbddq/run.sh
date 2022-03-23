#!/bin/sh

for N in 16 17 18 19 20 22 23 24 
do
#    make ldomino-$N-winA-true-end.pgbddq_data
#    make ldomino-$N-winB-false-end.pgbddq_data
    make ldomino-$N-winA-true-after.pgbddq_data
    make ldomino-$N-winB-false-after.pgbddq_data
done

for N in 15 21 25
do
#    make ldomino-$N-winB-true-end.pgbddq_data
#    make ldomino-$N-winA-false-end.pgbddq_data
    make ldomino-$N-winB-true-after.pgbddq_data
    make ldomino-$N-winA-false-after.pgbddq_data
done

