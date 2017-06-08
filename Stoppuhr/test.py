import sqlite3

class test:
	def __init__(self):
		self.conn = sqlite3.connect("bahl_stoppuhr.db")
		self.c = self.conn.cursor()
	def ausgabe(self):
		c = self.conn.cursor()
		
		rows = c.execute("select * FROM zeiten")
		for row in rows:
			print(row)

t = test()
t.ausgabe()
