###############
## Setup
## Story Path
label lbl_schoolyard_day_setup:
    play ambience 'audio/ambience/schoolyardweekday_ambience.ogg' fadein 1.0
    ## Morning With Effie
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Sex Everywhere at School
    elif main_story == 29:
        scene bg schoolyard_daysexworld
        with fade
        jump lbl_sex_everywhere_at_school
    ## Schoolyard Sexworld
    elif 30 <= main_story <= 33:
        scene bg schoolyard_daysexworld
        jump lbl_schoolyard_day
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        jump lbl_naked_man_of_the_hour
    ## Something is Following You Setup
    elif main_story == 45 and (date >= 26 or 10 <= date <= 14) and day <= 4:
        $ main_story = 45.5
    ## Morning After Crime
    elif main_story == 58 and day <= 4:
        jump lbl_morning_after_crime
    ## Something is Wrong with Me
    elif (main_story == 69 or main_story == 70) and day <= 4:
        jump lbl_something_is_wrong_with_me
    # ## Effie's Dad Threatens You
    # if main_story == 142 and day <= 4 and gtime == 0:
    #     jump lbl_effies_dad_threatens_you
    # ## Mixed School Reputation
    # if main_story == 143 and day <= 4 and gtime == 0:
    #     jump lbl_mixed_school_reputation
    ## Bad Omens and a Broken Van
    elif principallashley_path == 20 and day == 1:
        jump lbl_bad_omens_and_a_broken_van



    ## NOT SEX WORLD SIDE STORIES
    if insexworld == 0:
        ## For my Phone Bill
        if sister_path == 3 and day <= 4:
            scene bg schoolyard_day
            with fade
            jump lbl_for_my_phone_bill
        ## Effie Mentions Sister
        elif sister_path == 6 and day <= 4:
            scene bg schoolyard_day
            with fade
            jump lbl_effie_mentions_sister
        elif principallashley_path in (22.1,22.2):
            scene bg schoolhallway1_day
            if principallashley_path == 22.1:
                pov "Lashley wants to see me in the afternoon. I'll just kill some time in class till then."
            elif principallashley_path == 22.2:
                pov "Lashley wants to see me now. I shouldn't leave."
            jump lbl_schoolhallway1_day
        ## NO EVENT
        else:
            ## Weekend
            if day >= 5:
                jump lbl_schoolyard_day_setup_2
            ## Weekday
            else:
                jump lbl_schoolyard_day
    ## NO EVENT
    else:
        ## Weekend
        if day >= 5:
            jump lbl_schoolyard_day_setup_2
        ## Weekday
        else:
            jump lbl_schoolyard_day

## WEEKDAY
label lbl_schoolyard_day_setup_2:

    scene bg schoolyard_dayweekend
    pov "The school isn't open on the weekends."

    jump lbl_schoolyard_day

###############
## Room Navigation
## This is the map for school yard during the day
label lbl_schoolyard_day:
    if 30 <= main_story <= 33:
        scene bg schoolyard_daysexworld
    else:
        if day <= 4:
            scene bg schoolyard_day
        elif day >= 5:
            scene bg schoolyard_dayweekend
    call screen scr_schoolyard_day

screen scr_schoolyard_day():
    imagebutton auto "btn schoolyard_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_day_door")
    if 30 <= main_story <= 33:
        imagebutton auto "btn schoolyard_daysexworld_gym_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_day_gym")
    else:
        if day <= 4:
            if main_story >= 12:
                if gtime == 0:
                    if edward_path == 0:
                        imagebutton auto "btn schoolyard_day_edward_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meet_edward")
                    else:
                        imagebutton auto "btn schoolyard_day_edward_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_day_edward")
                else:
                    if jaiden_path == 0:
                        imagebutton auto "btn schoolyard_day_jaiden_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_meet_jaiden")
                    else:
                        imagebutton auto "btn schoolyard_day_jaiden_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_day_jaiden")
            imagebutton auto "btn schoolyard_day_gym_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_day_gym")
        else:
            imagebutton auto "btn schoolyard_dayweekend_gym_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_day_gym")

    use hud_overlay

###############
## Labels
## Conversations
## Sex Everywhere at School ##
label lbl_sex_everywhere_at_school:
    pov "{i}What. In the hell. Is going on?!{/i}"
    pov "{i}What is wrong with this town?!{/i}"
    pov "{i}Am I hallucinating? Everyone's. Just.. Everywhere...{/i}"
    $ main_story = 30
    $ renpy.notify("New Objective: Get to class")

    jump lbl_schoolyard_day_setup

## Locations
label lbl_schoolyard_day_door:
    if day >= 5:
        jump lbl_schoolyard_day_setup_2
    else:
        play ambience 'audio/ambience/schoolinteriorweekday_ambience.ogg' fadein 1.0
        jump lbl_schoolhallway1_day_setup

label lbl_schoolyard_day_gym:
    if day >= 5:
        jump lbl_schoolyard_day_setup_2
    else:
        jump lbl_schoolgym_day_setup
