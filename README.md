This is a small toy to generate multiplication tables for kids. It can vary the difficulty, the number on entries etc. 
It can print out the tables to a text file, or run an interactive quiz where the difficulty level will change, depending on their ability.
Usage: python tables.py -h

usage: tables.py [-h] [-s SAVE] [-r RANGE] [-n TOTAL_QUESTIONS]
                 [-m METRICS_FILE] [-d DEBUG]

Multiplication Table Quiz and Table Generator

options:
  -h, --help            show this help message and exit
  -s SAVE, --save SAVE  Save multiplication tables to a text file (e.g.,
                        multiplication_tables.txt)
  -r RANGE, --range RANGE
                        Number of entries in each table and number of tables
  -n TOTAL_QUESTIONS, --total-questions TOTAL_QUESTIONS
                        Total number of questions in the quiz
  -m METRICS_FILE, --metrics-file METRICS_FILE
                        File to save learning metrics
  -d DEBUG, --debug DEBUG
                        Print extra info during the quiz
                      
