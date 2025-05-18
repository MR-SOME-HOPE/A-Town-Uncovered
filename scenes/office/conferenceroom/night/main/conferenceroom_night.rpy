###############
## Setup
## Story Path
label lbl_conferenceroom_night_setup:
    jump lbl_conferenceroom_night

###############
## Room Navigation
## This is the map for Conference Room during the night
label lbl_conferenceroom_night:
    scene bg conferenceroom_daynight
    call screen scr_conferenceroom_night

screen scr_conferenceroom_night():
    imagebutton auto "btn conferenceroom_daynight_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officefloor_night_setup")

    use hud_overlay

###############
## Labels
