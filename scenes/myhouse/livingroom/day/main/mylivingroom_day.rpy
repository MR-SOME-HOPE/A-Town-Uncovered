###############
## Setup
## Story Path
label lbl_mylivingroom_day_setup:
    ## In Trouble by Mom
    if main_story == 15:
        scene bg mylivingroom_day
        with fade
        jump lbl_in_trouble_by_mom
    ## The Town is Crazy
    elif main_story == 34:
        scene bg mylivingroom_day
        with fade
        stop music fadeout 2.0
        jump lbl_the_town_is_crazy
    ## Welcome Home Asshat
    elif main_story == 40:
        jump lbl_welcome_home_asshat
    ## Welcome Home Asshat Part 2 Post
    elif main_story == 40.5:
        jump lbl_welcome_home_asshat_part2_2
    ## Breaking News
    elif main_story == 51:
        jump lbl_breaking_news
    ## Mom is Freaking Out
    elif main_story == 55:
        jump lbl_mom_is_freaking_out
    ## Home Early
    elif main_story == 63.3:
        jump lbl_home_early
    ## Girls Upstairs
    elif main_story == 77:
        jump lbl_girls_upstairs
    ## Sudden Dinner Plans
    elif main_story == 84 and investigations_complete == 1:
        jump lbl_sudden_dinner_plans
    ## Mom's Help
    elif 87 <= main_story <= 89 and gtime == 1:
        jump lbl_moms_help
    # ## Modern Day Parental Punishment
    # elif main_story == 141:
    #     jump lbl_modern_day_parental_punishment




    ## NOT IN THE SEX WORLD SIDE STORIES
    if insexworld == 0:
        ## Locked Basement
        if sister_path == 7 and day >= 5:
            jump lbl_locked_basement
        ## Unlocked Basement
        elif sister_path == 8.5 or (sister_path == 7.5 and know_lockpick == 1):
            jump lbl_unlocked_basement
        ## For My Phone Bill Payback
        elif sister_path >= 10 and formyphonebill_owe == 1 and not (gtime == 0 and day in (0,3)) and not (gtime == 1 and day == 4):
            scene bg mylivingroom_day
            jump lbl_for_my_phone_bill_payback
        ## Are You Playing Doctor
        elif sister_path == 12:
            jump lbl_are_you_playing_doctor
        ## She's at my House
        elif sister_path == 27.5:
            jump lbl_shes_at_my_house_pt2
        ## Sister Ask Stargazing
        elif sister_path == 35 and not (date < 14 and month == 5): #and gtime >= 1:#and date >= 15
            jump lbl_sister_ask_stargazing
        ## In Trouble By Mom School Trap
        if missallaway_path == 9:
            jump lbl_in_trouble_by_mom_school_trap
        ## Hitomi Living Room Doggy
        if hitomi_livingroomdoggy == 1:
            "You let Hitomi in."
            jump lbl_hitomi_livingroom_doggy
        ## Miss Allaway Missionary Sex - Sneak Her In
        if allawaybedroomsex_sneakherin == 1:
            jump lbl_sneak_allaway_in
        ## Mom Left Out Twin Fortress
        if mumsis_path == 9.1:
            jump lbl_mom_left_out_twin_fortress
        ## Mom Sis Camping Trip
        if mumsis_path >= 15:
            ## Surprise Weekend Camping Getaway
            if mumsiscamp_path <= 1 and day == 4 and gtime >= 1:
                jump lbl_surprise_weekend_camping_getaway
        ## Eventless
        else:
            jump lbl_mylivingroom_day
    ## Eventless
    else:
        jump lbl_mylivingroom_day

###############
## Room Navigation
## This is the map for my livingroom during the day
label lbl_mylivingroom_day:

    scene bg mylivingroom_day
    call screen scr_mylivingroom_day

screen scr_mylivingroom_day():

    ## Room Interactions
    if main_story == 21 or main_story == 78: ## Main Story
        pass
    elif hitomi_livingroomdoggy == 1: ## Hitomi Livingroom Doggy
        pass

    ## Mum Story
    elif mum_path == 6 and gtime == 1:
        imagebutton auto "btn mylivingroom_day_mother_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_day_mother")
    elif 11 <= mum_path <= 17 or ((mum_path == 22 or mum_path == 22.5) and day == 4):
        pass

    ## Shower Schedule
    elif ((day == 0 or day == 6) and gtime == 1):
        pass

    ## Kitchen
    elif gtime == 0:
        pass

    ## Twin Fortress Reveal
    elif sister_path == 33.5:
        pass
    ## Sneak Mis Allaway In
    elif allawaybedroomsex_sneakherin == 1:
        pass
    else:
        imagebutton auto "btn mylivingroom_day_mother_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_day_mother")
    if day <= 4 or gtime == 1: ## Dad Bedroom or Out
        pass
    elif mum_path >= 20: ## Dad out of Town
        pass
    elif gtime == 0 and day >= 5:
        if 27 <= sister_path <= 37:
            pass
        else:
            imagebutton auto "btn mylivingroom_day_dad_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_day_dad")
    imagebutton auto "btn mylivingroom_day_frontdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhousefront_day_setup")
    if gtime == 0 or (gtime == 1 and (day == 0 or day == 6)): ## Camgurl Confrontation
        pass
    else:
        if sister_path == 24 and not (day == 2 and gtime == 1):
            imagebutton auto "btn mylivingroom_day_sister_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_camgurl_confrontation")
        else:
            pass
    imagebutton auto "btn mylivingroom_day_kitchen_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mykitchen_day_setup")
    #imagebutton auto "btn mylivingroom_day_frontdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhousefront_day_setup")
    imagebutton auto "btn mylivingroom_day_basementdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybasement_day_setup")
    if main_story <= 4:
        pass
    else:
        use hud_overlay
