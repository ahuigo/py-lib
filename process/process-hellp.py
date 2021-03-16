from multiprocessing import Process
import os,time,signal

# 子进程要执行的代码
def run_proc(name):
        print('我Run child process %s (%s)...' % (name, os.getpid()))
        print('我2Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    p = Process(target=run_proc, args=('test',))
    p.start()
    #p.kill()
    #p.join()

