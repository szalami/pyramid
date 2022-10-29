from turtle import clear

import os
clear = lambda: os.system('cls')
clear()

height = int(input("Milyen magas legyen a piramis: "))
print()

for i in range(1, height + 1):
        
        space = height - i 
        at = i * 2 - 1
    
        print(space * " ", at * "@", end="" )   
        
        print()
        
print()