#!/bin/bash
clear
for NUM in {1..3}
do
	file_name=tsp_example_${NUM}.txt
    ./tsp $file_name >> tsp_example_times.txt
done
for NUM in {1..7}
do
	file_name=test-input-${NUM}.txt
	./tsp $file_name >> test-input-times.txt
done