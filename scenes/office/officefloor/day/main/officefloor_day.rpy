###############
## Setup
## Story Path
label lbl_officefloor_day_setup:
    ## Workplace Introduction Part 1
    if main_story == 93:
        jump lbl_workplace_introductions_part1
    ## Our First Shift
    elif main_story == 96:
        jump lbl_our_first_shift
    ## Daily Grind Part 1
    elif main_story == 101 and not received_eloise_text:
        jump lbl_daily_grind_part1
    ## Daily Grind Part 2
    elif main_story == 102 and day == 2 and not have_spoken_to_corrine_about_fistem:
        jump lbl_daily_grind_part2
    ## Daily Grind Part 3
    elif main_story == 103 and day == 3 and not received_eloise_text_again:
        jump lbl_daily_grind_part3
    ## Meeting with Eloise
    elif main_story == 104:
        jump lbl_meeting_with_eloise
    ## The R And D Tour
    elif main_story == 105:
        jump lbl_the_r_and_d_tour
    ## The End of Routine
    elif main_story == 106:
        jump lbl_the_end_of_routine
    ## COFFEE RUN TASK COMPLETE
    elif bought_coffee_run_drinks:
        jump lbl_returning_with_coffee_order
    ## NO EVENT
    jump lbl_officefloor_day

###############
## Room Navigation
## This is the map for Office Floor during the day
label lbl_officefloor_day:
    scene bg officefloor_day
    call screen scr_officefloor_day

screen scr_officefloor_day():
    imagebutton auto "btn officefloor_day_elevator_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_elevator_day_setup")
    imagebutton auto "btn officefloor_day_conferenceroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_conferenceroom_day_setup")
    imagebutton auto "btn officefloor_day_managersoffice_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_managersoffice_day_setup")
    imagebutton auto "btn officefloor_day_supplyroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_supplyroom_day")
    imagebutton auto "btn officefloor_day_officebathroom_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officebathroom_day")

    use hud_overlay

###############
## Labels
