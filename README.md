# recherche_lineaire_vs_dichotomique
recherche dichotomique versus séquentielle
# TP Python — Recherche séquentielle vs recherche dichotomique

Projet réalisé par **Yanis KHELIF**.

Ce projet illustre et compare deux algorithmes classiques de recherche dans un tableau :
- la **recherche séquentielle**
- la **recherche dichotomique** (ou recherche binaire)

Il met en évidence leurs différences de **performance** à l’aide de mesures de temps d’exécution et d’un graphique comparatif.

---

## 📁 Fichier du projet

- `RechercheDico_yk.py`  
  Script Python contenant :
  - l’implémentation des deux méthodes de recherche
  - des tests simples de validation
  - une comparaison expérimentale des temps d’exécution
  - un affichage graphique des performances

---

## 🎯 Objectifs pédagogiques

- Comprendre le fonctionnement :
  - de la **recherche séquentielle**
  - de la **recherche dichotomique**
- Mettre en évidence l’impact de la **taille du tableau** sur le temps d’exécution
- Comprendre pourquoi la recherche dichotomique est plus efficace sur un tableau **trié**
- Introduire la notion de **complexité algorithmique** (O(n) vs O(log n))

---

## 🧠 Algorithmes implémentés

### 🔹 Recherche dichotomique
```python
recherche_dt(tab, element)
