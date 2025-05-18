## Mom Movie Date - Romance ##
label lbl_mom_movie_date_romance_1:

    scene bg mommoviedate_romance_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg mommoviedate_romance_2
    $ renpy.pause(1,hard=True)
    show bg mommoviedate_romance_1
    $ renpy.pause(1,hard=True)
    show bg mommoviedate_romance_2
    $ renpy.pause(1,hard=True)

    jump lbl_mom_movie_date_romance_end

label lbl_mom_movie_date_romance_2:

    scene bg mommoviedatehj_romance_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_mom_movie_date_romance_end

label lbl_mom_movie_date_romance_3:

    scene bg mommoviedatebj_romance_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg mommoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_mom_movie_date_romance_end

label lbl_mom_movie_date_romance_end:
    if skill_cha <= 16:
        $ skill_cha += 4
    else:
        $ skill_cha = 20
    if premoviedate_changemind == 1:
        pass
    else:
        if mum_points <= 9:
            $ mum_points += 1
        else:
            $ mum_points = 10
        if winc == 0:
            $ renpy.notify("You gained 4 Charisma Points\nYour relationship with [missus] has increased")
        else:
            $ renpy.notify("You gained 4 Charisma Points\nYour relationship with Mom has increased")
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
