#z - prosek, x - zbir svih brojeva

def main():
    x=0
    z = type(float)
    n = eval(input("Unesite n:"))
    for i in range(1,n+1):
        print("Unesite ",i,". broj:")
        temp = eval(input())
        x+=temp
    z = x/n
    print("Prosek iznosi: ", z)

main()