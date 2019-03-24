#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:11 2019

@author: clairefischer
"""

    
#3
    
def centered_average(nums):
  array=nums
  mi=min(array)
  ma=max(array)
  array.remove(mi)
  array.remove(ma)
  return(sum(array)/len(array))
#Test
if centered_average([2,6,7,8,100])==7:
    print(True)#There is no error
else:
    print(False)