import psutil,sys
pid = int(sys.argv[1])
current_process = psutil.Process(pid)
children = current_process.children(recursive=True)
for child in children:
    print('Child pid is {}'.format(child.pid))
