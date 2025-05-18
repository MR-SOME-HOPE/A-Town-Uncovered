###############
## Setup
## Story Path
label lbl_apartmentsoutside_day_setup:
    ## First Day of university
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## First Day in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## NO EVENTS
    else:
        jump lbl_apartmentsoutside_day

###############
## Room Navigation
## This is the map for apartments outside during the day
label lbl_apartmentsoutside_day:
    scene bg apartmentsoutside_day
    call screen scr_apartmentsoutside_day

screen scr_apartmentsoutside_day():
    imagebutton auto "btn apartmentsoutside_day_leftdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_apartmentsoutside_day_door")
    imagebutton auto "btn apartmentsoutside_day_rightdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_apartmentsoutside_day_door")

    use hud_overlay

###############
## Labels
## Conversations
label lbl_apartmentsoutside_day_door:
    if hitomi_path >= 25:
        pov "{i}Hitomi's apartment building.{/i}"
    else:
        pov "{i}I don't know anyone who lives here.{/i}"
    jump lbl_apartmentsoutside_day
