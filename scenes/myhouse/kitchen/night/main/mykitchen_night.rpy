###############
## Setup
## Story Path
label lbl_mykitchen_night_setup:
    if main_story == 86:
        pov "{i}[missus] didn't want me to go back down there tonight. I should just go to bed.{/i}"
        jump lbl_myhallway_night_setup
    if mum_path == 28:
        pov "{i}If I want to go out, I should at least change out of my suit.{/i}"
        jump lbl_myhallway_night_setup
    if sister_path == 36.1:
        jump lbl_family_dinner
    if principallashley_path == 11:
        jump lbl_wine_heist

    ## This random choice determines what shows on the chalkboard.
    $ mykitchen_night_chalkboard = renpy.random.randint(1,10)
    jump lbl_mykitchen_night

###############
## Room Navigation
## This is the map for my kitchen during the night
label lbl_mykitchen_night:

    scene bg mykitchen_night
    call screen scr_mykitchen_night
    screen scr_mykitchen_night():
        add "img mykitchen_night_chalkboard_[mykitchen_night_chalkboard]"
        ## Room Interactions
        if (15 <= main_story <= 22 or 24 <= main_story <= 27 or main_story >= 35):
            #if ((mum_path == 0 and day != 1 and trustandsafety_shield == 0) or mum_path == 4) and not (sister_path != 10 or sister_path != 15 or sister_path != 16):
            if ((mum_path == 0 and day != 1 and trustandsafety_shield == 0) or mum_path == 4) and (sister_path not in (10, 15, 16) ):
                imagebutton auto "btn mykitchen_night_livingroom_motherwatching_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_night_setup")
            else:
                imagebutton auto "btn mykitchen_night_livingroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_night_setup")
        else:
            imagebutton auto "btn mykitchen_night_livingroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_night_setup")
        imagebutton auto "btn mykitchen_night_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_night_setup")
        imagebutton auto "btn mykitchen_night_dining_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mydiningroom_night_setup")
        use hud_overlay

###############
## Labels
