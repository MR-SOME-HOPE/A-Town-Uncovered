###############
## Setup
## Story Path
label lbl_supplyroom_day_setup:
    jump lbl_supplyroom_day

###############
## Room Navigation
## This is the map for Conference Room during the day
label lbl_supplyroom_day:
    scene bg supplyroom_daynight
    call screen scr_supplyroom_day

screen scr_supplyroom_day():
    imagebutton auto "btn supplyroom_daynight_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officefloor_day_setup")

    use hud_overlay

###############
## Labels
