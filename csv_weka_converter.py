#! /anaconda/bin/python

""" CSV to Weka-CSV Converter

author: Jordan N. Gumm

converts CSV file to weka-usable CSV file
usage:
    csv_weka_converter.py [-h] input_file output_file
command-line inputs:
    input_file - path to a CSV file to convert
    output_file - path to save converter CSV file to

"""

import h5py
import argparse
import numpy as np
import sys
import os.path


def remove_bad_chars(line):
    """ Remove bad characters
    
    Weka identifies certain characters as delimiters by
    default.  We only want commas to be left as a delimiter.
    So, we remove everything else.
    
    """
    return line.replace("'", "").replace("&", "").replace('"', "")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a weka-usable CSV file from a source.")
    parser.add_argument(
        "input_file",
        type=str,
        help='Path to a CSV file to convert.')
    parser.add_argument(
        "output_file",
        type=str,
        help='Path to save H5py file to.')

    args = parser.parse_args()
    
    if os.path.exists(args.output_file):
        print "Output file already exists.  Fail."
        quit()
    
    output = open(args.output_file, 'w+')
    for line in open(args.input_file, 'r'):
        output.write(remove_bad_chars(line))
    output.close()
    


if __name__ == '__main__':
    main()
