#!/usr/bin/env python3

import sys
import os


def main():
	"""main"""
	input = sys.argv
	if len(input) !=3:
		print('Usage: {} LEN STR'.format(sys.argv[0]))
		sys.exit(1)
	if input[1].isdigit():
		length = int(input[1])
		if length <1:
			print('Kmer size "{}" must be > 0'.format(length))
			sys.exit(1)
	else:
		print('Kmer size "{}" is not a number'.format(input[1]))
		sys.exit(1)
	seq = input[2]
	if length > len(seq):
		print('There are no {}-mers in "{}"'.format(length, seq))
		sys.exit(1)
	i = 0
	stop = len(seq)-length+1
	kmers = []
	
	for bp in seq:
		if i < stop:
			temp = seq[i:i+length] 
			kmers.append(temp)
			i += 1
	counts = dict()
	for kmer in kmers:
		if not kmer in counts:
			counts[kmer] = 0
		counts[kmer] +=1
	print('{}'.format(seq))
	for kmer in sorted(counts.keys()):
		print('{} {}'.format(kmer, counts[kmer]))



if __name__ == '__main__':
	main()

