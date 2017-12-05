#!/usr/bin/env python3

import os
import sys
from Bio import SeqIO
from collections import OrderedDict
args = sys.argv

if len(args) != 2:
    print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

infile = args[1]

if os.path.isfile(infile) == False:
	print('"{}" is not a file'.format(infile))
	sys.exit(1)

seq = OrderedDict()
with open(infile) as handle:
	for record in SeqIO.parse(handle, "fasta"):
		seq[str(record.id)] = str(record.seq)


for skey, s in seq.items():
	for tkey, t in seq.items():
		if s != t and s[-3:] == t[:3]:
			print('{} {}'.format(skey, tkey))
		




