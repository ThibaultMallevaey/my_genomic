#fichier test 


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

