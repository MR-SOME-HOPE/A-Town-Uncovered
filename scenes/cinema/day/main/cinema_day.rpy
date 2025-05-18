###############
## Setup
## Story Path
label lbl_cinema_day_setup:
    ## First Night
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## In the Sex World Night
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## In the Sex World Morning
    elif main_story == 29:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    else:
        jump lbl_cinema_day

###############
## Room Navigation
## This is the map for cinema during the day
label lbl_cinema_day:
    scene bg cinemaoutside_day
    call screen scr_cinema_day


screen scr_cinema_day():
    imagebutton auto "btn cinemaoutside_day_usher_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cinema_day_usher")
    imagebutton auto "btn street_day_abandonedlot_%s" xpos -1615 ypos -1 focus_mask True action Jump("lbl_abandonedlot_day_setup")

    use hud_overlay

################
## Labels
label lbl_cinema_day_usher:
    # menu:
    #     "wabee cheat":
    #         $ povname = "player"
    #         jump lbl_test111
    #     "pass":
    #         pass

    scene bg movieusher_day_2
    with dissolve
    ush "Hey! Sorry to say but there's some constructing going on inside."
    show bg movieusher_day_1
    pov "And you're here for the sole purpose of telling people that?"
    show bg movieusher_day_2
    ush "I get paid don't I?"
    show bg movieusher_day_1
    pov "Fair play."

    jump lbl_cinema_day
