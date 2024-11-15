# Projet Quiz Personnalisable

## Description
Ce projet est une application de quiz personnalisable développée avec Streamlit. Elle permet aux utilisateurs de créer, gérer et jouer à des quiz interactifs. L'application met en avant les fonctionnalités de Streamlit pour offrir une expérience d'apprentissage engageante et intuitive.

## Fonctionnalités
- **Création de Quiz Personnalisés** : Les utilisateurs peuvent créer des quiz en ajoutant des questions et des réponses adaptées à leurs besoins.
- **Interface Utilisateur Conviviale** : L'application est conçue pour être intuitive et facile à utiliser.
- **Interactivité et Engagement** : Les utilisateurs peuvent interagir avec le contenu de manière dynamique.
- **Feedback Instantané** : Les participants reçoivent des retours immédiats sur leurs réponses.
- **Gestion des Thèmes** : Les utilisateurs peuvent ajouter, supprimer et choisir des thèmes pour leurs quiz.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Malek-Boumedine/quizz_app_streamlit
   cd quizz_app_streamlit
   ```
2. Installez les dépendances :
   ```bash
   pip install streamlit pydantic
   ```

## Utilisation
1. Lancez l'application :
   ```bash
   streamlit run accueil.py
   ```
2. Suivez les instructions à l'écran pour créer un quiz, ajouter des questions et jouer à un quiz.

## Structure des Fichiers
- `accueil.py` : Page d'accueil de l'application.
- `classes.py` : Définitions des classes pour gérer les questions et les thèmes.
- `creer_un_quizz.py` : Interface pour créer des quiz.
- `jouer_a_un_quiz.py` : Interface pour jouer à un quiz.

## Réponses aux questions :

### 1. Quelle est la limite d'utiliser un fichier plat dans l'application ?

   L'utilisation d'un fichier plat (comme JSON ou CSV) pour stocker des données présente plusieurs limites, notamment :

   - Scalabilité : Les fichiers plats peuvent devenir difficiles à gérer et à manipuler lorsque le volume de données augmente, entraînant des temps de chargement plus longs et des performances réduites.
   - Concurrence : Les fichiers plats ne gèrent pas bien les accès simultanés, ce qui peut entraîner des conflits ou des corruptions de données si plusieurs utilisateurs tentent de modifier le fichier en même temps.
   - Recherche et filtrage : Les opérations de recherche et de filtrage dans un fichier plat sont moins efficaces par rapport à une base de données, ce qui peut ralentir les performances de l'application.

### 2. Quelle serait la prochaine étape pour scaler l'application ?

   Pour scaler l'application, la prochaine étape serait de migrer vers une base de données relationnelle (comme MySQL) ou NoSQL (comme MongoDB). Cela permettrait de :

   - Gérer des volumes de données plus importants de manière efficace.
   - Faciliter les opérations de lecture et d'écriture avec des performances optimisées.
   - Assurer la gestion des transactions et la concurrence, permettant à plusieurs utilisateurs d'interagir avec les données sans conflits.
   - Améliorer la structure des données et la possibilité d'effectuer des requêtes complexes.

