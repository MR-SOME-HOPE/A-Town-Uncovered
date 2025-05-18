###############
## Setup
## Story Path
label lbl_cinema_night_setup:

    ## Main Story
    if main_story == 1:
        pov "{i}That's the cinema. It's too late to watch a movie. From what I remember, my house has a red roof, that's where I should be heading.{/i}"

        jump lbl_townmap_setup

    ## Movie Dates
    if moviedate >= 1:
        jump lbl_cinema_moviedate

    ## Allaway Cold Feet
    if missallaway_path == 14: ## ACTIVATE IN 0.21
        jump lbl_allaway_date_cold_feet
    else:
        jump lbl_cinema_night

###############
## Room Navigation
## This is the map for cinema during the night
label lbl_cinema_night:

    scene bg cinemaoutside_night
    call screen scr_cinema_night

screen scr_cinema_night():
    imagebutton auto "btn cinemaoutside_night_usher_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cinema_night_usher")
    imagebutton auto "btn street_night_abandonedlot_%s" xpos -1615 ypos -1 focus_mask True action Jump("lbl_abandonedlot_night_setup")
    use hud_overlay

###############
## Labels
label lbl_cinema_night_usher:

    scene bg movieusher_night_2
    with dissolve
    ush "Hey! Sorry to say but there's some constructing going on inside."
    show bg movieusher_night_1
    pov "And you're here for the sole purpose of telling people that?"
    show bg movieusher_night_2
    ush "I get paid don't I?"
    show bg movieusher_night_1
    pov "Fair play."

    jump lbl_cinema_night

label lbl_cinema_moviedate:
    if moviedate == 1:
        jump lbl_pre_mom_movie_date
    elif moviedate == 2:
        jump lbl_pre_sister_movie_date
    elif moviedate == 3:
        jump lbl_pre_missallaway_movie_date
    elif moviedate == 4:
        jump lbl_pre_lashley_movie_date
    else:
        "Report this to GeeSeki as should not have happened."
        jump lbl_cinema_night_setup
