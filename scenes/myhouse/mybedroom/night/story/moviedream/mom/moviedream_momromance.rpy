## Movie Dream - Mom Romance ##
label lbl_movie_dream_mom_romance:
    if skill_cha <= 13:
        jump lbl_movie_dream_mom_romance_1
    else:
        jump lbl_movie_dream_mom_romance_2

label lbl_movie_dream_mom_romance_1:

    scene bg momdream_romance_1
    with fade
    $ renpy.pause()
    show bg momdream_romance_2
    mum "T-this... this is w-w-where it ends-s..."
    mum "T-there's-s only room f-for one p-p-person on the d-door..."
    show bg momdream_romance_3
    pov "A-a-actua-lly... T-there's room f-for the b-b-both of us..."
    show bg momdream_romance_4
    mum "..."
    show bg momdream_romance_5
    mum "N-n-no... No there i-isn't..."
    show bg momdream_romance_7
    mum "Let go you filthy peasant!"
    show bg momdream_romance_8
    $ renpy.pause(0.7,hard=True)
    show bg momdream_romance_9
    with dissolve
    $ renpy.pause(0.7,hard=True)
    show bg momdream_romance_10
    with dissolve
    $ renpy.pause(0.7,hard=True)
    show bg dream_wakeup_1
    pov "{i}*GASP*{/i}"
    pov "..."

    jump lbl_movie_dream_mom_horror_end

label lbl_movie_dream_mom_romance_2:

    scene bg momdream_romance_1
    with fade
    $ renpy.pause()
    show bg momdream_romance_2
    mum "T-this... this is w-w-where it ends-s..."
    mum "T-there's-s only room f-for one p-p-person on the d-door..."
    show bg momdream_romance_3
    pov "A-a-actua-lly... T-there's room f-for the b-b-both of us..."
    show bg momdream_romance_4
    mum "..."
    show bg momdream_romance_6
    pov "..."
    show bg momdream_romance_11
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_12
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_11
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_12
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_11
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_12
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_11
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_12
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_11
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_12
    $ renpy.pause(0.4,hard=True)
    show bg momdream_romance_11
    mum "Fucck! Oh, yeaah."
    show bg momdream_romance_12
    if winc == 0:
        pov "Oh God, [missus]... you feel so hot inside."
        show bg momdream_romance_11
        mum "Y-your dick feels s-smaller..."
        show bg momdream_romance_12
        pov "It's cold out here , [missus]!"
    else:
        pov "Oh God, Mom... you feel so hot inside."
        show bg momdream_romance_11
        mum "Y-your dick feels s-smaller..."
        show bg momdream_romance_12
        pov "It's cold out here , Mom!"
    show bg momdream_romance_11
    "{i}*Beeeeeeeeeeeeep*{/i}"
    show bg momdream_romance_12
    pov "Is that the ship?!"
    show bg dream_wakeup_1
    with fade
    "{i}*Beeeep beeeep beeeep*{/i}"
    pov "{i}Nope... just my alarm{/i}"

    jump lbl_movie_dream_mom_romance_end

label lbl_movie_dream_mom_romance_end:
    $ moviedate = 0
    $ moviedate_choice = 0

    jump lbl_mybedroom_night_sleep_1
