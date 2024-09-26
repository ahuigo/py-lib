import signal
import time

def handler(signum, frame):
    print(f"exit main process,sig={signum} ")

signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGSEGV, handler)
signal.signal(signal.SIGSYS, handler)

time.sleep(50)
