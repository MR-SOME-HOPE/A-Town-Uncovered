###############
## Setup
## Story Path
label lbl_officebathroom_night_setup:
    jump lbl_officebathroom_night

###############
## Room Navigation
## This is the map for Conference Room during the night
label lbl_officebathroom_night:
    scene bg officebathroom_daynight
    call screen scr_officebathroom_night

screen scr_officebathroom_night():
    imagebutton auto "btn officebathroom_daynight_officefloor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officefloor_night_setup")

    use hud_overlay

###############
## Labels
