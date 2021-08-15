import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Please provide input and output paths')

    parser.add_argument('-i', '--input', dest='input', type=str,
                        help='Path to input folder', required=True)

    parser.add_argument('-o', '--output', dest='output', type=str,
                        help='Path to output folder', required=True)

    parser.add_argument('-db', '--database', dest='database', type=str,
                        help='Path to database folder', required=True)
    args = parser.parse_args()

    return args
