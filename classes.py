import time
import json
import os
import streamlit as st
from pydantic import BaseModel, Field, constr
from typing import List, Optional



#############################################################################################################

# Modèle pour la structure d'une question

class Question(BaseModel):
    """
    Représente une question avec ses détails et fournit une méthode pour l'ajouter à une liste.

    Cette classe encapsule les propriétés d'une question, y compris son numéro, son énoncé, ses réponses possibles 
    et la bonne réponse. Elle inclut également une méthode pour ajouter la question à une liste de questions fournie.

    Attributs:
        numero (int): L'identifiant unique de la question.
        enonce (str): L'énoncé de la question, doit comporter au moins un caractère.
        reponses (List[str]): Une liste de réponses possibles, doit contenir au moins deux éléments.
        bonne_reponse (str): La bonne réponse parmi la liste des réponses possibles.

    Méthodes:
        ajouter_question(liste_question): Ajoute les détails de la question à la liste de questions fournie.

    """
    numero: int
    enonce: constr(min_length=1)
    reponses: List[str] = Field(min_items=2)
    bonne_reponse: str

    def ajouter_question(self, liste_question: List[dict]) -> List[dict]:
        """
        Ajoute les détails de la question actuelle à la liste de questions spécifiée.

        Cette méthode crée une représentation sous forme de dictionnaire de la question et l'ajoute à la liste fournie.

        Args:
            liste_question (List[dict]): La liste à laquelle la question sera ajoutée.

        Returns:
            List[dict]: La liste mise à jour des questions incluant la question nouvellement ajoutée.
        """
        question = {
            "numero": self.numero,
            "enonce": self.enonce,
            "reponses": self.reponses,
            "bonne_reponse": self.bonne_reponse
        }
        liste_question.append(question)
        return liste_question    



#############################################################################################################

class Theme(BaseModel) : 
    """Représente un thème contenant des questions et fournit des méthodes pour gérer les thèmes.

    Cette classe encapsule les détails d'un thème, y compris son nom, la durée requise et une liste de questions. 
    Elle offre des méthodes statiques pour créer, supprimer et lister des fichiers de thèmes, ainsi qu'une méthode 
    pour écrire les questions dans un fichier JSON.

    Attributs:
        nom_theme (str): Le nom du thème, doit comporter au moins un caractère.
        duree_requise (Optional[int]): La durée requise pour le thème, peut être None.
        questions (List[Question]): Une liste de questions, doit contenir au moins une question.

    Méthodes:
        creer_fichier_theme(nom): Crée un fichier JSON pour le thème spécifié.
        supprimer_theme(nom): Supprime le fichier JSON du thème spécifié.
        ecrire_questions(liste_questions): Écrit les questions du thème dans un fichier JSON.
        liste_themes(chemin): Renvoie une liste des noms de thèmes disponibles dans le chemin spécifié.
        choix_themes_jouer(chemin): Renvoie une liste des noms de thèmes disponibles pour jouer dans le chemin spécifié.
    """
    nom_theme: constr(min_length=1)
    duree_requise: Optional[int] = None
    questions: List[Question] = Field(min_items=1)  # au moins une question

    @staticmethod
    def creer_fichier_theme(nom: str) -> None : 
        """Crée un fichier JSON pour le thème spécifié.

        Cette méthode crée un fichier vide avec le nom du thème dans le répertoire des thèmes.

        Args:
            nom (str): Le nom du thème pour lequel le fichier sera créé.
        """
        with open(f"./themes/{nom}.json", "w") as f:
            pass


    @staticmethod
    def supprimer_theme(nom: str) -> None:
        """Supprime le fichier JSON du thème spécifié.

        Cette méthode vérifie si le fichier existe et le supprime s'il est présent.

        Args:
            nom (str): Le nom du thème dont le fichier sera supprimé.
        """
        chemin_fichier = f"./themes/{nom}.json"
        if os.path.exists(chemin_fichier):
            os.remove(chemin_fichier)
        
        
    def ecrire_questions(self, liste_questions : List[dict]) -> None :
        """Écrit les questions du thème dans un fichier JSON.

        Cette méthode crée un dictionnaire représentant le thème et l'écrit dans un fichier JSON.

        Args:
            liste_questions (List[dict]): La liste des questions à écrire dans le fichier.
        """
        theme = {
            "nom_theme" : self.nom_theme, 
            "duree_requise" : self.duree_requise, 
            "questions" : liste_questions
        }
        
        with open(f"./themes/{self.nom_theme}.json", "w", encoding='utf-8') as f:
            json.dump(theme, f, ensure_ascii=False, indent=4)
    
    
    @staticmethod
    def liste_themes(chemin : str) -> list : 
        """Renvoie une liste des noms de thèmes disponibles dans le chemin spécifié.

        Cette méthode parcourt le répertoire donné et extrait les noms des fichiers JSON.

        Args:
            chemin (str): Le chemin du répertoire contenant les fichiers de thèmes.

        Returns:
            list: Une liste des noms de thèmes.
        """
        liste_themes = []
        themes = os.listdir(chemin)
        for t in themes : 
            nom_split = t.split(".")
            if nom_split[-1].lower() == "json" : 
                nom = nom_split[0]
            liste_themes.append(nom)
        liste_themes.append("ajouter un thème")
        return liste_themes
    
    
    @staticmethod
    def choix_themes_jouer(chemin : str) -> list : 
        """Renvoie une liste des noms de thèmes disponibles pour jouer dans le chemin spécifié.

        Cette méthode parcourt le répertoire donné et extrait les noms des fichiers JSON.

        Args:
            chemin (str): Le chemin du répertoire contenant les fichiers de thèmes.

        Returns:
            list: Une liste des noms de thèmes.
        """
        liste_themes = []
        themes = os.listdir(chemin)
        for t in themes : 
            nom_split = t.split(".")
            if nom_split[-1].lower() == "json" : 
                nom = nom_split[0]
            liste_themes.append(nom)
        return liste_themes



#############################################################################################################

class Minuteur:
    """Représente un minuteur pour gérer le temps.

    Cette classe est conçue pour fournir des fonctionnalités de minuteur, permettant de suivre le temps écoulé 
    et de gérer des événements basés sur le temps. Les détails de son implémentation et de ses méthodes 
    seront définis ultérieurement.
    """
    pass


#############################################################################################################