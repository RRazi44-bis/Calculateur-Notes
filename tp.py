import tkinter as tk
import matplotlib.pyplot as plt

from PIL import Image,ImageTk
from tkinter import Canvas
from tkinter import ttk

fenetre = tk.Tk()
fenetre.title("Calculateur de moyenne d'UE")
fenetre.geometry("1280x720")
frm = ttk.Frame(fenetre)
frm.grid()

list_module = ["R101", "R102", "R103", "R104", "R105", "R006", "R107", "R108", "R109", "R110", "R111", "R112", "R113", "R114", "R115",
               "SAE11", "SAE12", "SAE13", "SAE14", "SAE15", "SAE16"]
list_entry = []

photo=None 

UE1_COEFF={
    "R101":  10,
    "R102":  10,
    "R103":  7,
    "R104":  7,
    "R105":  0,
    "R006":  5,
    "R107":  0,
    "R108":  6,
    "R109":  0,
    "R110":  5,
    "R111":  4,
    "R112":  2,
    "R113":  5,
    "R114":  5,
    "R115":  0,
    "SAE11": 20,
    "SAE12": 20,
    "SAE13": 0,
    "SAE14": 0,
    "SAE15": 0,
    "SAE16": 7
}

UE2_COEFF={
    "R101":  4,
    "R102":  0,
    "R103":  2,
    "R104":  8,
    "R105":  6,
    "R006":  0,
    "R107":  0,
    "R108":  0,
    "R109":  0,
    "R110":  5,
    "R111":  5,
    "R112":  2,
    "R113":  9,
    "R114":  9,
    "R115":  3,
    "SAE11": 0,
    "SAE12": 0,
    "SAE13": 29,
    "SAE14": 0,
    "SAE15": 0,
    "SAE16": 7
}

UE3_COEFF={
    "R101":  4,
    "R102":  0,
    "R103":  2,
    "R104":  0,
    "R105":  0,
    "R006":  5,
    "R107":  15,
    "R108":  6,
    "R109":  4,
    "R110":  5,
    "R111":  5,
    "R112":  2,
    "R113":  0,
    "R114":  0,
    "R115":  3,
    "SAE11": 0,
    "SAE12": 0,
    "SAE13": 0,
    "SAE14": 20,
    "SAE15": 20,
    "SAE16": 7
}

NOTE = {
    "R101":  -1,
    "R102":  -1,
    "R103":  -1,
    "R104":  -1,
    "R105":  -1,
    "R006":  -1,
    "R107":  -1,
    "R108":  -1,
    "R109":  -1,
    "R110":  -1,
    "R111":  -1,
    "R112":  -1,
    "R113":  -1,
    "R114":  -1,
    "R115":  -1,
    "SAE11": -1,
    "SAE12": -1,
    "SAE13": -1,
    "SAE14": -1,
    "SAE15": -1,
    "SAE16": -1
}

def average_note(note_dict, ue):
    """
    This function calculate the average note.
    In: note_dict, ue : dict
    out: average
    """
    # Récuperer les notes et grâce à la clé des notes, récupérer les coeffs 
    assert type(note_dict) == dict, "The type of note_dict must be a dictionnary." 
    assert type(ue) == dict, "The type of ue must be a string."
    nb_elt = 0 # Somme des coeffs.
    somme = 0 # Prends la somme de toutes les notes en prennant en compte le coeff.
    for module, note in note_dict.items(): # On parcours les couples (clés/valeurs) de UE.items
        coeff = ue[module]
        somme = somme + note * coeff
        nb_elt = nb_elt + coeff
    average = somme/nb_elt
    return average


def get_colors(values):
    """
    This function calculate the color of each value of a list.
    If the value is superior or equals than 10, it's green, 
    between 8 and 10 and inferior than 10, it's yellow,
    if it's inferior than 8, it's red.
    
    In: values (list)
    Out: colors (list)
    """
    colors = []
    for value in values:
        if value >= 10:
            colors.append("green")
        elif value >= 8:
            colors.append("yellow")
        else:
            colors.append("red")
    return colors


def display_result(names, values):
    """
    This function display the result in barre, with the names and values from parameters
    In: names, values: list.
    """
    assert type(names) == list, "The type of names must be a list"
    assert type(values) == list, "The type of values must be a list"
    assert len(names) == len(values), "The size of names and values must be the same"

    global photo
    axes = plt.clf()
    axes = plt.gca()
    axes.set_ylim(0, 20)
    colors = get_colors(values)
    plt.bar(names, values, color=colors)
    plt.savefig("graphic.jpg")
    # Chargement et conversion de l'image avec Pillow
    image = Image.open("graphic.jpg")
    image = image.resize((300,200))
    
    photo = ImageTk.PhotoImage(image)
    
    # Création du Label avec l'image
    canva = tk.Canvas(fenetre, width=300, height=200)
    canva.grid(column=2,row=0)
    
    canva.create_image(0, 0, image=photo, anchor="nw")

def calcul():
    i=0
    for entry in list_entry:
        NOTE[list_module[i]] = float(entry.get())
        i+=1
    note_ue1 = average_note(NOTE, UE1_COEFF)
    note_ue2 = average_note(NOTE, UE2_COEFF)
    note_ue3 = average_note(NOTE, UE3_COEFF)

    display_result(["UE1", "UE2", "UE3"],[note_ue1, note_ue2, note_ue3])


for i in range(len(list_module)):
    texte1 = ttk.Label(frm, text=list_module[i])
    entry  = ttk.Entry(frm)
    list_entry.append(entry)
    texte1.grid(column=0,row=i)
    entry.grid(column=1,row=i)

button = ttk.Button(frm, text="Calculer", command=calcul)
button.grid(column=2, row=0)

fenetre.mainloop()


