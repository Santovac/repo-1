#x - ukupan zbir

def main():
    x=0
    n = eval(input("Unesite n:"))
    for i in range(1,n+1):
        x+=i**2
    print("Ukupan zbir iznosi: ", x)
main()