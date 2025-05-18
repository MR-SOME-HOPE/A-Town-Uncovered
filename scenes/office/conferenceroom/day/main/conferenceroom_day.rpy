###############
## Setup
## Story Path
label lbl_conferenceroom_day_setup:
    jump lbl_conferenceroom_day

###############
## Room Navigation
## This is the map for Conference Room during the day
label lbl_conferenceroom_day:
    scene bg conferenceroom_daynight
    call screen scr_conferenceroom_day

screen scr_conferenceroom_day():
    imagebutton auto "btn conferenceroom_daynight_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officefloor_day_setup")

    use hud_overlay

###############
## Labels
