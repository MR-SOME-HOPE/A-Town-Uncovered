###############
## Setup
## Story Path
label lbl_lashleybedroom_day_setup:
    scene bg lashleybedroom_day
    with fade
    ## No Event
    #else:
    jump lbl_lashleybedroom_day

###############
## Room Navigation
## This is the map for lashley manor front during the day
label lbl_lashleybedroom_day:
    scene bg lashleybedroom_day
    call screen scr_lashleybedroom_day

screen scr_lashleybedroom_day():
    imagebutton auto "btn lashleybedroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashleybedroom_day_door")
    use hud_overlay2

###############
## Labels
## Locations
label lbl_lashleybedroom_day_door:

    jump lbl_lashleybedroom_day_setup
