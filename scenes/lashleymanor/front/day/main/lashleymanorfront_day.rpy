###############
## Setup
## Story Path
label lbl_lashleymanorfront_day_setup:
    scene bg lashleymanorfront_day
    with fade
    ## No Event
    #else:
    jump lbl_lashleymanorfront_day

###############
## Room Navigation
## This is the map for lashley manor front during the day
label lbl_lashleymanorfront_day:
    scene bg lashleymanorfront_day
    call screen scr_lashleymanorfront_day

screen scr_lashleymanorfront_day():
    imagebutton auto "btn lashleymanorfront_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashleymanorfront_day_door")
    use hud_overlay2

###############
## Labels
## Locations
label lbl_lashleymanorfront_day_door:

    jump lbl_lashleymanorfront_day_setup
