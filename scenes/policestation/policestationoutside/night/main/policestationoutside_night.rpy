###############
## Setup
## Story Path
label lbl_policestationoutside_night_setup:
    if main_story == 1:
        pov "{i}That's the police station, I {i}know{/i} how to get home. From what I remember, my house has a red roof.{/i}"
        jump lbl_townmap_setup
    else:
        jump lbl_policestationoutside_night

###############
## Room Navigation
## This is the map for Police Station outside during the night
label lbl_policestationoutside_night:
    scene bg policestationoutside_night
    call screen scr_policestationoutside_night

screen scr_policestationoutside_night():
    imagebutton auto "btn policestationoutside_night_entrance_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_policestationinside_night_setup")
    use hud_overlay

###############
## Labels
## Locations
