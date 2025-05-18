###############
## Setup
## Story Path
label lbl_beachbehindrocks_day_setup:
    $ random_event = renpy.random.randint(1,6)

    

    ## Violette 69 and NOT sexworld
    if random_event == 1 and main_story != 33:
        jump lbl_beachbehindrocks_day_violetteredhead69

    ## Miss Lashley Sunscreen and NOT sexworld
    elif random_event == 2 and main_story != 33:
        if principallashley_path >= 1:
            jump lbl_beachbehindrocks_day_principallashleysunscreen
        else:
            jump lbl_beachbehindrocks_day_violetteredhead69

    ## NO EVENT
    else:
        jump lbl_beachbehindrocks_day

###############
## Room Navigation
## This is the map for beach main during the day
label lbl_beachbehindrocks_day:

    scene bg beachbehindrocks_day
    call screen scr_beachbehindrocks_day

screen scr_beachbehindrocks_day():
    imagebutton auto "btn beachbehindrocks_day_rocks_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_day_setup")
    use hud_overlay
