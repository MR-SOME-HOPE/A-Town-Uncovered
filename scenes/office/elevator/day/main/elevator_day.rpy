###############
## Setup
## Story Path
label lbl_elevator_day_setup:
    if main_story == 91:
        pov "{i}I am not authorized to go in there at this moment.{/i}"
        jump lbl_officelobby_day
    elif main_story == 92:
        jump lbl_elevator_pitches_part_1
    elif main_story > 92:
        pass

###############
## Room Navigation
## This is the map for Elevator during the day
label lbl_elevator_day:
    scene bg elevator_daynight
    call screen scr_elevator_day

screen scr_elevator_day():
    imagebutton auto "btn elevator_daynight_buttons_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_daynight_buttons")

    use hud_overlay

###############
## Labels
label lbl_elevator_daynight_buttons:
    call screen scr_elevator_daynight_navigation
    #"Which floor do you want to go to?"
    #menu:
    #    "Top - Eloise's Floor":
    #        if gtime <= 1:
    #            jump lbl_eloiselobby_day_setup
    #        else:
    #            jump lbl_eloiselobby_night_setup
    #    "6th - Office Floor":
    #        if gtime <= 1:
    #            jump lbl_officefloor_day_setup
    #        else:
    #            jump lbl_officefloor_night_setup
    #    "Ground - Lobby":
    #        if gtime <= 1:
    #            jump lbl_officelobby_day_setup
    #        else:
    #            jump lbl_officelobby_night_setup

screen scr_elevator_daynight_navigation():
    #use hud_overlay
    add "bg elevatorbuttons_daynight"
    imagebutton auto "btn elevatorbuttons_daynight_eloise_button_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_daynight_buttons_eloise")
    imagebutton auto "btn elevatorbuttons_daynight_office_button_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_daynight_buttons_office")
    imagebutton auto "btn elevatorbuttons_daynight_lobby_button_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_daynight_buttons_lobby")

label lbl_elevator_daynight_buttons_eloise:
    if gtime <= 1:
        jump lbl_eloiselobby_day_setup
    else:
        jump lbl_eloiselobby_night_setup
label lbl_elevator_daynight_buttons_office:
    if gtime <= 1:
        jump lbl_officefloor_day_setup
    else:
        jump lbl_officefloor_night_setup
label lbl_elevator_daynight_buttons_lobby:
    if gtime <= 1:
        jump lbl_officelobby_day_setup
    else:
        jump lbl_officelobby_night_setup
