#!/usr/bin/env python

import sys

for line in sys.stdin:
  node, neighbors = line.strip().split("\t")
  neighbors = neighbors.split(",")
  for neighbor in neighbors: 
    print("%s\t%s\t%s" % (node, neighbor, 1))
