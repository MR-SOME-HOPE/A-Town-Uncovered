###############
## Setup
## Story Path
label lbl_lashleymanorfront_night_setup:
    scene bg lashleymanorfront_night ###
    with fade
    ## No Event
    #else:
    jump lbl_lashleymanorfront_night

###############
## Room Navigation
## This is the map for lashley manor front during the night
label lbl_lashleymanorfront_night:
    scene bg lashleymanorfront_night
    call screen scr_lashleymanorfront_night

screen scr_lashleymanorfront_night():
    imagebutton auto "btn lashleymanorfront_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashleymanorfront_night_door")
    use hud_overlay2

###############
## Labels
## Locations
label lbl_lashleymanorfront_night_door:

    jump lbl_lashleymanorfront_night_setup
