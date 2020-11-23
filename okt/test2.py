from math import sqrt,sin,cos



def main():
    zbir=0
    n = int(input('Unesite n:'))
    for i in range(2, n+1, 2):
        #print(i)
        zbir+=sqrt(i)
    print('Zbir: ',zbir)

main()