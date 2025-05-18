label lbl_beachchangeroom_gloryhole_day_nursehollickbj:
    show gloryhole nursehollickbj_1
    $ renpy.pause()
    $ gloryhole_nursehollickbj_counter = 0

    jump lbl_beachchangeroom_gloryhole_day_nursehollickbj_1

label lbl_beachchangeroom_gloryhole_day_nursehollickbj_1:
    $ gloryhole_nursehollickbj_counter += 1
    show gloryhole nursehollickbj_2
    $ renpy.pause(0.4,hard=True)
    show gloryhole nursehollickbj_3
    $ renpy.pause(0.4,hard=True)

    jump lbl_beachchangeroom_gloryhole_day_nursehollickbj_counter

label lbl_beachchangeroom_gloryhole_day_nursehollickbj_counter:
    if skill_sta <= 5 and gloryhole_nursehollickbj_counter == 2:
        jump lbl_beachchangeroom_gloryhole_day_nursehollickbj_2
    elif skill_sta <= 10 and gloryhole_nursehollickbj_counter == 4:
        jump lbl_beachchangeroom_gloryhole_day_nursehollickbj_2
    elif skill_sta <= 15 and gloryhole_nursehollickbj_counter == 6:
        jump lbl_beachchangeroom_gloryhole_day_nursehollickbj_2
    elif skill_sta <= 20 and gloryhole_nursehollickbj_counter == 8:
        jump lbl_beachchangeroom_gloryhole_day_nursehollickbj_2
    else:
        jump lbl_beachchangeroom_gloryhole_day_nursehollickbj_1

label lbl_beachchangeroom_gloryhole_day_nursehollickbj_2:
    show gloryhole nursehollickbj_4
    $ renpy.pause(2,hard=True)
    show gloryhole nursehollickbj_5
    $ renpy.pause(1,hard=True)
    show gloryhole nursehollickbj_6
    $ renpy.pause(1,hard=True)
    show gloryhole nursehollickbj_7
    $ renpy.pause()
    show gloryhole nursehollickbj_8
    with dissolve
    $ renpy.pause()
    show gloryhole nursehollickbj_9
    with dissolve
    nur "I wonder if he takes Zinc pills regularly or just naturally has a more than healthy volume of semen."

    jump lbl_beachmain_day_setup
