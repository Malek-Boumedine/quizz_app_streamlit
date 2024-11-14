import streamlit as st
import json
import pydantic
import classes
from classes import Theme, Question


# titre de la page
st.title("Création du quiz")

# récupérer la liste des thèmes
chemin = "./themes"
liste_themes = Theme.liste_themes(chemin)

# afficher la liste de themes dans une liste déroulante
choix_theme = st.selectbox(label="Choisissez un thème :", options=liste_themes)

# supprimer un thème
if choix_theme != "ajouter un thème" : 
    supprimer_theme = st.button("Supprimer le thème")
    if supprimer_theme : 
        Theme.supprimer_theme(choix_theme)
        st.rerun()

# ajouter le thème s'il n'existe pas
if choix_theme == "ajouter un thème" : 
    nouveau_theme = st.text_input("## Veuillez saisir le nom du thème à ajouter : ").capitalize()
    ajout_theme = st.button("Ajouter thème")
    if ajout_theme : 
        if nouveau_theme :
            Theme.creer_fichier_theme(nouveau_theme)
            st.success(f"Le thème '{nouveau_theme}' a été ajouté avec succès.")
            # RAFRAICHIR LA PAGE ICI
            st.rerun()
        else:
            st.error("Veuillez saisir un nom de thème valide.")

# saisir de la question, la stocker dans une variable pour l'utiliser dans la classe Question
enonce = st.text_area("## Veuillez saisir votre question puis appuyez sur ENTREE pour valider : ", height=100)
st.write("votre saisie : ", enonce)

# saisir les réponses, les enregistrer dans une liste pour les utiliser dans la classe Question
reponses = st.text_area("## Veuillez saisir vos réponses (une par ligne) puis appuyez CTRL + ENTREE pour valider : ", height=180)
st.write("votre saisie : ", reponses)
liste_reponses = reponses.split()

# Initialisation de la liste bonne_reponse
bonne_reponse = []

# affichage de chaque reponse dans une checkbox, l'ajouter à la liste de bonnes réponses si elle est cochée
for r in liste_reponses:
  if st.checkbox(r):
      bonne_reponse.append(r)

# Affichage de la valeur de bonne_reponse (une ou plusieurs vaeurs)
if bonne_reponse:
    if len(bonne_reponse) == 1 : 
        st.write(f"La bonne réponse sélectionnée : \n- {bonne_reponse[0]}")
    else :
        st.write(f"Les bonnes réponses sélectionnées : ")
        for r in bonne_reponse : 
            st.write(f"- {r}")
else:
    st.write("Aucune bonne réponse n'a été sélectionnée.")
    
# creation d'une liste de questions et ajout des questions une par une
liste_questions = []
numero = 1

# bouton pour ajouter une question et terminer :
ajouter_question, terminer = st.columns([6,1])

ajouter_question_btn = ajouter_question.button("Ajouter la question")
if ajouter_question_btn : 
    liste_questions.append(Question(numero, enonce, liste_reponses, bonne_reponse))
    numero += 1
    st.rerun()
    print(liste_questions)

# enregistrer le theme et ses questions dans le fichier correspondant
terminer_b = terminer.button("Terminer")
if terminer_b : 
    liste_questions_json_onject = json.dumps(liste_questions, indent = 6)
    with open(choix_theme, "w", encoding="utf8") as json_file : 
        json.dump(json_file, liste_questions_json_onject, ensure_ascii=True)
    st.rerun()









