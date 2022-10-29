

from turtle import clear


def build(base):  
    for i in range(0, base, 2):
        space = int((base - i ) / 2)   # spaces in left
        at = base - 2 * space           # number of '@'
    
        for j in range(space):
                print(" ", end="")

        for k in range(at):
                print("@", end="")  
        
        print()
    print()

def getNumber():
    base = int(input("Milyen magas legyen a piramis: "))
    
    base = base * 2 - 1   # calculate base width
    
    import os
    clear = lambda: os.system('cls')
    clear()
    build(base)


getNumber()