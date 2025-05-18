## Taken for Sacrifice ##
label lbl_taken_for_sacrifice:
    default takenforsacrifice_where = 0
    default takenforsacrifice_who = 0
    default takenforsacrifice_name = 0
    default takenforsacrifice_whyme = 0
    default takenforsacrifice_whyareyou = 0
    default takenforsacrifice_letmego = 0

    scene black
    $ renpy.pause()
    play music "audio/music/demons_lair_texture.ogg"

    scene bg takenforsacrifice_1
    with dissolve
    idk "Is he ready?"

    menu:
        "Hello?":
            pov "Hello?"
            show bg takenforsacrifice_2
            $ renpy.pause(0.2, hard=True)
            show bg takenforsacrifice_3
            $ renpy.pause(0.5, hard=True)
            show bg takenforsacrifice_4
            with dissolve
            $ renpy.pause()
            show bg takenforsacrifice_13
            $ renpy.pause()
            show bg takenforsacrifice_14
            idk "Hello, [povname]. Did you have a good sleep?"
            show bg takenforsacrifice_5
            idk "I hope that tranquilizer dart wasn't too painful for you."
            idk "And to answer your question..."
            idk "Well, not really something I can answer but, hello."

            jump lbl_taken_for_sacrifice_1
        "Who's there?":
            pov "Who's there?"
            show bg takenforsacrifice_2
            $ renpy.pause(0.2, hard=True)
            show bg takenforsacrifice_3
            $ renpy.pause(0.5, hard=True)
            show bg takenforsacrifice_4
            with dissolve
            $ renpy.pause()
            show bg takenforsacrifice_13
            $ renpy.pause()
            show bg takenforsacrifice_14
            idk "Hello, [povname]. Did you have a good sleep?"
            show bg takenforsacrifice_5
            idk "I hope that tranquilizer dart wasn't too painful for you."
            idk "And to answer your question..."
            xin "It's me, Xina. I understand if you didn't quite recognise me at first."
            xin "You must've been knocked right the fuck out. Powerful stuff this tranquilizer dart."
            $ takenforsacrifice_who = 1
            $ takenforsacrifice_name = 1

            jump lbl_taken_for_sacrifice_1
        "Where am I?":
            pov "Where am I?"
            show bg takenforsacrifice_2
            $ renpy.pause(0.2, hard=True)
            show bg takenforsacrifice_3
            $ renpy.pause(0.5, hard=True)
            show bg takenforsacrifice_4
            with dissolve
            $ renpy.pause()
            show bg takenforsacrifice_13
            $ renpy.pause()
            show bg takenforsacrifice_14
            idk "Hello, [povname]. Did you have a good sleep?"
            show bg takenforsacrifice_5
            idk "I hope that tranquilizer dart wasn't too painful for you."
            idk "And to answer your question..."
            idk "You're here, at the park."
            idk "I understand, you must feel a little confused and still in a daze but you'll be fine and dandy in a second.."
            idk "For a while."
            $ takenforsacrifice_where = 1

            jump lbl_taken_for_sacrifice_1

label lbl_taken_for_sacrifice_1:

    menu:
        "Who are you?" if takenforsacrifice_who == 0:
            show bg takenforsacrifice_4
            pov "Who are you?"
            show bg takenforsacrifice_5
            xin "It's me, Xina. I understand if you didn't quite recognise me at first."
            xin "You must've been knocked right the fuck out. Powerful stuff this tranquilizer dart."
            $ takenforsacrifice_who = 1
            $ takenforsacrifice_name = 1
            if takenforsacrifice_where == 0:
                jump lbl_taken_for_sacrifice_1
            else:
                jump lbl_taken_for_sacrifice_2
        "Where am I?" if takenforsacrifice_where == 0 and takenforsacrifice_name == 1:
            show bg takenforsacrifice_4
            pov "Where am I?"
            show bg takenforsacrifice_5
            xin "You're here, at the park."
            xin "I understand, you must feel a little confused and still in a daze but you'll be fine and dandy in a second.."
            xin "For a while."
            if takenforsacrifice_who == 0:
                jump lbl_taken_for_sacrifice_1
            else:
                jump lbl_taken_for_sacrifice_2
        "Where am I?" if takenforsacrifice_where == 0 and takenforsacrifice_name == 0:
            show bg takenforsacrifice_4
            pov "Where am I?"
            show bg takenforsacrifice_5
            idk "You're here, at the park."
            idk "I understand, you must feel a little confused and still in a daze but you'll be fine and dandy in a second.."
            idk "For a while."
            $ takenforsacrifice_where = 1
            if takenforsacrifice_who == 0:
                jump lbl_taken_for_sacrifice_1
            else:
                jump lbl_taken_for_sacrifice_2

