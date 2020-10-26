import math

def main():
    r = eval(input("Unesite r:"))
    wp = eval(input("Unesite cenu cele pice:")) #whole price
    s = 4*r**2*math.pi
    fp = wp/s #fraction price
    print("Cena pice po kvadratnom centimetru je: ", fp)

main()