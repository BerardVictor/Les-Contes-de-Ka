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
    play music "audio/ig_theme.ogg"

label intro :
    "Notre histoire commence 12 ans plus tard. Vous êtes une des survivantes du massacre."
    "Vous êtes Makaoka. Vos dons vous ont permis de devenir une aikarin ; le village compte sur vous pour bannir les esprits corrompus."
    $ persistent.wiki_unlocked.add("codex_makaoka")

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
    "Vous avez gagné +5 en Épaule. Épaule est passé à [epaule]."
    jump fuite

label artisane :
    "Mmmh... Artisane, une profession qui demande un esprit vif et des mains agiles."
    "Vous avez gagné +5 en Tête. Tête est passé à [tete]."
    jump fuite

label chamane :
    "Mmmh... Chamane, une profession qui demande une grande connexion avec les esprits."
    "Vous avez gagné +5 en Coeur. Coeur est passé à [coeur]."
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
    "Vous avez gagné +5 en Épaule. Épaule est passé à [epaule]."
    jump enfance

label ruse :
    "Ah oui, elle avait fabriqué un leurre avec ce qu'elle avait sous la main."
    "Vous avez gagné +5 en Tête. Tête est passé à [tete]."
    jump enfance

label charisme :
    " Ah oui, elle avait convaincu un des Karibs de la libérer."
    "Vous avez gagné +5 en Coeur. Coeur est passé à [coeur]."
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
    "Vous avez gagné +5 en Épaule. Épaule est passé à [epaule]."
    jump pret


label foret :
    "Forêts. Typique des gens qui aiment réfléchir..."
    "Vous avez gagné +5 en Tête. Tête est passé à [tete]."
    jump pret


label caverne :
    "Cavernes. Typique des personnes spirituelles..."
    "Vous avez gagné +5 en Coeur. Coeur est passé à [coeur]."
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
