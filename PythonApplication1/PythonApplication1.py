# t=open("tiny.txt","r").read()
import numpy as np

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

def parser(file_path):#traite un fichier � la fois
    text_init=lecture_traitement(file_path)
    text_tr1=only_caracter(text_init)
    liste_mots=spliter(text_tr1)
    dico_mot_init=liste_occurrences(liste_mots)
    dico_tr_1=reduction_occurence_unique(dico_mot_init)
    dico_tr2=tri_dico(dico_tr_1)    
    dico_f=reduction_occurence(dico_tr2,100)
    return [dico_f,liste_mots]

# liste des �l�ments � sauvegarder : liste_mots dans un fichier et un mot par ligne et dico_f dans un autre fichier
#compute_dict(dico_f_filepath) et en cl� ou valeur on donne sa position dans le fichier

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
    #
    pass

def compute_dict(l_mots):
    res = dict()
    j=0
    for i in l_mots:
        res[i]=j
        j=j+1
    return res



def compute_matrix(l_mots, k, d_index):
    matrix =  np.zeros((len(d_index),len(d_index)),dtype = int)

    return 0



#
 
def main():
    pass


    
a = {"a":1}
b={"a":2,"c":6}
c = {"r":0}
d={"r":7,"g":6}
"""
print((a|b))# ou alors c.update(d)
c.update(d)
the two lines do the same thing, the first line is only after version 3.9
"""

print(compute_dict(parser("tiny.txt")[0]))
print("rfe")
save_parsed_data(parser("hayku.txt"),"hayku")