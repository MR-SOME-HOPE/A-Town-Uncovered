###############
## Setup
## Story Path
label lbl_church_night_setup:

    ## Funky Teas
    if principallashley_path == 17:
        scene bg churchoutside_night
        scene black with fade
        jump lbl_funky_teas

    ## NO EVENTS
    else:
        jump lbl_church_night

###############
## Room Navigation
## This is the map for churchinside during the night
label lbl_church_night:
    scene bg church_night
    call screen scr_church_night

screen scr_church_night():
    imagebutton auto "btn church_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_church_night_door")
    imagebutton auto "btn church_night_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_church_night_exit")

    use hud_overlay2

###############
## Labels
## Conversations
label lbl_church_night_door:
    pov "{i}No reason to go in there at the moment.{/i}"

    jump lbl_church_night

label lbl_church_night_exit:
    jump lbl_churchoutside_night_setup
