# openssl rand -base64 32
import os,base64
password=base64.b64encode(os.urandom(24)).decode()
print(password)
