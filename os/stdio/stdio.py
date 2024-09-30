import fileinput,sys
#for line in fileinput.input(): pass
'''
#只读取一行
q=input() 

# 读取多行(ctrl+D)
sys.stdin.read() 
open(0).read() 
'''
print(sys.stdout,sys.stdin)

if __name__=="__main__":
    # read
    if sys.stdin.isatty:
        # read from tty(ctrl+D quit)
        print("read tty:",sys.stdin.read())
        print("read tty:",open(0).read())
    else:
        #read from pipe
        print("read pipe:",sys.stdin.read())
    # write
    out="out"
    print(sys.stdout.write(out))



