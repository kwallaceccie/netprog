import getpass
import telnetlib

file=open("switches.txt","r")

for switchIp in file:
    switchIp=switchIp.strip()
    print("Current switch: "+switchIp)
    user = input("Enter your username: ")
    password = getpass.getpass()

    tn = telnetlib.Telnet(switchIp)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    tn.write(b"int range fa 0/1-10\n")
    tn.write(b"auto qos voip cisco-phone\n")
    tn.write(b"end\n")
    tn.write(b"copy run star\n")
    tn.write(b"\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))

file.close()