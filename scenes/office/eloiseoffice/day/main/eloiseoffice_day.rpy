###############
## Setup
## Story Path
label lbl_eloiseoffice_day_setup:
    if main_story == 115:
        jump lbl_prelude_to_the_tour
    jump lbl_eloiseoffice_day

###############
## Room Navigation
## This is the map for Eloise's Office during the day
label lbl_eloiseoffice_day:
    scene bg eloiseoffice_day
    call screen scr_eloiseoffice_day

screen scr_eloiseoffice_day():
    imagebutton auto "btn eloiseoffice_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_eloiselobby_day_setup")

    use hud_overlay

###############
## Labels
