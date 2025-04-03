# **Projet : Implémentation et Visualisation des Algorithmes de Tri**

## **Introduction**

La gestion efficace des données est un défi récurrent en informatique. L’objectif de ce projet est d’implémenter plusieurs algorithmes de tri, d’analyser leur performance et de les visualiser pour mieux comprendre leur fonctionnement.

Nous allons aider Héron d’Alexandrie à organiser les papyrus de la bibliothèque en utilisant différents algorithmes de tri et en comparant leur rapidité.

---

## **Qu'est-ce qu'un algorithme performant ?**

Un algorithme performant est un algorithme qui exécute une tâche donnée avec un temps d'exécution optimal et une consommation de ressources minimale. Les critères d’évaluation incluent :

- **Complexité en temps** : mesure du nombre d'opérations nécessaires en fonction de la taille des données (notation Big-O).
- **Complexité en espace** : quantité de mémoire utilisée.
- **Stabilité** : conservation de l'ordre relatif des éléments égaux.
- **Adaptabilité** : efficacité selon l’ordre initial des données.

Un bon algorithme de tri doit être rapide sur de grandes entrées et utiliser une quantité raisonnable de mémoire.

---

## **Méthode de calcul de la complexité**

La complexité algorithmique est souvent exprimée en notation **Big-O**. Pour déterminer cette complexité, on analyse :

1. **Les boucles** : Un algorithme avec une boucle unique effectuant `n` opérations a une complexité **O(n)**. Si une boucle est imbriquée dans une autre, la complexité devient **O(n²)**.
2. **Les récursions** : Un algorithme divisé en sous-problèmes de taille réduite suit souvent une complexité logarithmique **O(n log n)**.
3. **Les accès mémoire** : L'utilisation d'espace supplémentaire peut affecter l'efficacité d'un algorithme.

Exemple : Le tri rapide divise les données en sous-listes à chaque appel récursif, réduisant ainsi le problème d'un facteur de moitié à chaque étape, ce qui donne une complexité **O(n log n)**.

---

## **Algorithmes de tri implémentés**

### **1. Tri par sélection (Selection Sort)**

####  **Étapes**

1. Parcourir la liste pour trouver le plus petit élément.
2. Échanger cet élément avec celui de la première position non triée.
3. Répéter jusqu’à ce que toute la liste soit triée.

####  **Complexité** : O(n²)

---

### **2. Tri à bulles (Bubble Sort)**

####  **Étapes**

1. Comparer chaque élément avec son voisin de droite.
2. Échanger si nécessaire.
3. Répéter jusqu’à ce qu’aucun échange ne soit nécessaire.

####  **Complexité** : O(n²)

---

### **3. Tri par insertion (Insertion Sort)**

####  **Étapes**

1. Prendre chaque élément et l'insérer au bon endroit.
2. Répéter jusqu’à ce que toute la liste soit triée.

####  **Complexité** : O(n²)

---

### **4. Tri fusion (Merge Sort)**

####  **Étapes**

1. Diviser la liste en deux jusqu'à obtenir des sous-listes d’un élément.
2. Fusionner les sous-listes triées.

####  **Complexité** : O(n log n)

---

### **5. Tri rapide (Quick Sort)**

####  **Étapes**

1. Choisir un pivot.
2. Placer les éléments plus petits à gauche et plus grands à droite.
3. Appliquer récursivement le tri rapide sur les sous-listes.

####  **Complexité** : O(n log n)

---

### **6. Tri par tas (Heap Sort)**

####  **Étapes**

1. Construire un tas max.
2. Extraire le maximum et reconstruire le tas.
3. Répéter jusqu’à obtention d’une liste triée.

####  **Complexité** : O(n log n)

---

### **7. Tri à peigne (Comb Sort)**

####  **Étapes**

1. Définir un écart initial.
2. Comparer et échanger les éléments espacés de cet écart.
3. Réduire l’écart et répéter jusqu’à convergence vers un tri à bulles.

####  **Complexité** : O(n log n)

---

## **Installation et Exécution**

```bash
git clone https://github.com/votre-repository/sorting-visualizer.git
cd sorting-visualizer
pip install -r requirements.txt
python main.py
```

---

## **Conclusion**

Ce projet permet d’explorer les algorithmes de tri, de comparer leur efficacité et de les visualiser.

###  **Prochaine étape** : Tester sur des jeux de données réels et améliorer la visualisation !

