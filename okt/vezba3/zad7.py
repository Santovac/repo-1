#lowercase - broj atoma, uppercase - masa jednog atoma, A - masa atoma

def main():

    C = 12.011
    H = 1.0079
    c = eval(input("Broj atoma ugljenika:"))
    h = eval(input("Broj atoma vodonika:"))
    A = C*c+H*h
    print("Ukupna masa atoma je: ", A)

main()