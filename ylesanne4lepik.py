#harjutus 4
#Henri Lepik
#03.02.22

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


#jalgpalli meesk


#tärnid


