# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:27:24 2019

@author: Adind
"""

# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('titanic.csv')
shape = data.shape
print("dimension : ",shape)
print()

print ("Data type each column : ")
for name, dtype in df.dtypes.iteritems():
    print(name," = ", dtype)
print()

survived = data[data['Survived'] == 1]
print("survived : ",len(survived))

not_survived = data[data['Survived'] == 0]
print("not survived : ",len(not_survived))
print()

#datadelete1 = data.drop['Nama']
#print(datadelete1)
#print()

datanewcolomn = data.insert(2,'new',1000)
print(datanewcolomn)
print()