#!/usr/bin/env python3

import sys
import os


def main():

	"""main"""
	args = sys.argv

	if len(args) < 2:
		print('Usage:', args[0], 'STRING')
		sys.exit(1)
	else:
		word = args[1]
		i = 0
	
		for letter in word:
			if letter in 'aeiou':
				i += 1

		if i == 1:
			print('There is {} vowel in "{}."' .format(i, word))

		else:	
			print('There are {} vowels in "{}."' .format(i, word))		

if __name__ == '__main__':
	main()
