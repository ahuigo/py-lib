import sys, termios,os,select

def getchar(timeout=20): # 20s
    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0

    try:
        termios.tcsetattr(fd, termios.TCSAFLUSH, new)
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            return sys.stdin.read(1)
        else:
            print("Timeout")
            return None
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)
