#A - apsolutna vrednost kvadratnog korena koristeci funkciju sqrt, NJ - vrednost kvadratnog korena dobijena koristeci Njutnovu metodu
from math import sqrt

def main():
    x = eval(input("Unesite x:"))
    n = eval(input("Unesite broj pokusaja:"))
    NJ=x/2
    for i in range(1,n+1):
        NJ=(NJ+x/NJ)/2
        if(NJ==sqrt(x)):
            break

    print("Kvadratni koren broja x pomocu funkcije sqrt iznosi:", sqrt(x),", a kvadratni koren dobijen Njutnovom metodom iznosi:", NJ)
    print("Broj pokusaja: ",i)

main()