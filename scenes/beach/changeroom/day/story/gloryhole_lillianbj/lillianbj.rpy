label lbl_beachchangeroom_gloryhole_day_lillianbj:
    $ gloryhole_lillianbj_counter = 0
    show gloryhole lillianbj_1
    $ renpy.pause()
    show gloryhole lillianbj_2
    lill "Hey, so... do you want me to suck you off or do you wanna fuck my throat?"

    menu:
        "Suck.":
            show gloryhole lillianbj_3
            pov "Suck me off."

            jump lbl_beachchangeroom_gloryhole_day_lillianbj_1
        "Fuck Throat":
            show gloryhole lillianbj_3
            pov "I wanna fuck your throat."

            jump lbl_beachchangeroom_gloryhole_day_lillianbj_2

label lbl_beachchangeroom_gloryhole_day_lillianbj_1:
    $ gloryhole_lillianbj_counter += 1
    show gloryhole lillianbj_4
    $ renpy.pause(0.4,hard=True)
    show gloryhole lillianbj_5
    $ renpy.pause(0.4,hard=True)

    jump lbl_beachchangeroom_gloryhole_day_lillianbj_counter

label lbl_beachchangeroom_gloryhole_day_lillianbj_2:
    $ gloryhole_lillianbj_counter += 1
    show gloryhole lillianbj_6
    $ renpy.pause(0.4,hard=True)
    show gloryhole lillianbj_7
    $ renpy.pause(0.4,hard=True)

    jump lbl_beachchangeroom_gloryhole_day_lillianbj_counter_2

label lbl_beachchangeroom_gloryhole_day_lillianbj_counter:
    if skill_sta <= 5 and gloryhole_lillianbj_counter == 2:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_3
    elif skill_sta <= 10 and gloryhole_lillianbj_counter == 4:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_3
    elif skill_sta <= 15 and gloryhole_lillianbj_counter == 6:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_3
    elif skill_sta <= 20 and gloryhole_lillianbj_counter == 8:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_3
    else:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_1

label lbl_beachchangeroom_gloryhole_day_lillianbj_counter_2:
    if skill_sta <= 5 and gloryhole_lillianbj_counter == 2:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_3
    elif skill_sta <= 10 and gloryhole_lillianbj_counter == 4:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_3
    elif skill_sta <= 15 and gloryhole_lillianbj_counter == 6:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_3
    elif skill_sta <= 20 and gloryhole_lillianbj_counter == 8:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_3
    else:
        jump lbl_beachchangeroom_gloryhole_day_lillianbj_2

label lbl_beachchangeroom_gloryhole_day_lillianbj_3:
    show gloryhole lillianbj_8
    $ renpy.pause(2,hard=True)
    show gloryhole lillianbj_9
    $ renpy.pause(1,hard=True)
    show gloryhole lillianbj_10
    $ renpy.pause(1,hard=True)
    show gloryhole lillianbj_11
    $ renpy.pause()
    show gloryhole lillianbj_12
    with dissolve
    lill "Fuck. I should really learn to say no to these changing room quickies..."
    show gloryhole lillianbj_13
    with dissolve
    lill "...But I just can't."

    jump lbl_beachmain_day_setup
