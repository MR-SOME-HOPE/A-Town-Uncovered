###############
## Setup
## Story Path
label lbl_effieroom_night_setup:

    ## Sex with Effie
    if main_story == 12:
        jump lbl_sex_with_effie

    ## Effie Post Sex
    elif main_story == 13:
        scene bg effieroom_nightlightson
        with fade
        if effie_exib >= 1:
            jump lbl_effie_post_sex
        else:
            jump lbl_effie_post_sex_clothed

    ## Effie Sex Again
    elif main_story >= 14:
        if effie_funlater == 1:
            jump lbl_sex_with_effie
        else:
            scene bg effieroom_nightlightson
            with fade
            if effie_mish >= 1:
                jump lbl_effie_post_sex_2_mish
            elif effie_exib >= 1:
                jump lbl_effie_post_sex_2_exib
            elif effie_bj >= 1:
                jump lbl_effie_post_sex_2_bj
            else:
                jump lbl_effie_post_sex_2_kiss

    ## No Event
    else:
        jump lbl_effieroom_night

###############
## Room Navigation
## This is the map for effie room during the night
label lbl_effieroom_night:

    scene bg effieroom_nightlightson
    call screen scr_effieroom_night

screen scr_effieroom_night():
    #imagebutton auto "btn effieroom_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effiehousehallway_night_setup_1")
    use hud_overlay

###############
## Labels
