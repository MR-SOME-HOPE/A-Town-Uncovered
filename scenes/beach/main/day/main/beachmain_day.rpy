###############
## Setup
## Story Path
label lbl_beachmain_day_setup:
    ## First Day of University
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## First Day in Sexworld
    elif insexworld == 1 and main_story <= 30:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## Sex Around Town
    elif insexworld == 1 and main_story == 33:
        if sexaroundtownbeach == 0:
            scene bg beachmain_daysexworld
            with fade
            jump lbl_sex_around_town_beach
        else:
            jump lbl_beachmain_day
    ## NOT IN SEX WORLD
    if insexworld == 0:
        ## The Lifeguard
        if violette_path == 0:
            scene bg beachmain_day
            with fade
            jump lbl_the_lifeguard
        ## Meet Violette
        elif violette_path == 1:
            if beach_naked == 1:
                scene bg beachmain_day
                with fade
                jump lbl_meet_violette
            else:
                jump lbl_beachmain_day
        ## Ara Asika
        elif violette_path == 12:
            jump lbl_ara_asika
        ## Naughty Winds
        elif hitomi_path == 17.6 and beach_naked == 1:
            jump lbl_naughty_winds
        ## Hitomi Beach Accident
        if beach_naked == 1 and day == 5 and hitomibeach_day == 0 and main_story >= 20:
            jump lbl_hitomi_beach_accident
        ## Beach Party Prelude
        if effie_path == 17 and day == 4:
            jump lbl_beach_party_prelude
        ## Beach Party Prelude
        elif effie_path == 18 and day == 4:
            jump lbl_beach_party_climax

    ## NO EVENT
    else:
        jump lbl_beachmain_day
        ## Hitomi at the Beach
        #$ randomevent_hitomibeach = renpy.random.randint(1,100)
        #if hitomi_path == 1 and randomevent_hitomibeach <= 20 and beach_naked == 0 and hitomibeach_day == 0 and (main_story <= 22 or main_story >= 35):
        #    scene bg beachmain_day
        #    with fade
        #    jump lbl_hitomibeach_1_0
        #elif hitomi_path == 2 and randomevent_hitomibeach <= 20 and beach_naked == 0 and hitomibeach_day == 0 and (main_story <= 22 or main_story >= 35):
        #    scene bg beachmain_day
        #    with fade
        #    jump lbl_hitomibeach_1_1
        #else:
        #    jump lbl_beachmain_day

###############
## Room Navigation
## This is the map for beach main during the day
label lbl_beachmain_day:
    if 28 <= main_story <= 33:
        scene bg beachmain_daysexworld
    else:
        scene bg beachmain_day
    call screen scr_beachmain_day

screen scr_beachmain_day():
    if main_story == 33:
        imagebutton auto "btn beachmain_daysexworld_chair_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_day_violette")
    elif main_story == 84:
        imagebutton auto "btn beachmain_day_chair_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_investigations_violette")

    else:
        imagebutton auto "btn beachmain_day_chair_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_day_violette")
    imagebutton auto "btn beachmain_day_rocks_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_day_behindtherocks")
    imagebutton auto "btn beachmain_day_blue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachchangeroom_blue_day_setup")
    imagebutton auto "btn beachmain_day_purple_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachchangeroom_purple_day_setup")
    imagebutton auto "btn beachmain_day_green_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachchangeroom_green_day_setup")
    imagebutton auto "btn beachmain_day_red_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachchangeroom_red_day_setup")

    use hud_overlay

###############
## Labels
label lbl_beachmain_day_behindtherocks:
    if main_story == 33:
        jump lbl_beachbehindrocks_day_setup
    if beach_naked == 0:
        jump lbl_stop_snooping_clothed
    else:
        jump lbl_beachbehindrocks_day_setup
