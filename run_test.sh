#!/bin/bash

pytest engine/test/problems/practica_1/test_n_queens.py -k test_eight_queen_breadth_first_graph_search > result.txt 
#pid=$!
#sleep 60
#if ps -p $pid > /dev/null; then
#    kill $pid
#fi
