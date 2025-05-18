###############
## Setup
## Story Path
label lbl_principaloffice_day_setup:
    ## Main Story
    ## Discussing the Incident
    if main_story == 44:
        jump lbl_discussing_the_incident
    ## Lashley's Strange Noise
    elif main_story == 73:
        jump lbl_lashleys_strange_noise

    ## NOT IN THE SEX WORLD
    if insexworld == 0:
        ## lashley lunch talk
        if principallashley_path == 2 and gtime == 1 and day >= 3:
            scene bg schoolhallway2_day
            pov "The office is locked. It doesn't sound like Director Lashley's in there."
            jump lbl_schoolhallway2_day
        ## What Lashley Likes
        elif principallashley_path == 3 and gtime == 1 and day <= 2:
            jump lbl_what_lashley_likes
        ## Framed
        elif principallashley_path == 5:
            jump lbl_framed
        ## Natural Urges
        elif principallashley_path == 6:
            jump lbl_natural_urges
        ## Very Special Prayer
        elif principallashley_path == 9 and gtime == 1 and main_story >= 17:
            jump lbl_very_special_prayer
        ## Bottoms Up
        elif principallashley_path == 12:
            jump lbl_bottoms_up
        ## Lashley's Busy
        elif principallashley_path == 13:
            jump lbl_lashleys_busy
        ## Lashley's Busy Post
        elif principallashley_path == 13.5:
            scene bg schoolhallway2_day
            pov "Director Lashley didn't want to be disturbed today."
            jump lbl_schoolhallway2_day
        ## Lashley Aftermath
        elif principallashley_path == 15:
            jump lbl_the_lashley_aftermath
        ## Lashley Aftermath Post
        elif principallashley_path == 15.1:
            pov "That's enough for today."
            jump lbl_schoolhallway2_day
        ## Hints of a Problem
        elif principallashley_path == 16:
            jump lbl_hints_of_a_problem
        ## Distractions
        elif principallashley_path == 19:
            jump lbl_distractions
        ## Aggressive Approach
        elif principallashley_path == 22 and day == 4 and gtime == 0:
            jump lbl_aggressive_approach
        ## Aggressive Approach Post
        elif principallashley_path == 22.1:
            scene bg schoolhallway2_day
            pov "I'm supposed to come back in the afternoon, after class."
            jump lbl_schoolhallway2_day
        ## Before Officially Meet Director Lashley
        elif principallashley_path == 0:
            scene bg schoolhallway2_day
            pov "I don't think I need to go in there right now. My classroom is downstairs."
            jump lbl_schoolhallway2_day
    ## NO EVENT
    else:
        jump lbl_principaloffice_day

###############
## Room Navigation
## This is the map for principal's office during the day
label lbl_principaloffice_day:

    scene bg principaloffice_day
    call screen scr_principaloffice_day

screen scr_principaloffice_day():
    imagebutton auto "btn principaloffice_day_hallway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway2_day_setup")
    imagebutton auto "btn principaloffice_day_principallashley_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_principaloffice_day_principallashley")
    use hud_overlay

###############
## Labels
label lbl_principaloffice_counter_check:
    if store_counter == 1:
        show counter principaloffice at right
        with dissolve
    else:
        pass
    return
