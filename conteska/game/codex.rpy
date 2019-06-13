################################################################################
## Écran d'encyclopédie dans lequel on retrouve des informations sur les objets,
## les personnages ou les lieux que l'on rencontre au fur et à mesure que l'on
## progresse dans le jeu
################################################################################
##Gère le bloquage des articles du codex
default persistent.wiki_unlocked = { "wiki_index" }

init python:

    def locked_handler(target):
        renpy.run(ShowMenu(target))

    def locked_sensitive(target):
        return target in persistent.wiki_unlocked

    config.hyperlink_handlers["locked"] = locked_handler
    config.hyperlink_sensitive["locked"] = locked_sensitive

define config.hyperlink_protocol = "locked"
define gui.hyperlink_text_insensitive_color = gui.insensitive_color
##########

define config.hyperlink_protocol = "showmenu"


screen codex :
    tag menu
    style_prefix "codex"
    image "images/bg_menu.png"

    use game_menu(_("Encyclopédie")):

        text _p("""
            {a=codex_objets} Objets {/a}{p}{p}
            {a=codex_perso} Personnages {/a}{p}{p}
            {a=codex_lieux} Lieux {/a}{p}{p}
            {a=codex_culture} Culture {/a}{p}{p}
            {a=codex_ff} Faune et Flore {/a}{p}
            """)

        vbar :
            xalign 0.15
            yalign 0.0
            ysize 800
            xsize 6


screen codex_objets :
    tag menu

    use game_menu(_("Objets")) :

        text _p("""
            {a=codex}Objets {/a}{p}
            {a=codex_trigonolithes}   Trigonolithes {/a}{p}{p}
            {a=codex_perso}Personnages {/a}{p}{p}
            {a=codex_lieux}Lieux {/a}{p}{p}
            {a=codex_culture}Culture {/a}{p}{p}
            {a=codex_ff}Faune et Flore {/a}{p}
            """)

        vbar :
            xalign 0.15
            yalign 0.0
            ysize 800
            xsize 6


screen codex_perso :
    tag menu

    use game_menu(_("Personnages")) :

        text _p("""
            {a=codex} Objets {/a}{p}{p}
            {a=codex_perso}Personnages {/a}{p}
            {a=codex_makaoka}    Makaoka {/a}{p}{p}
            {a=codex_lieux}Lieux {/a}{p}{p}
            {a=codex_culture}Culture {/a}{p}{p}
            {a=codex_ff}Faune et Flore {/a}{p}
            """)

        vbar :
            xalign 0.15
            yalign 0.0
            ysize 800
            xsize 6

screen codex_lieux :
    tag menu

    use game_menu(_("Encyclopédie")) :

        text _p("""
            {a=codex_objets} Objets {/a}{p}{p}
            {a=codex_perso} Personnages {/a}{p}{p}
            {a=codex_lieux} Lieux {/a}{p}{p}
            {a=codex_culture} Culture {/a}{p}{p}
            {a=codex_ff} Faune et Flore {/a}{p}
            """)

        vbar :
            xalign 0.15
            yalign 0.0
            ysize 800
            xsize 6




screen codex_culture :
    tag menu

    use game_menu(_("Encyclopédie")) :

        text _p("""
            {a=codex_objets} Objets {/a}{p}{p}
            {a=codex_perso} Personnages {/a}{p}{p}
            {a=codex_lieux} Lieux {/a}{p}{p}
            {a=codex_culture} Culture {/a}{p}{p}
            {a=codex_ff} Faune et Flore {/a}{p}
            """)

        vbar :
            xalign 0.15
            yalign 0.0
            ysize 800
            xsize 6




screen codex_ff :
    tag menu

    use game_menu(_("Encyclopédie")) :

        text _p("""
            {a=codex_objets} Objets {/a}{p}{p}
            {a=codex_perso} Personnages {/a}{p}{p}
            {a=codex_lieux} Lieux {/a}{p}{p}
            {a=codex_culture} Culture {/a}{p}{p}
            {a=codex_ff} Faune et Flore {/a}{p}
            """)

        vbar :
            xalign 0.15
            yalign 0.0
            ysize 800
            xsize 6




screen codex_trigonolithes :
    tag menu 
    use game_menu(_("Trigonolithes")) :

        image "images/interface_codex.png" :
            xalign 0.5
            yalign 0.0

        vbox :
            text("Dans ces sculptures à trois pointes, l'une des pointes agissait sur les cultures, l'autre sur les accouchements des femmes et la dernière sur la présence du soleil et de l'eau. En résumé, le trigonolithe était fortement lié à la fertilité tant agricole qu'humaine. Les représentations sont zoomorphes ou anthropomorphes.")
            xalign 0.5
            yalign 0.7
            xsize 800
            ysize 350

        text _p("""
            {a=codex}Objets {/a}{p}
            {a=codex_trigonolithes}   Trigonolithes {/a}{p}{p}
            {a=codex_perso}Personnages {/a}{p}{p}
            {a=codex_lieux}Lieux {/a}{p}{p}
            {a=codex_culture}Culture {/a}{p}{p}
            {a=codex_ff}Faune et Flore {/a}{p}
            """)

        vbar :
            xalign 0.15
            yalign 0.0
            ysize 800
            xsize 6


screen codex_makaoka :
    tag menu

    use game_menu(_("Makaoka")) :

        vbox :
            text("Vous êtes Makaoka. Vos dons vous ont permis de devenir une aikarin ; le village compte sur vous pour bannir les esprits corrompus.")
            xalign 0.5
            yalign 0.7
            xsize 800
            ysize 350

        text _p("""
            {a=codex_objets} Objets {/a}{p}{p}
            {a=codex}Personnages {/a}{p}
            {a=codex_perso}    Makaoka {/a}{p}{p}
            {a=codex_lieux}Lieux {/a}{p}{p}
            {a=codex_culture}Culture {/a}{p}{p}
            {a=codex_ff}Faune et Flore {/a}{p}
            """)

        vbar :
            xalign 0.15
            yalign 0.0
            ysize 800
            xsize 6
