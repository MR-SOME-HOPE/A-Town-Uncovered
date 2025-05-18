label lbl_beachchangeroom_gloryhole_day_missallawaybj:
    show gloryhole missallawaybj_1
    $ renpy.pause()
    $ gloryhole_missallawaybj_counter = 0

    jump lbl_beachchangeroom_gloryhole_day_missallawaybj_1

label lbl_beachchangeroom_gloryhole_day_missallawaybj_1:
    $ gloryhole_missallawaybj_counter += 1
    show gloryhole missallawaybj_2
    $ renpy.pause(0.4,hard=True)
    show gloryhole missallawaybj_3
    $ renpy.pause(0.4,hard=True)

    jump lbl_beachchangeroom_gloryhole_day_missallawaybj_counter

label lbl_beachchangeroom_gloryhole_day_missallawaybj_counter:
    if skill_sta <= 5 and gloryhole_missallawaybj_counter == 2:
        jump lbl_beachchangeroom_gloryhole_day_missallawaybj_2
    elif skill_sta <= 10 and gloryhole_missallawaybj_counter == 4:
        jump lbl_beachchangeroom_gloryhole_day_missallawaybj_2
    elif skill_sta <= 15 and gloryhole_missallawaybj_counter == 6:
        jump lbl_beachchangeroom_gloryhole_day_missallawaybj_2
    elif skill_sta <= 20 and gloryhole_missallawaybj_counter == 8:
        jump lbl_beachchangeroom_gloryhole_day_missallawaybj_2
    else:
        jump lbl_beachchangeroom_gloryhole_day_missallawaybj_1

label lbl_beachchangeroom_gloryhole_day_missallawaybj_2:
    show gloryhole missallawaybj_4
    $ renpy.pause(2,hard=True)
    show gloryhole missallawaybj_5
    $ renpy.pause(1,hard=True)
    show gloryhole missallawaybj_6
    $ renpy.pause(1,hard=True)
    show gloryhole missallawaybj_7
    $ renpy.pause()
    show gloryhole missallawaybj_8
    with dissolve
    $ renpy.pause()
    show gloryhole missallawaybj_9
    with dissolve
    mis "I just realized; I've probably sucked one of my students off and I didn't even know."

    jump lbl_beachmain_day_setup
