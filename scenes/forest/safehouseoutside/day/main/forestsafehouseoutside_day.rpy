###############
## Setup
## Story Path
label lbl_forestsafehouseoutside_day_setup:
    # ## First Day of university
    # if main_story <= 5:
    #     pov "{i}I can't go there yet, I have to get to university.{/i}"
    #     jump lbl_uptownmap_setup
    # ## In Trouble by Mom
    # elif main_story == 15:
    #     pov "{i}I should get home before I get into more trouble than I already am.{/i}"
    #     jump lbl_uptownmap_setup
    # ## First Day in the Sex World
    # elif insexworld == 1 and main_story <= 32:
    #     pov "{i}I should get to university. No fooling around today.{/i}"
    #     jump lbl_uptownmap_setup
    # ## Headache Awakening
    # elif main_story == 109:
    #     jump lbl_headache_awakening
    ## NO EVENTS
    # else:
    jump lbl_forestsafehouseoutside_day

###############
## Room Navigation
## This is the map for forest safehouse exterior during the day
label lbl_forestsafehouseoutside_day:
    scene bg forestsafehouseoutside_day
    call screen scr_forestsafehouseoutside_day

screen scr_forestsafehouseoutside_day():
    imagebutton auto "btn forestsafehouseoutside_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_forestsafehouseoutside_day_setup")

    use hud_overlay2

###############
## Labels

## Conversations
