#fichier test 

import os

def is_identifiant(line) :
    """
    Test si une ligne de fasta est un identifant ou une séquence.
    Entrée : Paramètre = line = ligne du fichier. Type = str
    Sortie : booléen
    """
    if ">" in line :
        return True
    else:
        return False
    

def test_is_identifiant():
    assert is_identifiant(">Test") == True
    assert is_identifiant("Test") == False

def read_file(filename):
    """
    Lire un fichier et retourner les lignes sous forme de listes.
    Paramètre = chemin du fichier = str
    Sortie = str = lignes du fichier
    """
    if os.path.exists(filename) :
        print(f"{filename} a ete trouve")
        # Lecture du fichier
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return lines
    

def parse_fasta(lines) :
    """
    Parcourir les lignes du fasta pour créer un dictionnaire {identifiant : séquence} 
    Entrée = str = lignes du fichier
    Sortie = dictionnaire des séquences {id:séquence}
    """
    i = 0
    dict_seq = {}
    identifiant = ""
    # Parcours des lignes
    while i < len(lines) :
        line = lines[i].strip()
        # Recupere l'identfiant de séquence
        if is_identifiant(line) :
            identifiant = line
        else :
            # Si la sequence est sur plusieurs lignes, ajoute la nouvelle ligne de sequence à la sequence existante
            if identifiant in dict_seq :
                dict_seq[identifiant] = dict_seq[identifiant] + line
            # Crée une nouvelle entrée dans le dictionnaire
            else :
                identifiant = identifiant.replace('>','')
                dict_seq[identifiant] = line
        i = i+1
    return dict_seq


