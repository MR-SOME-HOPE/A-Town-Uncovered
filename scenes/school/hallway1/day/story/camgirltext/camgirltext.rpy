## Cam Girl Text ##
label lbl_cam_girl_text:
    if winc == 0:
        jump lbl_cam_girl_text_winc0

    scene bg camgirltext_2
    with fade
    show bg camgirltext_1
    $ renpy.pause()
    pov "What the fuck..?"
    show bg camgirltext_2
    $ renpy.pause(0.5,hard=True)
    pov "{i}What the hell? Did she just delete it?{/i}"
    pov "{i}I swear I didn't just imagine what I saw.{/i}"
    show bg camgirltext_3
    $ renpy.pause()

    menu:
        "Did [missus] really say that?" if winc == 0:
            show bg camgirltext_4
            $ renpy.pause()
            show bg camgirltext_5
            $ renpy.pause()
            pov "{i}Sure... sure she did.{/i}"
        "Did Mom really say that?" if winc == 1:
            show bg camgirltext_4
            $ renpy.pause()
            show bg camgirltext_5
            $ renpy.pause()
            pov "{i}Sure... sure she did.{/i}"
        "What does that have to do with the cam feed?":
            show bg camgirltext_6
            $ renpy.pause()
            pov ".."
            pov "..."
            pov "...."
            pov "{i}I guess she's not going to respond.{/i}"
    $ sister_path = 2
    $ gtime = 1
    $ townmap_enabled = 1
    $ renpy.notify("New Objective: Confront [sister] about the text at night")

    jump lbl_schoolhallway1_day_setup

### NO WINC ###
label lbl_cam_girl_text_winc0:

    scene bg camgirltext_2_winc
    with fade
    show bg camgirltext_1_winc
    $ renpy.pause()
    pov "What the fuck..?"
    show bg camgirltext_2_winc
    $ renpy.pause(0.5,hard=True)
    pov "{i}What the hell? Did she just delete it?{/i}"
    pov "{i}I swear I didn't just imagine what I saw.{/i}"
    show bg camgirltext_3_winc
    $ renpy.pause()

    menu:
        "Did [missus] really say that?" if winc == 0:
            show bg camgirltext_4_winc
            $ renpy.pause()
            show bg camgirltext_5_winc
            $ renpy.pause()
            pov "{i}Sure... sure she did.{/i}"
        "Did Mom really say that?" if winc == 1:
            show bg camgirltext_4_winc
            $ renpy.pause()
            show bg camgirltext_5_winc
            $ renpy.pause()
            pov "{i}Sure... sure she did.{/i}"
        "What does that have to do with the cam feed?":
            show bg camgirltext_6_winc
            $ renpy.pause()
            pov ".."
            pov "..."
            pov "...."
            pov "{i}I guess she's not going to respond.{/i}"
    $ sister_path = 2
    $ gtime = 1
    $ townmap_enabled = 1
    $ renpy.notify("New Objective: Confront [sister] about the text at night")

    jump lbl_schoolhallway1_day_setup
