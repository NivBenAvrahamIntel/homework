#!/usr/bin/env python

import sys

current_dist = None
current_node = None
current_path = None
current_neighbours = 0
node = None 

for line in sys.stdin:
    line = line.strip().split('\t')

    if len(line) < 3:
        continue

    node = line[0]
    distance = line[1]
    if len(line) == 3:
        path = line[2]
        neighbours = 0
    if len(line) == 4:
        path = line[3]
        neighbours = line[2] if line[2] != "0" else 0

    try:
        distance = int(distance)
    except:
        continue

    if current_node == node:
        if distance < current_dist:
            current_dist = distance
            current_path = path
        if neighbours != 0:
            current_neighbours = neighbours
    else:
        if current_node:
            print('%s\t%s' % (current_node, current_dist))
        current_node = node
        current_dist = distance
        current_path = path
        current_neighbours = neighbours

if current_node == node:
    print('%s\t%s' % (current_node, current_dist))
