###############
## Setup
## Story Path
label lbl_schoolhallway2_day_setup:
    ## Watch It
    if jack_path == 0 and gtime == 1:
        jump lbl_watch_it
    ## Naked Man of the Hour
    if main_story == 43:
        scene bg schoolhallway1_day
        if gtime == 0:
            show btn schoolhallway1_day_jacob_idle
        elif gtime == 1:
            show btn schoolhallway1_day_zariah_idle
        pov "I don't want to be walking through more of the school right now. I should get into class quickly."
        jump lbl_schoolhallway1_day
    # ## Operation Get The Flyers Back
    # elif main_story == 154:
    #     jump lbl_operation_get_the_flyers_back

    ## NOT THE SEX WORLD (Side Stories)
    if insexworld == 0:
        if sister_path == 4 or (24 <= main_story >= 35): ## Skip Jacob Random Encounter
            pass
        ## Porn Police
        if principallashley_path == 1 and gtime == 1 and main_story >= 17:
            if day == 0 or day == 2 or day == 4:
                jump lbl_porn_police
        elif principallashley_path == 22.2:
            jump lbl_the_last_straw
        else:
            ## Jacob Passing by
            if main_story >= 19:
                if date == 20 and (month == 2 or month == 3 or month == 5 or month == 6 or month == 8 or month == 9) and randomencounter == 0:
                    scene bg schoolhallway2_day
                    with fade
                    $ randomencounter = 1

                    jump lbl_randomevent_schoolhallway2_jacob_1

            else:
                jump lbl_schoolhallway2_day

###############
## Room Navigation
## This is the map for school hallway 2 during the day
label lbl_schoolhallway2_day:
    if 31 <= main_story <= 33:
        scene bg schoolhallway2_daysexworld
    else:
        scene bg schoolhallway2_day
    call screen scr_schoolhallway2_day

screen scr_schoolhallway2_day():
    if main_story >= 12:
        ## Default
        if gtime == 0:
            if luna_path == 0:
                imagebutton auto "btn schoolhallway2_day_luna_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meet_luna")
            else:
                imagebutton auto "btn schoolhallway2_day_luna_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway2_day_luna")
    imagebutton auto "btn schoolhallway2_day_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway1_day_setup")
    imagebutton auto "btn schoolhallway2_day_principal_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_principaloffice_day_setup")
    if 30 <= main_story <= 33:
        imagebutton auto "btn schoolhallway2_daysexworld_cafeteria_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolcafeteria_day_setup")
    else:
        imagebutton auto "btn schoolhallway2_day_cafeteria_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolcafeteria_day_setup")
    use hud_overlay

###############
## Labels
