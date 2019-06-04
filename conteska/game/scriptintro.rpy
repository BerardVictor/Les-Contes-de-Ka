# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.

default epaule = 10
default tete = 10
default coeur = 10
default paix = 0


# Le jeu commence ici

label start :
    $ renpy.movie_cutscene("movie/intro.webm")
    scene bg_bassin
    play music "audio/main_menu_theme.ogg"

label intro :
    "Je vais vous raconter la catastrophe d’une autre époque. Dans un archipel que vous appelez les Antilles vivaient des tribus Arawak."
    "Ces peuples prospéraient, en harmonie avec la nature. Ils ne fabriquaient presque jamais d’armes mais imprégnaient leur art de puissantes magies."
    "Mais un jour -les jours funestes ne préviennent jamais- Kamanushi : le chef des sanguinaires guerriers Karibs tomba sur l’île de Kariani tel un sombre météore."
    "Tempête de flammes, destruction, malédiction et mort ! Le bruit des combats remplaça celui des vagues et l’odeur du sang couvrit le parfum des campêches."
    "Kamanushi ignorait quelque chose… Toutes les émotions qu’il avait déchaînées : la haine, la peur, la colère renforçaient les aikas, de farouches esprits !"
    "D’après vous ? Que s’est-il passé ? Ces esprits funestes tuèrent beaucoup de Karibs… Et Kamanushi fut leur première victime !"
    "Sans chef, l'invasion ne pouvait plus progresser."
    "Notre histoire commence 12 ans plus tard. Vous êtes une des survivantes du massacre."
    "Vous êtes Makaoka. Vos dons vous ont permis de devenir une aikarin ; le village compte sur vous pour bannir les esprits corrompus."


label metier :
    $ choice_menu = "tarot"
    menu :
        "Mais avant de continuer, j'ai quelques trous de mémoire au sujet de notre héroïne... Dites-moi, à quel métier Makaoka était destinée avant l'attaque de son île ?"
        "Chasseuse" :
            $ epaule += 5
            jump chasseuse

        "Artisane" :
            $ tete += 5
            jump artisane

        "Chamane" :
            $ coeur += 5
            jump chamane


label chasseuse :
    "Mmmh... Chasseuse, une profession qui demande de la force et de l'endurance."
    "Vous avez gagner +5 en Épaule. Épaule est passer à [epaule]."
    jump fuite

label artisane :
    "Mmmh... Artisane, une profession qui demande un esprit vif et des mains agiles."
    "Vous avez gagner +5 en Tête. Tête est passer à [tete]."
    jump fuite

label chamane :
    "Mmmh... Chamane, une profession qui demande une grande connexion avec les esprits."
    "Vous avez gagner +5 en Coeur. Coeur est passer à [coeur]."
    jump fuite


label fuite :
    menu :
        "Et... comment Makaoka s'était-elle échappée des Karibs ?"
        "Elle a utilisé la force" :
            $ epaule += 5
            jump force

        "Elle a utilisé la ruse" :
            $ tete += 5
            jump ruse

        "Elle a utilisé son charisme" :
            $ coeur += 5
            jump charisme


label force :
    "Ah oui, elle avait brisé ses liens... Et la tête de ceux qui se mettaient sur son chemin."
    "Vous avez gagner +5 en Épaule. Épaule est passer à [epaule]."
    jump enfance

label ruse :
    "Ah oui, elle avait fabriqué un leurre avec ce qu'elle avait sous la main."
    "Vous avez gagner +5 en Tête. Tête est passer à [tete]."
    jump enfance

label charisme :
    " Ah oui, elle avait convaincu un des Karibs de la libérer."
    "Vous avez gagner +5 en Coeur. Coeur est passer à [coeur]."
    jump enfance


label enfance :
    menu :
        "Une toute dernière chose... Où aimait-elle passer du temps quand elle était petite ?"
        "Dans la force des montagnes." :
            $ epaule += 5
            jump montagne

        "Dans la musique des forêts." :
            $ tete += 5
            jump foret

        "Dans le mystère des cavernes." :
            $ coeur += 5
            jump caverne


label montagne :
    "Montagnes. Typique des gens indomptables..."
    "Vous avez gagner +5 en Épaule. Épaule est passer à [epaule]."
    jump pret


label foret :
    "Forêts. Typique des gens qui aiment réfléchir..."
    "Vous avez gagner +5 en Tête. Tête est passer à [tete]."
    jump pret


label caverne :
    "Cavernes. Typique des personnes spirituelles..."
    "Vous avez gagner +5 en Coeur. Coeur est passer à [coeur]."
    jump pret

#style choice_button is button

label pret :
    $ choice_menu = "normal"
    menu :
        "Bien, on peut commencer ! Êtes-vous prêt ?"
        "Oui !" :
            jump p1
        "Non" :
            "Pause pipi, hein..."
            menu :
                "Et maintenant ? Êtes-vous prêt ?"
                "Oui !" :
                    jump p1
                "Non" :
                    "Pause plus longue ? Oh, je vois..."
                    menu :
                        "Et maintenant ? Êtes-vous prêt ?"
                        "Oui !" :
                            jump p1
                        "Non" :
                            jump loopnon

label loopnon :
    "Peut-être en mangeant plus de fibres ?"
    menu :
        "Et maintenant ? Êtes-vous prêt ?"
        "Oui !" :
            jump p1
        "Non" :
            jump loopnon
