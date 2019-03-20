#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:13 2019

@author: clairefischer
"""


#9
def array123(nums):
  if 1 in nums:
    for i in range(len(nums)):
      if nums[i]==1 and i<=(len(nums)-3):
        if nums[i+1]==2 and nums[i+2]==3:
          return True
    else:
      return False
  else:
    return False
#Test
if array123([1,1,2,3,1])==True and array123([2,6,1,3,2,3,8])==False:
    print(True)#There is no error
else:
    print(False)

