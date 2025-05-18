###############
## Setup
## Story Path
label lbl_hospitalroom_night_setup_1:

    ## Nurse Hollick
    if main_story == 25:
        ## Show my hospital room during the night.
        scene bg hospitalroom_night_lightson_closed
        with fade

        jump lbl_nurse_hollick

    ## Your Annual Examination
    elif main_story == 26:
        $ edgingunhealthiness = 0
        scene bg yourannualexamination_1
        with fade

        jump lbl_your_annual_examination

## A Healthy Ejaculation
    elif main_story == 27:
        jump lbl_a_healthy_ejaculation
    else:
        jump lbl_hospitalroom_night_setup

label lbl_hospitalroom_night_setup:

## Show my hospital room during the night.
    scene bg hospitalroom_night_lightson_closed

    jump lbl_hospitalroom_night

###############
## Room Navigation
## This is the map for my hospital room during the night
label lbl_hospitalroom_night:

    scene bg hospitalroom_night_lightson_closed
    call screen scr_hospitalroom_night

screen scr_hospitalroom_night():
    #imagebutton auto "btn mybedroom_night_bed_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_night_bed")
    #imagebutton auto "btn mybedroom_night_desk_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_night_desk")
    #imagebutton auto "btn mybedroom_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_night_door")
    use hud_overlay

###############
## Labels