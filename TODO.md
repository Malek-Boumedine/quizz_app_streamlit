+++ TOUT EN ORIENTE OBJET +++

- Page de création de quiz : 

    - avoir la possibilité de choisir un thème depuis une liste déroulante, si le thème n'existe pas donner la possibilité de saisir le thème
        - ~~ dans la liste déroulante, ajouter à la fin un choix "AJOUTER THEME" ce qui ouvrira un nouveau champs de saisie + un bouton "AJOUTER"(qui seront cachés de base)~~
        - ~~ si le thème existe, donner la possibilité soit : ~~
            - ~~ ajouter d'autres quetions au theme deja existant ~~
            - ~~ ecraser le theme(supprimer l'ancien fichier) ~~
        - ~~ lors de la saisie du thème on crée un fichier JSON portant le nom de ce thème~~
        - ~~les questions et réponses qui vont être saisies seront enregistrées dans ce fichier JSON ()~~
            - ~~le fichier json sera organisé comme suit : ~~
                - ~~{~~
                    - ~~nom_theme : nom (str)~~
                    - ~~duree_requise : int (temps en secondes)~~
                    - ~~questions : [~~
                        -~~ {numero_question : int, ~~
                        - ~~enonce : str, ~~
                        - ~~reponses : [liste des réponses], ~~
                        - ~~bonne_reponse : str}~~
                    - ~~]~~
                - ~~}~~
                    - ~~LISTE DE DICTIONNAIRES, chaque dictionnaire contient une question~~
        - valider les questions et réponses avec PYDANTIC
            - pas de question vide
            - pas de réponse vide (au moins 2)
            - bonne réponse INT (indice) et respecter le nombre d'indices

    - ~~champ de saisie de la question~~
    - ~~champ (plusieurs lignes) de saisie des réponses - retour à la ligne pour chaque réponse~~
    - ~~champ pour saisir la bonne réponse - indice~~
    - ~~bouton pour valider la question et ses réponses~~
        - ~~lorsque on clique sur ce bouton la réponse est enregistrée dans une liste de questions~~

    - ~~ajouter un bouton "TERMINER" lorsqu'on on aura fini de saisir toutes les questions~~
    - ~~lorsqu'on clique sur terminer, afficher un résumé de toutes les questions saisies (sans les réponses)~~
        - ~~afficher un champ "TEMPS NECESSAIRE" pour saisir le temps nécessaire en secondes (optionnel)~~
            - ~~soit saisir la durée et permet de lancer le chronometre~~
            - ~~si on ne saisit pas la durée on lance pas le chrono dans la "Page de quiz interactif"~~

- Page de quiz interactif

    - ~~avoir la possibilité de choisir un thème depuis une liste déroulante~~
        - ~~une fois le thème choisi, on lit le fichier correspond à notre choix (portant le nom du thème choisi)~~

    - ~~ajouter bouron "DEMARRER LE QUIZ" ce qui va lancer un chronometre qui va s'afficher sur la page~~
    ~~- afficher le numéro de la question ~~
    - ~~lire le fichier JSON de notre thème~~
    - ~~afficher une question à la fois avec ses réponses sur notre page ~~
        - ~~les réponses seront afficher sous forme soir bouton radio pour un seul choix ou case a cocher pour plusieurs réponses~~

    - ~~ajouter un bouton "suivant" pour passer à la question suivante~~
    - ajouter un fichier "précèdent" pour avoir la possibilité de revenir à la question précèdente
    - ~~lorsqu'on arrive à la dernière question, remplacer le bouton "SUIVANT" par "TERMINER"~~
        - ~~en cliquant sur "TERMINER", afficher le score final ~~
        - ~~afficher un bouton "RETOUR CHOIX THEME"~~

- deployer sur un serveur web sur le réseau local pour tester avec les camarades +++

- ajouter page de stats +++
    - nombre de questions
    - nombre de bonnes réponses + pourcentage
    - nombre de mauvaises réponses + pourcentage
    - graph montrant les stats

- ajouter authentification pour la création du questionnaire +++
