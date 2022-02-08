#harjutus 4
#Henri Lepik
#03.02.22


#paaris ja paaritu


#pisikekorrutustabel


#viisikud


#arvamismäng


#pank


#ruutude ja kuupde tabel




#loto



#tärnid

for l in range(1,6):
    for k in range(1,6):
        print("*",end="")
    print()

#ruut
a = int(input("1. kylg: "))
b = int(input("2. kylg: "))

if a==b:
    print("ruut")
else:
    print("ristkylik")

#matemaatika
arv1 = int(input("esimene arv: "))
arv2 = int(input("teine arv: "))
tehe = input("valige tehe:\n +\n -\n *\n /\n")

if tehe == "+":
    tehe2 = arv1 + arv2
elif tehe == "-":
    tehe2 = arv1 - arv2
elif tehe == "*":
    tehe2 = arv1 * arv2
elif tehe == "/":
    tehe2 = arv1 / arv2
print (f"{arv1}{tehe}{arv2}={tehe2}")

#juubel

aasta = input("sisesta sünniaeg kujul dd.mm.yyyy:")
d,m,y = aasta.split(".")
aasta1 = 2022
aasta2 = aasta1 - int(y)
if aasta2%5==0:
    print("sul on juubel")
else:
    print("sul pole juubel")

#müük

hind= int(input("kirjuta toote hind:"))
if hind > 10:
    print(hind - hind * 0.2)
else:
    print(hind - hind * 0.1)

#jalgpalli meesk

sugu = input("sisesta sugu: ")
if sugu == "m":
    vanus = int(input("sisesta oma vanus"))
    if vanus >= 16 and vanus <=18:
        print("oled jah")
    else:
        print("oled ei")
else:
    print("oled ei")

