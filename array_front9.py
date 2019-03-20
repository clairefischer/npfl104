#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:12 2019

@author: clairefischer
"""

    
#8
def array_front9(nums):
  if len(nums)<=4:
    if 9 in nums:
      return True
    else:
      return False
  else:
    array=nums[:4]
    if 9 in array:
      return True
    else:
      return False
#Test
if array_front9([2,6,8,6,9])==False and array_front9([1,9,9,4])==True:
    print(True)#There is no error
else:
    print(False)