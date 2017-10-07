#!/usr/bin/env python3

import sys
import os


def main():
	"""main"""
	seq = sys.argv[1:]
	
	if len(seq) != 1:
		print('Usage: {} STR' .format(sys.argv[0]))
		sys.exit(1)
	i=0
	gc= 0
	for bp in seq[0]:
		i += 1
		if bp in 'gGcC':
			gc += 1
	pgc = int((gc/i)*100)
	print('{}% GC'.format(pgc))
	
      
if __name__ == '__main__':
        main()
