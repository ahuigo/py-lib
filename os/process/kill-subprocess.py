import time
class T:

    def job(self, i):
        print("job %s"%i)
        time.sleep(10)

    def main(self):
        #run process
        processes = {}
        for i in range(3):
            p = Process(target=self.job, args=(i,))
            p.start()
            processes[i]=p.pid
        




T().main()
