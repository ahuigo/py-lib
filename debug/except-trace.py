#process BrokenPipeError: Broken pipe

def f3():
    return 1/0

def f2():
    f3()

def f1():
    #f2()
    try:
        f2()
    except Exception as e:
        sss()
        #raise e
    

def main():
    f1()

if __name__ == '__main__':
    main()
