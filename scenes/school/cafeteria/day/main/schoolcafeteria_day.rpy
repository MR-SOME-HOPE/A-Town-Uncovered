 ###############
## Setup
## Story Path
label lbl_schoolcafeteria_day_setup:
    ## NOT SEX WORLD OR TOO EARLY IN MAIN STORY
    if insexworld == 0 and main_story >= 16:

        ## Lashley Lunch Talk
        if principallashley_path == 2 and gtime == 1 and day >= 3:
            jump lbl_lashley_lunch_talk

        ## Eventless
        else:
            jump lbl_schoolcafeteria_day
            
    ## Eventless
    else:
        jump lbl_schoolcafeteria_day

###############
## Room Navigation
## This is the map for school cafeteria during the day
label lbl_schoolcafeteria_day:
    if 28 <= main_story <= 33:
        scene bg schoolcafeteria_daysexworld
    else:
        scene bg schoolcafeteria_day
    if gtime == 0 and main_story >= 12:
        show btn schoolcafeteria_day_cole_idle

    call screen scr_schoolcafeteria_day

screen scr_schoolcafeteria_day():
    if main_story >= 12:
        if gtime == 0:
            if cole_path == 0:
                imagebutton auto "btn schoolcafeteria_day_cole_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meet_cole")
            else:
                imagebutton auto "btn schoolcafeteria_day_cole_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolcafeteria_day_cole")
    imagebutton auto "btn schoolcafeteria_day_hallway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway2_day_setup")
    ## Sit With Allaway
    if missallaway_path == 3 and gtime == 1:
        imagebutton auto "btn schoolcafeteria_day_missallaway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sit_with_miss_allaway")
    ## Miss Allaway Date Plan
    elif missallaway_path == 13 and gtime == 1:
        imagebutton auto "btn schoolcafeteria_day_missallaway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_date_plan")

    use hud_overlay

###############
## Labels
