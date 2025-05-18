## Director Lashley Movie Date - Romance ##
label lbl_lashley_movie_date_romance_1:

    scene bg lashleymoviedate_romance_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg lashleymoviedate_romance_2
    $ renpy.pause(1,hard=True)
    show bg lashleymoviedate_romance_1
    $ renpy.pause(1,hard=True)
    show bg lashleymoviedate_romance_2
    $ renpy.pause(1,hard=True)

    jump lbl_lashley_movie_date_romance_end

label lbl_lashley_movie_date_romance_2:

    scene bg lashleymoviedatehj_romance_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_lashley_movie_date_romance_end

label lbl_lashley_movie_date_romance_3:

    scene bg lashleymoviedatebj_romance_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_lashley_movie_date_romance_end

label lbl_lashley_movie_date_romance_end:
    if skill_cha <= 16:
        $ skill_cha += 4
    else:
        $ skill_cha = 20
    if premoviedate_changemind == 1:
        pass
    else:
        if principallashley_points <= 9:
            $ principallashley_points += 1
        else:
            $ principallashley_points = 10
        $ renpy.notify("You gained 4 Charisma Points\nYour relationship with Director Lashley has increased")
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
