#!/bin/sh

#for N in 16 17 18 19 20 22 23 24 
for N in 16 17 18 19 20
do
    make ldomino-$N-winA-true-end.depqbf_data
    make ldomino-$N-winB-false-end.depqbf_data
    make ldomino-$N-winA-true-after.depqbf_data
    make ldomino-$N-winB-false-after.depqbf_data
done

#for N in 15 21 25
for N in 15 21
do
    make ldomino-$N-winB-true-end.depqbf_data
    make ldomino-$N-winA-false-end.depqbf_data
    make ldomino-$N-winB-true-after.depqbf_data
    make ldomino-$N-winA-false-after.depqbf_data
done

