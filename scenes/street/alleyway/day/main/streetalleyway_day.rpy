###############
## Setup
## Story Path
label lbl_streetalleyway_day_setup:
    ## MAIN STORY
    if main_story == 172: # Nothing here
        pass
        # jump lbl_revise_the_final_plan
    ## NO EVENT
    else:
        scene bg streetalleyway_day
        pov "{i}This place smells disgusting.{/i}"

        jump lbl_streetalleyway_day

###############
## Room Navigation
## This is the map for street alleyway during the day
label lbl_streetalleyway_day:

    scene bg streetalleyway_day
    call screen scr_streetalleyway_day

screen scr_streetalleyway_day():
    imagebutton auto "btn streetalleyway_day_street_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_day_setup")
    use hud_overlay

###############
## Labels