label lbl_taken_for_sacrifice_2:
    show bg takenforsacrifice_5
    xin "Anyway. Congratulations! You were picked to be this year's sacrifice."
    show bg takenforsacrifice_6
    xin "Hoorah!"
    show bg takenforsacrifice_7
    xin "Aren't you a lucky ducky."

    jump lbl_taken_for_sacrifice_2_menu

label lbl_taken_for_sacrifice_2_menu:

    menu:
        "Why me?!" if takenforsacrifice_whyme == 0:
            show bg takenforsacrifice_8
            pov "Why me?!"
            show bg takenforsacrifice_9
            xin "Hmm? Don't you know? You do know how the choosing process works right?"
            show bg takenforsacrifice_7
            xin "To put it plainly; you produce the best cum in all of town."
            show bg takenforsacrifice_8
            pov "M-my cum?"
            show bg takenforsacrifice_7
            xin "Mhmm, that white shit that comes out of your fucking stick? You got the good shit right there."
            show bg takenforsacrifice_15
            xin "It was brought to my attention that your cum was worth examining, so we needed get official samples."
            xin "Remember that oh so sexy nurse, Nurse Hollick?"
            show bg takenforsacrifice_7
            xin "Oh, I just love her. She takes great care of her patients..."
            xin "Ah yes... good times good times..."
            xin "OH! Right, of course. Sacrifice, let's get on to it."
            $ takenforsacrifice_whyme = 1
            if takenforsacrifice_whyareyou == 0 or takenforsacrifice_letmego == 0:
                jump lbl_taken_for_sacrifice_2_menu
            else:
                jump lbl_taken_for_sacrifice_3
        "Why are you sacrificing people?!" if takenforsacrifice_whyareyou == 0:
            show bg takenforsacrifice_8
            pov "Why are you sacrificing people?!"
            show bg takenforsacrifice_10
            xin "{i}*Sigh*{/i} Do we really have to go over this again? I mean I guess I could explain it to you."
            xin "Think of it like a bed time story. Except after tonight, you won't be waking up again."
            xin "Ever."
            xin "And ever."
            xin "Like a really long time."
            show bg takenforsacrifice_9
            xin "Where was I? Oh, yes! Sacrifices: The prologue."
            show bg takenforsacrifice_7
            xin "Um... something about blessing the town with lust, happiness, and fulfilled desires. Yadda yadda yadda."
            show bg takenforsacrifice_15
            xin "Life gave birth to man and now we must repay life with a life. Yadda yadda yadda."
            xin "Um... something about the greatest boat orgy with a world flooded with semen?"
            show bg takenforsacrifice_10
            xin "I'm not quite sure about part, that page had some ancient jizz stains on it..."
            show bg takenforsacrifice_7
            xin "But yeah, I hope that answers that question for ya."
            xin "Let's get on with the show!"
            $ takenforsacrifice_whyareyou = 1
            if takenforsacrifice_whyme == 0 or takenforsacrifice_letmego == 0:
                jump lbl_taken_for_sacrifice_2_menu
            else:
                jump lbl_taken_for_sacrifice_3
        "Let me go!" if takenforsacrifice_letmego == 0:
            show bg takenforsacrifice_8
            pov "Let me go!"
            show bg takenforsacrifice_11
            xin "..."
            show bg takenforsacrifice_10
            xin "Oh, shit... we've got ourselves a fighter..."
            show bg takenforsacrifice_15
            xin "I- I guess I have no option but to let him go..."
            show bg takenforsacrifice_10
            xin "He's defeated me..."
            show bg takenforsacrifice_12
            xin "Hey, wise-guy. Don't make me mutilate the only thing that's keeping you alive."
            $ takenforsacrifice_letmego = 1
            if takenforsacrifice_whyme == 0 or takenforsacrifice_whyareyou == 0:
                jump lbl_taken_for_sacrifice_2_menu
            else:
                jump lbl_taken_for_sacrifice_3

