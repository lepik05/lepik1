#henri lepik
#harjutus 5
#15.02.22


#LOOOB funktsiooni

def tervita(nimi, keel="de"):
    if keel=="et":
        print(f"tere {nimi}!")
    elif keel=="en":
        print(f"hi {nimi}!")
    else:
        print(f"hail {nimi}!")
     
n = input("sisestage nimi: ")
k = input("vali keel et/en/de: ")
tervita(n,k)


#ruumalavmdgi

import math

def kuup(a):
    v = a ** 3
    return v

def kera(r):
    v = round(4/3 ** math.pi * r ** 3,2)
    return v

def koonud(r, h):
    v = round(1/3*math.pi*r**2*h,2)
    return v

def silinder(r, h):
    v = round(math.pi*r**2*h,2)
    return v

print("valikujund: \n1 kuup\n2 kera\n3 koonus\n4 silinder\n5 EXIT")
valik = int(input("vali soovitud kujundi numer: "))
if valik == 1:
    a = int(input("sisestage kuubi yks kylg pikkus a="))
    print(kuup(a))

if valik == 2:
    r = int(input("sisestage kera raadius r="))
    print(kera(r))

if valik == 3:
    r = int(input("sisestage koonuse p6hja pindala Sp= "))
    h = int(input("sisestage koonuse korgus h= ")) 
    print(koonus(r,h))
    

if valik == 4:
    r = int(input("sisestage silindri pohjapindala Sp="))
    h = int(input("sisestage koonuse korgus H= "))
    print(silinder(r,h))


