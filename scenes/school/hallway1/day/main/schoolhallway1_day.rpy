###############
## Setup
## Story Path
label lbl_schoolhallway1_day_setup:
    ## I Work at the Cafe
    if main_story == 8:
        scene bg schoolhallway1_day
        with fade
        jump lbl_i_work_at_the_cafe
    ## Come Read Comics
    elif main_story == 17:
        if gtime == 0:
            scene bg classroom_day
            show btn classroom_day_door_idle
            show btn_classroom_day_effie_idle2
            show btn_classroom_day_missallaway_idle2
            pov "{i}I should stay for class right now.{/i}"
            jump lbl_classroom_day
        else:
            scene bg schoolhallway1_day
            with fade
            jump lbl_come_read_comics
    ## Sex Everywhere in the Hallways
    elif main_story == 30:
        scene bg schoolhallway1_daysexworld
        show btn schoolhallway1_day_jacob_idle
        with fade
        jump lbl_sex_everywhere_in_the_hallways
    ## School Hallway 1 Sexworld
    elif 30 <= main_story <= 34:
        scene bg schoolhallway1_daysexworld
        jump lbl_schoolhallway1_day
    ## There's Naked Pictures
    elif main_story == 42:
        jump lbl_theres_naked_pictures
    ## Crossroads
    elif main_story == 62:
        jump lbl_crossroads_of_the_day
    # ## School Detention Instead
    # elif main_story == 144:
    #     jump lbl_school_detention_instead

    ## SIDE STORY
    ## Cam Girl Text
    if sister_path == 1.5:
        jump lbl_cam_girl_text
    ## That Shit Ain't Mine
    if principallashley_path == 4 and gtime == 0:
        jump lbl_that_shit_aint_mine
    ## Bathroom Stakeout 1
    elif principallashley_path == 7 and gtime == 1:
        jump lbl_bathroom_stakeout_1
    ## Bathroom Stakeout 2
    elif principallashley_path == 8 and gtime == 1:
        jump lbl_bathroom_stakeout_2
    ## Jealousy
    elif principallashley_path == 18:
        jump lbl_jealousy
    ## Lord Have Mercy
    elif principallashley_path == 28:
        jump lbl_lord_have_mercy
    ## Transmogrified
    elif hitomi_path == 4.1:
        jump lbl_transmogrified
    ## NO EVENT
    else:
        ## Miss Allaway Passing By 1
        if main_story >= 16:
            if date == 16 and (month == 1 or month == 3 or month == 5 or month == 8 or month == 11) and randomencounter == 0:
                $ randomencounter = 1
                scene bg schoolhallway1_day
                with fade
                jump lbl_randomevent_schoolhallway1_missallaway_1
        else:
            jump lbl_schoolhallway1_day

###############
## Room Navigation
## This is the map for school hallway 1 during the day
label lbl_schoolhallway1_day:
    if 31 <= main_story <= 33:
        scene bg schoolhallway1_daysexworld
    else:
        scene bg schoolhallway1_day
    call screen scr_schoolhallway1_day

screen scr_schoolhallway1_day():
    if gtime == 0:
        if main_story <= 5:
            pass
        else:
            imagebutton auto "btn schoolhallway1_day_jacob_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway1_day_jacob")
    if main_story >= 12:
        if gtime == 1:
            if zariah_path == 0:
                imagebutton auto "btn schoolhallway1_day_zariah_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meet_zariah")
            else:
                imagebutton auto "btn schoolhallway1_day_zariah_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway1_day_zariah")
    if 30 <= main_story <= 33:
        imagebutton auto "btn schoolhallway1_daysexworld_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway2_day_setup")
    else:
        imagebutton auto "btn schoolhallway1_day_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway2_day_setup")
    imagebutton auto "btn schoolhallway1_day_maletoilets_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroommale_day_setup")
    imagebutton auto "btn schoolhallway1_day_femaletoilets_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolbathroomfemale_day_setup")
    imagebutton auto "btn schoolhallway1_day_classroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_classroom_day_setup")
    imagebutton auto "btn schoolhallway1_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_day_setup")
    use hud_overlay

###############
## Labels
