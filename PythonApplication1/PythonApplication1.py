# t=open("tiny.txt","r").read()
import numpy as np
import sys
import time

init_type = 2 #FF


"""
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
METTRE DANS LE README LA VERSION DE PYTHON DOIT ETRE SUPERIEUR A 3.10
"""

"""
valeurs definies dans init:
le(s) nom(s) des corpus a analyser
est ce que on rassemble les corpus en un seul corpus
si ils sont dans un corpus, est ce que on les separe par k+1 "FF"
la quantite des mots les plus frequents à retirer
le k-voisins
(potentiellemnt) si on optimise la matrice
lecture automatique et applications du traitements pour tout les fichiers texte 
deroulement du programme par default ou customisation (init_type)
le k+1 filler fait de "FF"
init_type =0 --> mode default
init_type = 1 --> mode customisable
init_type = 2 --> mode test (a retirer quand on rend le TP ou rendre impossible d'acces)
tout autre init_type --> fin du programme
"""
def init(init_type):

    param = []
    sep_corpus = False #0
    redu_ocu = 100 #1
    k_voisin = 3 #2
    filler_liste = " scpmeansecurecontainprotect " * k_voisin #3
    nbr_corpus = 1 #4
    compress = True #5

    param.append(sep_corpus)
    param.append(redu_ocu)
    param.append(k_voisin)
    param.append(filler_liste)
    param.append(nbr_corpus)
    param.append(compress)
    if init_type==0:
        param.append("hayku.txt")
        param.append("default")

    match init_type:
        case init_type if not (isinstance(init_type, int)):
            sys.exit()


        case 0:#default
            return param


        case 1:#customisable during exec
            return (init_custo(param))


        case _:#case default
            sys.exit()

    #something pour forcer l'indentation
    return param 



