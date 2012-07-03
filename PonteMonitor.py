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
    HOST = None
    PORT = None
    xmlFile = None
    tn = None

    #
    # Construtor, conecta ao instanciar
    #
    def __init__(self, host, port):
        '''
        Constructor
        '''
        self.HOST = host
        self.PORT = port
        self.tn = telnetlib.Telnet(self.HOST, self.PORT)
    
    # @todo: testar se conectou    
    def conectarMonitor(self):
        self.tn = telnetlib.Telnet(self.HOST, self.PORT)
        
    def fecharMonitor(self):
        self.tn.close()
    
    #
    # Confirma o último comando executado e devolve a resposta
    #
    def commit(self):
        self.tn.write('.\n')
        self.tn.write('exit\n')
        self.tn.write('.\n')
        return self.tn.read_all()
    
    def verificaRetorno(self, response):
        if response.find('OK: ') != -1:
            return True
        else:
            return False
        
    def statusServico(self):
        self.tn.write('nfe.statusServico()\n')
        self.tn.write('.\n')
        if self.commit().find('OK: ') != -1:
            return True
        else:
            return False
        
    #
    # Cria XML baseado no arquivo TXT
    #
    def criarNfeSefaz(self, arquivoTxt):
        self.tn.write('nfe.criarNfeSefaz(' + arquivoTxt + ', 1)\n')
        response = self.commit()
        if response.find('OK: ') != -1:
            # encontra arquivo XML na string
            # -3 porque ele pega algum lixo no caminho
            self.xmlFile = response.find('C:\\')
            self.xmlFile = response[self.xmlFile:(len(response)-3)]
            return True
        else:
            return False
        
    #
    # Valida XML
    #
    # @return: true or false
    #
    def validarNfe(self):
        self.tn.write('nfe.validarNfe(' + self.xmlFile + ')\n')
        response = self.commit()
        return self.verificaRetorno(response)
    
    #
    # Assina XML
    #
    # @return: true or false
    #    
    def assinarNfe(self):
        self.tn.write('nfe.assinarNfe(' + self.xmlFile + ')\n')
        response = self.commit()
        return self.verificaRetorno(response)
    
    #
    # Enviar XML
    #
    # @return: true or false
    #  
    def enviarNfe(self):
        self.tn.write('nfe.enviarNfe(' + self.xmlFile + ')\n')
        response = self.commit()
        return self.verificaRetorno(response)
    
    #
    # Enviar e-mail com XML ao cliente
    #
    # @param destino: e-mail de destino 
    # @return: true or false
    #  
    def enviarEmail(self, destino):
        self.tn.write('nfe.enviarEmail(' + destino + ',' + self.xmlFile + ',1)\n')
        response = self.commit()
        return self.verificaRetorno(response)
    
    #
    # Abre tela para impressão da DANFE no computador onde o ACBrNFeMonitor está rodando
    #
    # @return: true or false
    #  
    def imprimirDanfe(self):
        self.tn.write('nfe.imprimirDanfe(' + self.xmlFile + ')\n')
        response = self.commit()
        return self.verificaRetorno(response)
    
    