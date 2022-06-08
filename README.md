LOPLinear-Solver
============

Script python permettant de résoudre des systèmes linéaires 



## Caractéristique
- Résouds des équations linéaires comples
- Affiche les étapes de la résolutions des équations
- Enrégistre les résultat dans un script


## Utilisation
- Ecrire votre système dans un fichier (de préférence dans le dossier input). Ce fichier réprésente le système comme suit
```
4 4 -- Dimensions du systèmes 
2 2 -1 1 4 --Ligne du systèmes
4 3 -1 2 6
8 5 3 4 12
3 3 -2 2 6
```
- Executer le script avec comme paramètre nommé **--infile** le chemin vers le fichier contenant l'éqaution à résoudre et **--outfile** le nom du chemin du fichier ou écrire les résultats (Il seras crée s'il n'existe pas) (Le chemin par défaut que le script prend en compte pour les noms de fichier est celui du dossier input)
```
python solver.py --infile in.txt --outfile out.txt
Start solving the equation
L1<-L1 +((-4-0j)) * L0
L2<-L2 +((-8-0j)) * L0
L3<-L3 +((-3-0j)) * L0
L2<-L2 +((3-0j)) * L1
L3<-L3 +((-0-0j)) * L1
L3<-L3 +((0.5-0j)) * L2
Rang: 4
The solution is [[-0.5], [2.5], [0.5], [0.5]]
Saved to out.txt
```



