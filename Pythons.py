#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Kniga:
    def adds(self, name, phone, adress):
        self.name = name
        self.name = phone
        self.adress = adress
        name = input('add name: ')
        phone = input('add phone: ')
        adress = input('add adress: ')
    def AdresKniga():
        bd={
            'name' : ('name','phone', 'adress'),
        }
Kniga().adds()
