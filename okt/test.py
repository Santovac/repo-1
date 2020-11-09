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

x,y = input('Input coordinates(x,y): ')
print(x,y)