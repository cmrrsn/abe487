#!/usr/bin/env python3

import sys
import os

input = sys.argv
if len(input) !=2:
	print('Usage: {} SEQ'.format(sys.argv[0]))
	sys.exit(1)
rna = input[1]

procode = dict()
file = open('codons.rna').read().split()

count = 0
for line in file:
	if count % 2 ==0:
		procode[line] = '' 	
		prev = line
	else:
		procode[prev] = line
	count+=1
k=3
rnapiece = []
for i in range(0, len(rna), k):
	rnapiece.append(rna[i:i+k])

protein = []
for line in rnapiece:
	for key in procode.keys():
		if line.lower() == key.lower():
			protein.append(procode[key])

print('{}'.format(''.join(protein)))
	


