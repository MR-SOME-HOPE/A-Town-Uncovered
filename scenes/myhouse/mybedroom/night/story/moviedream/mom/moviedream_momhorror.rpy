## Movie Dream - Mom Horror ##
label lbl_movie_dream_mom_horror:
    if skill_sta <= 13:
        jump lbl_movie_dream_mom_horror_1
    else:
        jump lbl_movie_dream_mom_horror_2

label lbl_movie_dream_mom_horror_1:

    scene black
    $ renpy.pause
    "Later into the night..."
    show bg momdream_horror_1
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg momdream_horror_1
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg momdream_horror_2
    with dissolve
    show bg momdream_horror_3
    with hpunch
    show bg momdream_horror_4
    with hpunch
    show bg momdream_horror_3
    with hpunch
    show bg momdream_horror_4
    with hpunch
    show bg dream_wakeup_1
    $ renpy.pause(1,hard=True)
    show bg dream_wakeup_2
    pov "{i}Alright... no more horror movies for me for a while.{/i}"

    jump lbl_movie_dream_mom_horror_end

label lbl_movie_dream_mom_horror_2:

    scene black
    $ renpy.pause
    "Later into the night..."
    show bg momdream_horror_1
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg momdream_horror_1
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg momdream_horror_5
    with dissolve
    $ renpy.pause()
    if winc == 0:
        pov "[missus]..? Are-"
    else:
        pov "M-... Mom..? Are-"
    show bg momdream_horror_6
    pov "You-"
    show bg momdream_horror_7
    pov "Oka----!"

    scene white
    $ renpy.pause(0.1,hard=True)
    show bg momdream_horror_8
    with dissolve
    $ renpy.pause()
    show bg dream_wakeup_1
    $ renpy.pause(1,hard=True)
    show bg dream_wakeup_2
    $ renpy.pause()

    jump lbl_movie_dream_mom_horror_end

label lbl_movie_dream_mom_horror_end:
    $ moviedate = 0
    $ moviedate_choice = 0

    jump lbl_mybedroom_night_sleep_1
