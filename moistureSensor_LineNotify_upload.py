#!/usr/bin/env pytho
# -*- coding: utf8 -*-
import ADC0832
import time
import requests
import datetime

def init():
	ADC0832.setup()

def loop():
	while True:
		res = ADC0832.getResult()
		if 0 <= res < 50:
			print("very wet: " + 'raw value is  %d' % res)
			url = "https://notify-api.line.me/api/notify"
			access_token = '************'
			headers = {'Authorization': 'Bearer ' + access_token}
			message = {"水分たっぷりです。まだ水やりはいりません(^^)"}
			payload = {'message': message}
			r = requests.post(url, headers=headers, params=payload,)
                

		if 50 <= res < 150:
			print("wet: " + 'raw value is %d' % res)
			url = "https://notify-api.line.me/api/notify"
			access_token = '************'
			headers = {'Authorization': 'Bearer ' + access_token}
			message = {"まだ水やりは大丈夫ですが、暑い日は気を付けましょう٩(ˊᗜˋ*)و"}
			payload = {'message': message}
			r = requests.post(url, headers=headers, params=payload,)
                
		if 255 >= res > 200:
			print("very dry: " + 'raw value is %d' % res)
			url = "https://notify-api.line.me/api/notify"
			access_token = '************'
			headers = {'Authorization': 'Bearer ' + access_token}
			message = {"水やりしないと死にそうです。早く助けて༼⁰o⁰；༽"}
			payload = {'message': message}
			r = requests.post(url, headers=headers, params=payload,)
                

		if 200 >= res > 150:
			print("dry: " + 'raw value is %d' % res)
			url = "https://notify-api.line.me/api/notify"
			access_token = '************'
			headers = {'Authorization': 'Bearer ' + access_token}
			message = {"そろそろ苦しいです…早めに助けてください(·:ﾟдﾟ:·)ﾊｧﾊｧ"}
			payload = {'message': message}
			r = requests.post(url, headers=headers, params=payload,)
                break


if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'


        