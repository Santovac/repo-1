def main():
    s1 = input("String:")
    n=len(s1)
    lista = s1.split(",")
    for rec in lista:
        print(rec)

main()