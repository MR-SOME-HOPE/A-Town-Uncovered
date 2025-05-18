###############
## Setup
## Story Path
label lbl_mybedroom_night_setup:
    stop ambience fadeout 2.0

    ## The First Night
    if main_story == 1:
        scene black

        jump lbl_the_first_night

    ## NOT IN THE SEX WORLD
    if insexworld == 0:
        ## Stay With Mom Attendance Result
        if mum_path == 6:
            ## mompastsunset_attend == 1 & 5 - Missed | 2 & 3 - Refused to go
            if mompastsunset_attend == 0 and mompastsunset_went == 0:
                $ mompastsunset_attend = 5
                $ mum_path = 7

                jump lbl_mybedroom_night_setup
            elif mompastsunset_attend == 4 and mompastsunset_went == 0:
                $ mompastsunset_attend = 1
                $ mum_path = 7

                jump lbl_mybedroom_night_setup
            elif mompastsunset_attend == 2 or mompastsunset_attend == 3:
                $ mum_path = 7

                jump lbl_mybedroom_night_setup
            else:
                pass
        ## Feeling Abandoned
        elif mum_path == 8:
            jump lbl_feeling_abandoned
        ## Mom in my Bed
        elif mum_path == 10:
            if savemomfromdad == 1:
                jump lbl_mom_in_my_bed
            else:
                $ mum_path = 11
                jump lbl_mybedroom_night_setup
        ## Incest Porno with Mom (Fail Restart)
        elif mum_path == 22.5:
            $ mum_path = 22
        ## Mom Sex After Dinner Date
        elif mum_path == 28:
            $ mum_path = 29
            $ townmap_enabled = 1
            jump lbl_mom_bedroom_hscene_after_date
        ## Mom After Dinner Date Sex
        elif mum_path == 29:
            scene bg mybedroom_night
            with fade
            $ mum_path = 30
            jump lbl_mybedroom_night
        ## Mom After Dinner Date Sex
        elif mum_path == 30.5:
            $ mum_path = 31
            jump lbl_mom_bedroom_hscene_after_bj
        ## Mom Bedroom Sex
        elif mum_path >= 31 and mum_bedroomsex == 1:
            jump lbl_mom_bedroom_hscene_after_bj

        ## Dad Apologizing
        if sister_path == 37 and day != 2:
            $ townmap_enabled = 1
        ## Camgurl Substitute Favour (DECLINED RESTART)
        elif sister_path == 38.5 and day != 2:
            $ sister_path = 38
        ## Camgurl Substitute Favour (FAIL RESTART)
        elif sister_path == 39 and day == 2:
            jump lbl_camgurl_substitute_favour_fail
        ## Flashback to Blackmail Leave Allaway Post Setup
        if missallaway_path == 17.5:
            $ missallaway_path = 18
            jump lbl_mybedroom_night
        ## Beat the Shit out of Jack Training
        elif missallaway_path == 19.1:
            $ missallaway_path == 19
        ## The Night of the Job Text
        elif missallaway_path == 23:
            jump lbl_the_night_of_the_job_text

        ## Invited Miss Allaway for Sex at your Place but left her hanging
        if allawaybedroomsex_sneakherin == 1:
            $ allawaybedroomsex_sneakherin = 2
        ## Invited Miss Allaway for Sex at your Place Reset
        elif allawaybedroomsex_sneakherin == 3:
            $ allawaybedroomsex_sneakherin = 0

        ## Natural Urges Setup
        if principallashley_path == 5.5:
            if date == 8 or date == 18 or date == 28:
                $ principallashley_path = 6

        ## Stressed From Work Pre
        if mumsis_path == 2:
            $ townmap_enabled = 0
        ## Scolding for Spying on Them
        elif mumsis_path == 6:
            jump lbl_scolding_for_spying_on_them
        ## Mom and Sis Getting Close
        elif mumsis_path == 10:
            jump lbl_mom_and_sis_getting_close

        ## Close To You Like This
        if effie_path == 5:
            jump lbl_close_to_you_like_this

        ## The Text Ready
        if date >= 14 and 0 not in (violette_path, grundlesam_path, janae_path, meghan_path, cole_path, zariah_path, luna_path, jaiden_path, edward_path, hazel_path, phil_path, lailah_path): #and effie_path >= 2: ##Why effie_path >=2?
            ## MEET THE NEW STUDENTS AND FRIENDS'S PARENTS
            $ thetext_ready = 1
        ## The Text
        if main_story == 22 and (day <= 3 or day == 6) and thetext_reject == 0 and thetext_ready == 1 and date >= 14:
            ## Text won't show duing this part of Mom's Story or sis and pov released from jail drunk
            if 12 <= mum_path <= 17.5 or sister_path == 22:
                pass
            else:
                jump lbl_the_text
        # ## Stressful Times To Come
        # elif main_story == 87:
        #    jump lbl_stressful_times_to_come
        # ## Some Welcome Back Gifts
        # elif main_story == 164:
        #     if inventory.has_item(Items.flowerlilies) or inventory.has_item(Items.flowerroses) or inventory.has_item(Items.flowersunflowers):
        #         if inventory.has_item(Items.videogameaction) or inventory.has_item(Items.videogamedatingsim) or inventory.has_item(Items.videogameshooter):
        #             if not inventory.has_item(Items.chocolatebox):
        #                 $ main_story = 165
        else:
            jump lbl_mybedroom_night

