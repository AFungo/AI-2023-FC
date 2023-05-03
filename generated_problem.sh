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
      sleep 1
      if ps -p $pid > /dev/null; then
        echo "Problem no finish"
	      kill $PID
      else
        
        echo "Problem finish"
	      kill $PID
      fi
done

exec 3<&-
