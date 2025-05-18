###############
## Setup
## Story Path
label lbl_motelfront_night_setup:
    scene bg motelfront_night ###
    with fade
    ## No Event
    #else:
    jump lbl_motelfront_night

###############
## Room Navigation
## This is the map for motel front during the night
label lbl_motelfront_night:
    scene bg motelfront_night
    call screen scr_motelfront_night

screen scr_motelfront_night():
    imagebutton auto "btn motelfront_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_motelfront_night_door")
    use hud_overlay2

###############
## Labels
## Locations
label lbl_motelfront_night_door:

    jump lbl_motelfront_night_setup
