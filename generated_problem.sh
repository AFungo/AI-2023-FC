#!/bin/bash
# shellcheck disable=SC2155
export PYTHONPATH=$PYTHONPATH:$(pwd)


filename="./main/cfg_files/n_puzzle.csv"

exec 3< "$filename"
# shellcheck disable=SC2034
read -r header_line <&3

while IFS=',' read -r -u 3 result
do
#      echo "$result"
#      python -c "from engine.engine import *"
      python3 ./main/n_puzzle.py "$result"
done

exec 3<&-
