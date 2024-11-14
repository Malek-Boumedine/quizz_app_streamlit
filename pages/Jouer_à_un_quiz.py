import streamlit as st
from classes import Theme
import json


# --------------------------------------------------------------------------------------------------------

# page qui permet de jouer à un quiz
st.title("Jouer à un Quiz")

# récupérer la liste des thèmes
chemin = "./themes"
liste_themes = Theme.choix_themes_jouer(chemin)

# --------------------------------------------------------------------------------------------------------

# Initialisation des états
if 'desactiver_choix' not in st.session_state:
    st.session_state.desactiver_choix = False
    
if 'desactiver_valider' not in st.session_state:
    st.session_state.desactiver_valider = False
    
if 'demarrer' not in st.session_state:
    st.session_state.demarrer = False

if 'desactiver_demarrer' not in st.session_state:
    st.session_state.desactiver_demarrer = False

if 'nombre_questions' not in st.session_state:
    st.session_state.nombre_questions = 0

if 'index_question' not in st.session_state:
    st.session_state.index_question = 0
    
if 'score' not in st.session_state:
    st.session_state.score = 0
    
if 'afficher_score_final' not in st.session_state:
    st.session_state.afficher_score_final = False

# --------------------------------------------------------------------------------------------------------
    
# afficher la liste de themes dans une liste déroulante
choix_theme = st.selectbox(label="Choisissez un thème :", options=liste_themes, disabled=st.session_state.desactiver_choix)

# Bouton pour valider le choix et désactiver la liste des thèmes
valider = st.button("Validez votre choix", disabled=st.session_state.desactiver_valider)
      
if valider :
    st.session_state.desactiver_choix = True
    st.write(f"Vous avez choisi le thème : {choix_theme}")
    
    # ouvrir le fichier correspondant au thème choisi
    with open(f"./themes/{choix_theme}.json", "r") as json_file :
        donnees = json.load(json_file)
        st.session_state.questions = donnees["questions"]
        st.session_state.nombre_questions = len(donnees["questions"])
        

# --------------------------------------------------------------------------------------------------------

# Bouton pour démarrer le questionnaire
if st.session_state.desactiver_choix :
    demarrer = st.button("Démarrer le questionnaire", disabled = st.session_state.desactiver_demarrer)
    if demarrer:
        st.session_state.demarrer = True
        st.session_state.desactiver_valider = True
        st.session_state.desactiver_demarrer = True
        st.rerun()

# --------------------------------------------------------------------------------------------------------

# Afficher les questions si le questionnaire est démarré
if st.session_state.demarrer :
    st.title(f"\nThème du quizz : {choix_theme}\n")
    
      # Si on doit afficher le score final
    if st.session_state.afficher_score_final:
        st.write(f"Votre score final  :  {st.session_state.score}/{st.session_state.nombre_questions}")
        if st.button("Retour au choix du thème"):
            # Réinitialiser tous les états
            st.session_state.desactiver_choix = False
            st.session_state.desactiver_demarrer = False
            st.session_state.desactiver_valider = False
            st.session_state.index_question = 0
            st.session_state.score = 0
            st.session_state.demarrer = False
            st.session_state.afficher_score_final = False
            st.rerun()
    else :
        # Bouton question suivante et quitter
        question_suivante_b, quitter_b = st.columns([3,1])

    
        # Vérifier si on n'est pas à la dernière question
        if st.session_state.index_question < len(st.session_state.questions) - 1:
            question_suivante = question_suivante_b.button("Question suivante")
            if question_suivante:
                st.session_state.index_question += 1
                st.rerun()
            # boutons quitter :
            quitter = quitter_b.button("quitter le thème")
            if quitter : 
                st.session_state.desactiver_choix = False
                st.session_state.desactiver_demarrer = False
                st.session_state.desactiver_valider = False
                st.session_state.index_question = 0
                st.session_state.score = 0
                st.session_state.demarrer = False  
                st.rerun()
        else:
            st.write("C'est la dernière question !")
            terminer = st.button("TERMINER")
            if terminer :

                st.session_state.afficher_score_final = True
                st.rerun()

        # Afficher la question courante
        q = st.session_state.questions[st.session_state.index_question]
        
        st.markdown(f"<p style='font-size: 20px;'>Question {q['numero']}/{st.session_state.nombre_questions} :</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 20px;'>{q['enonce']} </p>", unsafe_allow_html=True)
        reponse = st.radio("Selectionnez une réponse : ", q["reponses"], key=f"q_{st.session_state.index_question}")
        if reponse == q["bonne_reponse"]:
            st.session_state.score += 1

# --------------------------------------------------------------------------------------------------------

