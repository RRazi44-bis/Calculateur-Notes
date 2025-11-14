import matplotlib.pyplot as plt

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
    "R101":  15,
    "R102":  15,
    "R103":  15,
    "R104":  15,
    "R105":  15,
    "R006":  11,
    "R107":  3,
    "R108":  4,
    "R109":  20,
    "R110":  12,
    "R111":  13,
    "R112":  1,
    "R113":  15,
    "R114":  -1,
    "R115":  12,
    "SAE11": 1,
    "SAE12": 6,
    "SAE13": 9,
    "SAE14": -1,
    "SAE15": 1,
    "SAE16": 15
}

list_module = ["R101", "R102", "R103", "R104", "R105", "R006", "R107", "R108", "R109", "R110", "R111", "R112", "R113", "R114", "R115",
               "SAE11", "SAE12", "SAE13", "SAE14", "SAE15", "SAE16"]

def input_note():
    for module in list_module:
        if NOTE[module] == -1:
            NOTE[module] == int(input(f"Entrez la note de {module} (Uniquement des chiffres, virgule possible) : "))

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
    axes = plt.gca()
    axes.set_ylim(0, 20)

    colors = get_colors(values) 
    plt.bar(names, values, color=colors)


input_note()

note_ue1 = average_note(NOTE, UE1_COEFF)
note_ue2 = average_note(NOTE, UE2_COEFF)
note_ue3 = average_note(NOTE, UE3_COEFF)

display_result(["UE1", "UE2", "UE3"],[note_ue1, note_ue2, note_ue3])