import signal
import time,os,sys

def handler(signum, frame):
    print(f"exit main process,sig={signum} ")
    sys.exit(1)

print("pid:", os.getpid())
signal.signal(signal.SIGTERM, handler) # process.terminate() 
signal.signal(signal.SIGINT, handler) # os.kill(pid, signal.SIGINT)
signal.signal(signal.SIGQUIT, handler)

signal.signal(signal.SIGCHLD, handler)
signal.signal(signal.SIGTSTP, handler)
signal.signal(signal.SIGSEGV, handler)
signal.signal(signal.SIGSYS, handler)
time.sleep(50)
'''
3. SIGTERM(15): Terminatted, (kill pid 默认就是15)
1. SIGINT(2): interrupt, Ctrl-c会发送(这在Python中其实被封装成了KeyboardInterrupt异常)，
2. SIGQUIT(3): quit, `Ctrl-\`发送SIGQUIT，
4. SIGKILL(9): force killed,cannot be ignored
3. SIGCHLD: 进程退出，向父进程发出SIGCHLD (chldhandler)
4. SIGTTIN 当后台进程读tty时，tty将发送该信号给相应的进程组，默认行为是暂停进程组中进程的执行
5. SIGCONT: `kill -SIGCONT PID`: Send a continue signal To continue a stopped process via PID
6. SIGHUP: 当tty的另一端挂掉的时候，比如ssh的session断开了，
7. SIGTSTP: 输入CTRL+Z时


'''

