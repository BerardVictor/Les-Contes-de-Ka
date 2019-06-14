default lua_atk = False
default lua_protected = False
default lua_hit = False

define l = Character('Lua', color="#fefefe")

label p2 :
    "Vous vous allongez et vos yeux se ferment doucement."
    menu :
        "Brusquement, vous entendez un hurlement à glacer le sang. Un cri de femme."
        "Rejoindre la zone du cri" :
            jump combat01

        "Attendre un peu":
            "Un homme fait irruption dans votre hutte.\"Madame Aikarin ! Un Aika ! Un Aika !\""
            jump combat01


label combat01 :
    "Vous filez entre les bohios (maisons tainos) tel un courant d'air. A chacune de vos foulées, la boue éclabousse Rhana qui peine à vous suivre."
    "En un éclair, vous êtes sur les lieux."
    "Un monstre aux formes indicibles menace une jeune femme. On dirait que les ténèbres elles-mêmes se sont accouplées avec un manicou, un poulpe et une poterie Arawak."
    "Bref, une vraie saleté. La femme attaquée ne se laisse pas faire. Elle est blessée mais continue de se protéger avec une dague."
    scene bg_combat01
    with hpunch

    call combat from _call_combat

#    menu :
#        "Attaquer l'aika" :
#            $ epaule += 2
#            $ lua_atk = True
#            "Vous vous jetez sur l'aika. Votre lance se plante dans ce qui lui sert de dos."
#            jump fin_combat01
#
#        "S'interposer" :
#            $ coeur += 2
#            $ lua_protected = True
#            "Vous sprintez et réussissez à parez le coup qui visait la jeune femme."
#            jump fin_combat01
#
#        "Rechercher une faille" :
#            $ tete += 3
#            $ coeur -= 1
#            $ lua_hit = True
#            "Vous gardez votre sang froid et recherchez une faille... Pendant ce temps, l'aika frappe la jeune femme, elle valdingue à quelques mètres."
#
#            if tete < 10 :
#                "Vous ne voyez rien de précis"
#                jump fin_combat01
#            else :
#                "Un morceau de poterie est exposé sous son flanc droit. Vous le fracassez avec le manche de votre arme. Le monstre vacille et vous en profitez pour le clouer de votre lance."
#                $ faille1 = 1
#                jump purge01


label fin_combat01 :
    with hpunch
    "Cet aika ne fait pas le poids contre vous. En fait, pour vous, c'est la routine. Après avoir esquivé quelques puissants coups, vous réussissez à le clouer au sol avec votre lance."
    jump purge01


label purge01 :
    scene bg_village
    menu :
        "Demander le maraca" :
            m "Rhana ! Envoie-moi Kaskabel !\", demandez-vous avec un ton pressé (l'aika essaye de se dégager)."
            "Rhana vous lance un maraca. Vous le saisissez et le secouez en rythme, autour du monstre. Il réagit. Il s'agite de plus bel puis se calme. On n'entend plus que le sable du maraca."
    menu :
        "Vous posez votre paume sur son front. Le tatouage caractéristique des aikarins sur le dos de votre main se met à tournoyer."
        "Continuer de jouer du maraca" :
            "De l'énergie sombre sous forme d'une nuée de chauve-souris s'échappe de lui, comme si sa substance était aspirée par le haut. Vos yeux se révulsent."
            "Alors que les chauve-souris vous traversent, vous ressentez quelque chose qui vient de la bête... de la haine. Après avoir repris vos esprits, il ne reste plus rien, que la relike du monstre : un morceau de poterie ivoire."
            jump renc_lua

label renc_lua :
    show makaoka :
        xalign 0.0 yalign 0.425
    with moveinleft
    show lua :
        xalign 1.0 yalign 0.425
    with moveinright

    if lua_atk :
        menu :
            "La jeune femme vient vers vous. Vous la reconnaissez : c'est Lua. Elle vous parle."
            "Continuer" :
                l "Comment tu as sauté sur lui ! Tu es une tête brulée... J'aime ça."

    if lua_protected :
        menu :
            "La jeune femme vient vers vous. Vous la reconnaissez : c'est Lua. Elle vous parle."
            "Continuer" :
                l "M... Merci d'avoir pris le coup à ma place, Aikarin."

    if lua_hit :
        menu :
            "La jeune femme vient vers vous. Vous la reconnaissez : c'est Lua. Elle vous parle."
            "Pourquoi avoir pris autant de temps !? J'aurais pu y passer !"

            "Demander des excuses" :
                m "Désolée, il fallait que j'analyse un peu la situation."

            "Lui expliquer" :
                m "Ne pas prendre de décision hâtive fait partie du métier."

            "L'envoyer paître" :
                m "Oh! Pour me faire des reproches tu dois être une aikarin aussi, non ? Non ? Bien."
                "Elle ne sait pas trop quoi répondre."

    menu :
        "Tout aika vient d'une émotion lourde. Vous avez ressenti de la haine lors de la purge. D'où toute cette haine peut bien venir ?"
        "Interroger Lua" :
            l "Elle vous révèle qu'elle était pressentie en tant que représentante du caciquat de Marien lors de la compétition de l'ambassadrice de l'île."
            l "Mais, il y a quelques jours, une femme est arrivée de nulle part et a pris sa place. Elle a peut-être généré du ressentiment depuis... Ce qui aurait créé l'aika."
            l " Cela vous parait un peu faible comme raison, mais pourquoi pas."
        "Rentrer chez vous" :
            m "Je suis fatiguée. On discutera de tout ça plus tard. Bonne nuit."
    hide makaoka with moveoutleft
    hide lua with moveoutright
