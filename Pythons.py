#!/usr/bin/env python3
import pickle

file = 'test.txt'

ab={}
name = input('Vedite name: ')
adress = input('Vedite adress: ')
phone = input('Vedite phone: ')
email = input('Vedite email: ')

ab[name]=(name, adress,phone,email)

f = open(file, 'wb')
pickle.dump(ab, f)
f.close

del ab

f = open(file, 'rb')
loadlist = pickle.load(f)
print(loadlist)

