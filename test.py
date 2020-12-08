'''from math import pi
c = 0
f = 32
table = "{:<10.3}{:<10}{:<10.3f}".format(pi+10,f,c)
print(table)



msg1 = "Ime je: {1} {0} {1}".format(c,f)

print(msg1)'''



'''f = open('vezba4/db/user_db.txt', 'r')
lines = f.readlines()
print(lines)
users = [None]*len(lines)
for i,line in enumerate(lines):
    s=lines[i].split("|")
    users[i]=s[0]
print(users)
f.close()'''

#x,y = input('Input coordinates(x,y): ')
#print(x,y)

import math

'''a = float(input('Unesite A:')
b = float(input('Unesite B:')
m = sqrt((cos(b)**2)/(sin(a+1)))
print(M)'''

'''from random import random

x=3
for i  in range(x):
    print(random())
    x+=1'''

a = ("berta", "gastozz", "arsa", "doggydog", "fulya", "cryyuuup", "hc", "estefan")
a = sorted(a, reverse=True)
print(a)