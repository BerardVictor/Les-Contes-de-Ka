label combat :


    scene bg_menu
    with hpunch

    show battle_mkk :
        xalign 0.05 yalign 0.3
    with moveinleft

    show battle_aika :
        xalign 0.95 yalign 0.3
    with moveinright




    $ aika_choice = renpy.random.choice(['Attaque', 'Esquive', 'Magie'])

    while maka_hp and aika_hp > 0 :

        show text ("Makaoka HP : [maka_hp] / 10                                                                                                                     Aika HP : [aika_hp] / 6") :
            xalign 0.4
            yalign 0.08

        if maka_hp <= 5 :
            hide battle_mkk
            show mkk_down :
                xalign 0.05 yalign 0.3

        if aika_hp <=3 :
            hide battle_aika
            show aika_down :
                xalign 0.95 yalign 0.3

#        init python :
#            from random import randint
#            t = ["Attaque", "Esquive", "Magie"]
#            aika_choice = t[randint(0,2)]

        menu :
            "Attaque" :
                $ maka_choice = "Attaque"
            "Esquive" :
                $ maka_choice = "Esquive"
            "Magie" :
                $ maka_choice = "Magie"




        if maka_choice == "Attaque" :
            if aika_choice == "Attaque" :
                "Ils se jettent l'un sur l'autre et se blessent tous deux dans l'attaque."
                $maka_hp -= 1
                $aika_hp -= 1

            elif aika_choice == "Esquive" :
                "L'aika esquive l'attaque de justesse et décoche un contre dévastateur ! (C'est très efficace !)"
                $maka_hp -= 2

            elif aika_choice == "Magie" :
                "Makaoka lance une série d'attaques ! L'aika subit de terribles entailles alors qu'il essayait de concentrer sa magie. (C'est très efficace !)"
                $aika_hp -= 2

        elif maka_choice == "Esquive" :
            if aika_choice == "Attaque" :
                "Makoka esquive l'attaque de justesse et décoche un contre dévastateur ! (C'est très efficace !)"
                $aika_hp -= 2

            elif aika_choice == "Esquive" :
                "Makoka et l'aika se jaugent mutuellement."

            elif aika_choice == "Magie" :
                "L'aika utilise sa magie Makaoka ne peut pas esquiver et se prend l'attaque de plein fouet ! (C'est très efficace !)"
                $aika_hp -= 2

        elif maka_choice == "Magie" :
            if aika_choice == "Attaque" :
                "L'aika lance une série d'attaques ! Makaoka subit de terribles entailles alors qu'elle essayait de concentrer sa magie. (C'est très efficace !)"
                $maka_hp -= 2

            elif aika_choice == "Esquive" :
                "Makoka fait appel à son zemi qui fait voler en éclat la protection de l'aika ! (C'est très efficace !)"
                $aika_hp -= 2

            elif aika_choice == "Magie" :
                "Les deux ondes s'entrechoquent et font exploser les poteries de la pièce."

        $ aika_choice = renpy.random.choice(['Attaque', 'Esquive', 'Magie'])

    if maka_hp == 0 :
        "Vous avez perdu"
    elif aika_hp == 0 :
        "Vous avez gagné"
