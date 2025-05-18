###############
## Setup
## Story Path
label lbl_abandonedlot_day_setup:
    ## First Day of university
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Before Jacob Invites You to the Comic Book Store
    elif main_story <= 17:
        pov "{i}I don't think I should go there, it looks like a dangerous area.{/i}"
        jump lbl_townmap_setup
    ## First Day in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## NO EVENTS
    else:
        jump lbl_abandonedlot_day

###############
## Room Navigation
## This is the map for abandoned lot during the day
label lbl_abandonedlot_day:
    scene bg abandonedlot_day
    call screen scr_abandonedlot_day

screen scr_abandonedlot_day():
    imagebutton auto "btn abandonedlot_day_street_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_day_setup")
    imagebutton auto "btn abandonedlot_day_cinema_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cinema_day_setup")

    use hud_overlay

###############
## Labels
## Conversations
