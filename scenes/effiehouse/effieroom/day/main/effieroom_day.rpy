###############
## Setup
## Story Path
label lbl_effieroom_day_setup:
    ## A Hectic Wakeup Call
    # Changed from 'Morning with Effie' for Effie's Side Story
    if main_story == 14:
        $ effie_path = 1
        jump lbl_a_hectic_wakeup_call
        #jump lbl_morning_with_effie
    ## No Event
    else:
        jump lbl_effieroom_day

###############
## Room Navigation
## This is the map for effie room during the night
label lbl_effieroom_day:

    scene bg effieroom_day
    call screen scr_effieroom_day

screen scr_effieroom_day():
    imagebutton auto "btn effieroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effiehousehallway_day_setup")
    use hud_overlay

###############
## Labels
