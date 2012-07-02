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
    tn = None


    def __init__(self):
        '''
        Constructor
        '''
    
    # @todo: testar se conectou    
    def conectarMonitor(self):
        self.tn = telnetlib.Telnet(self.HOST, self.PORT)
    
    def fecharConexaoMonitor(self):
        self.tn.write('exit\n')
        self.tn.write('.\n')
        self.tn.close()
        
    def statusServico(self):
        self.tn.write('nfe.statusServico()\n')
        self.tn.write('.\n')
        print self.tn.read_all()
        
# teste
def main():
    pm = PonteMonitor()
    pm.conectarMonitor()
    pm.statusServico()
    
    

if __name__ == "__main__":
    main()