label lbl_taken_for_sacrifice_3:
    show bg takenforsacrifice_16
    $ renpy.pause()
    show bg takenforsacrifice_17
    $ renpy.pause()
    show bg takenforsacrifice_18
    $ renpy.pause()
    if skill_int <= 10:
        show bg takenforsacrifice_19
        $ renpy.pause(0.6, hard=True)
        show bg takenforsacrifice_20
        $ renpy.pause(0.6, hard=True)
        show bg takenforsacrifice_21
        $ renpy.pause(1.5, hard=True)
    else:
        show bg takenforsacrifice_19
        mum "R"
        show bg takenforsacrifice_20
        mum "U"
        show bg takenforsacrifice_21
        mum "N"
    show bg takenforsacrifice_13
    $ renpy.pause(1, hard=True)
    show bg takenforsacrifice_14
    $ renpy.pause(1, hard=True)
    show bg takenforsacrifice_22
    $ renpy.pause()
    show bg takenforsacrifice_13
    $ renpy.pause()
    show bg takenforsacrifice_23
    $ renpy.pause(0.5, hard=True)
    show bg takenforsacrifice_24
    $ renpy.pause(1.5, hard=True)
    show bg takenforsacrifice_25
    xin "Come on, [povname]. This is what you're here for."
    xin "This is what destiny has in store for you."
    xin "I know you want to. Otherwise your giant cock is lying to you."
    xin "Don't keep everyone waiting, they want a show."

    menu:
        "Fuck her":
            show bg takenforsacrifice_26
            xin "And FYI, [povname]. No one puts it in my pussy. No one has ever put it in my pussy."
            xin "Not even you."
            xin "Shove it in my ass. Now."

            menu:
                "Fuck her in the ass":
                    show bg takenforsacrifice_27
                    $ renpy.pause()
                    show bg takenforsacrifice_28
                    xin "Let me know when you're about to cum, alright?"

                    jump lbl_taken_for_sacrifice_4_fuck
                "Run":
                    play music "audio/music/you_can_run.ogg"

                    jump lbl_taken_for_sacrifice_4_run
        "Run":
            play music "audio/music/you_can_run.ogg"

            jump lbl_taken_for_sacrifice_4_run

label lbl_taken_for_sacrifice_4_fuck:
    $ takenforsacrifice_anal = 0

    jump lbl_taken_for_sacrifice_4_fuck_0

label lbl_taken_for_sacrifice_4_fuck_0:
    if hscene_xray == 0:
        scene bg takenforsacrifice_29

        jump lbl_taken_for_sacrifice_4_fuck_1
    else:
        scene bg takenforsacrifice_29_1

        jump lbl_taken_for_sacrifice_4_fuck_1_xray

label lbl_taken_for_sacrifice_4_fuck_1:
    $ takenforsacrifice_anal += 1
    show bg takenforsacrifice_29
    $ renpy.pause(0.7, hard=True)
    show bg takenforsacrifice_30
    $ renpy.pause(0.7, hard=True)

    jump lbl_taken_for_sacrifice_4_fuck_2

label lbl_taken_for_sacrifice_4_fuck_1_xray:
    $ takenforsacrifice_anal += 1
    show bg takenforsacrifice_29_1
    $ renpy.pause(0.7, hard=True)
    show bg takenforsacrifice_30_1
    $ renpy.pause(0.7, hard=True)

    jump lbl_taken_for_sacrifice_4_fuck_2

label lbl_taken_for_sacrifice_4_fuck_2:
    if skill_sta <= 6 and takenforsacrifice_anal == 5:
        jump lbl_taken_for_sacrifice_4_fuck_3
    elif skill_sta <= 13 and takenforsacrifice_anal == 10:
        jump lbl_taken_for_sacrifice_4_fuck_3
    elif skill_sta <= 20 and takenforsacrifice_anal == 15:
        jump lbl_taken_for_sacrifice_4_fuck_3
    else:
        jump lbl_taken_for_sacrifice_4_fuck_0

label lbl_taken_for_sacrifice_4_fuck_3:
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
    $ takenforsacrifice_fuck = 1
    $ renpy.pause()
    $ renpy.notify("You lost 3 Strength Points\nYou lost 3 Stamina Points")

    jump lbl_taken_for_sacrifice_5

label lbl_taken_for_sacrifice_4_run:
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

    jump lbl_taken_for_sacrifice_5

label lbl_taken_for_sacrifice_5:

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
    $ main_story = 36
    $ gtime = 0
    if day <= 5:
        $ day += 1
    else:
        $ day = 0
    call lbl_next_date

    jump lbl_back_to_safety
