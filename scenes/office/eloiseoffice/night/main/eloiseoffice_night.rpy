###############
## Setup
## Story Path
label lbl_eloiseoffice_night_setup:
    jump lbl_eloiseoffice_night

###############
## Room Navigation
## This is the map for Eloise's Office during the night
label lbl_eloiseoffice_night:
    scene bg eloiseoffice_night
    call screen scr_eloiseoffice_night

screen scr_eloiseoffice_night():
    imagebutton auto "btn eloiseoffice_night_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_eloiselobby_night_setup")

    use hud_overlay

###############
## Labels
