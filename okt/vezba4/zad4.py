f = open("db/user_db.txt", "r")

list = f.readlines()
n = len(list)
for i in range(n):
    s=list[i]
    user=s.split("|")
    print(f'korisnicko ime: {user[0]}')
    print(f'lozinka: {user[1]}')

f.close()