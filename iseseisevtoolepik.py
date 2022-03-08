#iseseisev töö
#henri lepik
#08.03.22

#sisesta email

email = input("sisesta oma email kujul enimi.pnimi@server.com: ")


if("@" in email and "." in email):
    print("õige gmail")
    tukeldus = email.split(".")[0]
    print(f"Tere {tukeldus}, sinu email on server serveris ja domeeniks on sul com")
else:
    print("vale sisestus")
    
