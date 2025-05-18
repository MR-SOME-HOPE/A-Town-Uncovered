###############
## Setup
## Story Path
label lbl_cliff_night_setup:
    ## First Day of university
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_uptownmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_uptownmap_setup
    ## First Day in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_uptownmap_setup
    ## NO EVENTS
    else:
        jump lbl_cliff_night

###############
## Room Navigation
## This is the map for cliff during the night
label lbl_cliff_night:
    scene bg cliff_night
    with fade
    call screen scr_cliff_night

screen scr_cliff_night():
    #imagebutton auto "btn cliff_night_street_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_night_setup")

    use hud_overlay2

###############
## Labels
## Conversations
