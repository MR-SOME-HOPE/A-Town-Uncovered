###############
## Setup
## Story Path
label lbl_forestsafehouseinside_night_setup:
    ## Letting Effie Go Pt 2
    if main_story == 122.5:
        jump lbl_letting_effie_go_pt2
    ## Don't Blame Yourself
    elif main_story == 123:
        jump lbl_dont_blame_yourself
    ## NO EVENTS
    else:
        jump lbl_forestsafehouseinside_night

###############
## Room Navigation
## This is the map for forest safehouse during the night
label lbl_forestsafehouseinside_night:
    scene bg forestsafehouseinside_night
    call screen scr_forestsafehouseinside_night

screen scr_forestsafehouseinside_night():
    imagebutton auto "btn forestsafehouseinside_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_forestsafehouseoutside_night_setup")

    use hud_overlay2

###############
## Labels

## Conversations
