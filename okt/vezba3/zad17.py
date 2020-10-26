#x - ukupan zbir

def main():
    x=0
    n = eval(input("Unesite n:"))
    for i in range(1,n+1):
        print("Unesite ",i,". broj:")
        temp = eval(input())
        x+=temp
    print("Ukupan zbir iznosi: ", x)

main()