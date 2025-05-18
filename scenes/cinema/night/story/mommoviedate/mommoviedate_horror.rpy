## Mom Movie Date - Horror ##
label lbl_mom_movie_date_horror_1:

    scene bg mommoviedate_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg mommoviedate_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_mom_movie_date_horror_end

label lbl_mom_movie_date_horror_2:

    scene bg mommoviedatehj_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg mommoviedatehj_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_mom_movie_date_horror_end

label lbl_mom_movie_date_horror_3:

    scene bg mommoviedatebj_horror_1
    with fade
    $ renpy.pause(3,hard=True)

    scene bg mommoviedatebj_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_mom_movie_date_horror_end

label lbl_mom_movie_date_horror_end:
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
