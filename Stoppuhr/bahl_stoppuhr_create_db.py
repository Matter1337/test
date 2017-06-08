import sqlite3
import time

class DB:
	def __init__(self):
		self.conn = sqlite3.connect("bahl_stoppuhr.db")
		self.c = self.conn.cursor()
	def table(self):
		c = self.conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS zeiten
			(zeit float primary key,
			status text);""")
db = DB()
db.table()
