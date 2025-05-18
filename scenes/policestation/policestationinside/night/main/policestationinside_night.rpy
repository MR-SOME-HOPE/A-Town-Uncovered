###############
## Setup
## Story Path
label lbl_policestationinside_night_setup:
    jump lbl_policestationinside_night

###############
## Room Navigation
## This is the map for Police Station inside during the night
label lbl_policestationinside_night:
    scene bg policestationinside_daynight
    call screen scr_policestationinside_night

screen scr_policestationinside_night():
    imagebutton auto "btn policestationinside_daynight_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_policestationoutside_night_setup")
    imagebutton auto "btn policestationinside_daynight_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_policestationinside_night_door")
    imagebutton auto "btn policestationinside_daynight_frontdesk_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_policestationinside_night_frontdesk")

    use hud_overlay

###############
## Labels
## Locations
label lbl_policestationinside_night_door:
    pov "{i}I am not authorized to go in there at this moment.{/i}"

    jump lbl_policestationinside_night

label lbl_policestationinside_night_frontdesk:
    pov "{i}I don't have any inquiries at the moment.{/i}"

    jump lbl_policestationinside_night
