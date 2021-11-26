import telnetlib
import time

Host = '200.204.1.4'
username = 'a0080822'
password = 'Diogo@02'

tn = telnetlib.Telnet(Host)
tn.read_until(b"login as: ")
tn.write(username.encode("ascii") + b"\n") 
tn.read_until(b"password: ")
tn.write(password.encode('ascii') + b"\n")
print("Successfully connected to %s" % Host)
tn.write(b"ping 8.8.8.8\n")
time.sleep(2)
output = tn.read_very_eager()
print (type("output"))
print(output)
print("done")