###############
## Setup
## Story Path
label lbl_trainstation_day_setup:
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
        jump lbl_trainstation_day

###############
## Room Navigation
## This is the map for mine entrance during the day
label lbl_trainstation_day:
    scene bg trainstation_day
    with fade
    call screen scr_trainstation_day

screen scr_trainstation_day():
    #imagebutton auto "btn trainstation_day_entrance_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_trainstation_day_entrance")

    use hud_overlay2

###############
## Labels
## Conversations
