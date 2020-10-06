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
wocu = input('''Are you:
a.customer
b.worker
''')
if wocu == 'b':
    def main():
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
                                            
                                            
                                        else:
                                            print('i do not understund you pls try again')
                                            main()
                                    else:
                                        print('i do not understund you pls try again')    
                                        main()
                                else:
                                    print('i do not understund you pls try again')
                                    main()
                                            
                            else:
                                print('i do not understund you pls try again')
                                main()
                        else:
                            print('i do not understund you pls try again')
                            main()
                    else:
                        print('i do not understund you pls try again')
                        main()
                else:
                    print('i do not understund you pls try again')
                    main()
            else:
                print('i do not understund you pls try again')  
                main()
    main()
    def cargo():
        z = input('what do you want to name the bugati: ')
        y = input('how much is this bugati.Input price:')
        c.execute("INSERT INTO car VALUES(?,?)",(z,y))

        conn.commit()
        print('done bugat is on sell')
    
    cargo()
elif wocu == 'a':
    def cunstomer():
        print('we have this bugatis')
        c.execute("SELECT * FROM car ")
        a = c.fetchall()
        print(a)
        a = input('Input the bugati you want:')
        
        def total():
            print("your total is ")
            global autput
            autput = 0
            b = [c for charging in c.execute('SELECT price FROM car') for c in charging]
            d = sum(b)
            print(d)
            autput += d



        total()

        def paying():
            a = int(input('pls pay(pay more or equal):'))
            if a > autput:
                print('your channge is:')
                d = a - autput 
                print(d)
            else:
                print('i do not understund you pls try again')
        paying()
        
        c.execute("DELETE FROM car WHERE car_name=?", (a,))
        conn.commit()
        print('bugati succsefuly purchesed')
        print('good bye')
    cunstomer()
else:
    print('i do not understund you pls try again')
    wocu()
    