import signal
import time

'''
def handler(signum, frame):
    print(f"exit main process,sig={signum} ")
    quit()

signal.signal(signal.SIGINT, handler)
'''

def main():
    try:
        print("sleep")
        time.sleep(50)
    except Exception as e:
        print(e)
    finally:
        print("execut finnaly when keybord interupt signal!!!!!!!!!!!")

main()
