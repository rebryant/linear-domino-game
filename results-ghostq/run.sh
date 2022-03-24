#!/bin/sh

#for N in 16 17 18 19 20 22 23 24 
for N in 16 17 18 19 20 22 23 24
do
    make ldomino-$N-winA-true-end.ghostq_data
    make ldomino-$N-winB-false-end.ghostq_data
    make ldomino-$N-winA-true-after.ghostq_data
    make ldomino-$N-winB-false-after.ghostq_data
done

#for N in 15 21 25
for N in 15 21 25
do
    make ldomino-$N-winB-true-end.ghostq_data
    make ldomino-$N-winA-false-end.ghostq_data
    make ldomino-$N-winB-true-after.ghostq_data
    make ldomino-$N-winA-false-after.ghostq_data
done

