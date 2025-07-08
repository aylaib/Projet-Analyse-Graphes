\# Implémentation et Analyse de Complexité d'Algorithmes sur les Graphes



Ce projet a été réalisé dans le cadre du module "Algorithmique Avancée et Complexité" pour le Master 1 en Bio-Informatique à l'USTHB (Année 2023/2024).



Il s'agit d'une implémentation en Python d'opérations fondamentales sur les graphes, accompagnée d'une analyse de leur complexité. Le projet explore les deux représentations principales des graphes (matrice d'adjacence et liste d'adjacence) et compare leurs performances.



\## 📜 Description



Le programme `graph\_analyzer.py` offre une interface en ligne de commande pour :

\- Construire des graphes, orientés ou non.

\- Afficher graphiquement les structures créées.

\- Exécuter une série d'analyses algorithmiques sur le graphe courant.



\## ✨ Fonctionnalités



Le programme implémente les opérations suivantes :



\- \*\*Création et Affichage :\*\*

&nbsp; - Construction de graphes orientés et non orientés.

&nbsp; - Visualisation graphique à l'aide de `matplotlib`.



\- \*\*Analyse de Propriétés :\*\*

&nbsp; - Calcul de la \*\*densité\*\* du graphe.

&nbsp; - Calcul des \*\*degrés\*\* (degré simple, entrant et sortant).

&nbsp; - Vérification si un graphe est \*\*Eulérien\*\*.

&nbsp; - Vérification si un graphe est \*\*Complet\*\*.

&nbsp; - Vérification si un graphe est un \*\*Arbre\*\*.



\- \*\*Algorithmes de Parcours et de Recherche :\*\*

&nbsp; - Recherche de \*\*tous les chemins simples\*\* entre deux nœuds.

&nbsp; - Recherche du \*\*chemin le plus court\*\* entre deux nœuds (basé sur le nombre d'arêtes).

&nbsp; - Identification de tous les \*\*cycles\*\* dans un graphe orienté.



\## 🛠️ Prérequis



\- Python 3.6 ou supérieur

\- Les bibliothèques listées dans `requirements.txt`



\## 🚀 Comment l'exécuter



1\.  \*\*Clonez le dépôt (ou téléchargez les fichiers) :\*\*

&nbsp;   ```bash

&nbsp;   git clone https://github.com/VOTRE\_NOM\_UTILISATEUR/Projet-Analyse-Graphes.git

&nbsp;   cd Projet-Analyse-Graphes

&nbsp;   ```



2\.  \*\*Installez les dépendances :\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



3\.  \*\*Lancez le programme :\*\*

&nbsp;   ```bash

&nbsp;   python graph\_analyzer.py

&nbsp;   ```



4\.  Suivez les instructions du menu pour interagir avec le programme.



\## 📊 Documents de Référence



\- \[Rapport du Projet](./rapport\_projet.pdf) : Contient l'analyse théorique, les tableaux de complexité et l'évaluation expérimentale.

\- \[Énoncé du Devoir](./enonce\_devoir.pdf) : Le sujet original du projet.



