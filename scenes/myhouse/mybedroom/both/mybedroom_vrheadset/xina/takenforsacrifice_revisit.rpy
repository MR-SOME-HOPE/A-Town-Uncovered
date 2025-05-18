## Taken for Sacrifice ##
label lbl_taken_for_sacrifice_revisit_4_fuck:
    $ takenforsacrifice_anal = 0

    jump lbl_taken_for_sacrifice_revisit_4_fuck_0

label lbl_taken_for_sacrifice_revisit_4_fuck_0:
    if hscene_xray == 0:
        scene bg takenforsacrifice_29

        jump lbl_taken_for_sacrifice_revisit_4_fuck_1
    else:
        scene bg takenforsacrifice_29_1

        jump lbl_taken_for_sacrifice_revisit_4_fuck_1_xray

label lbl_taken_for_sacrifice_revisit_4_fuck_1:
    $ takenforsacrifice_anal += 1
    show bg takenforsacrifice_29
    $ renpy.pause(0.7, hard=True)
    show bg takenforsacrifice_30
    $ renpy.pause(0.7, hard=True)

    jump lbl_taken_for_sacrifice_revisit_4_fuck_2

label lbl_taken_for_sacrifice_revisit_4_fuck_1_xray:
    $ takenforsacrifice_anal += 1
    show bg takenforsacrifice_29_1
    $ renpy.pause(0.7, hard=True)
    show bg takenforsacrifice_30_1
    $ renpy.pause(0.7, hard=True)

    jump lbl_taken_for_sacrifice_revisit_4_fuck_2

label lbl_taken_for_sacrifice_revisit_4_fuck_2:
    if skill_sta <= 6 and takenforsacrifice_anal == 5:
        jump lbl_taken_for_sacrifice_revisit_4_fuck_3
    elif skill_sta <= 13 and takenforsacrifice_anal == 10:
        jump lbl_taken_for_sacrifice_revisit_4_fuck_3
    elif skill_sta <= 20 and takenforsacrifice_anal == 15:
        jump lbl_taken_for_sacrifice_revisit_4_fuck_3
    else:
        jump lbl_taken_for_sacrifice_revisit_4_fuck_0

label lbl_taken_for_sacrifice_revisit_4_fuck_3:
    play music "audio/music/hellraiser_texture.ogg"

    scene bg takenforsacrifice_31
    $ renpy.pause()

    scene bg takenforsacrifice_32
    $ renpy.pause()

    scene bg takenforsacrifice_33
    $ renpy.pause(0.5, hard=True)

    scene bg takenforsacrifice_34
    $ renpy.pause(0.5, hard=True)

    scene bg takenforsacrifice_35
    $ renpy.pause(0.2, hard=True)

    scene bg takenforsacrifice_36
    with vpunch
    $ renpy.pause(0.2, hard=True)

    scene bg takenforsacrifice_37
    if skill_str >= 3:
        $ skill_str -= 3
    else:
        $ skill_str = 0
    if skill_sta >= 3:
        $ skill_sta -= 3
    else:
        $ skill_sta = 0

    jump lbl_taken_for_sacrifice_revisit_5

label lbl_taken_for_sacrifice_revisit_4_run:
    play music "audio/music/you_can_run.ogg" fadein 1.0

    scene bg takenforsacrifice_38
    $ renpy.pause(1, hard=True)

    scene bg takenforsacrifice_39
    $ renpy.pause(0.2, hard=True)

    scene bg takenforsacrifice_40
    with vpunch
    $ renpy.pause(0.2, hard=True)

    scene bg takenforsacrifice_41
    $ renpy.pause()
    $ takenforsacrifice_fuck = 0

    jump lbl_taken_for_sacrifice_revisit_5

label lbl_taken_for_sacrifice_revisit_5:

    scene bg takenforsacrifice_42
    with dissolve
    play music "audio/music/you_can_run.ogg" fadein 1.0
    $ renpy.pause(1.5, hard=True)
    show bg takenforsacrifice_43
    $ renpy.pause(1.5, hard=True)
    show bg takenforsacrifice_44
    $ renpy.pause(1.5, hard=True)
    show bg takenforsacrifice_45
    $ renpy.pause(0.5, hard=True)
    show bg takenforsacrifice_46
    $ renpy.pause(0.5, hard=True)
    show bg takenforsacrifice_47
    $ renpy.pause(0.5, hard=True)
    show bg takenforsacrifice_48
    $ renpy.pause(0.5, hard=True)
    show bg takenforsacrifice_49
    $ renpy.pause(0.5, hard=True)
    show bg takenforsacrifice_50
    $ renpy.pause(0.5, hard=True)
    show bg takenforsacrifice_51
    $ renpy.pause(0.5, hard=True)
    show bg takenforsacrifice_52
    $ renpy.pause(0.3, hard=True)
    show bg takenforsacrifice_53
    $ renpy.pause(0.3, hard=True)
    show bg takenforsacrifice_54
    $ renpy.pause(0.3, hard=True)
    show bg takenforsacrifice_55
    $ renpy.pause(0.3, hard=True)
    show bg takenforsacrifice_56
    $ renpy.pause(0.5, hard=True)

    scene black
    stop music fadeout 3.0
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
