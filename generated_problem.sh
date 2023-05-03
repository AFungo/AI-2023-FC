#!/bin/bash
# shellcheck disable=SC2155
export PYTHONPATH=$PYTHONPATH:$(pwd)

filename="./main/cfg_files/n_puzzle.csv"

exec 3< "$filename"
# shellcheck disable=SC2034
read -r header_line <&3

# shellcheck disable=SC1073
while IFS=',' read -r -u 3 result
do
      timeout -s SIGKILL 10s python3 ./main/n_puzzle.py "$result"
      if [ $? -eq 0 ]; then
        echo "Problem finish" >> log.txt
      else
        echo "Problem no finish" >> log.txt
      fi
done

exec 3<&-
