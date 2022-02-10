#henri lepik
#harjutus 5
#10.02.22

#tärnid

import random
arvud=[]
for i in range(5):
    arvud.append(random.randint(1,99))
for i in range(len(arvud)):
    print("*"*arvud[i])


#vanused
import random
vanused=[]
for i in range(5):
    vanused.append(random.randint(1,99))
print(f"suurim arv: {max(vanused)}\nväikseim arm: {min(vanused)}\nvanuste summa: {sum(vanused)}\nkeskmine arv: {sum(vanused)/len(vanused)}")


#duplikaadid

opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
puhopilased=[]

for i in range(len(opilased)):
    if opilased[i] not in puhopilased:
        puhopilased.append(opilased[i])
        
        
for i in range(len(puhopilased)):   
    print(puhopilased[i],end=", ")


#õpilased

opilased = ['Juhan','Kati','Maarja','Mario','Mati']

print("\nVali nr mida muut")
for i in range(len(opilased)):
    print(f"{i+1}. {opilased[i]}")
valik=int(input("sisesta number: "))
del opilased[valik-1]
uusnimi=input("sisesta uus nimi: ")
opilased.insert(valik-1,uusnimi)
print("nimi muudetud")
print(opilased)

#nimede lisamine loendisse

nimed= []
for i in range(5):
    nimi=input("lisa nimi: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
    