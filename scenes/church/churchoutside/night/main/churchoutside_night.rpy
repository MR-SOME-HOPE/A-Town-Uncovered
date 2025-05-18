###############
## Setup
## Story Path
label lbl_churchoutside_night_setup:
    ## First Day of university
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_uptownmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_uptownmap_setup
    ## Before Jacob Invites You to the Comic Book Store
    elif main_story <= 17:
        pov "{i}I don't think I should go there, it looks like a dangerous area.{/i}"
        jump lbl_uptownmap_setup
    ## First Day in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_uptownmap_setup
    ## NO EVENTS
    else:
        jump lbl_churchoutside_night

###############
## Room Navigation
## This is the map for churchoutside during the night
label lbl_churchoutside_night:
    scene bg churchoutside_night
    call screen scr_churchoutside_night

screen scr_churchoutside_night():
    imagebutton auto "btn churchoutside_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_churchoutside_night_door")

    use hud_overlay2

###############
## Labels
## Conversations
label lbl_churchoutside_night_door:

    jump lbl_church_night_setup
