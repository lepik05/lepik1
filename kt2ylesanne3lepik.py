#kt2 ylesanne3
#Henri Lepik
#09.03.22

import random

def kysinum():
  while(1):
    try:
      kasutaja = int(input("kirjuta vastus: "))
      break
    except vale:
      print("vale vastus!")
      
  return kasutaja

def kysi():

  x = random.randint(1, 10)
  y = random.randint(1, 10)

  print("mis on " + str(x) + " + " +str(y))

  u = kysinum()

  if (u == x + y):
    return 1
  else:
    return 0

kokku = 4
oiged = 0
for i in range(kokku):
  oiged += kysi()
tulemus= oiged / kokku
protsent = round((tulemus * 100), 2)
while protsent <= 61:
    print("saamatu sa said alla 61%")
else:
    print("su tulemus oli ", protsent, "%. tubli")
   


