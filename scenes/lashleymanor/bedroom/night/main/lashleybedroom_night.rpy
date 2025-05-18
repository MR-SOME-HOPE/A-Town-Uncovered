###############
## Setup
## Story Path
label lbl_lashleybedroom_night_setup:
    scene bg lashleybedroom_night ###
    with fade
    ## No Event
    #else:
    jump lbl_lashleybedroom_night

###############
## Room Navigation
## This is the map for lashley manor front during the night
label lbl_lashleybedroom_night:
    scene bg lashleybedroom_night
    call screen scr_lashleybedroom_night

screen scr_lashleybedroom_night():
    imagebutton auto "btn lashleybedroom_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashleybedroom_night_door")
    use hud_overlay2

###############
## Labels
## Locations
label lbl_lashleybedroom_night_door:

    jump lbl_lashleybedroom_night_setup
