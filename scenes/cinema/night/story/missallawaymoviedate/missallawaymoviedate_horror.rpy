## Miss Allaway Movie Date - Horror ##
label lbl_missallaway_movie_date_horror_1:

    scene bg allawaymoviedate_horror_1
    with fade
    $ renpy.pause(3,hard=True)
    show bg allawaymoviedate_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_missallaway_movie_date_horror_end

label lbl_missallaway_movie_date_horror_2:

    scene bg allawaymoviedatehj_horror_1
    with fade
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatehj_horror_2
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatehj_horror_1
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatehj_horror_2
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatehj_horror_1
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatehj_horror_2
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatehj_horror_3
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_missallaway_movie_date_horror_end

label lbl_missallaway_movie_date_horror_3:

    scene bg allawaymoviedatebj_horror_1
    with fade
    $ renpy.pause(2,hard=True)
    show bg allawaymoviedatebj_horror_2
    with hpunch
    $ renpy.pause(2,hard=True)

    jump lbl_missallaway_movie_date_horror_end

label lbl_missallaway_movie_date_horror_end:
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
