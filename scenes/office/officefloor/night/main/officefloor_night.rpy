###############
## Setup
## Story Path
label lbl_officefloor_night_setup:
    jump lbl_officefloor_night

###############
## Room Navigation
## This is the map for Office Floor during the night
label lbl_officefloor_night:
    scene bg officefloor_night
    call screen scr_officefloor_night

screen scr_officefloor_night():
    imagebutton auto "btn officefloor_night_elevator_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_night_setup")
    imagebutton auto "btn officefloor_night_conferenceroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_conferenceroom_night_setup")
    imagebutton auto "btn officefloor_night_managersoffice_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_managersoffice_night_setup")
    imagebutton auto "btn officefloor_night_supplyroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_supplyroom_night")
    imagebutton auto "btn officefloor_night_officebathroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officebathroom_night")

    use hud_overlay

###############
## Labels
