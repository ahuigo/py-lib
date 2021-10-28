#process BrokenPipeError: Broken pipe

def f1():
    try:
        msg = 'msg'
        print(1/0)
    except Exception as e:
        print("I can read try var:",msg)

def main():
    f1()

if __name__ == '__main__':
    main()
