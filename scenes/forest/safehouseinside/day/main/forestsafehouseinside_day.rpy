################
## Setup
## Story Path
label lbl_forestsafehouseinside_day_setup:
    # ## Ready To Go Again
    # if main_story == 125 and gtime == 0 and day <= 4:
    #     jump lbl_ready_to_go_again
    # ## Second Rescue Summarized
    # elif main_story == 140.1:
    #     jump lbl_second_rescue_summarized
    # ## Second Rescue Summarized
    # elif main_story == 153:
    #     jump lbl_assign_roles_for_operation
    # ## NO EVENT
    # else:
    #     jump lbl_forestsafehouseinside_day

###############
## Room Navigation
## This is the map for forest safehouse during the day
label lbl_forestsafehouseinside_day:
    scene bg forestsafehouseinside_day
    call screen scr_forestsafehouseinside_day

screen scr_forestsafehouseinside_day():
    imagebutton auto "btn forestsafehouseinside_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_forestsafehouseoutside_day_setup")

    use hud_overlay2

###############
## Labels

## Conversations
