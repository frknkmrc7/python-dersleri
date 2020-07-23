# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:02:06 2020

@author: Furka
"""

def faktoriyel(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
a = int(input("Lütfen bir sayı giriniz:"))
print(a,"! = ",faktoriyel(a))

    