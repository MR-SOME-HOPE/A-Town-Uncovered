###############
## Setup
## Story Path
label lbl_managersoffice_day_setup:
    ## Workplace Introductions Pt 3
    if main_story == 95:
        jump lbl_workplace_introductions_part3
    ## NO EVENT
    else:
        jump lbl_managersoffice_day

###############
## Room Navigation
## This is the map for Manager's Office during the day
label lbl_managersoffice_day:
    scene bg managersoffice_daynight
    call screen scr_managersoffice_day

screen scr_managersoffice_day():
    imagebutton auto "btn managersoffice_daynight_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officefloor_day_setup")

    use hud_overlay

###############
## Labels
