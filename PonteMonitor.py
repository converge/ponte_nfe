#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

Created on 02/07/2012

@author: João Vanzuita <joao@fortunata.com.br> 
https://github.com/converge/ponte_nfe
 
'''

import telnetlib

class PonteMonitor(object):
    '''
    classdocs
    '''
    
    HOST = "192.168.1.75"
    PORT = "3436"
    arquivoXml = None
    X = "c:\\temp\\nfe_132.txt"
    tn = None


    def __init__(self):
        '''
        Constructor
        '''
        self.tn = telnetlib.Telnet(self.HOST, self.PORT)
    
    # @todo: testar se conectou    
    def conectarMonitor(self):
        self.tn = telnetlib.Telnet(self.HOST, self.PORT)
    
    def commit(self):
        self.tn.write('exit\n')
        self.tn.write('.\n')
        return self.tn.read_all()
        
    def statusServico(self):
        self.tn.write('nfe.statusServico()\n')
        self.tn.write('.\n')
        if self.commit().find('OK: ') != -1:
            return True
        else:
            return False
        
    def criarNfeSefaz(self, arquivoTxt):
        self.tn.write('nfe.criarNfeSefaz(' + arquivoTxt + ', 1)\n')
        self.tn.write('.\n')
        
        if self.commit().find("OK: ") != -1:
            # encontra arquivo XML na string
            # -3 porque ele pega algum lixo no caminho
            self.arquivoXml = self.commit().find('C:\\')
            self.arquivoXml = self.commit()[self.arquivoXml:(len(self.commit())-3)]
            return True
        else:
            return False 
        
        
        
# teste
def main():
    pm = PonteMonitor()
    pm.conectarMonitor()
    if pm.statusServico():
        print 'Status do Serviço: OK'
    else:
        print 'Status do Serviço: ERRO'
    pm.conectarMonitor()
    if pm.criarNfeSefaz():
        print 'Criação do arquivo XML: OK'
    else:
        print 'Criação do arquivo XML: ERRO'
    
    

if __name__ == "__main__":
    main()