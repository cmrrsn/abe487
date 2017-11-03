#!/usr/bin/env python3

import os
import sys

args = sys.argv

if len(args) < 3:
    print('Usage: {} STR STR'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if len(args[1]) >= len(args[2]):
    seq1 = args[1]
    seq2 = args[2]
else:
    seq1 = args[2]
    seq2 = args[1]

ham = len(seq1)-len(seq2)
count = 0

for bp in seq2:
    if bp.lower() != seq1[count].lower():
        ham += 1
    count += 1

print('{}'.format(ham))
