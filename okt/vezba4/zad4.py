f = open("user_db.txt","r")
list = f.readlines()
print(list.split("|"))

f.close()