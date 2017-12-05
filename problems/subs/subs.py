#!/usr/bin/env python3

import os
import sys

args = sys.argv

if len(args) < 3:
    print('Usage: {} ARG ARG'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)


ss = args[1]
tt = args[2]
output = []

for i in range(len(ss)):
	if ss[i:i+len(tt)] == tt:
		output.append(i+1)

if len(output) < 1:
	print('Not found'.format(tt, ss))
else:
	print (*output)
