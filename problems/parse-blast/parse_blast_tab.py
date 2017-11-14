#!/usr/bin/env python3

import argparse
import csv
import os
import sys

# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(description='Parse Blast Tab')
    parser.add_argument('tab', metavar='tab', help='Blast Tabulated Output')
    parser.add_argument('-p', '--pct_id', help='Percent Identity',
                        metavar='float', type=float, default=0.0)
    parser.add_argument('-e', '--evalue', help='maximum evalue',
                        metavar='float', type=float, default=1.0)
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    blastfile = args.tab
    pctid = args.pct_id
    evalue = args.evalue
    flds = 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'.split()

    for line in open(blastfile):
        row = dict(zip(flds, line.split('\t')))
        if float(row['pident']) >= pctid and float(row['evalue']) <= evalue:
            print('{}\t{}\t{}\t{}'.format(row['qseqid'], row['sseqid'], row['pident'], row['evalue']))   
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
