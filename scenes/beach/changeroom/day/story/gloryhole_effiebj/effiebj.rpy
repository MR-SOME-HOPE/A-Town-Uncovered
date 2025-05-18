label lbl_beachchangeroom_gloryhole_day_effiebj:
    show gloryhole effiebj_1
    $ renpy.pause()
    eff "Mmmm.."
    $ gloryhole_effiebj_counter = 0

    jump lbl_beachchangeroom_gloryhole_day_3_1

label lbl_beachchangeroom_gloryhole_day_3_1:
    $ gloryhole_effiebj_counter += 1
    show gloryhole effiebj_2
    $ renpy.pause(0.4,hard=True)
    show gloryhole effiebj_1
    $ renpy.pause(0.4,hard=True)

    jump lbl_beachchangeroom_gloryhole_day_3_counter

label lbl_beachchangeroom_gloryhole_day_3_counter:
    if skill_sta <= 5 and gloryhole_effiebj_counter == 2:
        jump lbl_beachchangeroom_gloryhole_day_3_2
    elif skill_sta <= 10 and gloryhole_effiebj_counter == 4:
        jump lbl_beachchangeroom_gloryhole_day_3_2
    elif skill_sta <= 15 and gloryhole_effiebj_counter == 6:
        jump lbl_beachchangeroom_gloryhole_day_3_2
    elif skill_sta <= 20 and gloryhole_effiebj_counter == 8:
        jump lbl_beachchangeroom_gloryhole_day_3_2
    else:
        jump lbl_beachchangeroom_gloryhole_day_3_1

label lbl_beachchangeroom_gloryhole_day_3_2:
    show gloryhole effiebj_3
    $ renpy.pause(2,hard=True)
    show gloryhole effiebj_4
    $ renpy.pause(1,hard=True)
    show gloryhole effiebj_5
    $ renpy.pause(1,hard=True)
    show gloryhole effiebj_6
    $ renpy.pause()
    show gloryhole effiebj_7
    with dissolve
    eff "Hmm.."
    show gloryhole effiebj_8
    with dissolve
    eff "Oh! [povname]! Hey! See you in class, dude!"

    jump lbl_beachmain_day_setup
