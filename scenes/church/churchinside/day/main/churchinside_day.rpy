###############
## Setup
## Story Path
label lbl_church_day_setup:
    ## Funky Teas SETUP
    if principallashley_path == 17:
        scene bg church_day
        pov "{i}It's too early to come here. I should come back at night.{/i}"
        jump lbl_church_day
    ## NO EVENTS
    else:
        jump lbl_church_day

###############
## Room Navigation
## This is the map for churchinside during the day
label lbl_church_day:
    scene bg church_day
    call screen scr_church_day

screen scr_church_day():
    imagebutton auto "btn church_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_church_day_door")
    imagebutton auto "btn church_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_church_day_exit")
    use hud_overlay2

###############
## Labels
## Conversations
label lbl_church_day_door:
    pov "{i}No reason to go in there at the moment.{/i}"

    jump lbl_church_day


label lbl_church_day_exit:
    jump lbl_churchoutside_day_setup
