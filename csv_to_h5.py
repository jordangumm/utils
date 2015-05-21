#! /anaconda/bin/python

""" CSV to h5py converter

author: Jordan N. Gumm

converts CSV file to H5py file
usage:
    csv_to_h5.py [-h] input_file output_file
command-line inputs:
    input_file - path to a CSV file to convert
    output_file - path to save H5py file to

"""

import h5py
import argparse
import numpy as np
import sys
import os.path


def get_targets(D):
    """ Extract targets from input file examples
    
    Targets are stored as first element in each row of the
    training data, D.
    
    Create a (2 x <d_shape>) matrix of zeros
    where <d_shape> is the number of rows in D
    
    For each target in row,
        if target is 1, set FIRST column of <targets> as 1
        else (if target is 0), set SECOND column of <targets> as 1
    
    """
    targets=np.zeros((D.shape[0], 2))
    for i in range(D.shape[0]):
        if D[i,0] == 1:
            targets[i,0] = 1
        else:
            targets[i,1] = 1
    return targets


def create_h5py(d, targets, output_file):
    """ Output H5py File
    
    """
    f = h5py.File(output_file, 'w')
    #dt = h5py.special_dtype(vlen=np.dtype('float32'))
    f.create_dataset('X', data=d[:,1:], dtype='int64')
    f.create_dataset('y', data=targets, dtype='int64')


def main():
    parser = argparse.ArgumentParser(
        description="Generate an H5py file for pylearn2.")
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
    
    D = np.genfromtxt(args.input_file, delimiter=',')
    targets = get_targets(D)
    create_h5py(D, targets, args.output_file)
    


if __name__ == '__main__':
    main()
