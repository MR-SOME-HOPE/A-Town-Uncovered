###############
## Setup
## Story Path
label lbl_classroom_day_setup:
    ## Make sure Intelligence doesn't go over 20
    if skill_intmax >= 20:
        $ skill_intmax = 20
    ## New Friends + English Teacher + Assignment
    if main_story == 5:
        scene bg classroom_day
        with fade
        jump lbl_new_friends
    ## How's School
    elif main_story == 16 and gtime == 0:
        scene bg classroom_day
        with fade
        jump lbl_hows_school
    ## Sex Everywhere in the Classroom
    elif main_story == 31:
        scene bg classroom_daysexworld
        with fade
        jump lbl_sex_everywhere_in_the_classroom
    ## Classroom Sexworld
    elif insexworld == 1:
        scene bg classroom_daysexworld
        jump lbl_classroom_day
    ## Recent Rumours
    elif main_story == 43:
        jump lbl_recent_rumours
    ## Discussing the Incident
    elif main_story == 44:
        show btn schoolhallway1_day_zariah_idle
        pov "{i}I'm supposed to go and see Director Lashley in her office.{/i}"
        jump lbl_schoolhallway1_day_setup
    ## School Anxiety
    elif main_story == 59 and day <= 4:
        jump lbl_school_anxiety
    ## Last Hour of School
    elif main_story == 61:
        jump lbl_last_hour_of_school
    ## Tension in the Room
    elif main_story == 71:
        jump lbl_the_tension_in_the_room
    # ## Cole Overhears
    # elif main_story == 145 and gtime == 1:
    #     jump lbl_cole_overhears
    # ## Discussing Stolen Evidence
    # elif main_story == 149 and gtime == 1:
    #     jump lbl_discussing_stolen_evidence
    # ## Confiscated Flyers
    # elif main_story == 150:
    #     jump lbl_confiscated_flyers
    # ## Welcome To The Team Cole
    # elif main_story == 152:
    #     jump lbl_welcome_to_the_team_cole



    ## NOT THE SEX WORLD (Side Stories)
    if insexworld == 0:
        ## Miss Allaway Scolding
        if missallaway_path == 2:
            scene bg classroom_day
            with fade
            jump lbl_miss_allaway_scolding
        elif missallaway_path == 3 and gtime == 1:
            scene bg classroom_day
            if luna_path >= 1:
                show btn classroom_day_luna_idle
            pov "Miss Allaway doesn't seem to have come back from lunch yet."
            jump lbl_classroom_day
        elif missallaway_path == 4 and insexworld == 0:
            scene bg classroom_day
            if gtime == 1 and luna_path >= 1:
                show btn classroom_day_luna_idle
            elif gtime == 0:
                show btn classroom_day_effie_idle
            pov "That's weird... Class is about to start, and Miss Allaway isn't here. Maybe she's in the bathroom."
            jump lbl_classroom_day
        elif missallaway_path == 13 and gtime == 1 and insexworld == 0:
            scene bg classroom_day
            if luna_path >= 1:
                show btn classroom_day_luna_idle
            pov "That's weird... Class is about to start, and Miss Allaway isn't here. Maybe she's in the cafetera still."
            jump lbl_classroom_day
        ## Detention with Allaway
        elif missallaway_path == 5 and gtime == 1:
            jump lbl_detention_with_allaway
        ## Allaway Picking on You
        elif missallaway_path == 7:
            jump lbl_allaway_picking_on_you
        ## Allaway is Paranoid
        elif missallaway_path == 10:
            jump lbl_allaway_is_paranoid
        ## Allaway is Cold
        elif missallaway_path == 15:
            jump lbl_allaway_is_cold
        ## Smarty Pants to Win Allaway / Flashback to Blackmail
        #elif missallaway_path == 16.5 and skill_intmax >= 19:#skill_int
        #    $ missallaway_path = 17
        #    jump lbl_classroom_day
        ## Left Miss Allaway in Flashback to Blackmail
        elif missallaway_path == 17.5:
            pov "{i}I should take some time away from her. I'm feeling really conflicted right now...{/i}"
            jump lbl_schoolhallway1_day_setup
        ## Ultimatum for a Beatdown
        elif missallaway_path == 18:
            jump lbl_ultimatum_for_a_beatdown
        ## Ask Allaway for Private Talk
        elif missallaway_path == 20:
            jump lbl_ask_allaway_for_private_talk
        ## Aftermath
        elif missallaway_path == 24:
            jump lbl_the_aftermath
        elif principallashley_path == 19:
            show btn schoolhallway1_day_zariah_idle
            pov "{i}I'm supposed to go and see Director Lashley in her office.{/i}"
            jump lbl_schoolhallway1_day_setup
        elif principallashley_path == 21 and day == 3:
            jump lbl_allaways_happy_accident
        elif principallashley_path in (22.1,22.2):
            scene bg schoolhallway1_day
            if principallashley_path == 22.1:
                pov "I'll spend some time in class."
                $ principallashley_path = 22.2
                $ gtime = 1
                scene black with fade
                $ renpy.pause(1.0)
            elif principallashley_path == 22.2:
                pov "Lashley wants to see me now in her office."
            jump lbl_schoolhallway1_day
        ## Cam Girl Text Setup
        if sister_path == 1:
            $ sister_path = 1.5
            $ townmap_enabled = 0
        elif hitomi_path == 4 and skill_int_times == 1:
            $ hitomi_path = 4.1
            $ townmap_enabled = 0

        ## Eventless
        else:
            jump lbl_classroom_day
    ## Eventless
    else:
        jump lbl_classroom_day

###############
## Room Navigation
## This is the map for my hallway during the day
label lbl_classroom_day:
    if 32 <= main_story <= 33:
        scene bg classroom_daysexworld
    else:
        scene bg classroom_day
    call screen scr_classroom_day

screen scr_classroom_day():
    imagebutton auto "btn classroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolhallway1_day_setup")
    imagebutton auto "btn classroom_day_desk_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_classroom_day_desk")
    #if (17 <= missallaway_path <= 18 and day < 4) or missallaway_path in (4, 19, 21) or missallaway_path == 13 and gtime:
    #    pass
    #else:
    if IsAllawayInClass():
        imagebutton auto "btn classroom_day_missallaway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_classroom_day_missallaway")
    if main_story >= 12:
        if insexworld == 0:
            if gtime == 1:
                if luna_path >= 1:
                    imagebutton auto "btn classroom_day_luna_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_classroom_day_luna")
                else:
                    imagebutton idle "btn classroom_day_luna_idle" xpos 0 ypos 0 focus_mask True action NullAction()
            elif gtime == 0:
                imagebutton auto "btn classroom_day_effie_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_classroom_day_effie")
        elif insexworld == 1:
            if gtime == 0:
                imagebutton auto "btn classroom_daysexworld_effie_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_classroom_day_effie")
    else:
        imagebutton idle "btn classroom_day_luna_idle" xpos 0 ypos 0 focus_mask True action NullAction()
    use hud_overlay
