###############
## Setup
## Story Path
label lbl_mykitchen_day_setup:
    $ mykitchen_day_chalkboard = renpy.random.randint(1,10)

    scene bg mykitchen_day
    ## Morning Mom
    if main_story == 2:
        with fade
        play music "audio/music/a_family_home.ogg"
        jump lbl_morning_mom
    ## Morning Dad
    elif main_story == 4:
        with fade
        jump lbl_morning_dad
    ## Found a Job
    elif main_story == 21:
        with fade
        jump lbl_found_a_job
    ## A Stranger Morning
    elif main_story == 28:
        with fade
        jump lbl_a_stranger_morning
    ## Three Staged Breakfast
    elif main_story == 50:
        jump lbl_three_staged_breakfast
    ## Mom is Worried
    elif main_story == 69:
        jump lbl_mom_is_worried
    ## Sweet Morning After
    elif main_story == 81:
        jump lbl_sweet_morning_after
    ## Mom Wants To Know
    elif main_story == 99:
        jump lbl_mom_wants_to_know
    # ## Seeing Sexworld Mom Again
    # elif main_story == 127:
    #     jump lbl_seeing_sexworld_mom_again
    # ## Comparing Flyer Maps
    # elif main_story == 147:
    #     jump lbl_comparing_flyer_maps

    ## NOT IN SEX WORLD SIDE STORIES
    if insexworld == 0:
        ## Stay with Me
        if mum_path == 5:
            with fade
            ## mompastsunset_attend 0 = Yet to go | 1 = Went but missed it | 2 = Refused to go | 3 = Refused to go once went | 4 = Yet to go AGAIN | 5 = Missed the first time
            default mompastsunset_attend = 0
            default mompastsunset_went = 0
            jump lbl_mom_stay_with_me
        ## Mom in bedroom
        if mum_path == 11 and sister_path >= 26:
            pov "{i}What's that noise coming from [missus]\'s bedroom?{/i}"
            jump lbl_myhallway_day
        ## Cheer Mom Up Payback
        elif mum_path >= 20 and cheermomup_owe >= 1:
            with fade
            jump lbl_cheer_mom_up_payback
        ## Dad Back from Out of Town
        elif mum_path == 25 and day >= 5:
            jump lbl_dad_back_from_out_of_town
        elif sister_path == 36:
            scene bg myhallway_day
            pov "{i}I should see where [sis] is, first.{/i}"
            jump lbl_myhallway_day
        ## Sister Eating Mom for Breakfast
        if mumsis_path == 8 and mum_path >= 22 and sister_path >= 22 and date >= 18 and gtime == 0:
            jump lbl_sister_eating_mom_for_breakfast
        ## Lashley - Ribbon Mating Press (Visit)
        if principallashley_path >= 28 and day == 6 and date >= 21 and lashleyribbonmatingpress_call == 0:
            jump lbl_lashley_ribbon_mating_press_call
        ## No Event
        else:
            jump lbl_mykitchen_day
    ## No Event
    else:
        jump lbl_mykitchen_day

###############
## Room Navigation
## This is the map for my kitchen during the day
label lbl_mykitchen_day:

    scene bg mykitchen_day
    call screen scr_mykitchen_day

screen scr_mykitchen_day():
    add "img mykitchen_day_chalkboard_[mykitchen_day_chalkboard]"

    ## Room Interactions
    if mum_path == 7 or (11 <= mum_path <= 16) or (mum_path == 17 and day != 4) or ((mum_path == 22 or mum_path == 22.5) and day == 4): ## Mom Story Pass
        pass
    elif (day == 2 and gtime == 0): ## Shower Schedule
        pass
    elif gtime == 1: ## Living Room
        pass
    elif main_story == 78:#after girls_upstairs sequence
        pass
    ## Mom Sis Bathing Together
    elif mumsis_path == 5 and mum_path >= 17.5 and sister_path >= 18 and date <= 12:
        pass
    elif mumsis_path == 6:
        pass
    else:
        imagebutton auto "btn mykitchen_day_mother_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mykitchen_day_mother")

    ## NORMAL
    imagebutton auto "btn mykitchen_day_stairs_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_day_setup")
    imagebutton auto "btn mykitchen_day_livingroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_day_setup")
    imagebutton auto "btn mykitchen_day_dining_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mydiningroom_day_setup")
    use hud_overlay

###############
## Label
