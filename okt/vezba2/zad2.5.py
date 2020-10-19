# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a x-year investment.")
    x = int(input("x="))

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(x):
        principal = principal * (1 + apr)

    x = str(x)
    print("The value in " +x+ " years is:",principal)

main()
