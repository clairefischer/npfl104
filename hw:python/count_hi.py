#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:12 2019

@author: clairefischer
"""

#5
def count_hi(str):
  return(str.count('hi'))
#Test
if count_hi('hi ab hi')==2:
    print(True)#There is no error
else:
    print(False)