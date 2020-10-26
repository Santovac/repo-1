#y - godina, c - vek

def main():

    y= eval(input("Unesite godinu:"))
    c=y/100
    e=(8+c/4-c+((8*c+13)/25)+11*(y%19))%30
    print("Epakt po Gregorijanskom kalendaru je:" ,e)

main()