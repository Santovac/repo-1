def main():
    s1 = input("Prvi string:")
    s2 = input("Drugi string:")
    n1 = len(s1)
    n2 = len(s2)
    for i in range(2):
        print(s1[:3], end="")
    print(s2[-3:])
main()