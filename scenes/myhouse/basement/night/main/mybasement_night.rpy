###############
## Setup
## Story Path
label lbl_mybasement_night_setup:

## Before Unlocking Basement
    if sister_path <= 8.5:
        pov "{i}It's locked. It hasn't been open since we moved in.{/i}"

        jump lbl_mylivingroom_night_setup

    ## Build The Fort
    elif sister_path == 10:
        jump lbl_build_the_fort

    ## 20Q with Sister
    elif sister_path == 16:
        jump lbl_20q_with_sister

    ## Fort Destroyed
    elif sister_path == 26.5:
        jump lbl_fort_destroyed

    ## No Event
    else:
        jump lbl_mybasement_night

###############
## Room Navigation
## This is the map for my basement during the night
label lbl_mybasement_night:
    if sister_path <= 10:
        scene bg mybasement_lightsonmessy
    elif sister_path <= 26.5:
        scene bg mybasement_lightson
    elif sister_path <= 32:
        scene bg mybasement_lightsonwreck
    else:
        scene bg mybasement_lightson2
    call screen scr_mybasement_night

screen scr_mybasement_night():
    imagebutton auto "btn mybasement_lightson_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_night_setup")
    if main_story <= 4:
        pass
    else:
        use hud_overlay
