import os
import logging
import argparse

def parse_arguments():
    logger = logging.getLogger('Verifying provided paths')
    parser = argparse.ArgumentParser(description='Please provide input and output paths')

    parser.add_argument('-i', '--input', dest='input', type=str,
                        help='Path to input folder', required=True)

    parser.add_argument('-o', '--output', dest='output', type=str,
                        help='Path to output folder', required=True)

    parser.add_argument('-db', '--database', dest='database', type=str,
                        help='Path to database folder', required=True)
    args = parser.parse_args()

    if all(os.path.isdir(args.input), os.path.isdir(args.output), os.path.isdir(args.database)):
        logger.info('All paths exists!')
        return args
    else:
        logger.info("Provided paths don't exist")
        break



