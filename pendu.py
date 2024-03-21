# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 22:20:15 2022

@author: livio ss

Objectif : Créer un pendu
"""

from random import choice # pour gérer l'aléatoire
import string # contient l'alphabet
from functools import partial # pour gérer la commande du bouton
from tkinter import *  # pour créer l'interface
from py.Extraction import Mots, transform_mot, alphabet_bis # liste des mots disponibles + transform_mot => tranforme le mot en une liste adéquate au jeu du pendu
#from pendu_fonctions import *

# initialisation :
Stats = [] #stocke True,False ou None en fonction du résultat de chaque partie
mot = choice(Mots) # choisit aléatoirement un mot parmis la liste des mots disponible
erreurs = 8 # définit le nombre d'erreurs par défaut
erreurs_variable = erreurs # définit l'erreur variable qui est modifié au cours de la partie
mot_search = transform_mot(mot) # liste adéquate au jeu du pendu (montre uniquement la première et dernière lettre)
if mot[0] == mot[-1] : 
        list_letters = [mot[0]]
else :
        list_letters = [mot_search[0],mot_search[-1]] # contient les lettres déja saisies lors de la partie courante

#fonctions

def new_game(): # crée une nouvelle partie
    global mot
    global erreurs
    global erreurs_variable
    global mot_search
    global list_letters
    global list_button
    if reconstruction(mot_search) == mot or erreurs_variable == 0 :
        pass
    else:
        Stats.append(None)
    for elt in list_button:
        elt.config(state="normal")
    mot = choice(Mots)
    erreurs_variable = erreurs
    mot_search = transform_mot(mot)
    if mot[0] == mot[-1] : 
        list_letters = [mot[0]]
    else :
        list_letters = [mot_search[0],mot_search[-1]]
    for letter in list_letters:
        list_button[alphabet_bis[letter]].config(state="disabled")
    Mot_search.set("\n{}".format(reconstruction(mot_search)))
    if len(str(erreurs_variable)) == 1:
        Erreurs_variable.set("Nombre d'essais restant : 0{}".format(erreurs_variable))
    else:
        Erreurs_variable.set("Nombre d'essais restant : {}".format(erreurs_variable))
    message.config(text = "Choisissez une lettre !\n")
def remove_erreurs(): # diminue de 5 erreurs le nombre d'erreurs de la partie courante
    global erreurs_variable
    if erreurs_variable - 5< 1:
        erreurs_variable = 1
    else:
        erreurs_variable -=5
    if len(str(erreurs_variable)) == 1:
        Erreurs_variable.set("Nombre d'essais restant : 0{}".format(erreurs_variable))
    else:
        Erreurs_variable.set("Nombre d'essais restant : {}".format(erreurs_variable))
def remove_global_erreurs(): # diminue de 5 le nombre d'erreurs de toutes les parties
    global erreurs_variable
    global erreurs
    if erreurs_variable -5 < 1:
        erreurs_variable = 1
    else:
        erreurs_variable -=5
    if erreurs - 5 < 1:
        erreurs = 1
    else:
        erreurs -=5
    if len(str(erreurs_variable)) == 1:
        Erreurs_variable.set("Nombre d'essais restant : 0{}".format(erreurs_variable))
    else:
        Erreurs_variable.set("Nombre d'essais restant : {}".format(erreurs_variable))
def add_erreurs(): # augmente de 5 erreurs le nombre d'erreurs de la partie courante
    global erreurs_variable
    
    if erreurs_variable +5 > 26:
        erreurs_variable = 26
    else:
        erreurs_variable +=5
    if len(str(erreurs_variable)) == 1:
        Erreurs_variable.set("Nombre d'essais restant : 0{}".format(erreurs_variable))
    else:
        Erreurs_variable.set("Nombre d'essais restant : {}".format(erreurs_variable))
def add_global_erreurs(): # augmente de 5 le nombre d'erreurs de toutes les parties
    global erreurs_variable
    global erreurs
    if erreurs_variable +5 > 26:
        erreurs_variable = 26
    else:
        erreurs_variable +=5
    if erreurs +5 > 26:
        erreurs = 26
    else:
        erreurs +=5
    if len(str(erreurs_variable)) == 1:
        Erreurs_variable.set("Nombre d'essais restant : 0{}".format(erreurs_variable))
    else:
        Erreurs_variable.set("Nombre d'essais restant : {}".format(erreurs_variable))
def re_init_erreurs(): # réinitialise les erreurs globales
    global erreurs
    global erreurs_variable
    erreurs = 10
    erreurs_variable = erreurs
    if len(str(erreurs_variable)) == 1:
        Erreurs_variable.set("Nombre d'essais restant : 0{}".format(erreurs_variable))
    else:
        Erreurs_variable.set("Nombre d'essais restant : {}".format(erreurs_variable))
def show_stats(): # affiche les statistiques des parties
    global Stats
    nb_T = 0
    nb_F = 0
    nb_N = 0
    for stat in Stats:
        if stat == True : 
            nb_T +=1
        if stat == False : 
             nb_F +=1
        if stat == None : 
             nb_N +=1
    message.config(text = "{} Victoire | {} Défaite | {} Incomplète\n".format(nb_T,nb_F,nb_N))
def affiche_lettres(): # affiche les lettres utilisés dans la partie courante
    global list_letters
    # if list_letters ==[]:
    #     message.config(text = "Aucune lettre n'a été saisi")
    #     return 
    Lettres = ""
    for letter in list_letters:
        Lettres +=letter+", "
    Lettres = list(Lettres)
    Lettres[-1]
    Lettres[-1]
    message.config(text = reconstruction(Lettres))
def re_init_stats(): # réinitialise les stats de la partie
    global Stats
    Stats = []
def reconstruction(list): # transforme une liste en str
    mot =''
    for k in list:
        mot +=k
    return mot
def pendu(letters): # prend en parametres la lettre du bouton et lance le programme principal
        global mot
        global erreurs_variable
        global mot_search
        global list_letters
        global Stats
        global list_button
        global alphabet_bis
        p = 0
        if letters in list_letters :
            message.config(text = "La lettre a déjà été remplie\n")
        else :
            
            list_letters.append(letters)
            list_button[alphabet_bis[letters]].config(state="disabled")
            for k in range(1, len(mot)-1) :
                if mot[k] == letters :
                    del mot_search[k]
                    mot_search.insert(k,letters)
                    if p == 0 :
                        message.config(text = "Bonne réponse !\n")
                        if reconstruction(mot_search) == mot :
                            message.config(text = "Vous avez gagné !\n")
                            Stats.append(True)
                            
                            for i in range(len(list_button)//2):
                                choice(list_button).flash()
                            for elt in list_button:
                                elt.config(state="disabled")
                    p +=1
            if p == 0:
                erreurs_variable -= 1 
                message.config(text = "Mauvaise réponse !\n")
                if erreurs_variable == 0 :
                    message.config(text = "Vous avez perdu !\nLe mot était {}".format(mot))
                    for elt in list_button:
                        elt.config(state="disabled")
                    Stats.append(False)
        if len(str(erreurs_variable)) == 1:
            Erreurs_variable.set("Nombre d'essais restant : 0{}".format(erreurs_variable))
        else:
            Erreurs_variable.set("Nombre d'essais restant : {}".format(erreurs_variable))
        Mot_search.set("\n{}".format(reconstruction(mot_search)))  
def nb_letter(): # affiche le nombre de lettres du mot 
    global mot
    nb = len(mot)       
    message.config(text = "Le mot contient {} lettres\n".format(nb))
def show_rules(): # affiche les règles du jeu
    message.config(text="Règles : Deviner le mot caché en choisissant des lettres")
def show_indice(): # affiche un indice (une lettre)
    global mot
    global mot_search
    global erreurs_variable
    mot_new = list(mot)
    if mot_new == mot_search:
        message.config(text="Vous avez déja trouvé le mot\n")
        return
    if erreurs_variable == 0:
        return
    indice_letter = []
    for i in range(len(mot_new)):
        if mot_new[i] != mot_search[i]:
            indice_letter.append(mot_new[i])
    indice = choice(indice_letter)   
    message.config(text="Le mot contient la lettre {}".format(indice))    
def show_solution(): # affiche le mot recherché
    global erreurs_variable
    global mot
    global mot_search
    if mot == reconstruction(mot_search):
        return
    if erreurs_variable == 0:
        return
    message.config(text="Solution : {}".format(mot))
#création de la fenêtre
window = Tk()
window.title("Jeu du Pendu")
window.geometry("720x480")
window.iconbitmap("ico/pendu.ico")
window.config(background="#78DB61") # ~ vert

#création de la frame principale
frame = Frame(window, bg ="#78DB61")

# création des frames secondaires
top_frame = Frame(frame, bg =  "#78DB61")
bottom_frame = Frame(frame, bg = "#78DB61")
message_frame = Frame(frame, bg = "#78DB61")
game_Buttons = Frame(frame, bg = "#78DB61")

# création d'une image
width = 200 
height = 200 
img = PhotoImage(file="png\jeu-du-pendu.png").zoom(20).subsample(40)
canvas = Canvas(top_frame, width = width, height = height, bg ='#78DB61', bd = 0, highlightthickness=0) 
canvas.create_image(width/2,height/2, image = img)
canvas.pack(expand = True)

# création du Mot à trouver et du nombre d'erreurs restant dans la partie Top
Mot_init="\n{}".format(reconstruction(mot_search)) 
Erreur_init="Nombre d'essais restant : {}".format(erreurs)
Mot_search = StringVar()
Erreurs_variable = StringVar()
Mot_search.set(Mot_init)
Erreurs_variable.set(Erreur_init)

Mot = Label(top_frame, textvariable = Mot_search, font=('Courier',25, "bold"), bg = "#78DB61", fg ="white")
Mot.pack(expand= True)
Erreurs = Label(top_frame, textvariable= Erreurs_variable, font=('Perpetua',15,"italic"), bg = "#78DB61", fg ="white")
Erreurs.pack(expand= True)

# création du clavier dans la partie Bottom
alphabet = string.ascii_uppercase
list_button = [Button(bottom_frame,text = letter,font=('Courier',12,"bold"), bg = "#78DB61", fg ="white",command =partial(pendu, letter),pady=2,padx=2,justify=CENTER,highlightthickness=0,bd=0,activebackground="white",activeforeground="#78DB61",overrelief="sunken",cursor="left_ptr") for letter in alphabet]
for elt in list_button:
    elt.pack(side=LEFT)   
#création du bouton rejouer 
new = Button(game_Buttons,text = "Rejouer",font=('Courier',18,"bold"), bg = "#78DB61", fg ="white",command =new_game,pady=5,padx=5,justify=CENTER,highlightthickness=1,bd=1,activebackground="white",activeforeground="#78DB61",overrelief="sunken",cursor="left_ptr") 
new.pack(expand=True)
#création du message variable
message = Label(message_frame,text="Bienvenue dans le Jeu du Pendu !\n",font=('Courier',15,"bold"), bg = "#78DB61", fg ="white")
message.pack()
#affichage des frames sous forme de grille
top_frame.grid(row=0, column = 0,sticky=N)
bottom_frame.grid(row=2, column = 0,sticky=S)
message_frame.grid(row=1,column=0)
game_Buttons.grid(row = 3, column=0)
frame.pack(expand=True)

# creation d'une barre de menu
menu_bar = Menu(window)

#création des menus

file_menu = Menu(menu_bar, tearoff =0)
file_menu.add_command(label = "Nouvelle partie", command = new_game)
file_menu.add_command(label = "Quitter le jeu", command = window.destroy)

edit_menu = Menu(menu_bar, tearoff =0)
edit_menu.add_command(label = "+ 5 erreurs dans la partie courante", command = add_erreurs)
edit_menu.add_command(label = "+ 5 erreurs pour toutes les parties", command = add_global_erreurs)
edit_menu.add_command(label = "- 5 erreurs dans la partie courante", command = remove_erreurs)
edit_menu.add_command(label = "- 5 erreurs pour toutes les parties", command = remove_global_erreurs)
edit_menu.add_command(label = "Réinitialiser les erreurs", command = re_init_erreurs)
edit_menu.add_command(label = "Réinitialiser les stats", command = re_init_stats)

display_menu = Menu(menu_bar, tearoff =0)
display_menu.add_command(label = "Nombre de lettres du mot", command = nb_letter)
display_menu.add_command(label = "Liste des lettres déja utilisé", command = affiche_lettres)
display_menu.add_command(label = "Statistiques des parties", command = show_stats)

help_menu = Menu(menu_bar, tearoff =0)
help_menu.add_command(label = "Règles du jeu", command = show_rules)
help_menu.add_command(label = "Indice", command = show_indice)
help_menu.add_command(label = "Solution", command = show_solution)

# on ajoute en cascade les menus à la barre de menu

menu_bar.add_cascade(label="Jeu", menu=file_menu)

menu_bar.add_cascade(label="Modifier", menu=edit_menu)

menu_bar.add_cascade(label ="Afficher", menu = display_menu)

menu_bar.add_cascade(label="Aide", menu=help_menu)

# configuration de notre fenetre pour ajouter notre barre de menu
window.config(menu = menu_bar)


# affichage de la fenêtre
window.mainloop()
                