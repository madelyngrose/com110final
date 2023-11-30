#!/usr/bin/env python
# coding: utf-8

# In[11]:


solve = input("What do you want to solve?: ")
if solve == 'pressure':
    volume = int(input('Enter volume in L: '))
    moles = int(input('Enter number of moles: '))
    temp = int(input('Emter temperature in Kelvin: '))
    pressure = (moles*.0831446*temp)/volume
    print(pressure, 'bars')
if solve == 'volume':
    pressure = int(input('Enter pressure in bars: '))
    moles = int(input('Enter number of moles: '))
    temp = int(input('Enter temperature in Kelvin: '))
    volume = (moles*.0831446*temp)/pressure
    print(volume)
if solve == 'moles':
    pressure = int(input('Enter pressure in bars: '))
    volume = int(input('Enter volume in L: '))
    temp = int(input('Enter temperature in Kelvin: '))
    moles = (pressure*volume)/(.0831446*temp)
    print(moles)
if solve == 'temperature':
    pressure = int(input('Enter pressure in bars: '))
    moles = int(input('Enter number of moles: '))
    volume = int(input('Enter volume in L: '))
    temp = (pressure*volume)/(.0831446*moles)
    print(temp)


# In[ ]:




