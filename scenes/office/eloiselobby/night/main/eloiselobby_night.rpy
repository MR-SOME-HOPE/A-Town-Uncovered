###############
## Setup
## Story Path
label lbl_eloiselobby_night_setup:
    jump lbl_eloiselobby_night

###############
## Room Navigation
## This is the map for Eloise's Lobby during the night
label lbl_eloiselobby_night:
    scene bg eloiselobby_night
    call screen scr_eloiselobby_night

screen scr_eloiselobby_night():
    imagebutton auto "btn eloiselobby_night_elevator_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_night_setup")
    # imagebutton auto "btn eloiselobby_night_receptionist_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_eloiselobby_night_receptionist")
    imagebutton auto "btn eloiselobby_night_eloiseoffice_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_eloiseoffice_night_setup")

    add "btn eloiselobby_night_receptionist_idle"

    use hud_overlay

###############
## Labels
label lbl_eloiselobby_night_receptionist:
    # show img inconstruction # Fixed
    with hpunch
    $ renpy.pause()

    jump lbl_eloiselobby_night
