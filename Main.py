from tkinter import *
from tkinter.font import Font
from sys import exit, argv
from os import path

class Ingredient:

    ### Classe définissant les Ingredients dans liste_ingredient

    def __init__(self, nom, numero, coeur=0, effet="Aucun", duree=30, niveau = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, valeur_max=None, valeur_enduro_vigueur=None, type="Normal"):
        self.nom = nom
        self.coeur = coeur
        self.effet = effet
        self.duree = duree
        self.numero = numero
        self.niveau = niveau
        self.type = type
        if effet == "Max":
            self.valeur_max = valeur_max
        if effet == 'Enduro' or effet == 'Vigueur':
            self.valeur_enduro_vigueur = valeur_enduro_vigueur

    ### Methode si l'ingredient est choisi dans une recette

    def choisi(self):
        global image_ingredient_choisi, liste_label, ingredients_choisis, compteur_ingredient, bouton_termine
        if compteur_ingredient == 5:
            pass
        else:
            if self in ingredients_choisis:
                ingredients_choisis[self] += 1  # Compte le nombre d'ingredients de chaque sorte
            else:
                ingredients_choisis[self] = 1  # Initie la valeur dans le dictionnaire
            compteur_ingredient = 0
            for valeur in ingredients_choisis.values():
                compteur_ingredient += valeur
            bouton_termine['state'] = NORMAL
            image_ingredient_choisi.append(PhotoImage(file=f"{path}/images/{self.numero}.png"))
            liste_label[compteur_ingredient-1]['image'] = image_ingredient_choisi[compteur_ingredient-1]

    ### Methode si l'ingredient doit donner ses informations 

    def information(self):
        global information_ingredient, test, ingredient_choisi, fenetre
        ingredient_choisi = self
        information_ingredient = self.__dict__
        test = True
        fenetre.destroy()

### Fonction qui est utilisée si l'utilisateur appuie sur le bouton Supprimer 

def supprimer():
    global ingredients_choisis, image_ingredient_choisi, compteur_ingredient
    ingredients_choisis = {}
    image_ingredient_choisi = []
    compteur_ingredient = 0
    bouton_termine['state'] = DISABLED

### Fonction qui ferme la fenetre_titre ou la fenetre principale

def close(a):
    global test, test1
    if a == 1:
        test1 = True
        fenetre_titre.destroy()
    else:
        test = True
        fenetre.destroy()
    
### Comme son nom l'indique, fonction qui fait changer de page.

def change_page(mouvement):
    global page, page_changee
    if mouvement == 'Suivant':
        page += 1
    else:
        page -=1
    page_changee = True
    fenetre.destroy()

### Fonction qui est utilisée si l'utilisateur clique sur le bouton "Information sur les Ingrédients"

def information():
    global is_recette, page_changee
    is_recette = False
    fenetre.destroy()
    page_changee = True

### Fonction qui est utilisée si l'utilisateur clique sur le bouton "Simulateur de recettes"

def recette():
    global is_recette, page_changee
    is_recette = True
    fenetre.destroy()
    page_changee = True

### Fonction qui est utilisée si l'utilisateur appuie sur le bouton "Recommencer" à la fin

def recommencer():
    global fenetre2, test2
    fenetre2.destroy()
    test2 = True

### Definition des ingredients et de leurs valeurs ###

