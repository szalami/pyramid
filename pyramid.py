

from turtle import clear


def build(x):  
    for i in range(0, x, 2):
        e = int((x - i ) / 2)   # spaces in left
        f = x - 2 * e           # number of '@'
    
        for j in range(e):
                print(" ", end="")

        for k in range(f):
                print("@", end="")  
        
        print()
    print()

def getNumber():
    x = int(input("Milyen magas legyen a piramis: "))
    
    x = x * 2 - 1   # calculate base width
    
    import os
    clear = lambda: os.system('cls')
    clear()
    build(x)


getNumber()