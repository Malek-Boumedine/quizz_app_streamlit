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
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DOSSIER>
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
