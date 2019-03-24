#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:43:31 2019

@author: clairefischer
"""

#1
def string_times(str, n):
  liste_char=''
  for i in range(n):
    liste_char=liste_char+str
  return liste_char
#Test
if string_times('Hello',2)=='HelloHello':
    print(True)#There is no error
else:
    print(False)
























