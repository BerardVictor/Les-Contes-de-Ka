define m = Character('Makaoka', color="#fefefe")
define r = Character('Rhana', color="#fefefe")

default rel_Rhana = 0
default rel_Lua = 0

default saoul = 0
default faille1 = 0


label p1 :
    scene bg_village
    "Vous vous réveillez en sursaut et en sueur. Vous êtes dans votre hamac, il fait nuit. Dehors, une pluie battante."
    "Un jeune garçon s'avance vers vous. Le voir vous met un peu mal à l'aise."
    show rhana :
        xalign 1.0 yalign 0.425
    with moveinright
    show makaoka :
        xalign 0.0 yalign 0.425
    with moveinleft
    menu :

        r "Tu as encore fait un cauchemar, Maman ?"
        "Laisse-moi tranquille, Rhana." :
            $ paix -=1
            "*Il baisse la tête et s'écarte.*"
        "Ça va aller, Rhana. J'ai l'habitude maintenant.":
            $ paix +=1
            "*Vous essayez de sourire.*"
    hide rhana with moveoutright
    hide makaoka with moveoutleft

    menu :
        "Une gourde pleine de ouicou (alcool de manioc) vous fait de l'œil... ça pourrait chasser vos idées noires... En tout cas, le temps de l'ivresse."
        "Boire" :
            menu :
                "A chaque grande gorgée, vous vous dîtes que c'est amer, que ça brûle... Et que c'est ce que vous recherchez."

                "Boire encore un coup" :
                    menu :
                        "*Gloup*. Ca commence à faire beaucoup, vous allez bientôt \"voir les zemis\". Mais c'est au moins ce qu'il faut pour calmer ces horribles visions."

                        "Finir la gourde " :
                            if epaule < 15 :
                                "*Gloups Gloups*. Vous ne vous sentez vraiment pas bien. Votre tête tourne et vos boyaux tissent un hamac."
                                $ tete -= 1
                                $ saoul += 1
                                "saoul = [saoul]"
                            else :
                                "*Gloups Gloups*. Vous avez un peu trop tiré sur la corde mais votre bonne constitution vous a sauvé... cette fois."
                                $ coeur +=  1

                        "Arrêter de boire" :
                            "Vous pourriez presque entendre votre foie vous remercier."
                            $ tete += 1

                "Arrêter de boire" :
                    "Vous pourriez presque entendre votre foie vous remercier."
                    $ tete += 1

        "Ne pas boire" :
            "Vous pourriez presque entendre votre foie vous remercier."
            $ tete += 1

    menu :
        "Rhana est dans son hamac. Vous croyez entendre des sanglots légèrement étouffés."
        "Essayer de le consoler" :
            show makaoka :
                xalign 0.0 yalign 0.425
            with moveinleft
            m "Je suis désolée, Rhana. Je suis un peu à cran en ce moment."
            $ paix += 2
            "Il vous sourit timidement."
            hide makaoka with moveoutleft

        "Tu devrais t'endurcir Rhana !" :
            $ coeur -= 1
            "Les sanglots s'atténuent lentement."

        "Ne rien dire" :
            $ paix -= 2
            $ coeur -= 1
    "Plus tard, les sensations de votre cauchemar commencent lentement à se dissiper."
    if saoul >= 1 :
        "Contrairement à votre gueule de bois"
    "La pluie diminue, comme si l'accalmie se liait à vos profondes inspirations.
    Tout est à nouveau calme. On n'entend plus que les stridulations des insectes"

    jump p2

return
