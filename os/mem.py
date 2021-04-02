import os, psutil; 
print(os.getpid())
print('常驻内存',psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "M")
print(psutil.Process(os.getpid()).memory_info())

