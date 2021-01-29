#!/bin/python3

import math
import os
import random
import re
import sys



n, m = map(int, input().split())
arr = ''.join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', arr))

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
