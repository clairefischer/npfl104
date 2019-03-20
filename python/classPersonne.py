#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:33:11 2019

@author: clairefischer
"""

class Personne:
    
    def __init__(self,Prenom,Nom, Age):
        self.prenom=Prenom
        self.nom=Nom
        self.age=Age
    def diff_age(self,Personne1,Personne2):
        return abs(Personne1.age-Personne2.age)
    
    def older(self,Personne1,Personne2):
        ma=max(Personne1.age,Personne2.age)
        if ma==Personne1.age:
            print('The oldest is',Personne1.prenom)
        else:
            print('The oldest is',Personne2.prenom)
        return(ma)
        
    def younger(self,Personne1,Personne2):
        mi=min(Personne1.age,Personne2.age)
        if mi==Personne1.age:
            print('The youngest is',Personne1.prenom)
        else:
            print('The youngest is',Personne2.prenom)
        return(mi)
    



C=Personne('Claire','Fischer',21)
H=Personne('Bertrand','Henriette',23)
print(C.older(C,H))