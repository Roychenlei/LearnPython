import threading
import time

def T1_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print("T2 finish\n")
def main():
    add_thread1 = threading.Thread(target=T1_job,name='T1')
    add_thread2 = threading.Thread(target=T2_job,name='T2')
    add_thread1.start() 
    add_thread2.start()
    add_thread1.join()
    print('done\n')
    


if __name__=='__main__':
    main()
