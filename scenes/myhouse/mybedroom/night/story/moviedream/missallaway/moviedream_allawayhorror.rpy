## Movie Dream - Mom Horror ##
label lbl_movie_dream_allaway_horror:
    if skill_sta <= 13:
        jump lbl_movie_dream_allaway_horror_1
    else:
        jump lbl_movie_dream_allaway_horror_2

label lbl_movie_dream_allaway_horror_1:

    scene black
    $ renpy.pause
    "Later into the night..."
    show bg allawaydream_horror_1
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    $ renpy.pause(0.5,hard=True)
    scene black
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_2
    with dissolve
    show bg allawaydream_horror_3
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_4
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_5
    $ renpy.pause(0.7,hard=True)
    show bg allawaydream_horror_6
    $ renpy.pause(0.7,hard=True)
    show bg allawaydream_horror_7
    $ renpy.pause(1.0,hard=True)
    show bg allawaydream_horror_8
    $ renpy.pause(2.0,hard=True)
    show bg allawaydream_horror_9
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_10
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_21
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_22
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_23
    $ renpy.pause(0.5,hard=True)
    show bg dream_wakeup_1
    $ renpy.pause(1,hard=True)
    show bg dream_wakeup_2
    pov "{i}Alright... no more horror movies for me for a while.{/i}"

    jump lbl_movie_dream_allaway_horror_end

label lbl_movie_dream_allaway_horror_2:

    scene black
    $ renpy.pause
    "Later into the night..."
    show bg allawaydream_horror_1
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    $ renpy.pause(0.5,hard=True)
    scene black
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_2
    with dissolve
    show bg allawaydream_horror_12
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_13
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_14
    $ renpy.pause(2.0,hard=True)
    show bg allawaydream_horror_15
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_16
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_17
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_18
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_19
    $ renpy.pause(0.5,hard=True)
    show bg allawaydream_horror_20
    $ renpy.pause(0.5,hard=True)
    show bg dream_wakeup_1
    $ renpy.pause(1,hard=True)
    show bg dream_wakeup_1
    $ renpy.pause(1,hard=True)
    show bg dream_wakeup_2
    $ renpy.pause()

    jump lbl_movie_dream_allaway_horror_end

label lbl_movie_dream_allaway_horror_end:
    $ moviedate = 0
    $ moviedate_choice = 0

    jump lbl_mybedroom_night_sleep_1