def init_custo(param):
    """
    permet de customiser les parametres du programme sans avoir a modifier les valeurs dans le code

    """
    loop= True
    miniLoop = True
    name_corpus_added = False

    sep_corpus = param[0] #0
    redu_ocu = param[1] #1
    k_voisin = param[2] #2
    filler_liste = param[3] #3
    nbr_corpus = param[4] #4
    compress = param[5] #5
    

    while loop:
        print(" \n "*150)
        print("Tapez 0 pour mettre fin \u00E0 la customisation.")
        print("\n")
        #print("\n")        
        print("Tapez 1 si vous voulez modifier le nombre de corpus \u00E0 traiter, par d\u00E9faut 1 seul corpus est trait\u00E9.")
        print("\n")
        print("\n")
        print("Tapez 2 pour saisir le(s) nom(s) des corpus.")
        print("\n")
        print("Il est obligatoire de saisir le(s) nom(s) des corpus.")
        print("\n")
        print("Si vous changez la quantit\u00E9 de corpus apr\u00E8s avoir saisi le nom de(s) corpus, veuillez les saisir \u00E0 nouveau.")
        print("\n")
        print("\n")
        print("Tapez 3 pour que les corpus soient trait\u00E9s de mani\u00E8re s\u00E9par\u00E9e avec 1 matrice par corpus \u00E0 la fin du programmme.")
        print("\n")
        print("\n")
        print("Tapez 4 pour que les corpus soient rassembl\u00E9s en 1 seul corpus, ce qui donnera 1 seule matrice \u00E0 la fin du programme.")
        print("\n")
        if not compress:
            print("Actuellement les corpus sont trait\u00E9s de mani\u00E8re s\u00E9par\u00E9e.")
        else:
            print("Actuellement les corpus sont rassembl\u00E9s en 1 seul corpus.")
            if sep_corpus:
                print("")#expliquer ce que fait sep_corpus si True
            else:
                print("")#expliquer ce que fait sep_corpus si False
        #
        print("\n")
        print("\n")
        print("Tapez 5 pour d\u00E9cider du nombre de mots les plus fr\u00E9quents qui seront retir\u00E9s.")
        print("\n")
        print("\n")
        print("Tapez 6 pour d\u00E9cider du k-contexte.")
        print("\n")
        #print("\n")
        temp = input("choisissez le param\u00E8tre \u00E0 modifier : ")
        if (temp.isdigit()):
            choice = int(temp)
        else:
            choice = 2512654
        match choice:

            case 2512654:
                print("saisie incorrecte, veuillez attendre 5 secondes avant de pouvoir continuer\n")
                time.sleep(5)

            case 1:#nombre des corpus a analyser
                if name_corpus_added:
                    name_corpus_added = False
                    if nbr_corpus>1:
                        l.clear
                    else:
                        l=""
                while miniLoop:
                    temp = input("tapez la quantit\u00E9 de corpus que vous souhaitez traiter : ")
                    if (temp.isdigit()):
                        nbr_corpus = int(temp)
                        if nbr_corpus>0:
                            break
                    print("entrer un entier sup\u00E9rieur \u00E0 0, sinon soit \u00E7a n'a pas de sens, soit c'est trop compliqu\u00E9 \u00E0 impl\u00E9menter")
                    print("veuillez attendre 5 secondes avant de pouvoir r\u00E9essayer de donner une quantit\u00E9")
                    time.sleep(5)


            case 3:#est ce que les corpus sont a analyser separement ou est ce qu'il doivent comprimer en 1 corpus
                compress = False

            case 4:#si plusieurs corpus sont rassemble dans 1 seul, est ce qu'ils doivent être separes par le filler
                compress = True
                temp = input("Si vous voulez que ..... pressez Y sinon pressez N : ")#expliquer ce que fait sep_corpus
                match temp:
                    case "Y":
                        sep_corpus = True
                    case "N":
                        sep_corpus = False
                    case _:
                        print("")#exprimer que sep_corpus est inchangé

            case 5:#la quantite des mots les plus frequents à retirer
                print("choisissez la quantit\u00E9 des mots les plus fr\u00E9quents \u00E0 retirer. Attention, si cette quantit\u00E9 exc\u00E9de la quantit\u00E9 de mots diff\u00E9rents aucune r\u00E9duction ne sera faite.\n")
                print("actuellement les " + str(redu_ocu) + " mots les plus fr\u00E9quents sont retir\u00E9\n")
                temp = input("veuillez saisir la quantit\u00E9 : ")
                if (temp.isdigit()):
                    redu_ocu = int(temp)
                    if redu_ocu<0:
                        redu_ocu=0
                        print("\nRetirer un nombre n\u00E9gatif de mots n'a aucun sens \nveuillez attendre 5 secondes avant de pouvoir continuer.")
                        time.sleep(5)
                else:
                    print("\nRetirer une quantit\u00E9 qui n'est pas un nombre n'as pas de sens \nveuillez attendre 5 secondes avant de pouvoir continuer.")
                    time.sleep(5)

            case 6:# choisir le k-voisin
                while miniLoop:
                    print("vous pouvez saisir un k-contexte qui est plus grand que le nombre de mots dans le corpus, le résultat sera le m\u00EAme que si vous avez demand\u00E9 un k-contexte \u00E9gal \u00E0 la taille du corpus\n")
                    print("Actuellement, le k-contexte est de : " + str(k_voisin) + " \n")
                    temp = input("tapez le k-contexte: ")
                    if (temp.isdigit()):
                        k_voisin = int(temp)
                        filler_liste = ""
                        filler_liste = " scpmeansecurecontainprotect "
                        if k_voisin>0:
                            break
                    print("entrer un entier sup\u00E9rieur \u00E0 0, sinon soit \u00E7a n'a pas de sens")
                    print("veuillez attendre 5 secondes avant de pouvoir r\u00E9essayer de donner une quantit\u00E9")
                    time.sleep(5)


            case 7:#(potentiellemnt) si on optimise la matrice
                a=0

            case 8:#(potentiellement)lecture automatique et applications du traitements pour tout les fichiers texte 
                a=0

            case 2:#nom des corpus
                print("si vous entrez des noms de fichiers qui n'existent pas, le programme va stopper son \u00E9x\u00E9cution avec une erreur file not found\n")
                print("auquel cas l'arr\u00EAt du programme est de votre faute et non pas celle des d\u00E9veloppeurs")
                print("le nombre de corpus \u00E0 saisir est : " + str(nbr_corpus))
                if nbr_corpus==1:
                    l = input("veuillez saisir le nom du fichier sans le .txt : ") + ".txt"
                else:
                    l=[]
                    for i in range(nbr_corpus):
                        l.append(input("veuillez saisir le nom du fichier sans le .txt : ") + ".txt")
                name_corpus_added = True



            case 0:#fin de la customisation
                print("\u00EAtes-vous s\u00FBr d'avoir fini de saisir tous les param\u00E8tres? \n")
                if name_corpus_added:
                    temp=input("si oui tapez 10 : ")
                    if (temp.isdigit() and int(temp) == 10):
                        loop = False
                else:
                    print("le nom de(s) corpus n'a pas \u00E9t\u00E9 d\u00E9fini, veuillez saisir le nom de(s) corpus")
                    print("veuillez attendre 5 secondes avant de pouvoir r\u00E9essayer de donner une quantit\u00E9")
                    time.sleep(5)
            #
            case _:
                a=0
    #
    
    param.clear()
    param.append(sep_corpus)
    param.append(redu_ocu)
    param.append(k_voisin)
    param.append(filler_liste)
    param.append(nbr_corpus)
    param.append(compress)
    param.append(l)
    param.append("placeholder")
    return param



