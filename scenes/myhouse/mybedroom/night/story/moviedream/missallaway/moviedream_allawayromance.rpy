## Movie Dream - Mom Romance ##
label lbl_movie_dream_allaway_romance:
    if skill_cha <= 13:
        jump lbl_movie_dream_allaway_romance_1
    else:
        jump lbl_movie_dream_allaway_romance_2

label lbl_movie_dream_allaway_romance_1:
    scene bg allawaydream_romance_1
    with fade
    $ renpy.pause()
    show bg allawaydream_romance_2
    $ renpy.pause()
    show bg allawaydream_romance_3
    $ renpy.pause()
    show bg allawaydream_romance_4
    $ renpy.pause()
    show bg allawaydream_romance_5
    $ renpy.pause(0.7,hard=True)
    show bg allawaydream_romance_6
    $ renpy.pause(2.0,hard=True)
    show bg allawaydream_romance_7
    $ renpy.pause(2.0,hard=True)

    show bg dream_wakeup_1
    pov "{i}*GASP*{/i}"
    pov "..."

    jump lbl_movie_dream_allaway_horror_end

label lbl_movie_dream_allaway_romance_2:

    scene bg allawaydream_romance_1
    with fade
    $ renpy.pause()
    show bg allawaydream_romance_2
    $ renpy.pause()
    show bg allawaydream_romance_3
    $ renpy.pause()
    show bg allawaydream_romance_4
    $ renpy.pause()
    show bg allawaydream_romance_5
    $ renpy.pause(2.0,hard=True)
    show bg dream_wakeup_1
    with fade
    "{i}*Beeeep beeeep beeeep*{/i}"
    pov "{i}Nope... just my alarm{/i}"

    jump lbl_movie_dream_allaway_romance_end

label lbl_movie_dream_allaway_romance_end:
    $ moviedate = 0
    $ moviedate_choice = 0

    jump lbl_mybedroom_night_sleep_1
