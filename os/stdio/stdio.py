import fileinput,sys
#for line in fileinput.input(): pass


print(sys.stdout,sys.stdin)

if __name__=="__main__":
    # read
    print("read:",sys.stdin.read())
    print("read:",open(0).read())
    # write
    out="out"
    print(sys.stdout.write(out))



