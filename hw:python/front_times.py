#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:11 2019

@author: clairefischer
"""

#2

def front_times(str, n):
  liste_char=''
  for i in range(n):
    if len(str)<=3:
      liste_char=liste_char+str
    else:
      liste_char=liste_char+str[:3]
  return liste_char
#Test
if front_times('Hello',2)=='HelHel' and front_times('abc',3)=='abcabcabc' :
    print(True)#There is no error
else:
    print(False)