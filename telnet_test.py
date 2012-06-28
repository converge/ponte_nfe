#!/usr/bin/env python

import telnetlib

HOST = "192.168.1.75"

tn = telnetlib.Telnet(HOST, "3436")

tn.write("nfe.statusservico\n")
tn.write(".\n")
tn.write("exit\n")
tn.write(".\n")

print tn.read_all()

tn.close() 

