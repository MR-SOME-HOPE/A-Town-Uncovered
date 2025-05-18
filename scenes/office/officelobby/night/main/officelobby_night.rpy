###############
## Setup
## Story Path
label lbl_officelobby_night_setup:
    if main_story == 90:
        pov "{i}I don't work here just yet. I need to meet [dadname] in the afternoon to get set up.{/i}"
        call screen scr_officeoutside_night
    elif main_story == 98:
        jump lbl_eloises_tour
    jump lbl_officelobby_night

###############
## Room Navigation
## This is the map for Office Lobby during the night
label lbl_officelobby_night:
    scene bg officelobby_night
    call screen scr_officelobby_night

screen scr_officelobby_night():
    imagebutton auto "btn officelobby_night_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officeoutside_night_setup")
    imagebutton auto "btn officelobby_night_elevator1_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_night_setup")
    imagebutton auto "btn officelobby_night_elevator2_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_night_setup")

    use hud_overlay

###############
## Labels
label lbl_officelobby_night_carmen:
    pov "{i}I don't need to talk to them right now.{/i}"
    # show img inconstruction # Fixed
    # with hpunch
    # $ renpy.pause()
    jump lbl_officelobby_night
    

label lbl_officelobby_night_skylar:
    pov "{i}I don't need to talk to them right now.{/i}"
    # show img inconstruction # Fixed
    # with hpunch
    # $ renpy.pause()
    jump lbl_officelobby_night
