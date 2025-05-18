###############
## Setup
## Story Path
label lbl_elevator_night_setup:
    if main_story == 91:
        pov "{i}I am not authorized to go in there at this moment.{/i}"
        jump lbl_officelobby_night
    elif main_story == 92:
        jump lbl_elevator_pitches_part_1
    elif main_story > 92:
        pass

###############
## Room Navigation
## This is the map for Elevator during the night
label lbl_elevator_night:
    scene bg elevator_daynight
    call screen scr_elevator_night

screen scr_elevator_night():
    imagebutton auto "btn elevator_daynight_buttons_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_daynight_buttons")

    use hud_overlay



###############
## Labels
