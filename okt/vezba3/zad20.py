#f - Fibonacijev broj

def main():
    x=0
    temp1=1
    temp2=1
    n = eval(input("Unesite n:"))
    if(n>=3):
        for i in range(3,n+1):
            if(i%2!=0):
                temp1+=temp2
                f=temp1
            else:
                temp2+=temp1
                f=temp2
    else:
        f=1
    print("Broj n u Fibonacijevom nizu iznosi: ", f)

main()