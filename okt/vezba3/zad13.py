#m - srednja linija trougla
from math import sqrt

def main():

    a,b,c = eval(input("Unesite stranice trougla u formatu a,b,c:"))
    m=(a+b+c)/2
    s=sqrt(m*(m-a)*(m-b)*(m-c))
    print("Povrsina trougla iznosi: ", s)

main()