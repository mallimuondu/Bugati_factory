import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()
import datetime as time
def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS car(car_name TEXT)')
    
table()
