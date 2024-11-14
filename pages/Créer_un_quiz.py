import streamlit as st
import pydantic
from classes import Theme, Question


# titre de la page
st.title("Création du quiz")

# récupérer la liste des thèmes
chemin = "./themes"
liste_themes = Theme.liste_themes(chemin)

# afficher la liste de themes dans une liste déroulante
choix_theme = st.selectbox(label="Choisissez un thème :", options=liste_themes)

# --------------------------------------------------------------------------------------------------------

# supprimer un thème ou selectionner un thème et rafraichir la page
if "confirmation_suppression" not in st.session_state:
    st.session_state.confirmation_suppression = False
if "suppression_reussie" not in st.session_state:
    st.session_state.suppression_reussie = False
    
if choix_theme != "ajouter un thème": 
    # selectionner_theme = st.button("Sélectionner le thème")
    supprimer_theme = st.button("Supprimer le thème")
    # if selectionner_theme :
    #     st.session_state.liste_questions = []
    #     st.rerun()
        
    if supprimer_theme: 
        st.session_state.confirmation_suppression = True
        st.session_state.theme_a_supprimer = choix_theme
        st.rerun()

if st.session_state.confirmation_suppression:
    st.warning(f"Êtes-vous sûr de vouloir supprimer le thème '{st.session_state.theme_a_supprimer}' ?")
    col1, col2 = st.columns(2)
    with col1:
        confirmer_suppression = st.button("Oui")
    with col2:
        annuler_suppression = st.button("Non")

    if confirmer_suppression:
        Theme.supprimer_theme(st.session_state.theme_a_supprimer)
        st.session_state.suppression_reussie = True
        st.session_state.confirmation_suppression = False
        st.rerun()

    elif annuler_suppression:
        st.session_state.confirmation_suppression = False
        st.rerun()

if st.session_state.suppression_reussie:
    st.success(f"Le thème '{st.session_state.theme_a_supprimer}' a été supprimé avec succès.")
    st.session_state.suppression_reussie = False

# --------------------------------------------------------------------------------------------------------

# ajouter le thème s'il n'existe pas
if "theme_ajoute" not in st.session_state:
    st.session_state.theme_ajoute = False
    st.rerun()
    
if choix_theme == "ajouter un thème" : 
    nouveau_theme = st.text_input("## Veuillez saisir le nom du thème à ajouter : ").capitalize()
    ajout_theme = st.button("Ajouter thème")
    if ajout_theme : 
        if nouveau_theme :
            Theme.creer_fichier_theme(nouveau_theme)
            st.session_state.theme_ajoute = True
            st.session_state.nom_nouveau_theme = nouveau_theme
            st.rerun()
        else:
            st.error("Veuillez saisir un nom de thème valide.")
            
if st.session_state.get("theme_ajoute"):
    st.success(f"Le thème '{st.session_state.nom_nouveau_theme}' a été ajouté avec succès.")
    st.session_state.theme_ajoute = False

# --------------------------------------------------------------------------------------------------------

if "enonce" not in st.session_state:
    st.session_state.enonce = ""
if "reponses" not in st.session_state:
    st.session_state.reponses = ""

# saisir la question, la stocker dans une variable pour l'utiliser dans la classe Question
st.session_state.enonce = st.text_area("## Veuillez saisir votre question puis appuyez sur ENTREE pour valider : ", value=st.session_state.enonce, height=100)

# saisir les réponses, les enregistrer dans une liste pour les utiliser dans la classe Question
st.session_state.reponses = st.text_area("## Veuillez saisir vos réponses (une par ligne) puis appuyez CTRL + ENTREE pour valider : ", value=st.session_state.reponses, height=180)
liste_reponses = st.session_state.reponses.splitlines()

# Affichage de la valeur de bonne_reponse (une ou plusieurs vaeurs)
bonne_reponse = st.radio("Selectionnez votre bonne réponse : ", liste_reponses)
   
# --------------------------------------------------------------------------------------------------------

# creation d'une liste de questions et ajout des questions une par une
if 'liste_questions' not in st.session_state:
    st.session_state.liste_questions = []
if 'nb_questions' not in st.session_state:
    st.session_state.nb_questions = 0

# bouton pour ajouter une question et terminer :
ajouter_question, terminer = st.columns([6,1])

ajouter_question_btn = ajouter_question.button("Ajouter la question")
if ajouter_question_btn : 
    st.session_state.nb_questions  += 1
    question = Question(st.session_state.nb_questions, st.session_state.enonce, liste_reponses, bonne_reponse)
    question.ajouter_question(st.session_state.liste_questions)
    st.session_state.enonce = ""
    st.session_state.reponses = ""
    st.rerun()

duree_input = st.text_input("Saisissez la durée en secondes pour répondre à toutes les questions : ")

if len(st.session_state.liste_questions) > 0 :
    st.write("liste des questions : ", st.session_state.liste_questions)

# --------------------------------------------------------------------------------------------------------

# enregistrer le theme et ses questions dans le fichier correspondant

if 'questionnaire_cree' not in st.session_state:
    st.session_state.questionnaire_cree = False
  
terminer_b = terminer.button("Terminer")
if terminer_b : 
    duree = int(duree_input) if duree_input else None
    theme = Theme(choix_theme, duree, st.session_state.liste_questions)
    theme.ecrire_questions(st.session_state.liste_questions)
    st.session_state.liste_questions = []
    st.session_state.questionnaire_cree = True
    st.session_state.nb_questions = 0
    st.rerun()
    
if st.session_state.questionnaire_cree :
    st.write("questionnaire créée avec succés !")
    st.session_state.questionnaire_cree = False

# --------------------------------------------------------------------------------------------------------
