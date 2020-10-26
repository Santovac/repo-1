#n - koiko clanova niza se sabire, p - broj pi, np - neparan delilac

def main():
    p=0
    x=0
    np=1
    n = eval(input("Unesite n:"))
    for i in range(1,n+1):
        if(i%2!=0):
            p+=4/np
        else:
            p-=4/np
        np+=2
    print("Aproksimacija broja Pi za n broj clanova je: ", p)
main()