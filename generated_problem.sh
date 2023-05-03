#!/bin/bash
# shellcheck disable=SC2155
export PYTHONPATH=$PYTHONPATH:$(pwd)

filename="./main/cfg_files/n_puzzle.csv"

exec 3< "$filename"
# shellcheck disable=SC2034
read -r header_line <&3

while IFS=',' read -r -u 3 result
do
      python3 ./main/n_puzzle.py "$result" &
      PID=$!
      timeout 10m || wait $PID
      # shellcheck disable=SC2181
      if [ $? -eq 0 ]; then
        echo "Problem result"
      else
        echo "Problem no result"
        kill $PID
      fi
done

exec 3<&-