def lecture_traitement(f):
    """
    lit le contenu d'un fichier dont le nom est donne par le parametre et renvoie tout le texte en minuscules
    """
    l=open(f,"r").read()
    return l.lower()
    


def only_caracter(ori_text):
    """
    prend un texte en parametre et remplace tous les caracteres qui ne sont pas des lettres par des espaces
    """
    letter ="azertyuiopqsdfghjklmwxcvbn"
    text_treated = ""
    for i in ori_text:
        if i in letter:
            text_treated = text_treated + i
        else:
            text_treated = text_treated + " "
    return text_treated





def liste_occurrences(l):
    """
    prend une liste de mots l en entree et compte le nombre de fois que chaque mot apparait dans cette liste. 
    Elle retourne un dictionnaire res ou les cles sont les mots et les valeurs sont les occurrences de ces mots.
    """
    res=dict()
    for i in l:
        if not i in res:
            res[i]=1
        else:
            res[i]+=1
    return res



def reduction_occurence_unique(d):
    """
    prend en entree un dictionnaire (d) ou les cles sont des mots et les valeurs sont le nombre d'occurrences de chaque mot. 
    retourne un nouveau dictionnaire (res) qui ne contient que les mots apparaissant plus d'une fois dans le dictionnaire d'origine.
    """
    res=dict()
    for i in d:
        if not d[i]==1:
            res[i]=d[i]
    return res



def tri_dico(d,ascending):
    """
    trie un dictionnaire d en fonction de ses valeurs, en ordre croissant ou decroissant, selon la valeur du booléen ascending
    retourne le dico trie
    """
    dico_trie = dict(sorted(d.items(), key=lambda item: item[1],reverse=ascending))
    "from : https://www.datacamp.com/fr/tutorial/sort-a-dictionary-by-value-python"
    return dico_trie



def reduction_occurence(d,t):
    """
    reduction_occurence prend en entrée un dictionnaire d et un entier t supérieur à 0. 
    reduction_occurence supprime t éléments du dictionnaire, à moins que le dictionnaire ne contienne moins de t éléments, et elle renvoie ce resultat
    """
    if len(d)<t:
        return d
    for i in range(t):
        d.popitem()

    return d



def parser(param):#traite un fichier a la fois
    text_init=""
    

    if (param[4]>1):# si on en traite plusieurs / nbr_corpus
        for i in range(0,param[4]): #nbr_corpus
            text_init=text_init + lecture_traitement(param[6][i])
            
            if param[0]:#si on separe les textes entre eux/ sep_corpus
                for i in range(0,param[2]):
                    text_init = text_init+" scpmeansecurecontainprotect "

    else:#si on traite 1 corpus
        text_init=text_init + lecture_traitement(param[6])
    #

    
    text_tr1=only_caracter(text_init)
    liste_mots=text_tr1.split()

    #on cree le dico
    dico_mot_init=liste_occurrences(liste_mots)
    dico_tr_1=reduction_occurence_unique(dico_mot_init)
    if param[0]:#sep_corpus
        del dico_tr_1["scpmeansecurecontainprotect"]
    dico_tr2=tri_dico(dico_tr_1,True)    
    dico_f=reduction_occurence(dico_tr2,param[1])#redu_ocu
    dico_f2=tri_dico(dico_f,False)
    return [dico_f2,liste_mots]



