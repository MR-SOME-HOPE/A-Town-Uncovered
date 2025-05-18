label lbl_beachchangeroom_gloryhole_day_mombj:
    show gloryhole mombj_1
    $ renpy.pause()
    mum "Mmmm.."
    $ gloryhole_mombj_counter = 0
    show gloryhole mombj_2
    $ renpy.pause(1,hard=True)
    show gloryhole mombj_1
    $ renpy.pause(1,hard=True)
    show gloryhole mombj_3
    mum "You should clean a little more thoroughly in the morning: I can taste the.."
    show gloryhole mombj_4
    if winc == 0:
        mum "Oh, sh- sorry. I didn't mean to lecture you. Just instincts."
    else:
        mum "Oh, sh- sorry. I didn't mean to mother you. Just instincts."
    pov "{i}That voice sounds reaally familiar...{/i}"

    menu:
        "Stay Silent":
            jump lbl_beachchangeroom_gloryhole_day_4_1
        "Leave":
            show gloryhole mombj_10
            with dissolve
            mum "I'm sorry, dear... person.. sir."

            jump lbl_beachmain_day_setup

label lbl_beachchangeroom_gloryhole_day_4_1:
    $ gloryhole_mombj_counter += 1
    show gloryhole mombj_2
    $ renpy.pause(0.4,hard=True)
    show gloryhole mombj_1
    $ renpy.pause(0.4,hard=True)

    jump lbl_beachchangeroom_gloryhole_day_4_counter

label lbl_beachchangeroom_gloryhole_day_4_counter:
    if skill_sta <= 5 and gloryhole_mombj_counter == 2:
        jump lbl_beachchangeroom_gloryhole_day_4_2
    elif skill_sta <= 10 and gloryhole_mombj_counter == 4:
        jump lbl_beachchangeroom_gloryhole_day_4_2
    elif skill_sta <= 15 and gloryhole_mombj_counter == 6:
        jump lbl_beachchangeroom_gloryhole_day_4_2
    elif skill_sta <= 20 and gloryhole_mombj_counter == 8:
        jump lbl_beachchangeroom_gloryhole_day_4_2
    else:
        jump lbl_beachchangeroom_gloryhole_day_4_1

label lbl_beachchangeroom_gloryhole_day_4_2:
    show gloryhole mombj_5
    $ renpy.pause(2,hard=True)
    show gloryhole mombj_6
    $ renpy.pause(1,hard=True)
    show gloryhole mombj_7
    $ renpy.pause(1,hard=True)
    show gloryhole mombj_8
    $ renpy.pause()
    show gloryhole mombj_9
    with dissolve
    mum "Uh.. sorry about what I said earlier.. again.."

    jump lbl_beachmain_day_setup
