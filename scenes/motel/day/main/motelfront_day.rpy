###############
## Setup
## Story Path
label lbl_motelfront_day_setup:
    scene bg motelfront_day ###
    with fade
    ## No Event
    #else:
    jump lbl_motelfront_day

###############
## Room Navigation
## This is the map for motel front during the day
label lbl_motelfront_day:
    scene bg motelfront_day
    call screen scr_motelfront_day

screen scr_motelfront_day():
    imagebutton auto "btn motelfront_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_motelfront_day_door")
    use hud_overlay2

###############
## Labels
## Locations
label lbl_motelfront_day_door:

    jump lbl_motelfront_day_setup
