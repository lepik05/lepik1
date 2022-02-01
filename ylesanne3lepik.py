#harjutus 3
#henri lepik
#01.02.22

#email
#henri lepik
#01.02.22
email= input("sisesta oma email: ")
print("@" in email)

#vandumine
#henri lepik
#01.02.22
S = input("ära kurat ütle: ")
S = S.lower()
V = S.replace("kurat","*****")


#tundide ajad
#henri lepik
#01.02.22
aeg1 = input("algusaeg:")
aeg2 = input("lõpuaeg:")
hh1, mm1 = aeg1.split(":")
hh2, mm2 = aeg2.split(":")
vastus = (int(hh2)*60+int(mm2)) - (int(hh1)*60+int(mm1))
h = vastus//60
m = vastus%60
print(f"{h}:{m}")

#palindroom
#henri lepik
#01.02.22
sisestus = input("sisesta aplindroom:")
print(sisestus == sisestus[::-1])