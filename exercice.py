#!/usr/bin/env python
# -*- coding: utf-8 -*-
#def majuscule(mot):
    # TODO completer la fonction ici
    #nouveau_mot = ""
    #for lettre in mot:
        #maj_lettre = chr(ord(lettre) - 32)
        #nouveau_mot = nouveau_mot + maj_lettre
    #return nouveau_mot


#def majuscule(mot):
    #nouveau_mot = ""
    #for i in mot:
    #    i_majuscule = chr(ord(i)-32)
     #   nouveau_mot = nouveau_mot + i_majuscule
    #return nouveau_mot

"""def majuscule(mot):
    nouveau_mot = ""
    for lettre in mot:
        lettre_maj = chr(ord(lettre)-32)
        nouveau_mot = nouveau_mot + lettre_maj
    return nouveau_mot"""

"""def majuscule(mot):
    new_mot = ""
    for i in mot:
        i_maj = chr(ord(i)-32)
        new_mot = new_mot + i_maj
    return new_mot"""

def majuscule(mot):
    new_word = ""
    for i in mot:
        new_i = chr(ord(i)-32)
        new_word = new_word + new_i
    return new_word

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
