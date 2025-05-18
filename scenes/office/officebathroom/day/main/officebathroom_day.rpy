###############
## Setup
## Story Path
label lbl_officebathroom_day_setup:
    jump lbl_officebathroom_day

###############
## Room Navigation
## This is the map for Office Bathroom during the day
label lbl_officebathroom_day:
    scene bg officebathroom_daynight
    call screen scr_officebathroom_day

screen scr_officebathroom_day():
    imagebutton auto "btn officebathroom_daynight_officefloor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officefloor_day_setup")

    use hud_overlay

###############
## Labels
