###############
## Setup
## Story Path
default already_in_sexworld = False

label lbl_park_day_setup:
    ## Make sure Stamina doesn't go over 20
    if skill_stamax >= 20:
        $ skill_stamax = 20
    ## MAIN STORY ########################
    ## First Day of School
    if main_story <= 5:
        pov "{i}I can't go there yet. I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## First Morning in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## Sex Around Town
    elif main_story == 33:
        if sexaroundtownpark == 0:
            scene bg park_daysexworld
            with fade
            jump lbl_sex_around_town_park
        else:
            scene bg park_daysexworld
            jump lbl_park_day
    ## Ready To Go Again #
    elif main_story == 125 and gtime == 0 and day <= 4:
        jump lbl_ready_to_go_again
    elif main_story == 125.1 and gtime == 0 and day <= 4:
        jump lbl_ready_to_go_again_call
    ## Go To Sexworld Safely
    elif main_story == 126:
        jump lbl_go_to_sexworld_safely
    ## Go To Sexworld Safely
    elif main_story == 126.5:
        $ already_in_sexworld = True
        jump lbl_hurry_to_the_office_building
    ## EFFIE SIDE STORY ########################
    ## A Predictable_Realization
    if effie_path == 2 and a_predicatable_realization_jogged == 1:
        jump lbl_a_predictable_realization
    elif effie_path == 12:
        jump lbl_effie_sudden_confessions
    ## NO EVENT
    else:
        jump lbl_park_day

###############
## Room Navigation
## This is the map for park during the day
label lbl_park_day:
    if main_story == 33:
        scene bg park_daysexworld
    else:
        scene bg park_day
    call screen scr_park_day

screen scr_park_day():
    if main_story == 33:
        imagebutton auto "btn park_daysexworld_bench_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_park_day_bench")
    else:
        imagebutton auto "btn park_day_bench_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_park_day_bench")
    imagebutton auto "btn park_day_dog_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_pet_a_dog")
    imagebutton auto "btn park_day_path_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_park_day_path")
    use hud_overlay

###############
## Labels
## Locations
label lbl_park_day_bench:
    if main_story == 33:
        pov "{i}I'm fine just standing here. I'm a little fucked in the head to enjoy all this right now.{/i}"

        jump lbl_park_day_setup
    else:
        pov "{i}Lovely seat. 10/10 would sit again.{/i}"

        jump lbl_park_day_setup
