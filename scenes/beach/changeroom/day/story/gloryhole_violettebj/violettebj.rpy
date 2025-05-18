label lbl_beachchangeroom_gloryhole_day_violettebj:
    show gloryhole violettebj_1
    $ renpy.pause()
    vio "Wow... it's bigger than I expected."
    $ gloryhole_violettebj_counter = 0

    jump lbl_beachchangeroom_gloryhole_day_5_1

label lbl_beachchangeroom_gloryhole_day_5_1:
    $ gloryhole_violettebj_counter += 1
    show gloryhole violettebj_2
    $ renpy.pause(0.4,hard=True)
    show gloryhole violettebj_3
    $ renpy.pause(0.4,hard=True)

    jump lbl_beachchangeroom_gloryhole_day_5_counter

label lbl_beachchangeroom_gloryhole_day_5_counter:
    if skill_sta <= 5 and gloryhole_violettebj_counter == 2:
        jump lbl_beachchangeroom_gloryhole_day_5_2
    elif skill_sta <= 10 and gloryhole_violettebj_counter == 4:
        jump lbl_beachchangeroom_gloryhole_day_5_2
    elif skill_sta <= 15 and gloryhole_violettebj_counter == 6:
        jump lbl_beachchangeroom_gloryhole_day_5_2
    elif skill_sta <= 20 and gloryhole_violettebj_counter == 8:
        jump lbl_beachchangeroom_gloryhole_day_5_2
    else:
        jump lbl_beachchangeroom_gloryhole_day_5_1

label lbl_beachchangeroom_gloryhole_day_5_2:
    show gloryhole violettebj_4
    $ renpy.pause(0.2,hard=True)
    show gloryhole violettebj_5
    $ renpy.pause(0.2,hard=True)
    show gloryhole violettebj_6
    $ renpy.pause(0.2,hard=True)
    show gloryhole violettebj_7
    $ renpy.pause(0.2,hard=True)
    show gloryhole violettebj_8
    $ renpy.pause(0.2,hard=True)
    show gloryhole violettebj_9
    $ renpy.pause(0.2,hard=True)
    show gloryhole violettebj_10
    $ renpy.pause(0.3,hard=True)
    show gloryhole violettebj_11
    $ renpy.pause(0.3,hard=True)
    show gloryhole violettebj_12
    $ renpy.pause(0.3,hard=True)
    show gloryhole violettebj_13
    $ renpy.pause()
    show gloryhole violettebj_14
    $ renpy.pause()
    show gloryhole violettebj_15
    $ renpy.pause()
    vio "{i}This is an absurd amount of cum from one man...{/i}"

    jump lbl_beachmain_day_setup
