# File: chaos.py
# A simple program illustrating chaotic behavior.

def main(): #funkcija main, glavna funkcija
    print("This program illustrates a chaotic function") #ispis opisa programa
    x = eval(input("Enter a number between 0 and 1: ")) #unos vrednosti
    for i in range(10): #for petlja koja ponavlja blok komandi 10 puta
        x = 3.9 * x * (1 - x) #izraz za dobijanje vrednosti x
        print(x) #ispis rezultata

main()