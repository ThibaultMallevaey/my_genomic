import os
import sys 
import sphinx
import argparse
from .tools import tool

"""
Module de fonctions utiles en génomique. 
"""


   
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

def convert_RNA(dict_seq):
    """
    Convertir les séquences d'ADN en séquence d'ARN
    Prend en entrée un dictionnaire et retourne un nouveau dictionnaire contenant les séquences converties
    """
    new_dict_seq = {}
    for key, seq in dict_seq.items():
        seq_rna = seq.replace('T', 'U')
        new_dict_seq[key] = seq_rna
    return(new_dict_seq)


def parse(filename):
        lines = read_file(filename)
        dict_seq = parse_fasta(lines)
        print(dict_seq)


def run():
    parser = argparse.ArgumentParser(
        prog="my-genomic",
        usage="my-genomic filename --RNA",
        description="Parse un fichier fasta"
    )

    parser.add_argument(
        "filename",
        type=str,
    )
    parser.add_argument(
        "--RNA",
        action='store_true',
    )
    
    arguments = parser.parse_args()
    filename = arguments.filename
    
    lines = tool.read_file(filename)
    dict_seq = parse_fasta(lines)

    if arguments.RNA :
        dict_seq = convert_RNA(dict_seq)
    print(dict_seq)
