#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:12 2019

@author: clairefischer
"""

#6
def cat_dog(str):
  if str.count('cat')==str.count('dog'):
    return True
  else:
    return False
#Test
if cat_dog('catcatdog')==False and cat_dog('catdogcatdog')==True:
    print(True)  #There is no error
else: 
    print(False)