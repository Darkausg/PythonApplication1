t=open("tiny.txt","r").read()

def lecture_traitement(f):
    l=open(f,"r").read()
    return l.lower()
    
ti=open("tiny.txt","r").read().lower()

def only_caracter(ori_text):
    letter ="azertyuiopqsdfghjklmwxcvbn"
    text_treated = ""
    for i in ori_text:
        if i in letter:
            text_treated = text_treated + i
        else:
            text_treated = text_treated + " "
    return text_treated

tin=only_caracter(open("tiny.txt","r").read().lower())

def spliter(f):
    return f.split()
    

tiny=spliter(tin)

def liste_occurrences(l):
    res=dict()
    print(l)
    print("l")
    for i in l:
        if not i in res:
            res[i]=1
        else:
            res[i]+=1
    return res

tinyy=liste_occurrences(tiny)

def reduction_occurence_unique(d):
    res=dict()
    for i in d:
        if not d[i]==1:
            res[i]=d[i]
    return res

tinyyy=reduction_occurence_unique(tinyy)

def tri_dico(d):
    dico_trié = dict(sorted(d.items(), key=lambda item: item[1]))
    "tiré de : https://www.datacamp.com/fr/tutorial/sort-a-dictionary-by-value-python"
    return dico_trié

def reduction_occurence(d,t):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    for i in range(t):
        d.popitem()
    return d
    
    


            
l=[["baa",4],["a",1],["baba",2],["bba",3]]    
 
    


    
    
    


