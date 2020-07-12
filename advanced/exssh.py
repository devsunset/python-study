# $ pip install paramiko

import paramiko
import getpass
import time

# case 1

# cli = paramiko.SSHClient()
# cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
# server = input("Server: ")  
# user = input("Username: ")  
# pwd = getpass.getpass("Password: ")
 
# cli.connect(server, port=22, username=user, password=pwd)
# stdin, stdout, stderr = cli.exec_command("ls -la")
# lines = stdout.readlines()
# print(''.join(lines)) 
# cli.close()

 
# case 2

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
cli.connect("test.com", username="user", password="pwd")

channel = cli.invoke_shell()
 
channel.send("ls -la\n")
time.sleep(1.0)

output = channel.recv(65535).decode("utf-8")
print(output)
 
cli.close()