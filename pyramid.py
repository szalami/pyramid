

from turtle import clear


def build(height):  
    print()
    
    for i in range(1, height + 1):
        space = (height + 1) - i 
        at = i * 2 - 1   
        print(space * " ", at * "@", end="")       
        print()
    print()

def getNumber():
    height = int(input("Milyen magas legyen a piramis: "))
    build(height)

def clearScreen():
    import os
    clear = lambda: os.system('cls')
    clear()
 
clearScreen()   
getNumber()