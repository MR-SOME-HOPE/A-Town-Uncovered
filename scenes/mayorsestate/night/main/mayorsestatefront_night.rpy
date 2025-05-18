###############
## Setup
## Story Path
label lbl_mayorsestatefront_night_setup:
    scene bg mayorsestatefront_night ###
    with fade
    ## No Event
    #else:
    jump lbl_mayorsestatefront_night

###############
## Room Navigation
## This is the map for mayoral estate front during the night
label lbl_mayorsestatefront_night:
    scene bg mayorsestatefront_night
    call screen scr_mayorsestatefront_night

screen scr_mayorsestatefront_night():
    imagebutton auto "btn mayorsestatefront_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mayorsestatefront_night_door")
    use hud_overlay2

###############
## Labels
## Locations
label lbl_mayorsestatefront_night_door:

    jump lbl_mayorsestatefront_night_setup
