#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://docs.python.org/2/library/argparse.html#choices
'''
Face Recognition

USAGE:

./recog.py 

@author Pedro Moreira
@date 20140718

'''
import sys, getopt, argparse, os, getpass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from imports import Folders, Folder
 
Base = declarative_base()
def main(argv):
    """
    Fazer o parse dos argumentos fornecidos pelo user
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-import_folders", 
                        required=False, 
                        action="store_true", 
                        help="Recursively Import Folders")
    parser.add_argument("-import_folder", 
                        required=False, 
                        action="store_true",
                        help="Import Folder")
    parser.add_argument("-recog", 
                        required=False, 
                        action="store_true",
                        help="recognize photo against DB")
    args = parser.parse_args()

    try:                  
        if args.import_folders:
            a = Folders()
        elif args.import_folder:
            a = Folder()
        elif args.recog:
            print "Recognizing photo against current db\r\n"
    finally:
        print "bye\r\n"

if __name__ == "__main__":
    main(sys.argv[1:])
