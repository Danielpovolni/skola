#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import pandas as pd 


# In[13]:


faks=[
    ["Marko", 6,6,6,6,9,9],
    ["Vesna", 6,7,6,7,9,9],
    ["Sandra", 7,7,6,7,9,9],
    ["Ivona", 6,7,6,7,8,9],
    ["Sara", 9,10,7,9,10,10]
     ]
predmeti = pd.DataFrame(faks)
predmeti.columns = ["Ime","IKT","Menadzment", "Matematika", "Rac_Sistemi","Ekonomija","Architektura"]



predmet1 = predmeti.set_index("Ime")


plt.figure(figsize=(13,5))
plt.bar(predmeti["Ime"], predmeti["Menadzment"], color="g")
plt.bar(predmeti["Ime"], predmeti["Matematika"], color="r")
plt.title("Ocene iz matematika i mnadzmenta")
plt.show()
plt.close()


# In[15]:


predmeti_ikt =predmet1.sort_values(by="IKT")
predmeti_ikt
plt.figure(figsize=(10,5))
plt.bar(predmeti_ikt.index, predmeti_ikt["IKT"])
plt.show()
plt.close()


# In[ ]:




