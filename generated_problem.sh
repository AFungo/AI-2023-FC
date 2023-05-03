#!/bin/bash
# shellcheck disable=SC2155
export PYTHONPATH=$PYTHONPATH:$(pwd)

filename="./main/cfg_files/n_puzzle.csv"
touch "log.txt"
#touch "python_log.txt"

exec 3< "$filename"
# shellcheck disable=SC2034
read -r header_line <&3

# shellcheck disable=SC1073
while IFS=',' read -r -u 3 result
do
      echo "$result" >> log_errors.txt
      # shellcheck disable=SC2028
      echo -e "\n" >> log_errors.txt
      timeout -s SIGKILL 10s python3 ./main/n_puzzle.py "$result" >> python_log.txt 2>> log_errors.txt
      # shellcheck disable=SC2181
      if [ $? -eq 0 ]; then
        echo "Problem finish $result" >> log.txt
      else
        echo "Problem no finish $result" >> log.txt
      fi
done

exec 3<&-
