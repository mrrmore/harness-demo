#!/bin/bash

echo "Hello from Harness CI"

echo "Printing Star Triangle"

for ((i=1; i<=5; i++))
do
    for ((j=1; j<=i; j++))
    do
        printf "* "
    done
    printf "\n"
done