liste_ingredient = [
    Ingredient("Pomme", 1, 1),
    Ingredient("Gland", 2, 0.5,),
    Ingredient("Champi d'Hyrule", 3, 1),
    Ingredient("Noix de Coco", 4, 2),
    Ingredient("Baie", 5, 1),
    Ingredient("Fruit d'Oiseau", 53, 0.5),
    Ingredient("Oeuf de Volaille", 54, 2),
    Ingredient("Bouteille de Lait Frais", 55, 1),
    Ingredient("Venaison", 6, 2),
    Ingredient("Viande de Volaille", 7, 2),
    Ingredient("Venaison Fine", 8, 3),
    Ingredient("Viande de Volaille Fine", 9, 3),
    Ingredient("Venaison Divine", 10, 6),
    Ingredient("Viande de Volaille Divine", 11, 6),
    Ingredient("Perche d'Hyrule", 12, 2),
    Ingredient("Herbes d'Hyrule", 13, 2),
    Ingredient("Champi Piment", 14, 1, "Piment", 150, {1: 1, 2: 1, 3: 2, 4: 2, 5: 2}),
    Ingredient("Champi Glagla", 15, 1, "Glagla", 150, {1: 1, 2: 1, 3: 2, 4: 2, 5: 2}),
    Ingredient("Champi Silencio", 16, 1, "Silencio", 120, {1: 1, 2: 1, 3: 2, 4: 2, 5: 3}),
    Ingredient("Champi Vigueur", 17, 1, "Vigueur", valeur_enduro_vigueur={1: 0.2, 2: 0.2, 3: 0.4, 4: 0.4, 5: 0.4}),
    Ingredient("Champi Enduro", 18, 1, "Enduro", valeur_enduro_vigueur={1: 0.2, 2: 0.4, 3: 0.8, 4: 1, 5: 1.4}),
    Ingredient("Champi Tempo", 19, 1, "Tempo", 60, {1: 1, 2: 1, 3: 1, 4: 1, 5: 2}),
    Ingredient("Champi Lame", 20, 1, "Lame", 50, {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}),
    Ingredient("Champi Armo", 21, 1, "Armo", 50, {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}),
    Ingredient("Champi Volt", 22, 1, "Volt", 150, {1: 1, 2: 2, 3: 3, 4: 3, 5: 3}),
    Ingredient("Fruit de Lotus Tempo", 23, 1, "Tempo", 60, {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}),
    Ingredient("Rayon de Miel Enduro", 24, 4, "Enduro", valeur_enduro_vigueur={1: 0.4, 2: 1, 3: 1.6, 4: 2.2, 5: 2.8}),
    Ingredient("Fruit Volt", 25, 1, "Volt", 150, {1: 1, 2: 2, 3: 3, 4: 3, 5: 3}),
    Ingredient("Melon Glagla", 26, 1, "Glagla", 150, {1: 1, 2: 1, 3: 2, 4: 2, 5: 2}),
    Ingredient("Citrouille Armo", 61, 1, "Armo", 50, {1: 1, 2: 2, 3: 3, 4: 3, 5: 3}),
    Ingredient("Carpe Lame", 28, 2, "Lame", 50, {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}),
    Ingredient("Carpe Armo", 29, 2, "Armo", 50, {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}),
    Ingredient("Carpe Tricolore", 30, 2),
    Ingredient("Truite Volt", 31, 2, "Volt", 150, {1: 1, 2: 3, 3: 3, 4: 3, 5: 3}),
    Ingredient("Truite Glagla", 32, 2, "Glagla", 150, {1: 1, 2: 2, 3: 2, 4: 2, 5: 2}),
    Ingredient("Truite Piment", 33, 2, "Piment", 150, {1: 1, 2: 2, 3: 2, 4: 2, 5: 2}),
    Ingredient("Truite Silencio", 34, 2, "Silencio", 120, {1: 1, 2: 2, 3: 2, 4: 3, 5: 3}),
    Ingredient("Daurade Lame", 35, 2, "Lame", 50, {1: 1, 2: 2, 3: 3, 4: 3, 5: 3}),
    Ingredient("Daurade Armo", 36, 2, "Armo", 50, {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}),
    Ingredient("Perche Max", 57, 2, "Max", valeur_max=2),
    Ingredient("Perche Enduro", 37, 2, "Enduro", valeur_enduro_vigueur={1: 1, 2: 2.2, 3: 3, 4: 3, 5: 3}),
    Ingredient("Saumon Max", 56, 8, "Max", valeur_max=4),
    Ingredient("Escargot Silencio", 58, 2, "Silencio", 120, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
    Ingredient("Turbo Max", 59, 6, "Max", valeur_max=4),
    Ingredient("Fleur Armo", 38, effet="Armo", duree=50, niveau={1: 1, 2: 1, 3: 1, 4: 1, 5: 2}),
    Ingredient("Fleur Lame", 39, effet="Lame", duree=50, niveau={1: 1, 2: 1, 3: 1, 4: 1, 5: 2}),
    Ingredient("Fleur Silencio", 40, effet="Silencio", duree=50, niveau={1: 1, 2: 1, 3: 1, 4: 1, 5: 2}),
    Ingredient("Herbe Volt", 41, effet="Volt", duree=150, niveau={1: 1, 2: 1, 3: 1, 4: 2, 5: 2}),
    Ingredient("Herbe Glagla", 42, effet="Glagla", duree=150, niveau={1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
    Ingredient("Herbe Piment", 43, effet="Piment", duree=150, niveau={1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
    Ingredient("Truffe Max", 44, 4, effet="Max", valeur_max=1),
    Ingredient("Grosse Truffe Max", 45, 6, "Max", valeur_max=4),
    Ingredient("Radis Max", 46, 5, "Max", valeur_max=3),
    Ingredient("Gros Radis Max", 47, 8, "Max", valeur_max=5),
    Ingredient("Durian Max", 48, 6, "Max", valeur_max=4),
    Ingredient("Crabe Lame", 62, 2, "Lame", 50, {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}),
    Ingredient("Crabe Armo", 63, 2, "Armo", 50, {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}),
    Ingredient("Carpe Enduro", 50, 2, "Enduro", valeur_enduro_vigueur={1: 0.4, 2: 1, 3: 1.6, 4: 2.2, 5: 2.8}),
    Ingredient("Boisseau de Riz", 51, 2),
    Ingredient("Boisseau de Blé", 52, 2),
    Ingredient("Carotte Tempo", 60, 1, "Tempo", 60, {1: 1, 2: 1, 3: 1, 4: 1, 5: 2}),
    Ingredient("Carotte Vigueur", 27, 4, "Vigueur", valeur_enduro_vigueur={1: 0.4, 2: 0.8, 3: 1.2, 4: 1.6, 5: 2}),
    Ingredient("Fée", 49, 10),
    Ingredient("Papillon Glagla", 65, effet="Glagla", duree=150, niveau={1: 1, 2: 1, 3: 1, 4: 1}, type="Remede"),
    Ingredient("Papillon Piment", 66, effet="Piment", duree=150, niveau={1: 1, 2: 1, 3: 1, 4: 1}, type="Remede"),
    Ingredient("Papillon Volt", 67, effet="Volt", duree=150, niveau={1: 1, 2: 1, 3: 1, 4: 2}, type="Remede"),
    Ingredient("Papillon Ignifus", 68, effet="Ignifus", duree=150, niveau={1: 1, 2: 1, 3: 1, 4: 2}, type="Remede"),
    Ingredient("Libellule Glagla", 69, effet="Glagla", duree=150, niveau={1: 1, 2: 1, 3: 2, 4: 2}, type="Remede"),
    Ingredient("Libellule Piment", 70, effet="Piment", duree=150, niveau={1: 1, 2: 1, 3: 2, 4: 2}, type="Remede"),
    Ingredient("Libellule Volt", 71, effet="Volt", duree=150, niveau={1: 1, 2: 2, 3: 3, 4: 3}, type="Remede"),
    Ingredient("Sauterelle Enduro", 72, effet="Enduro", valeur_enduro_vigueur={1: 0.2, 2: 0.4, 3: 0.8, 4: 1}, type="Remede"),
    Ingredient("Scarabée Lame", 73, effet="Lame", duree=50, niveau={1: 1, 2: 1, 3: 1, 4: 1}, type="Remede"),
    Ingredient("Scarabée Armo", 74, effet="Armo", duree=50, niveau={1: 1, 2: 1, 3: 1, 4: 1}, type="Remede"),
    Ingredient("Scarabée Enduro", 75, effet="Enduro", valeur_enduro_vigueur={1: 1.6, 2: 3, 3: 3, 4: 3}, type="Remede"),
    Ingredient("Luciole de la Sérénité", 76, effet="Silencio", duree=120, niveau={1: 1, 2: 1, 3: 1, 4: 1}, type="Remede"),
    Ingredient("Grenouille Tempo", 77, effet="Tempo", duree=60, niveau={1: 1, 2: 1, 3: 2, 4: 3}, type="Remede"),
    Ingredient("Grenouille Vigueur", 78, effet="Vigueur", valeur_enduro_vigueur={1: 0.2, 2: 0.4, 3: 0.6, 4: 0.8}, type="Remede"),
    Ingredient("Lezard Tempo", 79, effet="Tempo", duree=60, niveau={1: 1, 2: 1, 3: 1, 4: 1}, type="Remede"),
    Ingredient("Lezard Max", 80, effet="Max", valeur_max=4, type="Remede"),
    Ingredient("Lezard Tempo", 81, effet="Ignifus", duree=150, niveau={1: 1, 2: 1, 3: 1, 4: 1}, type="Remede"),
    Ingredient("Corne de Bokoblin", 64, duree=70, type="Monstre"),
    Ingredient("Croc de Bokoblin", 82, duree=110, type="Monstre"),
    Ingredient("Viscere de Bokoblin", 83, duree=190, type="Monstre"),
    Ingredient("Corne de Moblin", 84, duree=70, type="Monstre"),
    Ingredient("Croc de Moblin", 85, duree=110, type="Monstre"),
    Ingredient("Viscere de Moblin", 86, duree=190, type="Monstre"),
    Ingredient("Corne de Lézalfos", 87, duree=70, type="Monstre"),
    Ingredient("Griffe de Lézalfos", 88, duree=70, type="Monstre"),
    Ingredient("Queue de Lézalfos", 89, duree=190, type="Monstre"),
    Ingredient("Queue Bleue de Lézalfos", 90, duree=190, type="Monstre"),
    Ingredient("Queue Rouge de Lézalfos", 91, duree=190, type="Monstre"),
    Ingredient("Queue Jaune de Lézalfos", 92, duree=190, type="Monstre"),
    Ingredient("Corne de Lynel", 93, duree=70, type="Monstre"),
    Ingredient("Sabot de Lynel", 94, duree=110, type="Monstre"),
    Ingredient("Viscere de Lynel", 95, duree=190, type="Monstre"),
    Ingredient("Gelée Chuchu", 96, duree=70, type="Monstre"),
    Ingredient("Gelée Chuchu Blanche", 97, duree=110, type="Monstre"),
    Ingredient("Gelée Chuchu Rouge", 98, duree=110, type="Monstre"),
    Ingredient("Gelée Chuchu Jaune", 99, duree=110, type="Monstre"),
    Ingredient("Aile Griffue", 100, duree=70, type="Monstre"),
    Ingredient("Aile de Glace", 101, duree=110, type="Monstre"),
    Ingredient("Aile de Feu", 102, duree=110, type="Monstre"),
    Ingredient("Aile Electrique", 103, duree=110, type="Monstre"),
    Ingredient("Oeil de Chauve-Souris", 104, duree=190, type="Monstre"),
    Ingredient("Tentacule Octo", 105, duree=70, type="Monstre"),
    Ingredient("Oeil Octo", 106, duree=110, type="Monstre"),
    Ingredient("Baudruche Octo", 107, duree=70, type="Monstre"),
    Ingredient("Aileron de Moldarquor", 108, duree=110, type="Monstre"),
    Ingredient("Viscere de Moldarquor", 109, duree=190, type="Monstre"),
    Ingredient("Ongle d'Hinox", 110, duree=70, type="Monstre"),
    Ingredient("Dent d'Hinox", 111, duree=110, type="Monstre"),
    Ingredient("Viscere d'Hinox", 112, duree=190, type="Monstre"),
    Ingredient("Vis Antique", 113, duree=70, type="Monstre"),
    Ingredient("Ressort Antique", 114, duree=70, type="Monstre"),
    Ingredient("Rouage Antique", 115, duree=110, type="Monstre"),
    Ingredient("Arbre Antique", 116, duree=110, type="Monstre"),
    Ingredient("Coeur Antique", 117, duree=190, type="Monstre"),
    Ingredient("Coeur Antique Geant", 118, duree=190, type="Monstre"),
]

### Affichage de la fenêtre titre

test1 = False
path = path.dirname(argv[0])
fenetre_titre = Tk()
fenetre_titre.title('Accueil')
fenetre_titre.resizable(height=False, width=False)
background_photo = PhotoImage(file=f"{path}/images/background.png", master=fenetre_titre)
logo = PhotoImage(file=f"{path}/images/Logo.png", master=fenetre_titre)
Label(fenetre_titre, image=background_photo).place(x=0, y=0, relwidth=1, relheight=1)
Label(fenetre_titre, image=logo, bg='black', fg='white').grid(columnspan=2)
Button(fenetre_titre, text="Commencer", command=lambda : close(1), bg='black', fg='white',font=Font(size=20), padx=170, pady=8).grid(columnspan=2)
fenetre_titre.mainloop()
is_recette = True

### Définition des variables nécessaires au début du programme 
### et quand l'utilisateur appuie sur "Recommencer" à la fin.

while test1: ### Si test1 == False c'est que l'utilisateur a fermé la fenetre titre et n'a pas cliqué sur "Commencer"
    coeurs = 0
    test2 = False
    valeur_max = 0
    duree = 0
    valeur_endurance = 0
    niveau = 0
    compteur = 0
    compteur_ingredient = 0
    liste_label = []
    types = []
    image_ingredient_choisi = []
    compteur2 = 0
    page = 1
    test = False
    page_changee = False
    ingredients_enduro_vigueur = {}
    ingredients_choisis = {}

### Création des variables et widgets affichés tout le temps à l'ouverture de la fenetre principale

    while not test:
        compteur = 0
        page_changee = False
        compteur2 = 0
        fenetre = Tk()
        Label(fenetre, pady=20).grid(row=0, column=0) # Label servant à occuper la row 0 
        fenetre.geometry("+0+0")
        fenetre.resizable(width=False, height=False)
        background_photo = PhotoImage(file=f"{path}/images/background.png", master=fenetre)
        background_label = Label(fenetre, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
### Mise en place des widgets spécifiques au simulateur de recettes (tout le temps le cas au lancement du programme)
        
        if is_recette:
            fenetre.title('Choix des Ingredients')
            bouton_recette = Button(fenetre, text="Simulateur de Recettes", bg='black', fg='white', command=recette, relief=FLAT, font=Font(size=15), padx=20, pady=10, state=DISABLED)
            bouton_information = Button(fenetre, text="Informations sur les ingrédients", command=information, bg='black', fg='white', relief=FLAT, font=Font(size=15), padx=20, pady=10)
            bouton_recette.place(x=250, y=0)
            bouton_information.place(x=750, y=0)
            if liste_label != []:
               liste_label = []
               image_ingredient_choisi = []
            ### S'il y a eu un changement de page, cette boucle for affiche à nouveau les ingredients choisis dans les carrés en haut
            for ingredient, valeur in ingredients_choisis.items():
                for nombre in range(valeur):
                    image_ingredient_choisi.append(PhotoImage(file=f"{path}/images/{ingredient.numero}.png"))
                    liste_label.append(Label(fenetre, bg='black', pady=40, padx=50, image=image_ingredient_choisi[compteur2]))
                    liste_label[-1].grid(row=2, column=compteur2+2)
                    compteur2 += 1
            ### Puis complète avec des carrés vides 
            while len(liste_label) != 5:
                liste_label.append(Label(fenetre, bg='black', pady=40, padx=50))
                liste_label[-1].grid(row=2, column=compteur2+2)
                compteur2 += 1
            Button(fenetre, text='Supprimer', bg='black', fg='white', padx = 100, pady = 30, command=supprimer).grid(row=2, column=7, columnspan=3)
            bouton_termine = Button(fenetre, text="Terminé", command=lambda : close(2), width=100, bg='black', fg='white', font=100, pady=20)
            bouton_termine.grid(row=8, column=1, columnspan=8)
        
### Mise en place des widgets si le bouton "Information sur les ingredients" a été cliqué
        
        else:
            fenetre.title("Choix de l'Ingredient")
            bouton_recette = Button(fenetre, text="Simulateur de Recettes", bg='black', command=recette, fg='white', relief=FLAT, font=Font(size=15), padx=20, pady=10)
            bouton_information = Button(fenetre, text="Informations sur les ingrédients", command=information, bg='black', fg='white', relief=FLAT, font=Font(size=15), padx=20, pady=10, state=DISABLED)
            bouton_recette.place(x=250, y=0)
            bouton_information.place(x=750, y=0)

### Affichage des boutons ingredients en fonction de la page

        for ingredient in liste_ingredient:
            if compteur < 50*(page-1): # Traduction : Si l'ingredient ne doit pas être affiché, la boucle for passe à l'ingredient suivant
                compteur += 1
                continue
            elif compteur == 50*page: # Traduction : Si tous les ingredients sont affichés, la boucle for s'arrete.
                break
            
            else:
                ligne = (compteur-((page-1)*50)) // 10
                colonne = (compteur-((page-1)*50)) % 10
                compteur += 1
                ingredient_photo = PhotoImage(file=f"{path}/images/{ingredient.numero}.png", master=fenetre)
                image_coeur = PhotoImage(file=f"{path}/images/coeur.png", master=fenetre)   
            ### J'ai l'impression que les lignes 330 à 341 peuvent être opti...
                if ingredient.effet != "Aucun" and is_recette: 
                    image_effet = PhotoImage(file=f"{path}/images/{ingredient.effet}.png", master=fenetre, height=20, width=20)
                    Button(fenetre, image=ingredient_photo,command=lambda ingredient=ingredient, ingredient_photo=ingredient_photo, image_coeur=image_coeur,image_effet=image_effet: ingredient.choisi(), relief=FLAT, bg='black').grid(row=ligne + 3, column=colonne, padx=12, pady=12)
                    Label(fenetre,image=image_effet, bg='black').grid(column=colonne, row=ligne+3, sticky=SE, padx=15, pady=15)
                elif ingredient.effet != "Aucun" and not is_recette:
                    image_effet = PhotoImage(file=f"{path}/images/{ingredient.effet}.png", master=fenetre, height=20, width=20)
                    Button(fenetre, image=ingredient_photo,command=lambda ingredient=ingredient, ingredient_photo=ingredient_photo, image_coeur=image_coeur,image_effet=image_effet: ingredient.information(), relief=FLAT, bg='black').grid(row=ligne + 3, column=colonne, padx=12, pady=12)
                    Label(fenetre,image=image_effet, bg='black').grid(column=colonne, row=ligne+3, sticky=SE, padx=15, pady=15)
                elif ingredient.effet == "Aucun" and is_recette:
                    Button(fenetre, image=ingredient_photo, relief=FLAT, command=lambda ingredient=ingredient, ingredient_photo=ingredient_photo,image_coeur = image_coeur: ingredient.choisi(), bg='black').grid(row=ligne + 3, column=colonne, pady=12, padx=12)
                else:
                    Button(fenetre, image=ingredient_photo, relief=FLAT, command=lambda ingredient=ingredient, ingredient_photo=ingredient_photo,image_coeur = image_coeur: ingredient.information(), bg='black').grid(row=ligne + 3, column=colonne, pady=12, padx=12)
                Label(fenetre, image=image_coeur, bg='black').grid(row=ligne + 3, column=colonne, sticky=NE, padx=20, pady=23)
        
### Si aucun ingredient a été selectionné avant l'ouverture de la fenetre le bouton "Terminé" est désactivé pour éviter les erreurs
        
        if compteur_ingredient == 0 and is_recette:
            bouton_termine['state'] = DISABLED
        
### Affiche ou non les boutons permettant de changer de page

        if page != 1:
            image_back = PhotoImage(file=f'{path}/images/Back.png', master=fenetre)
            Button(fenetre, image=image_back, bg='black', command= lambda : change_page("Précédent")).grid(row=8)
        if page != 3:
            image_next = PhotoImage(file=f'{path}/images/Next.png', master=fenetre)
            Button(fenetre, image=image_next, bg='black', command= lambda : change_page("Suivant")).grid(row=8, column=9)
        fenetre.mainloop() ### La fenetre s'ouvre
        if not page_changee and not test: # Traduction : Si l'utilisateur a fermé la fenetre, 
            exit(1)                       # le programme s'arrete.

### L'utilisateur a choisi les ingredients de sa recette ou l'ingredient dont il veut avoir les infos 
### et maintanant il faut calculer le résultat ou trouver les bonnes infos et l'afficher à l'écran
    
    ### Calcul du résultat de la recette

    if is_recette:
        for ingredient in ingredients_choisis.keys(): # Pour chaque type d'ingredient dans la recette
            for valeur in range(ingredients_choisis[ingredient]):# Pour chaque ingredient de ce type
            ### Calcul des coeurs jaunes rendus par l'ingredient s'il est Max
                if ingredient.effet == "Max":
                    valeur_max += ingredient.valeur_max
            ### Si l'ingredient a un effet Enduro/Vigueur, ajoute 1 au nombre de cet ingredient 
            ### dans le dico ingredient_enduro_vigueur
                if ingredient.effet == "Enduro" or ingredient.effet == "Vigueur":
                    if ingredient in ingredients_enduro_vigueur:
                        ingredients_enduro_vigueur[ingredient] += 1
                    else:
                        ingredients_enduro_vigueur[ingredient] = 1
                coeurs += ingredient.coeur ### Calcul des coeurs rendus par la recette
                duree += ingredient.duree  ### Calcul de la durée de l'effet de la recette
            ### Calcul de l'effet de la recette
                if not "effet" in locals() and ingredient.effet != "Aucun":
                    effet = ingredient.effet
                elif ingredient.effet == "Aucun" or ingredient.effet == effet:
                    pass
                else:
                    effet = "Aucun"
            ### Si l'ingredient est un matériau de monstre ou un ingredient de remède, l'enregistre dans la liste types
                if ingredient.type != "Normal" and not ingredient.type in types:
                    types.append(ingredient.type)

    ### Si la recette contient que des ingredients de remède sans ingredient de monstre ou vice-versa, 
    ### le résultat est un plat douteux sans effet qui diminue par 2 le nombre de coeurs rendus par la recette.
        if types == ["Remede"] or types == ["Monstre"]:
            effet = "Aucun"
            if coeurs == 0:
                coeurs = 0.5
            else:
                coeurs /= 2
    ### Si il y a des ingredients de monstre et de remède, cela crée un remède qui rend 0 coeurs
        elif types == ["Remede", "Monstre"] or types == ["Monstre", "Remede"]:
            coeurs = 0
        if not "effet" in locals():
            effet = "Aucun"
    ### Calcul de l'endurance rendue/donnée
        if effet == "Enduro" or effet == "Vigueur":
            for ingredient, valeur in ingredients_enduro_vigueur.items():
                valeur_endurance += ingredient.valeur_enduro_vigueur[valeur]
    ### Calcul de la durée en minutes et secondes
        duree_min = duree // 60
        duree_sec = duree % 60
    ### Calcul du niveau de la recette et borne le niveau max
        if effet != "Aucun":
            for ingredient, valeur in ingredients_choisis.items():
                niveau += ingredient.niveau[valeur]
            if (effet != "Glagla" or effet != "Piment") and niveau > 3 :
                niveau = 3
            elif (effet == "Glagla" or effet == "Piment") and niveau > 2:
                niveau = 2
        if coeurs == 0 and effet == "Aucun":
            coeurs = 1
    
### Affichage de la fenetre résultat

        fenetre2 = Tk()
        fenetre2.resizable(width=False, height=False)
        fenetre2.title("Résultat")
        photo = PhotoImage(file=f"{path}/images/background.png", master=fenetre2)
        Label(fenetre2, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
        Label(fenetre2, text="Résultat", bg='black', fg='white', font=100).grid(columnspan=5)
    ### Affichage du nombre de coeurs rendus
        if coeurs != 0:
            Label(fenetre2, text=f"Points de vie : {'Récupération Complète' if effet == 'Max' or coeurs >= 30 else ''}", bg='black', fg='white', font=Font(size=12)).grid(row=1, sticky=W)
            effet_y = 49 ### Ce type de variable sert à savoir où positionner des widgets
        else:
            effet_y = 25
        image_coeur10=PhotoImage(file=f'{path}/images/coeur10.png', master=fenetre2)
        image_coeur5=PhotoImage(file=f'{path}/images/coeur5.png', master=fenetre2)
        image_coeur=PhotoImage(file=f'{path}/images/coeur.png', master=fenetre2)
        compteur = 0
        if coeurs != 0 and coeurs != 30 and effet != "Max":
            for coeur10 in range(int(round(coeurs, 0))//10):
                compteur +=1
                Label(fenetre2, image=image_coeur10, bg='black').place(x=110+(compteur-1)*18, y=30)
            for coeur5 in range(int(round(coeurs, 0))%10//5):
                compteur += 1
                Label(fenetre2, image=image_coeur5, bg='black').place(x=110+(compteur-1)*18,y=30)
            for coeur in range((int(round(coeurs, 0))%10)%5):
                compteur += 1
                Label(fenetre2, image=image_coeur, bg='black').place(x=110+(compteur-1)*18,y=30)
            if type(coeurs) == float:
                compteur += 1
                image_demi_coeur = PhotoImage(file=f'{path}/images/coeur0.5.png', master=fenetre2)
                Label(fenetre2, image=image_demi_coeur, bg='black').place(x=110+(compteur-1)*18,y=30)
    ### Affichage de l'effet 
        if effet != "Aucun":
            if effet == "Enduro" or effet == "Vigueur" or effet == "Silencio" or effet == "Glagla" or effet == "Piment":
                x_effet = 160 ### Encore une variable qui sert à savoir où placer un widget
            elif effet == "Max" or effet == "Volt":
                x_effet = 135
            else:
                x_effet = 150
            Label(fenetre2, text=f"Effet Spécial : {effet}", bg='black', fg='white', font=Font(size=12)).grid(row=2, sticky=W)
            image_effet = PhotoImage(file=f'{path}/images/{effet}.png', master=fenetre2)
            Label(fenetre2, image=image_effet, bg='black').place(x=x_effet, y=effet_y)
        ### Affichage des coeurs jaunes rendus
            if effet == "Max":
                image_coeur_jaune = PhotoImage(file=f'{path}/images/coeur_jaune.png', master=fenetre2)
                Label(fenetre2, text=f"Coeurs Jaunes :", bg='black', fg='white', font=Font(size=12)).grid(row=3, sticky=W)
                compteur = 0
                for coeur_jaune in range(valeur_max):
                    Label(fenetre2,image=image_coeur_jaune, bg='black').place(x=120+compteur*17, y=77)
                    compteur += 1
                y = 96
        ### Affichage de l'endurence rendue/donnée
            elif effet == 'Enduro' or effet == 'Vigueur':
                Label(fenetre2, text=f"Puissance : ", bg='black', fg='white', font=Font(size=12)).grid(row=3, sticky=W)
                image_cercle02 = PhotoImage(file=f"{path}/images/cercle_{'jaune' if effet == 'Vigueur' else 'vert'}0.2.png", master=fenetre2)
                image_cercle04 = PhotoImage(file=f"{path}/images/cercle_{'jaune' if effet == 'Vigueur' else 'vert'}0.4.png", master=fenetre2)
                image_cercle06 = PhotoImage(file=f"{path}/images/cercle_{'jaune' if effet == 'Vigueur' else 'vert'}0.6.png", master=fenetre2)
                image_cercle08 = PhotoImage(file=f"{path}/images/cercle_{'jaune' if effet == 'Vigueur' else 'vert'}0.8.png", master=fenetre2)
                image_cerclecomplet = PhotoImage(file=f"{path}/images/cercle_{'jaune' if effet == 'Vigueur' else 'vert'}.png", master=fenetre2)
                compteur = 0
                if types == ["Monstre", "Remede"] or types == ["Remede", "Monstre"]:
                    y_max_enduro = 52 ### Une autre variable de placement
                else:
                    y_max_enduro = 75
                for cerclecomplet in range(int(valeur_endurance // 1)):
                    Label(fenetre2, image=image_cerclecomplet, bg='black').place(x=85+18*compteur, y=y_max_enduro)
                    compteur += 1
                    valeur_endurance -= 1
                for cercle08 in range(int(round(valeur_endurance, 1)//0.8)): ### round() est obligatoire car il y a des petits problèmes de calcul 
                    Label(fenetre2, image=image_cercle08, bg='black').place(x=85+18*compteur, y=y_max_enduro)
                    compteur += 1
                    valeur_endurance -= 0.8
                for cercle06 in range(int(round(valeur_endurance, 1)//0.6)):
                    Label(fenetre2, image=image_cercle06, bg='black').place(x=85+18*compteur, y=y_max_enduro)
                    compteur += 1
                    valeur_endurance -= 0.6
                for cercle04 in range(int(round(valeur_endurance, 1)//0.4)):
                    Label(fenetre2, image=image_cercle04, bg='black').place(x=85+18*compteur, y=y_max_enduro)
                    compteur += 1
                    valeur_endurance -= 0.4
                for cercle02 in range(int(round(valeur_endurance, 1)//0.2)):
                    Label(fenetre2, image=image_cercle02, bg='black').place(x=85+18*compteur, y=y_max_enduro)
                    compteur += 1
                    valeur_endurance -= 0.2
                y = 96
        ### Affichage du niveau et de la durée si la recette n'est ni max ni enduro ni vigueur
            else:
                Label(fenetre2, text=f"Niveau : {niveau}", bg='black', fg='white', font=Font(size=12)).grid(row=3, sticky=W)
                Label(fenetre2, text=f"Durée : {'0' if duree_min < 10 else ''}{duree_min}:{duree_sec}{'0' if duree_sec == 0 else ''}", bg='black', fg='white', font=Font(size=12)).grid(row=4, sticky=W)
                y = 120
        else:
            y = 48
        fenetre2.geometry(f"360x{y+53}") # Resize de la fenetre
    ### Affichage des boutons "Recommencer" et "Arreter"
        Button(fenetre2, text="Recommencer", command=recommencer, padx=33, pady=10, bg='black', fg='white', font=75).place(x=1, y=y)
        Button(fenetre2, text="Arrêter", command=lambda : exit(1), padx=52, pady=10, bg='black', fg='white', font=75).place(x=185, y=y)
        fenetre2.mainloop()### Ouverture de la fenetre
        if not test2: ### Cela arrive si la fenetre a été fermée par l'utilisateur
            exit(1)
        del effet
    else:

    ### Affichage des informations de l'ingredient choisi

        fenetre2 = Tk()
        fenetre2.resizable(width=False, height=False)
        fenetre2.title("Résultat")
        image_coeur10 = PhotoImage(file=f'{path}/images/coeur10.png', master=fenetre2)
        image_coeur5 = PhotoImage(file=f'{path}/images/coeur5.png', master=fenetre2)
        image_coeur = PhotoImage(file=f'{path}/images/coeur.png', master=fenetre2)
        image_demi_coeur = PhotoImage(file=f'{path}/images/coeur0.5.png', master=fenetre2)
        image_coeur0 = PhotoImage(file=f'{path}/images/coeur0.png', master=fenetre2)
        background_photo = PhotoImage(file=f"{path}/images/background.png", master=fenetre2)
        image_ingredient = PhotoImage(file=f"{path}/images/{ingredient_choisi.numero}.png", master=fenetre2)
        Label(fenetre2, image=background_photo).place(x=0, y=0, relwidth=1, relheight=1)
        compteur = 0
        ### Pour chaque information de l'ingredient choisi
        for information, valeur in information_ingredient.items():
            match information:
            ### Affichage du nom de l'ingredient
                case "nom":
                    Label(fenetre2, text=f"{valeur}", bg='black', fg='white', font=Font(size=15)).place(x=70)
            ### Affichage du nombre de ceours rendus s'il est utilisé dans une recette
                case "coeur":
                    Label(fenetre2, text="Points de Vie : ", bg='black', fg='white', font=Font(size=12)).place(x=0, y=23)
                    if valeur == 0:
                        Label(fenetre2, image=image_coeur0, bg='black', fg='white').place(x=110, y=28)
                    else:
                        for coeur10 in range(int(round(valeur, 0))//10):
                            compteur +=1
                            Label(fenetre2, image=image_coeur10, bg='black').place(x=110+(compteur-1)*18, y=28)
                        for coeur5 in range(int(round(valeur, 0))%10//5):
                            compteur += 1
                            Label(fenetre2, image=image_coeur5, bg='black').place(x=110+(compteur-1)*18,y=28)
                        for coeur in range((int(round(valeur, 0))%10)%5):
                            compteur += 1
                            Label(fenetre2, image=image_coeur, bg='black').place(x=110+(compteur-1)*18,y=28)
                        if type(coeurs) == float:
                            compteur += 1
                            Label(fenetre2, image=image_demi_coeur, bg='black').place(x=110+(compteur-1)*18,y=28)
            ### Affichage de l'effet de l'ingredient dans une recette
                case "effet":
                    if valeur != "Aucun":
                        if information_ingredient['effet'] == "Enduro" or information_ingredient['effet'] == "Vigueur" or information_ingredient['effet'] == "Silencio" or information_ingredient['effet'] == "Glagla" or information_ingredient['effet'] == "Piment":
                            x_effet = 160
                        elif information_ingredient['effet'] == "Max" or information_ingredient['effet'] == "Volt":
                            x_effet = 135
                        else:
                            x_effet = 150
                        image_effet = PhotoImage(file=f'{path}/images/{valeur}.png', master=fenetre2)
                        Label(fenetre2, image=image_effet, bg='black').place(x=x_effet, y=48)
                    Label(fenetre2, text=f"Effet Spécial : {valeur}", bg='black', fg='white', font=Font(size=12)).place(y=47) 
            ### Affichage du niveau de l'ingredient en fonction du nombre de cet ingredient dans le recette
                case "niveau":
                    if valeur == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0} and information_ingredient['effet'] == "Aucun":
                        y_fenetre = 150
                        continue
                    if information_ingredient['effet'] != "Max" and information_ingredient['effet'] != "Enduro" and information_ingredient['effet'] != "Vigueur":
                        compteur=0
                        Label(fenetre2, text='Niveau :', bg='black', fg='white', font=Font(size=12)).place(y=70)
                        tableau_niveau=Canvas(fenetre2, height=50, width=122, bg='black')
                        tableau_niveau.create_line(25, 0, 25, 55, 50, 55, 50, 0, 75, 0, 75, 55, 100, 55, 100, 0, 125, 0, 125, 25, 0, 25, fill='white')
                        for nombre, niveau in valeur.items():
                            Label(fenetre2, text=str(nombre), bg='black', fg='white', font=Font(size=11)).place(x=68+25*compteur, y=75)
                            Label(fenetre2, text=str(niveau), bg='black', fg='white', font=Font(size=11)).place(x=68+25*compteur, y=101)
                            compteur += 1
                        tableau_niveau.place(x=63, y=73)
                        y_fenetre = 210
                    elif information_ingredient['effet'] == "Max":
                        y_fenetre = 210
                    else: 
                        y_fenetre = 285
            ### Affichage de la durée que donne l'ingredient dans une recette
                case "duree":
                    if information_ingredient['effet'] != "Max" and information_ingredient['effet'] != "Enduro" and information_ingredient['effet'] != "Vigueur" and information_ingredient['type'] != "Monstre":
                        y_duree = 127
                    else:
                        y_duree = 70
                    duree_min = valeur // 60
                    duree_sec = valeur % 60
                    Label(fenetre2, text=f"Durée : {'0' if duree_min < 10 else ''}{duree_min}:{'0' if duree_sec < 10 else ''}{duree_sec}", bg='black', fg='white', font=Font(size=12)).place(y=y_duree)
            ### Affichage du nombre de coeurs jaunes donnés par l'ingredient (uniquement s'il est d'effet max)
                case "valeur_max":
                    image_coeur_jaune = PhotoImage(file=f'{path}/images/coeur_jaune.png', master=fenetre2)
                    Label(fenetre2, text=f"Coeurs Jaunes :", bg='black', fg='white', font=Font(size=12)).place(x=12, y=90)
                    compteur = 0
                    for coeur_jaune in range(valeur):
                        Label(fenetre2,image=image_coeur_jaune, bg='black').place(x=130+compteur*18, y=95)
                        compteur += 1
            ### Affcihage de l'endurence rendue/donnée par l'ingredient en fonction du nombre de cet ingredient dans la recette
            ### (uniquement s'il est d'effet Enduro ou Vigueur)
                case "valeur_enduro_vigueur":
                    image_cercle02 = PhotoImage(file=f"{path}/images/cercle_{'jaune' if information_ingredient['effet'] == 'Vigueur' else 'vert'}0.2.png", master=fenetre2)
                    image_cercle04 = PhotoImage(file=f"{path}/images/cercle_{'jaune' if information_ingredient['effet'] == 'Vigueur' else 'vert'}0.4.png", master=fenetre2)
                    image_cercle06 = PhotoImage(file=f"{path}/images/cercle_{'jaune' if information_ingredient['effet'] == 'Vigueur' else 'vert'}0.6.png", master=fenetre2)
                    image_cercle08 = PhotoImage(file=f"{path}/images/cercle_{'jaune' if information_ingredient['effet'] == 'Vigueur' else 'vert'}0.8.png", master=fenetre2)
                    image_cerclecomplet = PhotoImage(file=f"{path}/images/cercle_{'jaune' if information_ingredient['effet'] == 'Vigueur' else 'vert'}.png", master=fenetre2)
                    Label(fenetre2, text="Endurance donnée :", bg='black', fg='white', font=Font(size=12)).place(y=90)
                    tableau_enduro_vigueur = Canvas(fenetre2, height=90, width=122, bg='black')
                    tableau_enduro_vigueur.create_line(25, 0, 25, 155, 50, 155, 50, 0, 75, 0, 75, 155, 100, 155, 100, 0, 125, 0, 125, 25, 0, 25, fill='white')
                    tableau_enduro_vigueur.place(x=20, y=113)
                    compteur = 0
                    compteur2 = 0
                    for nombre, effet in valeur.items():
                        compteur2 = 0
                        Label(fenetre2, text=str(nombre), bg='black', fg='white', font=Font(size=11)).place(x=25+25*compteur, y=115)
                        for cerclecomplet in range(int(effet) // 1):
                            Label(fenetre2, image=image_cerclecomplet, bg='black').place(x=24+25*compteur, y=143+20*compteur2)
                            compteur2 += 1
                            effet -= 1
                        for cercle08 in range(int(round(effet, 1)//0.8)):
                            Label(fenetre2, image=image_cercle08, bg='black').place(x=24+25*compteur, y=143+20*compteur2)
                            compteur2 += 1
                            effet -= 0.8
                        for cercle06 in range(int(round(effet, 1)//0.6)):
                            Label(fenetre2, image=image_cercle06, bg='black').place(x=24+25*compteur, y=143+20*compteur2)
                            compteur2 += 1
                            effet -= 0.6
                        for cercle04 in range(int(round(effet, 1)//0.4)):
                            Label(fenetre2, image=image_cercle04, bg='black').place(x=24+25*compteur, y=143+20*compteur2)
                            compteur2 += 1
                            effet -= 0.4
                        for cercle02 in range(int(round(effet, 1)//0.2)):
                            Label(fenetre2, image=image_cercle02, bg='black').place(x=24+25*compteur, y=143+20*compteur2)
                            compteur2 += 1
                            effet -= 0.2
                        compteur += 1
            ### Informations inutiles et non affichées
                case "numero":
                    pass
                case "type":
                    pass
        fenetre2.geometry(f"350x{y_fenetre}")### Resize de la fenetre
        ### Affichage des boutons "Recommencer" et "Arrêter"
        Button(fenetre2, text="Recommencer", command=recommencer, padx=33, pady=10, bg='black', fg='white', font=75).place(x=1, y=y_fenetre-50)
        Button(fenetre2, text="Arrêter", command=lambda : exit(1), padx=52, pady=10, bg='black', fg='white', font=75).place(x=185, y=y_fenetre-50)
        ### Affcihage de l'image de l'ingredient
        Label(fenetre2, image=image_ingredient, bg='black').place(x=250)
        fenetre2.mainloop()
        if not test2:
            exit(1)