###############
## Setup

## Story Path
label lbl_adultstore_day_setup:
    jump lbl_adultstore_day

###############
## Room Navigation
## This is the map for adult store during the day
label lbl_adultstore_day:

    scene bg adultstore_day
    call screen scr_adultstore_day

screen scr_adultstore_day():
    imagebutton auto "btn adultstore_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_adultstore_day_exit")
    if insexworld == 0:
        if hazel_path == 0:
            imagebutton auto "btn adultstore_day_hazel_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meet_hazel")
        else:
            imagebutton auto "btn adultstore_day_hazel_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_adultstore_day_hazel")
    else:
        imagebutton auto "btn adultstore_day_hazelsexworld_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_adultstore_day_hazel")
    use hud_overlay

###############
## Labels
label lbl_adultstore_day_exit:
    if sister_path == 18:
        jump lbl_sister_in_the_adultstore_2
    else:
        jump lbl_street_day_setup

label lbl_adultstore_counter_check:
    if store_counter == 1:
        show counter adultstore at right
        with dissolve
    else:
        pass
    return