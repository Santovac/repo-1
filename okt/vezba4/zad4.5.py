def get_user_list():
    f = open('db/user_db.txt', 'r')
    lines=f.readlines()
    lines = f.readlines()
    users = [None] * len(lines)
    for i, line in enumerate(lines):
        s = lines[i].split("|")
        users[i] = s[0]
    print(f"Users: {users}")
    f.close()

def find_user_line(who): #function changes global var this_line to point to the line which includes the searched username (var 'who')
    f = open('db/user_db.txt', 'r')
    lines = f.readlines()
    global this_line
    for i,line in enumerate(lines):
        if line.startswith(who):
            this_line = i
    f.close()

def append_new_transaction(this_line, price):
    f = open('db/transactions.txt', 'r+')
    s = str(price)
    lines = f.readlines()
    for i,line in enumerate(lines):
        if(i==this_line):
            lines[i]=lines[i].strip() + s + '|\n'
    f.seek(0)
    for line in lines:
        f.write(line)
    f.close()

def display_statistics():
    print("Checking for new users...")

#///MAIN///MAIN///MAIN///MAIN///MAIN///MAIN///MAIN///MAIN///MAIN///MAIN///MAIN///MAIN///
this_line=-1
answer = input("1. Add a new transaction\n2. Display Statistics\nOption (1/2): ")
if(answer=='1'):
    who = input("Username: ")
    find_user_line(who)
    if(this_line==-1):
        print("User does not exist.")
    price = float(input("Price of the sold article: "))
    append_new_transaction(this_line, price)
answer = input("Display new statistics(y/n)?: ")
if(answer=='y'):
    display_statistics()