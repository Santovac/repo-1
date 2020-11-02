def main():
    s1 = input("Prvi string:")
    list=s1.split(" ")
    n = len(list)
    for i in range(n):
        print(list[i][0].upper(), end="")
main()