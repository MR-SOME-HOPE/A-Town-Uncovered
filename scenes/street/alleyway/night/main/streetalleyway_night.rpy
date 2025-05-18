###############
## Setup
## Story Path
label lbl_streetalleyway_night_setup:
    ## MAIN STORY
    # if main_story == 157:
    #     jump lbl_down_the_garbage_bin
    # elif main_story == 162:
    #     jump lbl_masks_off_get_dressed
    ## SIDE STORY
    ## Psycho Breakdown Alley
    if principallashley_path == 25 or principallashley_path == 26:
        jump lbl_psycho_breakdown_alley
    ## NO EVENT
    else:
        scene bg streetalleyway_night
        pov "{i}This place smells even more disgusting at night.{/i}"

    jump lbl_streetalleyway_night

###############
## Room Navigation
## This is the map for street alleyway during the night
label lbl_streetalleyway_night:

    scene bg streetalleyway_night
    call screen scr_streetalleyway_night

screen scr_streetalleyway_night():
    imagebutton auto "btn streetalleyway_night_street_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_night_setup")
    use hud_overlay

###############
## Labels
