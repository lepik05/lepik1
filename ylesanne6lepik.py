#henri lepik
#harjutus 5
#10.02.22

# facebooki poliitikud

re, kesk = 0, 0
erakonnad = []

with open('s6pru_l6ustaraamatus.txt','r') as sobrad:
    for rida in sobrad:
        enimi, pnimi, er, likes = rida.split()
        print(f"{enimi:11} {pnimi:11} {er:4} {likes:5}",end="")
        if er=="RE":
            re+=1
        elif er=="KE":
            kesk+1

print()
print(f"reformikad: {re}\nkeskikuid: {kesk}\n")
print(f"erakondikokku: {len(erakonnad)}")
