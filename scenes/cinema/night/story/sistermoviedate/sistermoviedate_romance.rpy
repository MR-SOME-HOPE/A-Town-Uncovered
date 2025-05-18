## Sister Movie Date - Romance ##
label lbl_sister_movie_date_romance_1:

    scene bg sistermoviedate_romance_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg sistermoviedate_romance_2
    $ renpy.pause(1,hard=True)
    show bg sistermoviedate_romance_1
    $ renpy.pause(1,hard=True)
    show bg sistermoviedate_romance_2
    $ renpy.pause(1,hard=True)

    jump lbl_sister_movie_date_romance_end

label lbl_sister_movie_date_romance_2:

    scene bg sistermoviedatehj_romance_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatehj_romance_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_sister_movie_date_romance_end

label lbl_sister_movie_date_romance_3:

    scene bg sistermoviedatebj_romance_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_1
    $ renpy.pause(0.5,hard=True)
    show bg sistermoviedatebj_romance_2
    $ renpy.pause(0.5,hard=True)

    jump lbl_sister_movie_date_romance_end

label lbl_sister_movie_date_romance_end:
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
