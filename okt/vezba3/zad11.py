from math import sqrt

def main():

    x1,y1 = eval(input("Unesite koordinate prve tacke (u formatu x,y):"))
    x2,y2 = eval(input("Unesite koordinate druge tacke (u formatu x,y):"))
    d=sqrt((x2-x1)**2+(y2-y1)**2)
    print("Rastojanje izmedju dve tacke je:" ,d)

main()