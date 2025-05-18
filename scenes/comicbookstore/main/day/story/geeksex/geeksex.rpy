## Geek Sex
label lbl_geek_sex:
    #-This scene its just a collection of sex scenes all over the shop and the
    # backroom as according to the guideline-

    if hitomi_backroommatingpress == 0 or hitomi_countercunnilingus == 0 or hitomi_entrancedoggy == 0:
        menu:
            "Seated Mating Press" if hitomi_backroommatingpress == 0:
                jump lbl_hitomi_backroom_matingpress
            "Eat Her Out" if hitomi_countercunnilingus == 0:
                jump lbl_hitomi_counter_cunnilingus
            "Hit From Behind" if hitomi_entrancedoggy == 0:
                jump lbl_hitomi_entrance_doggy
    else:
        $ gtime += 1

        if gtime <= 1:
            scene bg street_day
            with fade

            jump lbl_street_day_setup
        else:
            scene bg street_night
            with fade

            jump lbl_street_night_setup

    #-You both make frantic, young, animalistic love with each other, in 3
    # positions around the comic book store and even the backroom without a care
    # in the world except in the moment, you both only see each other in this
    # empty world-

    # HSCENE 1 - Hitomi getting eaten out on the counter

    # HSCENE 2 - Hitomi in mating press on the chair in backrooms

    # HSCENE 3 - Doggy Ass up from behind view at the store entrance

    #-Scene ends with a final fade to black and now Hitomi is available for dates,
    # hangouts at her apartment and repeated sex scenes either on the shop or at
    # her place-



    #=SCENE END=
    #=ROUTE END=
