from daterbase import *
now = time.datetime.now()
hour = now.hour

if hour < 12:
    print("Good morning")
elif hour >= 12 and hour <= 18:
    print("Good afternoon")         
elif hour > 18 and hour < 19: 
    print("Good evening")
else:
    print('Have a nice night.')
def main():
    wocu = input('''Are you:
    a.worker
    b.customer
    ''')
    if wocu == 'a':
        print(' Get the body component')
        b = input('press E or e to continue:')
        if b == 'e' or b == 'E':
            print('Put the body component on the stands')
            c = input('press E or e to continue:')
            if c == 'e' or c == 'E':
                print('Put the automatic shift unit in front of the engine')
                d = input('press E or e to continue:')
                if d == 'e' or d == 'E':
                    print('Put the automatic shift unit in front of the engine')    
                    f = input('press E or e to continue:')
                    if f == 'e' or f == 'E':
                        print('Mount the finished side section on the engine block')
                        g = input('press E or e to continue:')
                        if g == 'e' or g == 'E':
                            print('Fit the exhaust system')
                            h = input('press E or e to continue:')
                            if h == 'e' or h == 'E':
                                print('Install the brake disks')
                                i = input('press E or e to continue:')
                                if i == 'e' or i == 'E':
                                    print('Attach the front and the back part together and add tires')
                                    k = input('press E or e to continue:')
                                    if k == 'e' or k == 'E':
                                        print('Put dors and others.Take the car to the test station')
                                        print('Now the bugati is ready')
                                        z = input('what do you want to name the bugati: ')
                                        c.execute("INSERT INTO car (car_name)VALUES(?)",(z,))

                                        conn.commit()

main()
                