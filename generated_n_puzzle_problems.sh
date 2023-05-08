#!/bin/bash
# shellcheck disable=SC2155
export PYTHONPATH=$PYTHONPATH:$(pwd)

filename="./main/cfg_files/n_puzzle_new.csv"
touch "n_puzzle_metrics/python_log.txt"
touch "n_puzzle_metrics/log_errors.txt"
echo "" > n_puzzle_metrics/log_errors.txt
exec 3< "$filename"
# shellcheck disable=SC2034
read -r header_line <&3

# shellcheck disable=SC1073
while IFS=',' read -r -u 3 result
do
      echo "$result" >> n_puzzle_metrics/log_errors.txt
      # shellcheck disable=SC2028
      echo -e "\n" >> n_puzzle_metrics/log_errors.txt
      timeout -s SIGKILL 10s python3 ./main/n_puzzle.py "$result" >> n_puzzle_metrics/python_log.txt 2>> n_puzzle_metrics/log_errors.txt
      # shellcheck disable=SC2181
      if [ $? -eq 0 ]; then
        echo "Problem finish $result" >> n_puzzle_metrics/log.txt
      else
        echo "Problem no finish $result" >> n_puzzle_metrics/log.txt
        python3 ./main/n_puzzle_not_goal.py "$result"
      fi
done

exec 3<&-
