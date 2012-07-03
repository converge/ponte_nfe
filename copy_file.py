#!/usr/bin/env python

import glob
import os
from shutil import *

PATH = "/Users/joao/Downloads/"

os.chdir(PATH)

for files in glob.glob('nfe_111.txt'):
    print files
    copyfile(PATH + files, "/Users/joao/Downloads/teste/" + files)
    #move(PATH + files, "/Users/joao/Downloads/teste/" + files)