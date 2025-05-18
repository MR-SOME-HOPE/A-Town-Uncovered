###############
## Setup
## Story Path
label lbl_mayorsestatefront_day_setup:
    scene bg mayorsestatefront_day ###
    with fade
    ## No Event
    #else:
    jump lbl_mayorsestatefront_day

###############
## Room Navigation
## This is the map for mayor estate front during the day
label lbl_mayorsestatefront_day:
    scene bg mayorsestatefront_day
    call screen scr_mayorsestatefront_day

screen scr_mayorsestatefront_day():
    imagebutton auto "btn mayorsestatefront_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mayorsestatefront_day_door")
    use hud_overlay2

###############
## Labels
## Locations
label lbl_mayorsestatefront_day_door:

    jump lbl_mayorsestatefront_day_setup
