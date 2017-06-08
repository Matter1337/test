import RPi.GPIO as GPIO
import time
import sqlite3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(29, GPIO.IN)

class Ansteuern:

	def start(self):
		self.läuft = False
		zeit = time.time()
		conn = sqlite3.connect("bahl_stoppuhr.db")
		c = conn.cursor()
		print(zeit)
		try:
			while True:
				if(GPIO.input(29) == True and self.läuft == False):
					self.läuft = True
					print("Start!")
					c.execute("""INSERT INTO zeiten(zeit, status)
						 VALUES('%s', 'start')""" %(zeit))
					GPIO.output(37, GPIO.HIGH)
					conn.commit()
				elif(GPIO.input(29) == True and self.läuft == True):
					print("Stop!")
					self.läuft = False
					c.execute("""INSERT INTO zeiten(zeit, status)
						 VALUES('%s', 'stop')""" %(zeit))
					GPIO.output(37, GPIO.LOW)
					conn.commit()
				time.sleep(0.3)
					
		except KeyboardInterrupt:
			GPIO.cleanup()
"""	def stop(self):
		zeit = time.strftime('%H:%M:%S')
		conn = sqlite3.connect("bahl_stoppuhr.db")
		c = conn.cursor()
		print(zeit,"Stop!")
		try:
			while True:
				if(GPIO.input(29) == True):
					c.execute("INSERT INTO zeiten(zeit, status) 
						VALUES('%s', 'stop')" %(zeit))
					GPIO.output(37, GPIO.LOW)
					conn.commit()
		except KeyboardInterrupt:
			GPIO.cleanup()
"""
a = Ansteuern()
a.start()
