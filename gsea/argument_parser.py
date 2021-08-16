import os
import sys
import logging
import argparse
from os.path import realpath

def parse_arguments():
    logger = logging.getLogger()
    logger.info('Verifying paths provided')
    parser = argparse.ArgumentParser(description='Please provide input and output paths')

    parser.add_argument('-i', '--input', dest='input', type=str,
                        help='Path to input folder', required=True)

    parser.add_argument('-o', '--output', dest='output', type=str,
                        help='Path to output folder', required=True)

    parser.add_argument('-db', '--database', dest='database', type=str,
                        help='Path to database folder', required=True)

    parser.add_argument('-f', '--format', dest='file_type', type=str,
                        help='Type of input files (s = Seurat or d = DESeq2)', required=True)
    args = parser.parse_args()

    if all((os.path.isdir(realpath(args.input)),
           os.path.isdir(realpath(args.output)),
           os.path.isdir(realpath(args.database)))):
        logger.info('All paths exists!')
        return args
    else:
        logger.error("Provided paths don't exist")
        sys.exit()

