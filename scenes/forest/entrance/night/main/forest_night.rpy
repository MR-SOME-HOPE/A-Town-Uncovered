###############
## Setup
## Story Path
label lbl_forest_night_setup:
    ## Start of Game
    if main_story == 1:
        pov "{i}That abandoned lot looks very shady and dangerous, I should just get home. From what I remember, my house has a red roof.{/i}"
        jump lbl_uptownmap_setup
    ## NO EVENTS
    else:
        jump lbl_forest_night

###############
## Room Navigation
## This is the map for forest during the night
label lbl_forest_night:
    scene bg forest_night
    with fade
    call screen scr_forest_night

screen scr_forest_night():
    imagebutton auto "btn forest_night_enter_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_forest_night_enter")

    use hud_overlay2

###############
## Labels
label lbl_forest_night_enter:
    ## Before Finding Hideout
    if main_story < 113:
        pov "{i}Best not wander into the forest, especially at night. Who knows what could be in there.{/i}"
    ## Friends In High Places
    elif main_story == 113:
        jump lbl_friends_in_high_places
    # ## Down The Garbage Bin (READY)
    # elif main_story == 157.5:
    #     menu:
    #         "Call everyone to meet at the alleyway":
    #             jump lbl_down_the_garbage_bin_ready
    #         "Nevermind":
    #             jump lbl_forest_day
    # ## Theorizing the Cult
    # elif main_story == 163:
    #     jump lbl_theorizing_the_cult
    else:
        pov "{i}I don't need to visit the safehouse right now. Especially at night.{/i}"
    jump lbl_forest_night

## Conversations
