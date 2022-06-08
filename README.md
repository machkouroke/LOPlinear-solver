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
2 2  -- Dimensions du systèmes
1 1 6 -- Lignes des coefficients du systèmes
-3 1 2
```
- Executer le script avec comme paramètre nommé **--infile** le chemin vers le fichier contenant l'éqaution à résoudre et **--outfile** le nom du chemin du fichier ou écrire les résultats (Il seras crée s'il n'existe pas) (Le chemin par défaut que le script prend en compte pour les noms de fichier est celui du dossier input)
```
python solver.py --infile in.txt --outfile out.txt
Start solving the equation
x: 0
y: 1
L1<-L1 +((3-0j)) * L0
x: 1
Rang: 2
The solution is [[1.0], [5.0]]
Saved to out.txt
```



