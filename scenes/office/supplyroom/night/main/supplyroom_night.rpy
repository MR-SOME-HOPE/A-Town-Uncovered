###############
## Setup
## Story Path
label lbl_supplyroom_night_setup:
    jump lbl_supplyroom_night

###############
## Room Navigation
## This is the map for Conference Room during the night
label lbl_supplyroom_night:
    scene bg supplyroom_daynight
    call screen scr_supplyroom_night

screen scr_supplyroom_night():
    imagebutton auto "btn supplyroom_daynight_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officefloor_night_setup")

    use hud_overlay

###############
## Labels
