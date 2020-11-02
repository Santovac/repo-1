def main():
    s1 = input("String:")
    lista = s1.split(",")
    n=len(lista)
    for i in range(n):
        if(i%2==0):
            print(lista[i])


main()