#!/usr/bin/env pytho
import ADC0832
import time

def init():
	ADC0832.setup()

def loop():
	while True:
		res = ADC0832.getResult()
		if 0 <= res < 50:
			print("very wet: " + 'raw value is  %d' % res)
		if 50 <= res < 150:
			print("wet: " + 'raw value is %d' % res)
		if 255 >= res > 200:
			print("very dry: " + 'raw value is %d' % res)
		if 200 >= res > 150:
			print("dry: " + 'raw value is %d' % res) 
		time.sleep(2)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'