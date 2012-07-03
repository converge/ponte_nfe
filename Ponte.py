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
    
    # config producao ->
    '''PATH = "/Users/joao/Downloads/nfe/"
    
    pa = PonteArquivos(PATH)
    pm = PonteMonitor()
    
    files = pa.processaNovosArquivos()
    print files
    for file in files:
        print pm.criarNfeSefaz(PATH + file) '''

    
    # config teste ->
    PATH_tmp = "/Users/joao/Downloads/nfe/"
    PATH = "c:\\temp\\nfe_132.txt"
    
    pa = PonteArquivos(PATH_tmp)
    pm = PonteMonitor('192.168.1.75', '3436')
    
    if pm.criarNfeSefaz(PATH):
        print 'Criação do XML: OK'
        pm.conectarMonitor()
        if pm.validarNfe():
            print 'Validação do XML: OK'
            pm.conectarMonitor()
            if pm.enviarNfe():
                print 'Envio do XML: OK'
                pm.conectarMonitor()
                if pm.enviarEmail('joao@fortunata.com.br'):
                    print 'Envio do e-mail ao cliente: OK'
                    pm.conectarMonitor()
                    if pm.imprimirDanfe():
                        print 'Impressão da DANFE: OK'
                    else:
                        print 'Impressão da DANFE: ERRO'
                else:
                    print 'Envio do e-mail ao cliente: ERRO'
            else:
                print 'Envido do XML: ERRO'
        else:
            print 'Validação do XML: ERRO'
    else:
        print 'Criação do XML: ERRO'
    
    
    
    

if __name__ == "__main__":
    main()