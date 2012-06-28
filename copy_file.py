#!/usr/bin/env python

import glob
import os
from shutil import *

PATH = "/Users/joao/Downloads/nfe/"

os.chdir(PATH)

for files in glob.glob('nfe_99.txt'):
    print files
    #copyfile(PATH + files, "/Users/joao/Downloads/teste/" + files)
    move(PATH + files, "/Users/joao/Downloads/teste/" + files)