f=open("tiny.txt","r").read()

def lecture_traitement(f):
    pass
    

def only_caracter(ori_text):
    letter ="azertyuiopqsdfghjklmwxcvbn"
    text_treated = ""
    for i in ori_text:
        if i in letter:
            text_treated = text_treated + i
        else:
            text_treated = text_treated + " "
    return text_treated

only_caracter(f)


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


def parser(f):
    ori_text = lecture_traitement(f)
    text_treated = only_caracter(ori_text)
    text_treated.split()
    print(text_treated)
    occurence = liste_occurrences(text_treated)
    print(occurence)

  

            
            
        
        
    


    
    
    


