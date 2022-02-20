#!/usr/bin/python
import sys

#loading data using stdin - reading from reducer1
for row in sys.stdin:
    row = row.strip()
    row = row.split("\t")
    print(f"{row[2]}\t{row[3]}\t{1}")