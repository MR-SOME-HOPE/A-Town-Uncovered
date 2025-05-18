###############
## Setup
label lbl_mydiningroom_night_setup:
    ## An Awkward Dinner Situation
    if main_story == 85:
        jump lbl_an_awkward_dinner_situation

    ## Help Build a Fort
    elif sister_path == 10:
        pov "{i}[sister] is waiting for me in the basement.{/i}"
        jump lbl_mykitchen_night_setup

    ## 20Q with Sister
    elif sister_path == 16:
        pov "{i}I have to wait for [sister] in the basement.{/i}"
        jump lbl_mykitchen_night_setup

    ## Family Dinner
    elif sister_path == 36:
        jump lbl_family_dinner

    ## No Event
    else:
        jump lbl_mydiningroom_night

###############
## Room Navigation
label lbl_mydiningroom_night:
    if mowed_lawn == 1:
        scene bg mydiningroom_night
    else:
        scene bg mydiningroom_night_grassy
    call screen scr_mydiningroom_night

screen scr_mydiningroom_night():
    imagebutton auto "btn mydiningroom_night_kitchen_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mykitchen_night_setup")
    if mowed_lawn == 1:
        imagebutton auto "btn mydiningroom_night_backyard_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_night_setup")
    else:
        imagebutton auto "btn mydiningroom_night_backyardgrassy_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_night_setup")
    use hud_overlay
