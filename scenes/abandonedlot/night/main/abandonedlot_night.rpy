###############
## Setup
## Story Path
label lbl_abandonedlot_night_setup:
    stop music fadeout 2.0
    ## Start of Game
    if main_story == 1:
        pov "{i}That abandoned lot looks very shady and dangerous, I should just get home. From what I remember, my house has a red roof.{/i}"
        jump lbl_townmap_setup
    ## Before Jacob Invites You to the Comic Book Store
    elif main_story <= 19:
        pov "{i}I don't think I should go there, it looks like a dangerous area.{/i}"
        jump lbl_townmap_setup
    ## No EVENT
    else:
        jump lbl_abandonedlot_night

###############
## Room Navigation
## This is the map for abandoned lot during the night
label lbl_abandonedlot_night:
    scene bg abandonedlot_night
    call screen scr_abandonedlot_night

screen scr_abandonedlot_night():
    imagebutton auto "btn abandonedlot_night_street_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_night_setup")
    imagebutton auto "btn abandonedlot_night_cinema_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cinema_night_setup")

    use hud_overlay

###############
## Labels
## Conversations
