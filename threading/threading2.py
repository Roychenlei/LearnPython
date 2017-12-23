#!/usr/bin/env python
import threading
import time

def thread_job():
	print("T1 start")
	for i in range(10):
		time.sleep(0.001)
	print ('T1 finish')

def T2_job():
	print ("T2 start\n")
	print ("T2 finish\n")

def main():
	added_threading = theading.Thread(target=threawd_job,name= 'T1')
	thread2=threading.Thread(target=T2_job,name='T2')
	added_thread.start()
	thread2.start()
	print ('all done')

if __name__ == '__main__':
	main()
