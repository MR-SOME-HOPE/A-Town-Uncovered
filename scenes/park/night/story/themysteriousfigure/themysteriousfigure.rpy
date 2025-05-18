## The Mysterious Figure ##
label lbl_the_mysterious_figure:
    show bg themysteriousfigure_1_1
    pov "{i}Where's Effie? I don't see her anywhere.{/i}"
    pov "{i}I hope she's not hiding and about to jump out and scare me...{/i}"
    pov "..."
    pov "{i}Naah, she's probably still on her way here.{/i}"
    play music "audio/music/hellraiser_texture.ogg"
    show bg themysteriousfigure_1_1_1
    $ renpy.pause(1.2,hard=True)
    show bg themysteriousfigure_1_2
    $ renpy.pause(1.2,hard=True)
    show bg themysteriousfigure_1_3
    $ renpy.pause(1.2,hard=True)
    pov "{i}What the hell is that..?{/i}"
    pov "{i}I've seen that before...{/i}"
    pov "{i}That can't be Effie.{/i}"
    show bg themysteriousfigure_1_4
    $ renpy.pause(1,hard=True)
    show bg themysteriousfigure_1_5
    $ renpy.pause(1,hard=True)
    show bg themysteriousfigure_1_6
    $ renpy.pause(1,hard=True)
    show bg themysteriousfigure_1_7
    $ renpy.pause(1,hard=True)
    show bg themysteriousfigure_1_8
    $ renpy.pause(1,hard=True)
    show bg themysteriousfigure_1_9
    $ renpy.pause(1,hard=True)
    show bg themysteriousfigure_1_10
    $ renpy.pause(2,hard=True)
    show bg themysteriousfigure_1_10_1
    $ renpy.pause()
    pov "What the.. fuck?"
    pov "Is she just staring.. at me?"
    show bg themysteriousfigure_1_10_1
    $ renpy.pause(2,hard=True)
    show bg themysteriousfigure_1_11
    $ renpy.pause(0.1,hard=True)
    show bg themysteriousfigure_1_11_1
    $ renpy.pause(0.1,hard=True)
    show bg themysteriousfigure_1_11_2
    $ renpy.pause(0.1,hard=True)
    show bg themysteriousfigure_1_1
    $ renpy.pause(0.5,hard=True)
    stop music fadeout 1.0
    pov "Oh my God."

    menu:
        "Dive in and save her":
            show bg themysteriousfigure_2_7
            $ renpy.pause(1,hard=True)
            show bg themysteriousfigure_2_8
            $ renpy.pause(1,hard=True)
            show bg themysteriousfigure_2_9
            $ renpy.pause(1,hard=True)
            show bg themysteriousfigure_2_10
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_11
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_11_1
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_11_2
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_11_3
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_12
            $ renpy.pause(3,hard=True)
            show bg themysteriousfigure_3_6
            $ renpy.pause(0.5,hard=True)
            show bg themysteriousfigure_3_7
            $ renpy.pause(0.5,hard=True)
            show bg themysteriousfigure_3_8
            $ renpy.pause(0.5,hard=True)
            show bg themysteriousfigure_3_9
            $ renpy.pause(0.5,hard=True)
            show bg themysteriousfigure_3_10
            $ renpy.pause(0.5,hard=True)

            jump lbl_the_mysterious_figure_2
        "Watch her drown":
            show bg themysteriousfigure_1_1
            $ renpy.pause(1,hard=True)
            show bg themysteriousfigure_1_11_2
            $ renpy.pause(0.3,hard=True)
            show bg themysteriousfigure_1_12
            $ renpy.pause ()
            pov "Oh, fuck it."
            show bg themysteriousfigure_2_1
            $ renpy.pause(1,hard=True)
            show bg themysteriousfigure_2_2
            $ renpy.pause(1,hard=True)
            show bg themysteriousfigure_2_3
            $ renpy.pause(1,hard=True)
            show bg themysteriousfigure_2_4
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_5
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_5_1
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_5_2
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_5_3
            $ renpy.pause(0.2,hard=True)
            show bg themysteriousfigure_2_6
            $ renpy.pause(3,hard=True)
            show bg themysteriousfigure_3_1
            $ renpy.pause(0.5,hard=True)
            show bg themysteriousfigure_3_2
            $ renpy.pause(0.5,hard=True)
            show bg themysteriousfigure_3_3
            $ renpy.pause(0.5,hard=True)
            show bg themysteriousfigure_3_4
            $ renpy.pause(0.5,hard=True)
            show bg themysteriousfigure_3_5
            $ renpy.pause(0.5,hard=True)

            jump lbl_the_mysterious_figure_2

label lbl_the_mysterious_figure_2:
    show bg themysteriousfigure_4_1
    $ renpy.pause(0.4,hard=True)
    show bg themysteriousfigure_4_2
    $ renpy.pause(0.4,hard=True)
    show bg themysteriousfigure_4_3
    $ renpy.pause(0.4,hard=True)
    show bg themysteriousfigure_4_4
    $ renpy.pause(0.4,hard=True)
    show bg themysteriousfigure_4_5
    $ renpy.pause(0.4,hard=True)
    show bg themysteriousfigure_4_6
    $ renpy.pause(0.4,hard=True)
    show black
    $ renpy.pause ()

    $ insexworld = 1
    
    $ main_story = 24

    jump lbl_survived_the_drowning
