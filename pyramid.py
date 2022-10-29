

from turtle import clear


def build(base):  
    print()
    
    for i in range(0, base, 2):
        space = int((base - i ) / 2)   # spaces in left
        at = base - 2 * space           # number of '@'      
        print(space * " ", end="") 
        print(at * "@", end="")        
        print()
    print()

def getNumber():
    base = int(input("Milyen magas legyen a piramis: "))  
    base = base * 2 - 1   # calculate base width
    build(base)

def clearScreen():
    import os
    clear = lambda: os.system('cls')
    clear()
 
clearScreen()   
getNumber()