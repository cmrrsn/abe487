#!/usr/bin/env python3

import argparse
import os
import sys
from Bio import SeqIO
# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(description='Argparse Python script')
    parser.add_argument('file', metavar='file', help='FASTA file')
    parser.add_argument('-s', '--start', help='Start position',
                        metavar='int', type=int, default=0)
    parser.add_argument('-e', '--end', help='End position',
                        metavar='int', type=int, default=None)
    parser.add_argument('-m', '--min', help='Minimum length',
			metavar='int', type=int, default=0)
    parser.add_argument('-o', '--outfile', help='Output file', 
                        metavar='str', type=str, default='')
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    start = args.start
    end = args.end
    mint = args.min
    outfile = args.outfile
    infile = args.file
    
    if start > 0:
        start = start - 1
    
    if len(outfile) ==0:
        outfile = infile + '.trimmed'
    
    outfh = open(outfile,'w')
    numtaken= 0
    with open(infile) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            seq = str(record.seq[start:end])
            if len(seq) >= mint:
                numtaken +=1
                outfh.write('\n'.join(['>' + record.id, seq, '']))
    print('Wrote {} sequence{} to "{}"'.format(numtaken, '' if numtaken == 1 else 's', outfile))
                  
# --------------------------------------------------
if __name__ == '__main__':
    main()