# liliste des elements a sauvegarder : liste_mots dans un fichier et un mot par ligne et dico_f dans un autre fichier
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





def compute_dict(dico):
    """
    compute_dict renvoie un nouveau dictionnaire (res) 
    res associe a chaque cle du dictionnaire d'origine (dico) un numero d'index
    """
    res = dict()
    j=0
    for i in dico:
        res[i]=j
        j=j+1
    return res



def compute_matrix(d_index, k, l_mots):
    matrix =  np.zeros((len(d_index),len(d_index)),dtype = int)
    nb_mot = len(l_mots)
    """
    add (k+2)*"SCPmeansecurecontainprotect" at the begining and end of l_mot pour ne pas avoir a faire de cas special pour les extremites de la liste des mots
    """
    filler = []
    for i in range(k):
        filler.append("SCPmeansecurecontainprotect")

    #l_mots.insert(0,filler)
    #l_mots.append(filler)
    l_mots = filler + l_mots + filler
    index = k
    for i in l_mots[k:-k]:                      #it should work, I think, I really really  hope it work 
        index=index-k
        if (i == "SCPmeansecurecontainprotect") or (i =="scpmeansecurecontainprotect") or (not(i in d_index)) :
            index = index+k+1
            continue

        for j in range(index,1+index+2*k):      #pourquoi il y a des boucles dans des boucles, pourquoi le code ne peut pas etre simple?
            if j == (index+k) :                  #on saute le mot qu'on analyse
                continue
            #check existence l_mots[j] dans d_index
            if not ( l_mots[j] in d_index ) :      #on saute si il n'est pas dans d_index
                continue
            #on rajoute le mot dans la matrice d'occurence
            matrix[ d_index[i] , d_index[ l_mots[j] ] ] =  matrix[ d_index[i] , d_index[ l_mots[j] ] ] +1
        
           
        index = index+k+1
    
    return ((matrix/nb_mot).astype(np.float32)) #some



"""
    parametre initialise dans la fonction init
    le #nombre represente l'indice dans la liste control
    sep_corpus = False #0
    redu_ocu = 100 #1
    k_voisin = 3 #2
    filler_liste = " FF " * k_voisin #3
    nbr_corpus = 1 #4
    compress = True #5
    nom des corpus #6

"""
 
def main():
    control = init(1)#initialise tous les parametres
    print("param in main= ")
    print(control)


    if not control[5]:#si non comprime en un bloc de text
        if not (control[4]==1):#si il y a plus d'1 corpus
            #do something
            return 0
    dataSet1 = parser(control) 
    #mettre une demande pour verifier si on sauvegarde dans init_custom
    if True:
        save_parsed_data(dataSet1,control[7])# control[7] aucune idee de comment le definir, c'est un nom pour les fichiers


    #est ce que on lit a partir d'un fichier ou est ce que on a deja la liste de mot et le dico en memoire
    if True:
        temp=compute_dict(dataSet1[0])
        dataSet1[0].clear
        dataSet1[0]=temp.copy()
    else:
        dataSet1= read_saved_data(control[7])# mettre cette ligne de code après le print(control) dans un if False; fonctionnalite non devellope


    #calcule la matrice
    matrix_result = compute_matrix(dataSet1[0], control[2], dataSet1[1])
    print(matrix_result)

    sys.exit()
    return 0


    


main()
#print("rfe")
#save_parsed_data(parser("hayku.txt"),"hayku")
#data = read_saved_data("hayku")
#print(compute_matrix(data[0],3,data[1]))
#transformer en matrice à trous
