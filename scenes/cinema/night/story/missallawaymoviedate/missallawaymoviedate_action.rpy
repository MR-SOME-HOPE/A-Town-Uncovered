## Miss Allaway Movie Date - Action ##
label lbl_missallaway_movie_date_action_1:

    scene bg allawaymoviedate_action_3
    with fade
    $ renpy.pause(1,hard=True)
    show bg allawaymoviedate_action_4
    $ renpy.pause(0.2,hard=True)
    show bg allawaymoviedate_action_3
    $ renpy.pause(1,hard=True)
    show bg allawaymoviedate_action_4
    $ renpy.pause(0.2,hard=True)
    show bg allawaymoviedate_action_3
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedate_action_4
    $ renpy.pause(0.2,hard=True)
    show bg allawaymoviedate_action_3
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedate_action_4
    $ renpy.pause(0.2,hard=True)
    show bg allawaymoviedate_action_3
    $ renpy.pause(1,hard=True)
    show bg allawaymoviedate_action_4
    $ renpy.pause(0.2,hard=True)
    show bg allawaymoviedate_action_3
    $ renpy.pause(1,hard=True)

    jump lbl_missallaway_movie_date_action_end

label lbl_missallaway_movie_date_action_2:

    scene bg allawaymoviedatehj_action_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatehj_action_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_missallaway_movie_date_action_end

label lbl_missallaway_movie_date_action_3:

    scene bg allawaymoviedatebj_action_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_1
    $ renpy.pause(0.5,hard=True)
    show bg allawaymoviedatebj_action_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_missallaway_movie_date_action_end

label lbl_missallaway_movie_date_action_end:
    if skill_str <= 16:
        $ skill_str += 4
    else:
        $ skill_str = 20
    if premoviedate_changemind == 1:
        pass
    else:
        if missallaway_points <= 9:
            $ missallaway_points += 1
        else:
            $ missallaway_points = 10
        $ renpy.notify("Your relationship with Miss Allaway has increased")
        $ renpy.pause(1,hard=False)
    $ renpy.notify("You gained 4 Strength Points")
    $ renpy.pause(1,hard=False)
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
