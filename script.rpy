## Python modules!
init python:
    import math
    import random
    renpy.music.register_channel("ambience","sfx",True,tight=True)#loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False
    renpy.music.register_channel("sex_sounds","sfx",True,tight=True)
    renpy.music.register_channel("sex_voices","voice",True,tight=True)

################################################################################
## Splashscreen
label splashscreen:
    $ renpy.pause(0)
    scene black
    $ renpy.pause(1,hard=True)
    show bg premenu_importantage
    with dissolve

    call screen scr_premenu_importantage

screen scr_premenu_importantage():
    add "bg premenu_importantage"
    imagebutton auto "btn premenu_importantage_yes_%s" xpos 0 ypos 0 focus_mask True action Jump("splashscreen_2")#lbl_mom_bedroom_hscene_after_mish
    imagebutton auto "btn premenu_importantage_no_%s" xpos 0 ypos 0 focus_mask True action Quit(False)

label splashscreen_2:
    # show bg premenu_important_inalpha
    # with fade
    # $ renpy.pause()
    # show bg premenu_important_savefile
    # with fade
    # $ renpy.pause()
    show bg premenu_geeseki
    with fade
    $ renpy.pause()
    scene black
    with dissolve
    return

## Default My Version
default myversion = "1.0"
default myversion_simplified = 1

################################################################################
## Start
label start:
    scene black
    stop music fadeout 1.0
    $ myversion = "1.0"
    $ myversion_simplified = 1
    window hide

    jump lbl_gstart

## After Load
label after_load:
    if not myversion.startswith("1.0"):
        stop music fadeout 1.0
        $ cheat_on = 2
        scene black with None
        centered "!!! WARNING !!!\n\n
                THE CURRENT VERSION OF THE GAME IS [config.version].\n\n
                YOU ARE LOADING AN OLD SAVE FILE FROM A PREVIOUS VERSION ([myversion])!\n\n
                By doing this, you may experience bugs, errors, and problems which would have been avoidable."
        centered "Please 'Start' a new game or 'Start' from a loaded preset.\n\n
                Otherwise, you may continue playing this old save file at your own risk.\n\n
                I also ask for you not to report any bugs if you are using this old save file."
    return

################################################################################
## Game start
label lbl_gstart:
    pass

## Ask for Hscene X-ray Preference
label lbl_start_preferences:
    "Do you want x-ray enabled for sex scenes?"
    menu:
        "Yes":
            $ hscene_xray = 1
        "No":
            $ hscene_xray = 0

    ## Set Date and Time
    $ month = 5
    $ date = 9
    $ day = 6
    $ gtime = 3

    ## Set Family Relationship
    $ winc = 0

    ## Set Starting Place
    $ startnewgame = 0

    ## Ask to start from the start or continue from a preset game state
    if renpy.seen_label("intro_cutscene"):
        "Do you want to start from the very start or continue from one of the last few updates?"
        menu:
            "Start a new game":
                $ startnewgame = 1
                jump lbl_start_name_pov
            "Continue from the end of a previous update":
                jump lbl_start_name_pov
    else:
        $ startnewgame = 1
        jump lbl_start_name_pov
