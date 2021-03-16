import os, sys, time

ttlForParent = 60;
for i in range(0, 10):
    pid_1 = os.fork()
    print("Hello Worlds!!!")
    if pid_1 == 0:
        time.sleep(30)
        sys.exit();

time.sleep(5);
print("os.wait 会阻塞，等子进程结束后回收子进程")
os.wait()
