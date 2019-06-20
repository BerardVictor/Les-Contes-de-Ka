label maracas_mini_game :
#    play music "audio/maracas_theme.ogg"
    init python:
        import time
        import pygame
        MOUSEBUTTONDOWN=pygame.MOUSEBUTTONDOWN

        class RhythmD(object):
            def __init__(self, sprite, speed, delay, ypos=0):
                self.sprite = sprite
                self.speed = speed
                self.delay = delay
                self.show = manager.create(sprite)
                self.show.x = -50
                self.show.y = ypos
                self.moving = False # No point in checking if it isn't.

            def update(self):
                if store.t + self.delay < time.time():
                    self.moving = True
                    self.x = self.x + self.speed
                else:
                    pass

            @property
            def x(self):
                return self.show.x
            @x.setter
            def x(self, value):
                self.show.x = value

            @property
            def y(self):
                return self.show.y
            @y.setter
            def y(self, value):
                self.show.y = value



        def sprites_update(st):
            for sprite in sprites[:]:
                sprite.update()
                if sprite.x > config.screen_width:
                    sprite.show.destroy()
                    sprites.remove(sprite)
            return 0.05

        def sprites_event(ev, x, y, st):
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    hit = False
                    for sprite in sprites[:]:
                        if sprite.moving:
                            if int(sprite.x) in store.targets:
                                store.hits += 1
                                hit = True
                                # We destroy the sprite, making it impossible to it twice :)
                                sprite.show.destroy()
                                sprites.remove(sprite)
                                break
                    if not hit:
                        store.misses += 1
                    renpy.restart_interaction()
#                    if hits == 5 :
#                        renpy.call(purge02)
#
#                    if misses == 5 :
#                        renpy.call(maracas_mini_game)

    screen show_vars:
        image "images/maracas_zone.png" :
            xalign 0.5
            yalign 0.07

        text "Ratés: [misses], Réussis: [hits]!" :
            xalign 0.5
            size 50

        text "Appuyez":
            xalign 0.5
            yalign 0.15
            size 80

        imagebutton :
            idle "images/maracas.png"
            hover "images/maracas_click.png"
            idle_foreground Text("{size=20}{font=Eraser.ttf}Appuyez{/font}{/size}" , xalign=0.5, yalign=0.5)
            hover_foreground Text("{size=28}{font=Eraser.ttf}Appuyez{/font}{/size}" , xalign=0.5, yalign=0.5)
            action renpy.sound.play ("audio/maracas_hit.ogg")
            xalign 0.5
            yalign 0.5


    label maracas_start:
        python:
            hits = 0
            misses = 0
            t = time.time()
            manager = SpriteManager(update=sprites_update, event=sprites_event)
            sprite = Image("images/maracas_hit.png")
            targets = set(960+i for i in xrange(-40, 40)) # Just checking 1000 would be close to impossible to hit...
            sprites = []
            td = 0
            for i in xrange(100):
                td += renpy.random.random() + 0.5
                sprites.append(RhythmD(Image("images/maracas_hit.png"), 10, td, 75))

            renpy.show_screen("show_vars")
            renpy.show("_", what=manager, zorder=1)



        while True:
            $ result = ui.interact()
