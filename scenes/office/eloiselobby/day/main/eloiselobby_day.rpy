###############
## Setup
## Story Path
label lbl_eloiselobby_day_setup:
    jump lbl_eloiselobby_day

###############
## Room Navigation
## This is the map for Eloise's Lobby during the day
label lbl_eloiselobby_day:
    scene bg eloiselobby_day
    call screen scr_eloiselobby_day

screen scr_eloiselobby_day():
    imagebutton auto "btn eloiselobby_day_elevator_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_day_setup")
    # imagebutton auto "btn eloiselobby_day_receptionist_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_eloiselobby_day_receptionist")
    imagebutton auto "btn eloiselobby_day_eloiseoffice_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_eloiseoffice_day_setup")

    add "btn eloiselobby_day_receptionist_idle"

    use hud_overlay

###############
## Labels
label lbl_eloiselobby_day_receptionist:
    # show img inconstruction # Fixed
    with hpunch
    $ renpy.pause()

    jump lbl_eloiselobby_day
