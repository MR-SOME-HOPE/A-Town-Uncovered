## Lashley Movie Date - Action ##
label lbl_lashley_movie_date_action_1:

    scene bg lashleymoviedate_action_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg lashleymoviedate_action_2
    $ renpy.pause(0.2,hard=True)
    show bg lashleymoviedate_action_1
    $ renpy.pause(1,hard=True)
    show bg lashleymoviedate_action_2
    $ renpy.pause(0.2,hard=True)
    show bg lashleymoviedate_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedate_action_2
    $ renpy.pause(0.2,hard=True)
    show bg lashleymoviedate_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedate_action_2
    $ renpy.pause(0.2,hard=True)
    show bg lashleymoviedate_action_1
    $ renpy.pause(1,hard=True)
    show bg lashleymoviedate_action_2
    $ renpy.pause(0.2,hard=True)
    show bg lashleymoviedate_action_1
    $ renpy.pause(1,hard=True)

    jump lbl_lashley_movie_date_action_end

label lbl_lashley_movie_date_action_2:

    scene bg lashleymoviedatehj_action_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_lashley_movie_date_action_end

label lbl_lashley_movie_date_action_3:

    scene bg lashleymoviedatebj_action_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg lashleymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_lashley_movie_date_action_end

label lbl_lashley_movie_date_action_end:
    if skill_str <= 16:
        $ skill_str += 4
    else:
        $ skill_str = 20
    $ renpy.notify("You gained 4 Strength Points")
    if skill_strmax <= skill_str:
        $ skill_str = skill_strmax
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
