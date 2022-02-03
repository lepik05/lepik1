# Harjutus 2
# Henri Lepik
# 01.02.22


# Kolmnurga ümbermõõt
# Henri Lepik
# 01.02.22

a,b,c = 15,16,18

Kolmnurk = 15+16+18

print("Kolmnurga ümbermõõt: ",Kolmnurk)

# Toote hind
# Henri Lepik
# 01.02.22

Toode = 36.75
Soodus = 0.4
Kogus = 3
summa = round(Kogus*(Toode-(Toode*Soodus)), 2)
print(Kogus, "Toote hind on",summa, "€")

# Pitsa
# Henri Lepik
# 01.02.23

sober = 3
Hind = 12.90
Joot = 0.1
summa = round(sober/(Hind*Joot),2)
print("Iga üks peab plekima ",summa,"€")

# Rulluisud
# Henri Lepik
# 01.02.22

kiirus = 29.9 #km/h
aeg = 24 # minut
kulunddaeg = round(((kiirus/60)*aeg),2)
print("Rulluikude kiirus" ,str(kiirus), "km/h jõuaks kohale" ,aeg, "minutiga," ,kulundaeg, "km kaugele")

# Kolmnurga hüpotenus
# Henri Lepik
# 01.02.22

a = 16
b = 9
c2 = a*a+b*b
c = round(sqrt(c2),2)
print("Hüpetnuus on",c)

# Ajateisendus
# Henri Lepik
# 01.02.22

minutid = int(input("kirjuta minutite arv: "))
aeg = minutid//60
aeg2 = minutid-(aeg*60)
print("Aeg on siis:",aeg,":",aeg2)

# Arvusysteemid
# Henri Lepik
# 01.02.22

number = int(input("kirjuta number : "))
number2 = bin(number)
print(number2)
number3 = hex(number)
print(number3)

# Kütus
# Henri Lepik
# 01.02.22

kytus = int(input("kirjuta kulutatud kütus (Liitrides): "))
maa = int(input("kirjuta selle kütusega sõidetud maa (km): "))
kulund1 = kytus/(maa/100)
print("kulub 100 km kohta",kulund1,"liitrit kütust")


    











