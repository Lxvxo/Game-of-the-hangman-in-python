# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:11:29 2022

@author: livio ss

obectif : Récupérer les mots d'un fichier txt'
"""

def Extraction(Fichier):
    Mots =[]
    Dico = open(Fichier,'r')
    for mot in Dico:
        Mots+=[mot.rstrip('\n')]
        #Le rstrip permet de retirer le saut de ligne marqué par le caractère \n
    Dico.close()
    return Mots

global Mots
Mots = Extraction("donnees/dictionnaire_fr.txt")

def transform_mot(mot):
    mot_search = [mot[0]] + ["_"] * (len(mot) - 2) + [mot[-1]]
    for k in range(1,len(mot)-1):
        if mot[k] == mot[0]:
            mot_search[k] = mot[0]
        if mot[k] == mot[-1]:
            mot_search[k] = mot[-1]
    return mot_search

alphabet_bis = {}
for k in range(65,91):
    alphabet_bis[chr(k)] = k-65