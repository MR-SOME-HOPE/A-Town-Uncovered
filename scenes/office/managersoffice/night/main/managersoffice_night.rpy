###############
## Setup
## Story Path
label lbl_managersoffice_night_setup:
    jump lbl_managersoffice_night

###############
## Room Navigation
## This is the map for Manager's Office during the night
label lbl_managersoffice_night:
    scene bg managersoffice_daynight
    call screen scr_managersoffice_night

screen scr_managersoffice_night():
    imagebutton auto "btn managersoffice_daynight_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officefloor_night_setup")

    use hud_overlay

###############
## Labels
