from daterbase import *
z = input('what do you want to name the bugati: ')
c.execute("INSERT INTO car (car_name)VALUES(?)",(z,))

conn.commit()
c.execute("SELECT * FROM car ")

a = c.fetchall()

print(a)