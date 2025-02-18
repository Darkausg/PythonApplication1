# t=open("tiny.txt","r").read()
import numpy as np

sep_corpus = False
knbf = 0
redu_ocu = 100
k_voisin = 3
"""
valeur definit dans init:
le(s) nom(s) des corpus a analyser
est ce que on rassemble les corpus en un seul corpus
si ils sont dans un corpus, est ce que on les separe par k+1 "FF"
la quantite des mots les plus frequent à retirer
le k-voisins
(potentiellemnt) si on optimise la matrice
lecture automatique et applications du traitements pour tout les fichiers texte 
deroulements du programmes par default ou customisation (init_type)
le k+1 filler fait de "FF"
"""
def init(init_type):
    pass


def lecture_traitement(f):
    l=open(f,"r").read()
    return l.lower()
    
# ti=open("tiny.txt","r").read().lower()

def only_caracter(ori_text):
    letter ="azertyuiopqsdfghjklmwxcvbn"
    text_treated = ""
    for i in ori_text:
        if i in letter:
            text_treated = text_treated + i
        else:
            text_treated = text_treated + " "
    return text_treated

# tin=only_caracter(open("tiny.txt","r").read().lower())

def spliter(f):
    return f.split()
    

# tiny=spliter(tin)

def liste_occurrences(l):
    res=dict()
    for i in l:
        if not i in res:
            res[i]=1
        else:
            res[i]+=1
    return res

# tinyy=liste_occurrences(tiny)

def reduction_occurence_unique(d):
    res=dict()
    for i in d:
        if not d[i]==1:
            res[i]=d[i]
    return res

#tinyyy=reduction_occurence_unique(tinyy)

def tri_dico(d):
    dico_trie = dict(sorted(d.items(), key=lambda item: item[1]))
    "from : https://www.datacamp.com/fr/tutorial/sort-a-dictionary-by-value-python"
    return dico_trie

def reduction_occurence(d,t):
    if len(d)<t:
        return d
    for i in range(t):
        d.popitem()

    return d

def parser(file_path):#traite un fichier a la fois
    text_init=""


    if (knbf>0):# si on en traite plusieurs
        for i in range(0,knbf+1):
            text_init=text_init + lecture_traitement(file_path[i])
            
            if sep_corpus:#si on separe les textes entre eux
                for i in range(0,k_voisin+1):
                    text_init = text_init+" FF "

    else:#si on traite 1 corpus
        text_init=text_init + lecture_traitement(file_path)
    #

    
    text_tr1=only_caracter(text_init)
    liste_mots=spliter(text_tr1)

    #on cree le dico
    dico_mot_init=liste_occurrences(liste_mots)
    dico_tr_1=reduction_occurence_unique(dico_mot_init)
    if sep_corpus:
        del dico_tr_1['FF']
    dico_tr2=tri_dico(dico_tr_1)    
    dico_f=reduction_occurence(dico_tr2,redu_ocu)
    return [dico_f,liste_mots]



# liste des elements a sauvegarder : liste_mots dans un fichier et un mot par ligne et dico_f dans un autre fichier
#compute_dict(dico_f_filepath) et en key ou valeur on donne sa position dans le fichier

def save_parsed_data(dataSet,name):
    text_word = dataSet[0]
    liste_word = dataSet[1]
    with open("01"+name+"ensemble.txt","w") as l:
        for i in liste_word:
            l.write(i+"\n")
    with open("02"+name+"dico.txt","w") as d:
        for i in text_word.keys():
            d.write(i+"\n")
    with open("03Repertoire.txt","a") as r:
        r.write(name+"ensemble.txt\n"+name+"dico.txt\n")
    pass

def read_saved_data(name):
    l_mot = []
    dico=dict()
    n=0
    with open("01"+name+"ensemble.txt","r") as l:#liste de mots
        for i in l:
            l_mot.append(i.strip())
    with open("02"+name+"dico.txt","r") as d:#dico
        for i in d:
            dico[i.strip()] = n
            n+=1
    return[dico,l_mot]





def compute_dict(l_mots):
    res = dict()
    j=0
    for i in l_mots:
        res[i]=j
        j=j+1
    return res



def compute_matrix(l_mots, k, d_index):
    matrix =  np.zeros((len(d_index),len(d_index)),dtype = int)
    nb_mot = len(l_mots)
    """
    add (k+2)*"FF" at the begining and end of l_mot
    """
    filler = []
    for i in range(k):
        filler.append("FF")

    #l_mots.insert(0,filler)
    #l_mots.append(filler)
    l_mots = filler + l_mots + filler
    index = k
    for i in l_mots[k:-k]:                      #it should work, I tink, I really really  hope it work 
        index=index-k
        if i == "FF" or (not (i in d_index)):
            index = index+k+1
            continue

        for j in range(index,1+index+2*k):      #pourquoi il y a des boucles dans des boucles, pourquoi le code ne peut pas etre simple?
            if j == (index+k):                  #on saute le mot qu'on analyse
                continue
            #check existence l_mots[j] dans d_index
            if not (l_mots[j] in d_index):      #on saute si il n'est pas dans d_index
                continue
            #on rajoute le mot dans la matrice d'occurence
            matrix[ d_index[i] , d_index[ l_mots[j] ] ] =  matrix[ d_index[i] , d_index[ l_mots[j] ] ] +1
        
           
        index = index+k+1
    
    return (matrix/nb_mot)



#
 
def main():
    init(1)
    

    return 0


    
a = {"a":1}
b={"a":2,"c":6}
c = {"r":0}
d={"r":7,"g":6}
"""
print((a|b))# ou alors c.update(d)
c.update(d)
the two lines do the same thing, the first line is only after version 3.9
"""

#print(compute_dict(parser("tiny.txt")[0]))
#print("rfe")
save_parsed_data(parser("hayku.txt"),"hayku")
data = read_saved_data("hayku")
print(compute_matrix(data[1],3,data[0]))
#transformer en matrice à trous
