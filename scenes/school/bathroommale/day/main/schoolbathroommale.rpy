###############
## Setup
## Story Path
label lbl_schoolbathroommale_day_setup:

    ## NOT INSIDE THE SEXWORLD
    if not 31 <= main_story <= 35:
        ## Caught Allaway with Jack
        if missallaway_path == 17 and day <= 3:
            jump lbl_caught_allaway_with_jack
        ## Private Talk with Allaway
        elif missallaway_path == 21:
            pov "..."
            pov "{i}The bathroom is locked...{/i}"
            pov "{i}That fuckin cunt must be in there with her...{/i}"

            jump lbl_schoolhallway1_day_setup

    ## Eventless
    else:
        jump lbl_schoolbathroommale_day

###############
## Room Navigation
## This is the map for school bathroom male during the day
label lbl_schoolbathroommale_day:

    scene bg schoolbathroommale_day
    call screen scr_schoolbathroommale_day

screen scr_schoolbathroommale_day():
    if main_story >= 12:
        if gtime == 1:
            if phil_path == 0:
                imagebutton auto "btn schoolbathroom_day_phil_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meet_phil")
            else:
                imagebutton auto "btn schoolbathroom_day_phil_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroommale_day_phil")
    imagebutton auto "btn schoolbathroom_day_hallway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway1_day_setup")
    use hud_overlay

###############
## Labels