###############
## Room Navigation
## This is the map for my bedroom during the night
label lbl_mybedroom_night:

    scene bg mybedroom_night
    call screen scr_mybedroom_night

screen scr_mybedroom_night():
    imagebutton auto "btn mybedroom_night_bed_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_night_bed")
    imagebutton auto "btn mybedroom_night_desk_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_desk")
    imagebutton auto "btn mybedroom_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_night_setup")
    imagebutton auto "btn mybedroom_night_calander_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_calander")
    # if vrheadset_chest == 1:
    imagebutton auto "btn mybedroom_night_chest_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_chest_night")
    use hud_overlay

###############
## Labels
## Items
label lbl_mybedroom_night_bed:
## NOT IN THE SEX WORLD
    if insexworld == 0:
    ## The Text - Meet Effie at the Park
        if main_story == 23:
            pov "{i}I should meet Effie at the park like I agreed to.{/i}"
            jump lbl_mybedroom_night_setup
    ## The Polaroid
        elif main_story == 67 and day not in (4,5):
            jump lbl_the_polaroid
        ## An Awkward Dinner Situation
        elif main_story == 85:
            pov "{i}[missus] wanted me downstairs in the dining room to help set up for dinner.{/i}"
            jump lbl_mybedroom_night_setup
        elif main_story == 86:
            jump lbl_stressful_times_to_come
    ## Mom at the Park
        if mum_path == 21:
            pov "{i}I need to find out where Mom is first.{/i}"
            jump lbl_mybedroom_night_setup
    ## Mom Midnight Fun
        elif (mum_path == 23 and day != 4) or (mum_path >= 23 and (date == 8 or date == 15 or date == 29) and incestpornowithmom == 1 and day != 4):
            scene black
            with fade
            jump lbl_mom_midnight_fun
    ## Help Build a Fort
        if sister_path == 9 and (day == 2 or day == 6):
            if 11 <= mum_path <= 17:
                pass
            else:
                scene black
                with fade
                jump lbl_help_build_a_fort
    ## Build a Fort with Sister
        elif sister_path == 10:
            pov "{i}I can't go back to sleep, [sister] is waiting for me downstairs.{/i}"
            jump lbl_mybedroom_night_setup
    ## 20 Questions Game
        elif sister_path == 16:
            pov "{i}I can't go to sleep. I need to meet [sister] downstairs in the basement.{/i}"
            jump lbl_mybedroom_night_setup
    ## Fort Destroyer
        elif sister_path == 26.5:
            pov "{i}I can't just ignore what I heard. [sister]'s crying for help in the basement.{/i}"
            jump lbl_mybedroom_night_setup
    ## Sister Nightmare
        elif sister_path == 34 and day == 4:
            jump lbl_sisters_nightmare
        ## Camgurl Substitute Favour (FAIL RESTART)
        elif sister_path == 39 and day == 2:
            jump lbl_camgurl_substitute_favour_fail_naked
        ## Midnight Booty Calls
        elif principallashley_path == 13.5:
            jump lbl_midnight_booty_calls
        ##
        elif principallashley_path == 14 and not 21 <= sister_path <= 22:
            pov "{i}Director Lashley is expecting me at the school.{/i}"
            jump lbl_mybedroom_night_setup
        ##
        elif missallaway_path == 21:
            pov "{i}I need to meet Allaway in the park just now.{/i}"
            jump lbl_mybedroom_night_setup
        ## Zariah's Party Pt. 1
        elif principallashley_path == 23 and day == 5:
            pov "{i}Zariah's party at the nightclub is just now.{/i}"
            jump lbl_mybedroom_night_setup
    ## Movie Dream
        if moviedate >= 1:
            jump lbl_movie_dream
        else:
            menu:
                "Nap" if gtime == 2:
                    jump lbl_mybedroom_night_nap
                "Sleep":
                    jump lbl_mybedroom_night_sleep
                "Nevermind":
                    jump lbl_mybedroom_night_setup
    ## No Event
    else:
        menu:
            "Nap" if gtime == 2:
                jump lbl_mybedroom_night_nap
            "Sleep":
                jump lbl_mybedroom_night_sleep
            "Nevermind":
                jump lbl_mybedroom_night_setup
