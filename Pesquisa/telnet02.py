#!/usr/bin/python
import getpass
import sys
import telnetlib

HOST = "177.159.105.251"
user = raw_input("Digite seu usuario Tacacs: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ping 8.8.8.8\n")
