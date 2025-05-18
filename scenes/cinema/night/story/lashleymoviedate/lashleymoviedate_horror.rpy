## Lashley Movie Date - Horror ##
label lbl_lashley_movie_date_horror_1:

    scene bg lashleymoviedate_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg lashleymoviedate_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_lashley_movie_date_horror_end

label lbl_lashley_movie_date_horror_2:

    scene bg lashleymoviedatehj_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg lashleymoviedatehj_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_lashley_movie_date_horror_end

label lbl_lashley_movie_date_horror_3:

    scene bg lashleymoviedatebj_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg lashleymoviedatebj_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_lashley_movie_date_horror_end

label lbl_lashley_movie_date_horror_end:
    if skill_sta <= 16:
        $ skill_sta += 4
    else:
        $ skill_sta = 20
    $ renpy.notify("You gained 4 Stamina Points")
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
