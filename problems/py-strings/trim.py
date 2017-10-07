#!/usr/bin/env python3

import sys
import os

def trimmed(seq, cuts):
	trim = []
	i = 0
	for bp in seq:
		if i < cuts:
			trim.append(bp)
			i +=1
		else:
			break
	return ''.join(trim)

def main():
	"""main"""

	input = sys.argv
	if len(input) < 2:
        	print('Usage: {} FILE [INT]' .format(sys.argv[0]))
        	sys.exit(1)
		
	if len(input) > 2:
		cuts = int(input[2])
	else:
		cuts = 5
	
	if os.path.isfile(input[1]) == True:
		for line in open(input[1]):
			trim = trimmed(line, cuts)
			print('{}'.format(trim))
	else:		
		trim = trimmed(input[1], cuts)
		print('{}'.format(trim))

if __name__ == '__main__':
	main()
