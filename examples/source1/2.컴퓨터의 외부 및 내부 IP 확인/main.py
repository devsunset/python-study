import socket
import requests
import re

ip_addr = socket.gethostbyname(socket.gethostname())
print(ip_addr)

print("=====================================")

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부IP: ",in_addr.getsockname()[0])

print("=====================================")

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부IP: ",out_addr)