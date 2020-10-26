#

def main():

    x1,y1 = eval(input("Unesite koordinate prve tacke (u formatu x,y):"))
    x2,y2 = eval(input("Unesite koordinate druge tacke (u formatu x,y):"))
    m=(y2-y1)/(x2-x1)
    print("Nagib iznosi:" ,m)

main()