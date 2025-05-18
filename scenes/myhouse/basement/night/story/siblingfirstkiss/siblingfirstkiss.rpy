## Sibling First Kiss ##
label lbl_sibling_first_kiss:
    default siblingfirstkiss_honest = 0
    show bg 20qwithsister_4
    pov "If my calculations are correct, that'd be 20 questions?"
    show bg 20qwithsister_8
    sis "I counted 20 each as well."
    show bg 20qwithsister_4
    pov "..."
    show bg 20qwithsister_9
    sis "That was fun..."
    show bg 20qwithsister_10
    pov "Oh, yeah. I- uh- learnt a lot more about you than I thought I would."
    sis "..."
    if twentyqwithsister_honest >= 11:
        $ siblingfirstkiss_honest = 1
        show bg 20qwithsister_9
        sis "Thanks for being so open to me."
        show bg 20qwithsister_10
        if winc == 0:
            pov "Of course, we're [sisrole]s. We're as close as [sisrole] should be."
        else:
            pov "Of course, we're twins. We're as close as sibling should be."
    else:
        show bg 20qwithsister_14
        sis "I wish you'd be more open with me though..."
        show bg 20qwithsister_16
        pov "Why would you think I'm not ope-"
        show bg 20qwithsister_14
        if winc == 0:
            sis "I'm your [sisrole], [povname]. I know when you are and aren't bullshitting me."
        else:
            sis "I'm your twin sister, [povname]. I know when you are and aren't bullshitting me."
    pov "..."
    show bg 20qwithsister_10
    sis "..."

    menu:
        "Stare at her legs":
            if siblingfirstkiss_honest == 1:
                show bg siblingfirstkiss_1
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_2
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_3
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_4
                $ renpy.pause(1.5,hard=True)
                show bg siblingfirstkiss_5
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_6
                $ renpy.pause()
            else:
                $ renpy.pause()
                sis "Thanks for the game, [povname]. We should head to bed now though."
                pov "Yeah... Goodnight, [sister]."
        "Stare into her eyes":
            if siblingfirstkiss_honest == 1:
                show bg siblingfirstkiss_7
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_2
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_8
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_9
                $ renpy.pause(0.2,hard=True)
                show bg siblingfirstkiss_10
                $ renpy.pause(1.5,hard=True)
                show bg siblingfirstkiss_11
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_12
                $ renpy.pause()
                show bg siblingfirstkiss_13
                sis "Thanks for the game, [povname]."
            else:
                $ renpy.pause()
                sis "Thanks for the game, [povname]. We should head to bed now though."
                pov "Yeah... Goodnight, [sister]."
        "Give her a quick peck on the lips":
            if siblingfirstkiss_honest == 1:
                show bg siblingfirstkiss_7
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_14
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_15
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_16
                $ renpy.pause(0.2,hard=True)
                show bg siblingfirstkiss_17
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_18
                sis "{i}*Ahem*{/i}"
                sis "W-we should get to bed. T-Thanks for the game, [povname]."
                show bg siblingfirstkiss_19
                pov "Y-yeah... Goodnight, [sister]."
            else:
                show bg siblingfirstkiss_7
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_14
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_15
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_16
                $ renpy.pause(0.2,hard=True)
                show bg siblingfirstkiss_17
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_20
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_21
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_22
                sis "..."
                sis "I- I... think we should get to bed. Uh.. thanks for the game, [povname]."
        "Pull her in for a kiss":
            if siblingfirstkiss_honest == 1:
                show bg siblingfirstkiss_7
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_14
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_15
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_23
                $ renpy.pause()
            else:
                show bg siblingfirstkiss_7
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_14
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_15
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_16
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_17
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_20
                $ renpy.pause(0.5,hard=True)
                show bg siblingfirstkiss_21
                $ renpy.pause(1,hard=True)
                show bg siblingfirstkiss_22
                sis "..."
                sis "I- I... think we should get to bed. Uh.. thanks for the game, [povname]."

    scene black
    with fade
    $ renpy.pause()
    $ sister_path = 17
    $ townmap_enabled = 1
    "The next morning..."

    scene bg mybedroom_day
    with fade

    jump lbl_mybedroom_night_sleep_1
