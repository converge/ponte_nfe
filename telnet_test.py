#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import telnetlib

HOST = "192.168.1.75"
PORT = "3436"

X = "c:\\temp\\nfe_132.txt"


def criarNfeSefaz():
    tn = telnetlib.Telnet(HOST, PORT)
    tn.write('nfe.criarNfeSefaz(' + X + ', 1)\n')
    tn.write('.\n')
    
    tn.write('exit\n')
    tn.write('.\n')
    
    response = tn.read_all()
    
    if response.find("OK: ") != -1:
        print 'Criação do XML: OK'
        
        # encontra arquivo XML na string
        # -3 porque ele pega algum lixo no caminho
        arquivoXml = response.find('C:\\')
        arquivoXml = response[arquivoXml:(len(response)-3)]
        
        tn.close()
        
        validarNfe(arquivoXml)
        
    else:
        print 'Criação do arquivo XML: ERRO'
        tn.close()
    
def validarNfe(arquivoXml):
    
    tn = telnetlib.Telnet(HOST, PORT)
    tn.write('nfe.validarNfe(' + arquivoXml + ')\n')
    tn.write('.\n')
    
    tn.write('exit\n')
    tn.write('.\n')
    
    response = tn.read_all()
    
    if response.find("OK: ") != -1:
        print 'Validação do XML: OK'
        tn.close()
        assinarNfe(arquivoXml)
    else:
        print 'Validação do XML: ERRO'
        tn.close()
    
    tn.close()

def assinarNfe(arquivoXml):
    
    tn = telnetlib.Telnet(HOST, PORT)
    tn.write('nfe.assinarNfe(' + arquivoXml + ')\n')
    tn.write('.\n')
    
    tn.write('exit\n')
    tn.write('.\n')
    
    response = tn.read_all()
    
    if response.find("OK: ") != -1:
        print 'Assinatura do XML: OK'
        tn.close()
        enviarNfe(arquivoXml)
    else:
        print 'Assinatura do XML: ERRO'
        tn.close()
        
def enviarNfe(arquivoXml):

    tn = telnetlib.Telnet(HOST, PORT)
    tn.write('nfe.enviarNfe(' + arquivoXml + ')\n')
    tn.write('.\n')
    
    tn.write('exit\n')
    tn.write('.\n')
    
    response = tn.read_all()
    
    if response.find("OK: ") != -1:
        print 'Envio do XML: OK'
        tn.close()
        enviarEmail(arquivoXml)
    else:
        print 'Envio do XML: ERRO'
        tn.close()
        
def enviarEmail(arquivoXml):
    
    destiny = raw_input('Informe o e-mail de destino: ')
    
    tn = telnetlib.Telnet(HOST, PORT)
    tn.write('nfe.enviarEmail(' + destiny + ',' + arquivoXml + ',1)\n')
    tn.write('.\n')
    
    tn.write('exit\n')
    tn.write('.\n')
    
    response = tn.read_all()
    
    if response.find("OK: ") != -1:
        print 'Envio do XML por e-mail: OK'
        tn.close()
        imprimirDanfe(arquivoXml)
    else:
        print 'Envio do XML por e-mail: ERRO'
        tn.close()
    
def imprimirDanfe(arquivoXml):
    
    tn = telnetlib.Telnet(HOST, PORT)
    tn.write('nfe.imprimirDanfe(' + arquivoXml + ')\n')
    tn.write('.\n')
    
    tn.write('exit\n')
    tn.write('.\n')
    
    response = tn.read_all()
    
    if response.find("OK: ") != -1:
        print 'Impressão da DANFE: OK'
        tn.close()
    else:
        print 'Impressão da DANFE: ERRO'
        tn.close()

def main():
    criarNfeSefaz()
    

if __name__ == "__main__":
    main()



