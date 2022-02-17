#henri lepik
#harjutus 8
#17.02.22



import datetime
from dateutil.relativedelta import relativedelta

kuud = ["JAANUAR","VEEBRUAR","MÄRTS"]

kuup = datetime.date.today()
kuu = int(kuup.month)
kuup2 = datetime.date(kuup.year, kuu , kuup.day)
print(kuup2.strftime("%d")+"."+str(kuud[kuu-1])+" "+kuup2.strftime("%Y"))  


ik = "50416121910"
aasta = int("20"+ik[1]+ik[2])
paev = int(ik[3]+ik[4])
kuu = int(ik[5]+ik[6])
sp = datetime.date(aasta,kuu,paev)


myBirthday = datetime.datetime(aasta,kuu,paev,0,0,0,0)
now = datetime.datetime.now()



difference = relativedelta(now, myBirthday)
print("su vanus: "+str(difference.years))

  



