

from turtle import clear


def build(x):  
    for i in range(1,x + 1,2):
        e = int(( x - i ) / 2)
        f = x - 2 * e
    
        for j in range(e):
                print(" ", end="")

        for k in range(f):
                print("@", end="")  
        
        print("")
    print()

def getNumber():
    x = int(input("Milyen széles legyen a piramis alja:"))
    
    a = x % 2
    
    if( a != 1):
        print("Páratlan számok kérek!")
        getNumber()
    else:
        import os
        clear = lambda: os.system('cls')
        clear()
        build(x)


getNumber()