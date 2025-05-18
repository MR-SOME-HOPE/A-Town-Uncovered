###############
## Setup
## Story Path
label lbl_mybedroom_day_setup:
    stop ambience fadeout 2.0
    hide screen scr_gui_phone_skills

## Gtime Failsafe
    # if gtime <= 6:
    #     pass
    # else:
    #     $ gtime = 0

    ## NOT IN THE SEX WORLD
    if insexworld == 0:
        ## After 'What Are You Watching?'
        if mum_path == 1:
            $ townmap_enabled = 0
        ## After 'Mom Fallen Asleep'
        elif mum_path == 5:
            $ townmap_enabled = 0
        ## Stay With Mom Attendance Result
        elif mum_path == 6:
            ## mompastsunset_attend == 1 & 5 - Missed | 2 & 3 - Refused to go
            if (mompastsunset_attend == 0 or mompastsunset_attend == 4) and mompastsunset_went == 1:
                $ mompastsunset_went = 0
            else:
                jump lbl_mybedroom_day
        ## Didn't Save Mom from Dad
        elif mum_path == 9:
            $ mum_path = 11
            if sister_path >= 26:#FORT DESTROYED
                $ townmap_enabled = 0
                pov "{i}What was that! It sounded like an argument in the hallway.{/i}"
        elif mum_path == 11:
            if sister_path >= 26:#FORT DESTROYED
                $ townmap_enabled = 0
                pov "{i}What was that! It sounded like an argument in the hallway.{/i}"
        ## Mom Comes Out of her Room after Cheer Up Mom
        elif mum_path == 15 and day == 0:
            $ mum_path = 16
        ## Before Healed Eye
        elif mum_path == 17 and bathwithmom_eyereveal == 1 and day == 4:
            $ townmap_enabled = 0
        ## Skipping talking to Mom about Healed Eye if it wasn't revealed
        elif mum_path == 17 and bathwithmom_eyereveal == 0 and day == 4:
            $ mum_path = 17.5
        ## After a few days from talking about the Healed Eye
        elif mum_path == 17.5 and day == 1:
            $ mum_path = 18
        ## Dad Out of Town
        elif mum_path == 19:
            jump lbl_dad_out_of_town
        elif mum_path == 30.5:
            $ mum_path = 31
        ### AFTER Date H-scene revisit trigger reset
        elif mum_path >= 31 and mum_bedroomsex == 1:
            $ mum_bedroomsex = 0

        ## Go to the university at Night after Why Am I In Touble (Miss Allaway)
        if missallaway_path == 1.5:
            $ missallaway_path = 2
        ## Miss Allaway Studied
        elif missallaway_path == 16.5 and skill_intmax >= 19:
            $ missallaway_path = 17
        ## Night Job Setup
        elif missallaway_path == 22 and date >= 21:
            $ missallaway_path = 23

        ## She's At My House Part 1
        if sister_path == 27:
            jump lbl_shes_at_my_house_pt1
        ## How is Sister
        elif sister_path == 28 and day == 0:
            $ sister_path = 28.5
        ## Pre Fort Rebuild Reveal
        elif sister_path == 33 and gtime == 1:
            jump lbl_pre_fort_rebuild_reveal
        ## Post Sister's Nightmare
        elif sister_path == 34.5:
            jump lbl_post_sisters_nightmare
        elif sister_path == 35.5:
            $ sister_path = 36
            $ gtime = 1
            $ townmap_enabled = 0
            pov "{i}I guess I slept in.{/i}"
        ## Dad Apologizing
        elif sister_path == 37 and day != 2:
            $ townmap_enabled = 0
        ## Camgurl Substitute Favour
        elif sister_path == 38 and day == 2 and sister_points >= 8:
            jump lbl_camgurl_substitute_favour
        ## Camgurl Substitute Favour Refuse Restart
        elif sister_path == 38.5 and day == 3:
            $ sister_path = 39
        ## Camgurl Substitute Favour Fail Restart
        elif sister_path == 39.1 and day == 2:
            $ sister_path = 39

        ## Stressed From Work Pre
        elif mumsis_path == 2:
            $ townmap_enabled = 0
        ## Start of Punishment
        if mumsis_path == 7:
            jump lbl_start_of_punishment
        ## Snuggled Awake
        elif mumsis_path == 11 and mum_path >= 24 and sister_path >= 36 and gtime == 0 and day == 3:
            jump lbl_snuggled_awake
        ## The Car Ride To Camp
        elif mumsiscamp_path == 2 and gtime == 0 and day == 5:
            jump lbl_the_car_ride_to_camp

        ## activate bathroom stakeout 1
        if principallashley_path == 6.9:
            $ principallashley_path = 7
        elif principallashley_path == 7.9 and day == 0:
            $ principallashley_path = 8
        elif principallashley_path == 8.9 and day == 0:
            $ principallashley_path = 9

        ## The Lashley Aftermath
        elif principallashley_path == 14.1:
            $ principallashley_path = 14.5
        elif principallashley_path == 14.5 and day == 0:
            $ principallashley_path = 15
        elif principallashley_path == 15.1:
            $ principallashley_path = 15.5
        elif principallashley_path == 15.5 and day == 0:
            $ principallashley_path = 16
        elif principallashley_path == 17.5:
            $ principallashley_path = 17.9
        elif principallashley_path == 17.9 and day == 0:
            $ principallashley_path = 18
        elif principallashley_path == 19.9 and day == 0:
            $ principallashley_path = 20
        elif principallashley_path == 20.9 and day == 0:
            $ principallashley_path = 21
        elif principallashley_path == 21.5 and day == 4:
            $ principallashley_path = 22
        elif principallashley_path == 22.5:
            $ principallashley_path = 23
        elif principallashley_path == 23.9:
            $ principallashley_path = 24

        ## Rock Solid Modeling
        if hitomi_path == 11:
            jump lbl_rocksolid_modelling
        ## The Porn Purge PRE
        if hitomi_path == 25 and date in [19,20,21,22,23,24,25]:
            jump lbl_the_porn_purge_pre

        ## Effie Text Invitation
        if effie_path == 6 and day == 3 and gtime == 0:
            jump lbl_effie_text_invitation
        ## Effie Calling
        elif effie_path == 11 and day == 1 and gtime == 0:
            jump lbl_effie_calling

        ## Getting a Job
        if 18 <= main_story <= 20:
            if nextday_ajob == 0:
                if winc == 0:
                    pov "{i}I should get a job before I show my face to [missus]. I'll go check the mall.{/i}"
                else:
                    pov "{i}I should get a job before I show my face to Mom. I'll go check the mall.{/i}"
                jump lbl_townmap_setup
            elif nextday_ajob == 1:
                if main_story < 20:
                    pov "{i}I found a job but I know [missus] will make a big deal about it. I'll go back later.{/i}"

                    jump lbl_townmap_setup
                else:
                    $ main_story = 21

                    jump lbl_myhousefront_day

        ## The Text Reset
        elif main_story == 22:
            if day not in (0,3) and sister_path == 0:
                $ townmap_enabled = 0
            if thetext_reject == 1:
                $ thetext_reject = 0

                jump lbl_mybedroom_day
            elif thetext_reject == 2 and day == 0:
                $ thetext_reject = 0

                jump lbl_mybedroom_day
        ## The Morning Headache
        elif main_story == 68 and day not in (5,6):
            jump lbl_the_morning_headache
        ## Hang at the Mall - Next Day
        elif main_story == 75.4:
            $ main_story = 75.5
        ## Quality Family Time
        elif main_story == 78:
            if winc == 0:
                pov "I'm supposed to meet the girls in [missus]'s room."
            else:
                pov "I'm supposed to meet the girls in Mom's room."
            jump lbl_myhallway_day_setup
        ## Post Femme Fatale
        elif main_story == 99:
            $ townmap_enabled = 0
        ## Daily Grind Setup
        elif main_story == 101.9:
            $ main_story = 102
        ## Daily Grind Setup
        elif main_story == 102.9:
            $ main_story = 103
        ## Quick Reminder
        elif main_story == 107 and gtime == 0:
            jump lbl_quick_reminder
        ## Second Rescue Summarized Text
        elif main_story == 139.1:
            $ main_story = 140
            $ townmap_enabled = 1
            jump lbl_second_rescue_summarized_text
        ## Buukakki Followers Are Everywhere
        # elif main_story == 150.5 and date == 0:
        #     $ main_story = 151
        # ## Some Welcome Back Gifts
        # elif main_story == 164:
        #     if inventory.has_item(Items.flowerlilies) or inventory.has_item(Items.flowerroses) or inventory.has_item(Items.flowersunflowers):
        #         if inventory.has_item(Items.videogameaction) or inventory.has_item(Items.videogamedatingsim) or inventory.has_item(Items.videogameshooter):
        #             if inventory.has_item(Items.chocolatebox):
        #                 $ main_story = 165


    ## IN SEX WORLD
    elif insexworld == 1:
        ## First Day in Sex World
        if main_story == 28:
            $ townmap_enabled = 0
        # ## Sexworld Mom Reunite Sex
        # elif main_story == 128:
        #     jump lbl_sexworld_mom_reunite_sex
        # ## Effie is Okay In Sexworld
        # elif main_story == 129:
        #     jump lbl_effie_is_okay_in_sexworld
        # ## Did My Friends Save Me
        # elif main_story == 130:
        #     jump lbl_did_my_friends_save_me
        # ## Sexworld Mom Rides
        # elif main_story == 131:
        #     jump lbl_sexworld_mom_rides
        # ## You're Safe She Swears
        # elif main_story == 132:
        #     jump lbl_youre_safe_she_swears

    ## Eventless
    #else:
        ## Show my bedroom during the day.

    jump lbl_mybedroom_day

