###############
## Setup
## Story Path
label lbl_policestationoutside_day_setup:
    if main_story <= 5:
        pov "{i}I can't go there yet. I have to get to university.{/i}"
        jump lbl_townmap_setup
    else:
        jump lbl_policestationoutside_day

###############
## Room Navigation
## This is the map for Police Station outside during the day
label lbl_policestationoutside_day:
    scene bg policestationoutside_day
    call screen scr_policestationoutside_day

screen scr_policestationoutside_day():
    imagebutton auto "btn policestationoutside_day_entrance_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_policestationinside_day_setup")
    use hud_overlay

###############
## Labels
## Locations
