###############
## Setup
## Story Path
label lbl_cafeinside_day_setup:
    ## MAIN STORY ############################
    ## Free Drink
    if main_story == 9 and gtime == 1:
        jump lbl_free_drink
    ## Sexworld
    elif main_story == 33:
        if sexaroundtowncafe == 0:
            scene bg cafeinside_daysexworld
            show btn cafeinside_daysexworld_effie_idle
            with fade

            jump lbl_cafeinside_day
        else:
            scene bg cafeinside_daysexworld
            show btn cafeinside_daysexworld_effie_idle

            jump lbl_cafeinside_day
    ## Investigations
    elif main_story == 84 and investigations_effie == 0:
        jump lbl_investigations_effie
    ## MISS ALLWAY ############################
    ## Allaway At The Cafe
    elif missallaway_path == 6 and day >= 5 and brock_path >= 1:
        jump lbl_allaway_at_the_cafe
    ## HITOMI ############################
    ## The Effie Charm
    if hitomi_path == 15:
        eff "I'm done with work for today. Let's go to the comicbook store."
        jump lbl_cafeoutside_day
    ## EFFIE ############################
    if effie_path == 8:
        jump lbl_coffee_and_sparks

    ## NO EVENT
    else:
        jump lbl_cafeinside_day

###############
## Room Navigation
## This is the map for cafe inside during the day
label lbl_cafeinside_day:
    if main_story == 33:
        scene bg cafeinside_daysexworld
        show btn cafeinside_daysexworld_effie_idle
    else:
        scene bg cafeinside_day
        if main_story == 84:
            show btn cafeinside_day_effie_idle
        elif gtime == 0 or (27 <= sister_path <= 33):
            show btn cafeinside_day_brock_idle
        elif gtime == 1:
            show btn cafeinside_day_effie_idle
    call screen scr_cafeinside_day

screen scr_cafeinside_day():
    if main_story == 33:
        imagebutton auto "btn cafeinside_daysexworld_effie_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeinside_day_effie")
    elif main_story == 84:
        imagebutton auto "btn cafeinside_day_effie_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeinside_day_effie")
    else:
        if gtime == 0:
            imagebutton auto "btn cafeinside_day_brock_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeinside_day_brock")
        elif gtime == 1:
            ## Sister staying at Effie's
            if (27 <= sister_path <= 33):
                imagebutton auto "btn cafeinside_day_brock_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeinside_day_brock")
            else:
                imagebutton auto "btn cafeinside_day_effie_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeinside_day_effie")
    imagebutton auto "btn cafeinside_day_sign_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeoutside_day_setup")
    use hud_overlay ## ONLY TOWN MAP DISABLED

###############
## Labels
## People
label lbl_cafeinside_counter_check:
    if store_counter == 1:
        show counter cafe at right
        with dissolve
    else:
        pass
    return
