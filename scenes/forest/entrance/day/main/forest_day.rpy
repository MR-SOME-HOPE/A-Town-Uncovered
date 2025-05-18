################
## Setup
## Story Path
label lbl_forest_day_setup:
    ## First Day of university
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_uptownmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_uptownmap_setup
    ## First Day in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_uptownmap_setup
    ## Headache Awakening
    elif main_story == 109:
        jump lbl_headache_awakening
    ## NO EVENTS
    else:
        jump lbl_forest_day

###############
## Room Navigation
## This is the map for forest during the day
label lbl_forest_day:
    scene bg forest_day
    with fade
    call screen scr_forest_day

screen scr_forest_day():
    imagebutton auto "btn forest_day_enter_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_forest_day_enter")

    use hud_overlay2

###############
## Labels
label lbl_forest_day_enter:
    ## Before Finding the Hideout
    if main_story < 113:
        pov "{i}Best not wander into the forest. Who knows what could be in there.{/i}"
    ## Friends in High Places
    elif main_story == 113:
        pov "{i}I should come back tonight.{/i}"
    ## Mission Briefing
    elif main_story == 117:
        jump lbl_mission_briefing
    ## The Big Heist
    elif main_story == 118:
        menu:
            "Begin the operation":
                jump lbl_the_big_heist
            "Come back later":
                pass
    # ## Second Rescue Summarized
    # elif main_story == 140.1:
    #     jump lbl_second_rescue_summarized
    # ## Second Rescue Summarized
    # elif main_story == 153:
    #     jump lbl_assign_roles_for_operation
    # ## Put The Maps Together
    # elif main_story == 155:
    #     jump lbl_put_the_maps_together
    # ## Decipher the Intel
    # elif main_story == 169:
    #     jump lbl_decipher_the_intel
    # ## BDSM Black Attire / Ready To Gear Up
    # elif gtime == 0 and main_story == 170 and inventory.has_item(Items.bdsmgear):
    #     menu:
    #         "Gather everyone":
    #             $ main_story = 171
    #             jump lbl_ready_to_gear_up
    #         "Come back later":
    #             pass
    # ## Ready To Gear Up (come back)
    # elif main_story == 171.5 and gtime == 0:
    #     jump lbl_ready_to_gear_up_2
    ## NO EVENT
    else:
        pov "{i}I don't need to visit the safehouse right now.{/i}"
    jump lbl_forest_day

## Conversations
