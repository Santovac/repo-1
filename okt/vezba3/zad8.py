#v - brzina zvuka [m/s], d - rastojanje posmatraca od munje, t - vremenska razlika za koju zvuk munje stigne do posmatraca


def main():

    v = 340
    t = eval(input("Unesite vremensku razlika t:"))
    d = v*t
    print("Rastojanje munje i posmatraca je: ", d)

main()