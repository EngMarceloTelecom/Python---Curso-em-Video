from telnetlib import Telnet

host = '200.204.1.4'
with Telnet('host') as tn:
    tn.interact()