###############
## Room Navigation
## This is the map for my bedroom during the day
label lbl_mybedroom_day:

    scene bg mybedroom_day
    call screen scr_mybedroom_day

screen scr_mybedroom_day():
    imagebutton auto "btn mybedroom_day_bed_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_day_bed")
    imagebutton auto "btn mybedroom_day_desk_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_desk")
    imagebutton auto "btn mybedroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_day_setup")
    imagebutton auto "btn mybedroom_day_calander_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_calander")
    #if vrheadset_chest == 1:
    imagebutton auto "btn mybedroom_day_chest_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_chest_day")
    use hud_overlay

###############
## Labels
## Items

label lbl_mybedroom_day_bed:
    if main_story <= 6:
        pov "{i}I should go downstairs and get ready for my first day of university.{/i}"
        call screen scr_mybedroom_day
    elif main_story == 16:
        pov "{i}I should get going to university. [missus] is quite angry already.{/i}"
        call screen scr_mybedroom_day
    elif main_story == 22 and sister_path == 0 and day not in (0,3):
        pov "{i}This is no time to sleep in.{/i}"
        call screen scr_mybedroom_day
    elif 28 <= main_story <= 29:
        pov "{i}I should go downstairs and get ready for university.{/i}"
        call screen scr_mybedroom_day
    elif 30 <= main_story <= 34:
        pov "{i}I don't have time for that. I'll sleep when I get answers.{/i}"
        call screen scr_mybedroom_day
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        call screen scr_mybedroom_day
    elif main_story == 50:
        pov "{i}What's that heavenly smell? It's coming from downstairs.{/i}"
        call screen scr_mybedroom_day
    elif main_story == 69:
        pov "{i}[missus] wanted me downstairs for breakfast.{/i}"
        call screen scr_mybedroom_day
    elif main_story == 80:
        pov "{i}[missus] wanted me downstairs for breakfast.{/i}"
    elif main_story == 99:
        pov "{i}I should let [missus] know how my first day at the office went. I didn't get a chance to see her last night.{/i}"
        call screen scr_mybedroom_day
    elif main_story == 99:
        pov "{i}Jacob wanted to see me right away. It sounded serious.{/i}"
        call screen scr_mybedroom_day
    elif mum_path == 11 and sister_path > 26:
        pov "{i}I'm hungry. Time to eat some breakfast.{/i}"
        call screen scr_mybedroom_day
    elif mum_path == 17 and day == 4:
        pov "{i}I'm hungry. Time to eat some breakfast.{/i}"
        call screen scr_mybedroom_day
    elif mum_path == 24:
        pov "{i}I'm hungry. Time to eat some breakfast.{/i}"
        call screen scr_mybedroom_day
    elif sister_path == 22:
        pov "{i}I should check whether [sister] is feeling okay.{/i}"
        call screen scr_mybedroom_day
    elif sister_path == 33.5:
        pov "{i}I should be in the basement waiting for Effie and [sister].{/i}"
        call screen scr_mybedroom_day
    elif sister_path == 35 and not (date < 14 and month == 5):
        pov "{i}I should go look for [sister].{/i}"
        call screen scr_mybedroom_day
    elif sister_path == 36:
        pov "{i}I better check on [sister] after last night.{/i}"
        call screen scr_mybedroom_day
    elif sister_path == 36.1:
        pov "{i}I should kill some time before dinner.{/i}"
        call screen scr_mybedroom_day
    elif missallaway_path == 21:
        pov "{i}I need to be in the park tonight. I should stay awake.{/i}"
        call screen scr_mybedroom_day
    elif principallashley_path == 23 and day == 5:
        pov "{i}I need to be at the party tonight. I shouldn't risk it.{/i}"
        call screen scr_mybedroom_day


    else:
        menu:
            "Nap":
                #Camgurl Substitute Favour (FAIL RESTART)
                if sister_path == 39 and day == 2 and gtime == 1:
                    scene bg mybedroom_day_sleep
                    with dissolve
                    $ renpy.pause(1,hard=True)
                    if gtime == 0:
                        $ renpy.pause(1,hard=True)
                    show bg mybedroom_night_sleep
                    with dissolve
                    scene black
                    jump lbl_camgurl_substitute_favour_fail_naked
                jump lbl_mybedroom_day_nap
            "Sleep":
                #Camgurl Substitute Favour (FAIL RESTART)
                if sister_path == 39 and day == 2:
                    scene bg mybedroom_day_sleep
                    with dissolve
                    $ renpy.pause(1,hard=True)
                    if gtime == 0:
                        $ renpy.pause(1,hard=True)
                    show bg mybedroom_night_sleep
                    with dissolve
                    scene black
                    jump lbl_camgurl_substitute_favour_fail_naked
                jump lbl_mybedroom_day_sleep
            "Nevermind":
                jump lbl_mybedroom_day_setup
