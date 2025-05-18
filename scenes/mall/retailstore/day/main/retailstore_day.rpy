###############
## Setup
## Story Path
label lbl_retailstore_day_setup:
    jump lbl_retailstore_day

###############
## Room Navigation
## This is the map for retailstore during the day
label lbl_retailstore_day:
    if main_story == 33:
        scene bg retailstore_daysexworld
    else:
        scene bg retailstore_day
    show btn retailstore_day_janae_idle
    call screen scr_retailstore_day

screen scr_retailstore_day():
    imagebutton auto "btn retailstore_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_setup")
    imagebutton auto "btn retailstore_day_giftcardrack_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_giftcard_day")
    imagebutton auto "btn retailstore_day_janae_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_janae")

    use hud_overlay

###############
## Labels
## People
label lbl_retailstore_day_janae:
    if janae_path == 0:
        jump lbl_meet_janae
    elif 30 <= main_story <= 33:
        jump lbl_mall_daysexworld_janae
    elif main_story == 84:
        jump lbl_investigations_janae
    else:
        jump lbl_how_can_i_help_you_0

label lbl_retailstore_counter_check:
    if store_counter == 1:
        show counter retailstore at right
        with dissolve
    else:
        pass
    return
