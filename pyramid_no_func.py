from turtle import clear

import os
clear = lambda: os.system('cls')
clear()

base = int(input("Milyen magas legyen a piramis: "))

base = base * 2 - 1                    # calculate base width

for i in range(0, base, 2):
        
        space = int((base - i ) / 2)   # calc spaces in left
        
        at = base - 2 * space          # calc number of '@'
    
        print(space * " ", end="") 

        print(at * "@", end="")    
        
        print()
        
print()