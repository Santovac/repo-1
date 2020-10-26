# m - kolicina narucene kafe u kg, p - ukupna cena dostave


def main():

    # cena kafe je 105rsd/kg, dostava je 18rsd/kg+15rsd
    m = eval(input("Unesite koliko kg kafe je naruceno:"))
    p = m*105+m*18+15
    print("Ukupna cena kucne porudzbine je:" ,p)

main()