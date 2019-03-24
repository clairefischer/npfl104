#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:12 2019

@author: clairefischer
"""

#4
def double_char(str):
  liste_char=''
  for char in str:
    for i in range(2):
      liste_char=liste_char+char
  return liste_char
#Test
if double_char('Hi')=='HHii':
    print(True)#There is no error
else:
    print(False)