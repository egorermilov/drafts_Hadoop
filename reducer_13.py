#!/usr/bin/python

# TASK :: Total sales value and total number of sales acress all the stores

import sys

salesSum = 0
countSum = 0
oldKey = None


for line in sys.stdin:
    thisSale = line.strip()
    
    salesSum += float(thisSale)
    countSum += 1

print salesSum, "\t", countSum

