#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:13 2019

@author: clairefischer
"""

#10
def xyz_there(str):
  bool=False
  if len(str)<=2:
    return False
  elif len(str)==3:
    if str=='xyz':
      return True
    else:
      return False
  elif len(str)>3:
    if 'xyz' in str:
      for i in range(len(str)):
        if str[i]=='x' and str[i+1]=='y' and str[i+2]=='z' and str[i-1]!='.':
          bool+=True
    return bool==1
#Test
if xyz_there('abdxyz')==True and xyz_there('ab.xyz')==False:
    print(True)#There is no error
else:
    print(False)