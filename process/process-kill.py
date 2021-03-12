from multiprocessing import Process
import os,time,signal

# 子进程要执行的代码
def run_proc(name):
        print('我Run child process %s (%s)...' % (name, os.getpid()))
        time.sleep(10000)
        print('我2Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
        print('Parent process %s.' % os.getpid())
        p = Process(target=run_proc, args=('test',))
        print('Child process will start.')
        p.start()
        if hasattr(p, 'kill'):
            p.kill()
        else:
            os.kill(p.pid, signal.SIGTERM)
        #p.join()
        print('Child process end.')

