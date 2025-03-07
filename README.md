# PythonApplication1

membre du binôme:
-Rémi Debavelaere
-Gabriel Colomer

Le code nécessite python 3.10 et numpy
pour lancer le code avec python 3.9, il suffit de retirer l'instruction match dans la fonction init et de retirer toute la fonction init_custo

En théorie il suffit de lancer l'application PythonApplication1.py pour que tout le code s'exécute, sinon la fonction à exécuter pour lancer le programme est la fonction main

Le paramètre 0 dans control = init(0) (1er ligne de la fonction main) nécessite d'avoir les quatre fichiers textes (movies_text.txt,soap_text.txt,tv_text.txt,wiki_text.txt) dans le même dossier que l'application
Mettre 1 comme paramètre dans control = init(1) permet de contrôler les paramètres lors de l'exécution sans avoir à modifier le code (nécessite python 3.10)


On a décider de rajouter, au début et à la fin de la liste des mots, k fois un mot qui n'est pas pris en compte pour la création de la matrice de co-occurences.
Cette décision à été faite pour ne pas avoir à faire un cas spécial pour les mots au débuts et à la fin du corpus: le premier et dernier mots du corpus qu'on analyse ont k fois un mot qu'on ignore avant et après, respectivement.
SCPmeansecurecontainprotect a été utilisé comme mots afin d'être sûr qu'il n'existe pas dans le corpus de texte, et donc qu'aucune donnée ne soit perdu parce que on ignore ce mots


La condition if os.path.exists("03" + control[7] + "repertoire.txt") permet d'éviter de refaire le traitement du texte puisque normalement le résultat du traitement du texte à été sauvegardé dans des fichiers. 
control[7] est un string qui agit comme un identifiant pour la combinaison de paramètre qu'on demande.
Par exemple je lance le programme avec control = init(0), cela va créer un fichier 03defaultrepertoire.txt. 
Maintenant si je lance le programme(en modifiant le code) avec  control = init(1), et que je demande au programme d'analyser un seul fichier et que le nom de la matrice est default,
Le programme va assigner la valeur default dans control[7] et va utiliser les données qui ont été crées lors de la première utilisation du programme.
C'est une conséquence non prévu de vouloir réutiliser les données qui ont déjà été traité si elles existent déjà.

