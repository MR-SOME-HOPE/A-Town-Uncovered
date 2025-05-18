###############
## Setup
## Story Path
label lbl_mylivingroom_night_setup:
    ## Ceremony Dress Up
    # if main_story == 133 and gtime >= 2:
    #     jump lbl_ceremony_dress_up

    ## NOT IN THE SEX WORLD
    if insexworld == 0:
        ## Mum Story ###############################
        ## What are you watching?
        if (mum_path == 0 and day != 1 and trustandsafety_shield == 0) and (sister_path != 10 or sister_path != 15 or sister_path != 16):
            jump lbl_what_are_you_watching
        ## Mom Fallen Asleep
        elif mum_path == 4:
            jump lbl_mom_fallen_asleep
        ## Caught My Parents
        elif mum_path == 7 and not (sister_path == 10 or sister_path == 16):
            jump lbl_caught_my_parents
        ## Save Mom From Dad
        elif mum_path == 9:
            jump lbl_save_mom_from_dad
        ## Sister Story ###############################
        ## Pre Fort Destroyer
        if sister_path == 26.5:
            jump lbl_pre_fort_destroyed
        ## Sister Passed Out
        if day == 4 and (mumsis_path == 1 and mum_path >= 1 and sister_path >= 5) and not ((sister_path == 10 or sister_path == 16) or mum_path == 7 or main_story == 85):
            jump lbl_sister_passed_out
        ## Sister Passed Out Post
        # elif mumsis_path == 2 and not (sister_path in (10,16) or mum_path == 7 or main_story == 85):
        #     "I'll leave them be for tonight."
        #     jump lbl_mykitchen_night
        ## Effie Story ###############################
        ## Pouring Rain
        if effie_path == 4:
            jump lbl_pouring_rain
        ## There is No Webflix
        elif effie_path == 14:
            jump lbl_there_is_no_webflix
        ## No Event
        else:
            jump lbl_mylivingroom_night
    ## No Event
    else:
        jump lbl_mylivingroom_night

###############
## Room Navigation
## This is the map for my livingroom during the night.

label lbl_mylivingroom_night:

    scene bg mylivingroom_night
    call screen scr_mylivingroom_night

screen scr_mylivingroom_night():
    imagebutton auto "btn mylivingroom_night_kitchen_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mykitchen_night_setup")
    imagebutton auto "btn mylivingroom_night_frontdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhousefront_night_setup")
    imagebutton auto "btn mylivingroom_night_basementdoor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybasement_night_setup")
    use hud_overlay
