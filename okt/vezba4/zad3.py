f = open("user_db.txt", "a")
korisnik = input("Korisnicko ime: ")
lozinka = input("Lozinka: ")
s=korisnik+"|"+lozinka+"\n"
f.write(s)
f.close()