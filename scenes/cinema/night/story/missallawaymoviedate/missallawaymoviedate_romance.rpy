## Miss Allaway Movie Date - Romance ##
label lbl_missallaway_movie_date_romance_1:

    scene bg allawaymoviedate_romance_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg allawaymoviedate_romance_2
    $ renpy.pause(1,hard=True)
    show bg allawaymoviedate_romance_1
    $ renpy.pause(1,hard=True)
    show bg allawaymoviedate_romance_2
    $ renpy.pause(1,hard=True)

    jump lbl_missallaway_movie_date_romance_end

label lbl_missallaway_movie_date_romance_2:

    scene bg allawaymoviedatehj_romance_1
    with fade
    $ renpy.pause(0.8,hard=True)
    show bg allawaymoviedatehj_romance_2
    $ renpy.pause(0.8,hard=True)
    show bg allawaymoviedatehj_romance_1
    $ renpy.pause(0.8,hard=True)
    show bg allawaymoviedatehj_romance_2
    $ renpy.pause(0.8,hard=True)
    show bg allawaymoviedatehj_romance_1
    $ renpy.pause(0.8,hard=True)
    show bg allawaymoviedatehj_romance_2
    $ renpy.pause(0.8,hard=True)
    show bg allawaymoviedatehj_romance_1
    $ renpy.pause(0.8,hard=True)
    show bg allawaymoviedatehj_romance_2

    jump lbl_missallaway_movie_date_romance_end

label lbl_missallaway_movie_date_romance_3:

    scene bg allawaymoviedatebj_romance_1
    with fade
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_2
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_1
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_2
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_1
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_2
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_1
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_2
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_1
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_2
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_1
    $ renpy.pause(0.7,hard=True)
    show bg allawaymoviedatebj_romance_2
    $ renpy.pause(0.7,hard=True)

    jump lbl_missallaway_movie_date_romance_end

label lbl_missallaway_movie_date_romance_end:
    if skill_cha <= 16:
        $ skill_cha += 4
    else:
        $ skill_cha = 20
    $ renpy.notify("You gained 4 Charisma Points")
    if skill_chamax <= skill_cha:
        $ skill_cha = skill_chamax
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
