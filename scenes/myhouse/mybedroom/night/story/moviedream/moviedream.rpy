## Movie Dream ##
label lbl_movie_dream:

    scene black
    with fade
    $ renpy.pause()

    ## First Movie Date
    if mum_path == 18:
        $ mum_path = 19

    ## Mom
    if moviedate == 1:
        if moviedate_choice == 1:
            jump lbl_movie_dream_mom_action
        elif moviedate_choice == 2:
            jump lbl_movie_dream_mom_horror
        elif moviedate_choice == 3:
            jump lbl_movie_dream_mom_romance

    ## Sister
    elif moviedate == 2:
        pass
        #"Developer Note: [sister] doesn't have any movie dream sequences yet."

    ## Miss Allaway
    elif moviedate == 3:
        if moviedate_choice == 1:
            jump lbl_movie_dream_allaway_action
        elif moviedate_choice == 2:
            jump lbl_movie_dream_allaway_horror
        elif moviedate_choice == 3:
            jump lbl_movie_dream_allaway_romance
        
    $ moviedate = 0

    jump lbl_mybedroom_night_sleep
