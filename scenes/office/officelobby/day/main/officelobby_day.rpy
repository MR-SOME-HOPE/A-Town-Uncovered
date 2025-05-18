###############
## Setup
## Story Path
label lbl_officelobby_day_setup:
    if main_story == 90:
        pov "{i}I don't work here just yet. I need to meet [dadname] in the afternoon to get set up.{/i}"
        call screen scr_officeoutside_day
    jump lbl_officelobby_day

###############
## Room Navigation
## This is the map for Office Lobby during the day
label lbl_officelobby_day:
    scene bg officelobby_day
    show btn_officelobby_day_skylar_idle2
    show btn_officelobby_day_carmen_idle2
    call screen scr_officelobby_day

screen scr_officelobby_day():
    imagebutton auto "btn officelobby_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officeoutside_day_setup")
    imagebutton auto "btn officelobby_day_elevator1_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_day_setup")
    imagebutton auto "btn officelobby_day_elevator2_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_day_setup")
    imagebutton auto "btn officelobby_day_carmen_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officelobby_day_carmen")
    imagebutton auto "btn officelobby_day_skylar_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officelobby_day_skylar")

    use hud_overlay

###############
## Labels
label lbl_officelobby_day_elevator:
    jump lbl_elevator_day_setup

label lbl_officelobby_day_carmen:
    if main_story == 91:
        jump lbl_first_step_into_the_rat_race
    else:
        pov "{i}I don't need to talk to them right now.{/i}"
        # show img inconstruction # Fixed
        # with hpunch
        # $ renpy.pause()

        jump lbl_officelobby_day

label lbl_officelobby_day_skylar:
    if main_story == 91:
        jump lbl_first_step_into_the_rat_race
    else:
        pov "{i}I don't need to talk to them right now.{/i}"
        # show img inconstruction # Fixed
        # with hpunch
        # $ renpy.pause()

        jump lbl_officelobby_day


## Office Lobby Counter
label lbl_officelobbysingle_counter_check:
    if store_counter == 1:
        show counter officelobbysingle at right
        with dissolve
    else:
        pass
    return

label lbl_officelobbydouble_counter_check:
    if store_counter == 1:
        show counter officelobbysingle at right
        with dissolve
    else:
        pass
    return
