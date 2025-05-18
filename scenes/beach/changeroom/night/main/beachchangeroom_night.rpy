###############
## Setup
label lbl_beachchangeroom_blue_night_setup:
    call lbl_beachchangeroom_night_setup ("blue")

label lbl_beachchangeroom_purple_night_setup:
    call lbl_beachchangeroom_night_setup ("purple")

label lbl_beachchangeroom_green_night_setup:
    call lbl_beachchangeroom_night_setup ("green")

label lbl_beachchangeroom_red_night_setup:
    call lbl_beachchangeroom_night_setup ("red")

label lbl_beachchangeroom_night_setup(color):
    scene
    $ renpy.show("bg beachchangeroom_%s_night" % color)
    if color != "red":
        call lbl_beachchangeroom_night_random_event
    call lbl_beachchangeroom_night (color)

label lbl_beachchangeroom_night_random_event:
    $ random_event = renpy.random.randint(1,2)

## Sex World
    if main_story == 28:
        pass

## Normal
    else:
        if beachchangeroom_fishbite == 1:
            jump lbl_beachchangeroom_fishmermaid
        elif random_event == 1 and violette_path >= 1:
            jump lbl_beachchangeroom_violettechanging
    return

###############
## Room Navigation
label lbl_beachchangeroom_night(color):
    call screen scr_beachchangeroom_night(color)
    screen scr_beachchangeroom_night(color):
        imagebutton auto ("btn beachchangeroom_night_%s_%%s" % color) xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_night_setup")
