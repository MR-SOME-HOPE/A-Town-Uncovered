## Sister Movie Date - Horror ##
label lbl_sister_movie_date_horror_1:

    scene bg sistermoviedate_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg sistermoviedate_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_sister_movie_date_horror_end

label lbl_sister_movie_date_horror_2:

    scene bg sistermoviedatehj_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg sistermoviedatehj_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_sister_movie_date_horror_end

label lbl_sister_movie_date_horror_3:

    scene bg sistermoviedatebj_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg sistermoviedatebj_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_sister_movie_date_horror_end

label lbl_sister_movie_date_horror_end:
    if skill_sta <= 16:
        $ skill_sta += 4
    else:
        $ skill_sta = 20
    if premoviedate_changemind == 1:
        pass
    else:
        if sister_points <= 9:
            $ sister_points += 1
        else:
            $ sister_points = 10
        $ renpy.notify("You gained 4 Stamina Points\nYour relationship with [sister] has increased")
    if skill_stamax <= skill_sta:
        $ skill_sta = skill_stamax
    else:
        pass
    $ gtime = 3

    scene black
    with fade
    $ renpy.pause()
    "After the movie..."

    scene bg mybedroom_night
    with fade

    jump lbl_mybedroom_night_setup
