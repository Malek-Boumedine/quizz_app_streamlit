import time
import json
import os



#############################################################################################################

class Question :
    
    def __init__(self, numero : int, enonce : str, reponses : list[str], bonne_reponse : list[str]) -> None :
        self.__numero = numero
        self.__enonce = enonce
        self.reponses = reponses
        self.__bonne_reponse = bonne_reponse
        
        
    def creer_question(self, liste_question : list["Question"]) -> list["Question"]: 
        question = {
            "numero " : self.__numero, 
            "enonce" : self.__enonce,
            "reponses" : self.reponses,
            "bonne_reponse" : self.__bonne_reponse
        }
        liste_question.append(question)
        return liste_question



#############################################################################################################

class Theme : 
    
    def __init__(self, nom_theme : str, duree_requise : int, questions : list[Question]) -> None :
        self.__nom = nom_theme
        self.duree_requise = duree_requise
        self.questions = questions


    @staticmethod
    def creer_fichier_theme(nom : str) -> None : 
        with open(f"./themes/{nom}.json", "w") as f:
            pass


    @staticmethod
    def supprimer_theme(nom : str) -> None:
        chemin_fichier = f"./themes/{nom}.json"
        if os.path.exists(chemin_fichier):
            os.remove(chemin_fichier)
        else:
            pass
        
        
    def ecrire_questions(self, liste_question : list["Question"]) -> None :
        liste_question_obj_json = json.dumps(liste_question, indent = 4)
        theme = {
            "nom_theme" : self.__nom,
            "duree_requise" : self.duree_requise,
            "questions" : liste_question_obj_json
        }
        
        objet_json = json.dumps(theme, indent = 4)
        with open(f"{self.__nom}.json", "w") as f:
            json.dump(objet_json, f)
    
    
    @staticmethod
    def liste_themes(chemin) -> list : 
        liste_themes = []
        themes = os.listdir(chemin)
        for t in themes : 
            nom_split = t.split(".")
            if nom_split[-1].lower() == "json" : 
                nom = nom_split[0]
            liste_themes.append(nom)
        liste_themes.append("ajouter un thème")
        return liste_themes




#############################################################################################################

class Chronometre:
    
    """Une classe pour mesurer le temps écoulé.

    Cette classe permet de démarrer, d'arrêter et de récupérer le temps écoulé. 
    Elle offre également une méthode pour afficher le temps dans un format lisible.

    Attributs:
        temps_debut (float): Le temps de début du chronomètre.
        temps_fin (float): Le temps de fin du chronomètre.
        en_marche (bool): Indique si le chronomètre est actuellement en cours d'exécution.
    """

    def __init__(self):

        """Initialise le Chronometre avec des valeurs par défaut.

        Cette méthode définit les attributs de temps de début et de fin à zéro, 
        et initialise l'état d'exécution à False, indiquant que le chronomètre n'est pas en cours.

        Args:
        self: L'instance du Chronometre.
        """

        # Initialisation des attributs
        self.temps_debut = 0
        self.temps_fin = 0
        self.en_marche = False

    def demarrer(self):
    
        """Démarre le chronomètre.

        Cette méthode enregistre le temps de début si le chronomètre n'est pas déjà en cours d'exécution 
        et met à jour l'état d'exécution pour indiquer que le chronomètre est maintenant actif.

        Args:
        self: L'instance du Chronometre.
        """

        # Vérification si le chronomètre est déjà en marche
        if not self.en_marche:
            # Enregistrement du temps de début
            self.temps_debut = time.time()
            self.en_marche = True

    def arreter(self):
        
        """Arrête le chronomètre.

        Cette méthode enregistre le temps de fin si le chronomètre est en cours d'exécution 
        et met à jour l'état d'exécution pour indiquer que le chronomètre est arrêté.

        Args:
        self: L'instance du Chronometre.
        """

        # Vérification si le chronomètre est en marche
        if self.en_marche:
            # Enregistrement du temps de fin
            self.temps_fin = time.time()
            self.en_marche = False

    def obtenir_temps(self):
    
        """Récupère le temps écoulé depuis le démarrage du chronomètre.

        Cette méthode retourne le temps écoulé en secondes. Si le chronomètre est en cours d'exécution, 
        elle calcule le temps depuis le début, sinon elle calcule le temps total entre le début et la fin.

        Args:
        self: L'instance du Chronometre.

        Returns:
        float: Le temps écoulé en secondes.
        """

        # Calcul du temps écoulé
        if self.en_marche:
            return time.time() - self.temps_debut
        return self.temps_fin - self.temps_debut

    def afficher_temps(self):
        """Formate le temps écoulé en une chaîne lisible.

        Cette méthode calcule le temps écoulé en heures, minutes et secondes, 
        puis retourne une chaîne formatée pour une lecture facile au format HH:MM:SS.

        Args:
        self: L'instance du Chronometre.

        Returns:
        str: Le temps écoulé formaté en chaîne au format HH:MM:SS.
        """

        # Récupération du temps écoulé
        temps = self.obtenir_temps()
        heures = int(temps // 3600) # Calcul des heures
        minutes = int((temps % 3600) // 60) # Calcul des minutes
        secondes = int(temps % 60) # Calcul des secondes
        return f"{heures:02d}:{minutes:02d}:{secondes:02d}" # Formatage de la chaîne


#############################################################################################################

def refresh() : 
    __name__