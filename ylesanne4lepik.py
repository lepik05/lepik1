#harjutus 4
#Henri Lepik
#03.02.22


#paaris ja paaritu


#pisikekorrutustabel

for k in range(1,11):
    arv = 5
    v = k * arv
    print(f"{arv} x {k} = {v}")

#viisikud
    
for i in range(1,21):
    for j in range(5,6):
        print('{0:>3}'.format(j*i), end=" ")
    print()

#arvamismäng
import random
nr = random.randint(1,50)
loop = 1
kord = 1
 
print('Arva ära number 1-50')
 
while loop == 1:
    if kord <= 3:
        arva = int(input('Sisesta täisarv 1-50 : '))
    else:
        veel=input("tahad weel w  jah/ei :")
        if veel == "jah":        
            kord = 0
        else:
            loop = 0
        
    if arva == nr:
        kord += 1
        print('Tubli, pakkumisi kokku: ',kord)
        loop = 0
    elif arva < nr:
        kord += 1
        print('Sinu pakutud arv on liiga väike')
    else:
        kord += 1
        print('Sinu pakutud arv on liiga suur')

#bÄnk

konto = 0
raha = int(input("pane raha panka : "))
intress= 0.05
aastad= int(input("mitu aastat : "))
konto += raha
for i in range(aastad):
    kasum = konto*intress
    print(f"{i:4}{konto:10.2f} {kasum:10.2f} {konto+kasum:10.2f}")
    konto+=kasum
    
#ruutude ja kuupde tabel

for h in range(1,11):
    print(f"{h:4}")


#loto
print("loto arv on:")
import random
arv= random.randint(10000,99999)
print(arv)

#tärnid

for l in range(1,6):
    print("* "*l)

for i in range(1,6):
    for j in range(1,6):
        print("* ",end="")
    print()
k=5 
for l in range(1,6):
    print("* "*k)
    k=k-1
    
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

