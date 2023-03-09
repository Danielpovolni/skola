#!/usr/bin/env python
# coding: utf-8

# In[6]:


Visina = [1.72, 1.69, 1.54, 1.70, 1.81, 1.62, 1.65, 1.71, 1.70, 1.56, 1.67]
def prosek(Visina):
    return sum(Visina)/len(Visina)
prosek_visina = prosek(Visina)
Visina_ispod_proseka = [x for x in Visina if x < prosek_visina]
print("Visine koje su ispod proseka su:", Visina_ispod_proseka)


# In[9]:


ocene = [4,4,5,3,5,5,2,4,5,4,3,5,4]
ocena5 = ocene.count(5)
ocena4 = ocene.count(4)
ocena3 = ocene.count(3)
ocena2 = ocene.count(2)
ocena1 = ocene.count(1)
print("Ucenik ima", ocena5, "petica")
print("Ucenik ima", ocena4, "cetvorki")
print("Ucenik ima", ocena3, "trojki")
print("Ucenik ima", ocena2, "dvojki")
print("Ucenik ima", ocena1, "keca")


# In[10]:


broj = len(ocene)
pro5 = 100.0 * ocena5 / broj
pro4 = 100.0 * ocena4 / broj
pro3 = 100.0 * ocena3 / broj
pro2 = 100.0 * ocena2 / broj
pro1 = 100.0 * ocena1 / broj
print("Ucenik ima", round(pro5, 2), "% petica")
print("Ucenik ima", round(pro4, 2), "% cetvorki")
print("Ucenik ima", round(pro3, 2), "% trojki")
print("Ucenik ima", round(pro2, 2), "% dvojki")
print("Ucenik ima", round(pro1, 2), "% keceva")


# In[4]:


#import matplotlib
znamky=[5,3,4,5,5,2,5,5,3,4,2,5,5,5,3]
#kelko jesto z kazdej znamki
znamka5 = znamky.count(5)
znamka4 = znamky.count(4)
znamka3 = znamky.count(3)
znamka2 = znamky.count(2)
znamka1 = znamky.count(1)
#percenta pre kazdu znamku
celkovo = znamka5 + znamka4 +  znamka3 + znamka2 + znamka1
zpercenta = 100/celkovo
percenta_znamka5 = zpercenta * znamka5
percenta_znamka4 = zpercenta * znamka4
percenta_znamka3 = zpercenta * znamka3
percenta_znamka2 = zpercenta * znamka2
percenta_znamka1 = zpercenta * znamka1
#Pie diagram
import matplotlib.pyplot as plt
percenta=[percenta_znamka5,percenta_znamka4,percenta_znamka3,percenta_znamka2,percenta_znamka1]
znamki_labels=["znamka 5", "znamka 4", "znamka 3", "znamka 2", "znamka 1"]
e = [0,0,0.1,0,0]
plt.figure(figsize=(6,6))
plt.pie(percenta, labels=znamki_labels, explode=e )
plt.title("Percenta Ziakov po znamky")

#plt.show()
#plt.close()


# In[2]:


import matplotlib.pyplot as plt
opstine =["Bar", "Vozdovac","Vracar","grocka", "zvezdara","zemun"]
broj_stanovnika = [26798,169495, 57856,86908,168118,175550]


# In[15]:


plt.plot(opstine, broj_stanovnika, color="g")
plt.title("Stanovnistvo opstina")
plt.xlabel("Naziv opstina")
plt.ylabel("Broj stanovnistva")

plt.show
plt.close


# In[18]:


plt.bar(opstine, broj_stanovnika, color="g")
plt.title("Stanovnistvo opstina")
plt.xlabel("Naziv opstina")
plt.ylabel("Broj stanovnistva")
plt.figure(figsize=(10,60))

plt.show
plt.close


# In[21]:


plt.pie(broj_stanovnika, labels=opstine)
plt.title("Stanovnistvo opstina")
plt.xlabel("Naziv opstina")
plt.ylabel("Broj stanovnistva")
plt.figure(figsize=(10,60))

plt.show
plt.close


# In[25]:


ucestalost=[5,9,2,15,28,52]
ocene=[10,9,8,7,6,5] 
ocena8=[0,0,0.3,0,0,0]
plt.pie(ucestalost, labels=ocene, explode=ocena8)
plt.title("Prikaz ucesalosti ocena")
plt.show()
plt.close()


# In[47]:


predmeti =["mat","srp","lik","fiz","muz","bio"]
ocene=[5,2,4,6,2,3]
prosecna_ocene= sum(ocene)/len(predmeti)
prosek=[prosecna_ocene]
n=len(ocene)


import matplotlib.pyplot as plt
plt.bar(predmeti, ocene, color="g", label="ocene")
plt.title("Ocene i predmeti")
plt.xlabel("predmeti")
plt.ylabel("ocene")
plt.plot(predmeti,[prosek]*n, color="r", label="prosek")
plt.legend()
plt.show()
plt.close()


# In[80]:


import matplotlib.pyplot as plt

zarade=[530,620,790,540]

def prosek(zarade):
    return sum(zarade)/len(zarade)
zarade.sort
n = len(zarade)
plt.bar(range(n), zarade)
plt.bar([n//2],[zarade[n//2]], color="red")









# In[ ]:


\

