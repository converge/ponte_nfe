#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

Created on 02/07/2012

@author: João Vanzuita <joao@fortunata.com.br> 
https://github.com/converge/ponte_nfe
 
'''

from PonteArquivos import PonteArquivos
from PonteMonitor import PonteMonitor

def main():
    
    # config
    PATH = "/Users/joao/Downloads/"
    
    pa = PonteArquivos(PATH)
    pm = PonteMonitor()

    files = pa.processaNovosArquivos()
    print files
    for file in files:
        print pm.criarNfeSefaz(PATH + file)
    
    
    
    

if __name__ == "__main__":
    main()