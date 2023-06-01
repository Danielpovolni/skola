'''
sest = [7]*6
print(sest)
'''

'''
#generisanje liste brojeva 100-1
from random import randint
list  = []
for i in range (50):
    list.append(randint(1,100))
print(list)
'''
''''
redni_brojevi =[]
for i in range(0,20):
    redni_brojevi.append(i)

print(redni_brojevi)
'''
'''
brojevi = list(range(0,20,4))
print(brojevi)
'''
'''
cips = 150
sok = 100
cokolada = 50

broj_cipseva = int (input("koliko cipseva zelis da kupis: "))
broj_sokova = int (input("koliko sokova zelis da kupis: "))
broj_cokolada = int (input("Koliko cokovada zelis da kupis: "))
ukupno_za_placanje = (cips*broj_cipseva) + (sok*broj_sokova)+(cokolada*broj_cokolada)
print("Ukupno za placanje: ", ukupno_za_placanje, "din")
'''
'''
#2a2(1+√2)

a = int(input("unesi duzinu a"))
b = int(input("unesi duzinu b"))
c = int(input("unesi duzinuc"))
d = int(input("unesi duzinud"))
e = int(input("unesi duzinue"))
f = int(input("unesi duzinuf"))

obim = a+b+c+d+e+f
print(obim)
'''
'''
obim = 0
for i in range(6):
    unos= int(input("unesi: "))
    obim = obim + unos
print(obim)
'''



#sortiranje 
ucenici = [
    {'Ime': 'Marko', 'razred': 7, 'ocena': 4.75},
      {'Ime': 'Jovan', 'razred': 8, 'ocena': 2.75},
      {'Ime': 'Petar', 'razred': 7, 'ocena': 3.75},
      {'Ime': 'Dragan', 'razred': 6, 'ocena': 5.00},
    ]


ucenici.sort(key=lambda x: x.get('Ime'))
print(ucenici)

ucenici.sort(key=lambda x: x.get('razred'))
print(ucenici)


#preslikavanje

def obim(a,b,c,d,e,f):
    return a*b*c*d*e*f
uglovi= {
    (1,2,3,4,5,6),
    (1,3,2,4,3,5),
    (7,6,4,3,2,4),
    (9,8,7,6,5,4),
}

for ugao in uglovi:
    print(obim(*ugao))
'''
'''
for i in range(3):
    visina = int(input("kolika je visina" ))
    if visina >= 160:
        print(visina, "Nedozvoljen pristup")
    else:
        print(visina,"Dozvoljen pristup")


dozvoljena_visina=[]
n= int(int(input("unesi broj zainteresovanih: ")))
for i in range(n):
    visina= int(input("kolika je tvoja visina: "))
    if visina >160:
        print("nedozvoljena visina" )    
    if visina <160:
        visina = dozvoljena_visina.append(visina)
        print("dozvoljeana visina")

'''
