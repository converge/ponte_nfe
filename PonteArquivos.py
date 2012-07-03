#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

Created on 02/07/2012

@author: João Vanzuita <joao@fortunata.com.br> 
https://github.com/converge/ponte_nfe
 
'''

import glob
import os

class PonteArquivos(object):
    '''
    classdocs
    '''

    sourceFoler = None 

    def __init__(self, source):
        '''
        Constructor
        '''
        self.sourceFolder = source
        os.chdir(self.sourceFolder)
        
    
    def processaNovosArquivos(self):
        return glob.glob('nfe_111.txt')


# teste
def main():
    
    PATH = "/Users/joao/Downloads/"
    pa = PonteArquivos(PATH)
    files = pa.processaNovosArquivos()
    
    
    
    

if __name__ == "__main__":
    main()
        
        
        
        