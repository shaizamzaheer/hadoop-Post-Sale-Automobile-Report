#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.split(",")
    key = line[2]
    value = (line[1],line[3],line[5])
    print (f'{key}\t{value[0]}\t{value[1]}\t{value[2]}')
    # a= (f'{key}\t{value}')
    # print(a.split('\t')[1])
    # b = a.split(',')[0]
    # print(b)
