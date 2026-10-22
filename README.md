# Jeu de Serpent — Python / Tkinter

Un jeu de serpent simple développé avec Python et Tkinter lorsque j'apprenais les bases de la programmation Python.

Ce mini projet fait partie de mes premières réalisations en programmation. Il reprend le principe du jeu classique Snake, dans lequel le joueur contrôle un serpent, récupère de la nourriture et tente d'obtenir le meilleur score possible sans heurter les murs ni son propre corps.

## Fonctionnalités

- Déplacement du serpent à l'aide des quatre flèches du clavier.
- Collecte de nourriture pour augmenter le score.
- Détection des collisions avec les murs.
- Détection des collisions avec le corps du serpent.
- Affichage du score en temps réel.
- Interface graphique simple réalisée avec Tkinter.

## Technologies utilisées

- **Python :** logique du jeu et programmation orientée objet.
- **Tkinter :** création de l'interface graphique.
- **Random :** génération aléatoire de la position de la nourriture.

## Prérequis

- Python 3.x
- Tkinter, généralement inclus dans les installations standard de Python.

## Installation et lancement

Cloner le dépôt :

```bash
git clone https://github.com/AdoumOMT/Snake-Game.git
```

Accéder au dossier du projet :

```bash
cd Snake-Game
```

Lancer le jeu :

```bash
python serpant.py
```

Selon le système utilisé, il peut être nécessaire d'exécuter :

```bash
python3 serpant.py
```

## Commandes du jeu

| Touche | Action |
| --- | --- |
| ↑ | Déplacer le serpent vers le haut |
| ↓ | Déplacer le serpent vers le bas |
| ← | Déplacer le serpent vers la gauche |
| → | Déplacer le serpent vers la droite |

## Notions mises en pratique

Ce projet m'a permis de découvrir et de pratiquer plusieurs notions fondamentales de Python :

- Les classes et les objets.
- Les listes, les tuples et les conditions.
- La gestion des événements clavier.
- La logique d'un jeu et la détection des collisions.
- La création d'interfaces graphiques avec Tkinter.
- La planification d'actions répétitives avec la méthode `after()`.

## Améliorations envisagées

Plusieurs évolutions pourront être apportées dans de futures versions :

- Empêcher le serpent de faire demi-tour directement sur lui-même.
- Éviter que la nourriture apparaisse sur le corps du serpent.
- Ajouter un écran de fin de partie et une option de redémarrage.
- Améliorer l'interface graphique et l'affichage du score.
- Ajouter plusieurs niveaux de difficulté.

## État du projet

**Version 1.0 — Projet d'apprentissage initial**

Cette version conserve le code original réalisé lors de mon apprentissage de Python. Des améliorations pourront être apportées progressivement afin d'enrichir les fonctionnalités du jeu et de mettre en pratique de nouvelles notions de programmation.

## Auteur

Adoum Oumar Moussa Tahir — Étudiant en informatique — systèmes intelligents et recherche opérationnelle.

GitHub : `https://github.com/AdoumOMT`