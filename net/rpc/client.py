
#Client.py：
#from xmlrpclib import ServerProxy            #导入xmlrpclib的包 
from xmlrpc import client
s = client.ServerProxy("http://127.0.0.1:8092") #定义xmlrpc客户端 
print(s.fun_add(2,3))
