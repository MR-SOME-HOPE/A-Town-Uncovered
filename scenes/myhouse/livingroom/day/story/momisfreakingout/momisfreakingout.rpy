## Mom is Freaking Out
label lbl_mom_is_freaking_out:
    scene bg mylivingroom_day
    with dissolve
    show pov neutral_talk at left
    with dissolve
    show mum angry at right
    with dissolve
    pov "I'm hom-"
    show pov confused at left
    show mum angry_talk at right
    mum "What took you so long?!"
    ## CG Scene Start
    #scene bg momisfreakingout_temp1
    scene bg momisfreakingout
    with hpunch
    $ renpy.pause()
    mum "I told you to get here as soon as possible; and it takes you twenty minutes to get back?!"
    mum "What if those people were still around and decided to take you when you are wasting time?!"
    pov "Mmmf! Mnphnn, Mphhh Mnnnmm!"

    #"You are unable to say much as she is currently choking you out between her breasts not letting you breath."

    if winc == 0:
        sis "[missus], you are choking him!"
    else:
        sis "Mom, you are choking him!"

    scene bg mylivingroom_day
    with fade
    show pov embarrassed_talk at left
    with dissolve
    show sis smirk at Position(xpos=1300)
    with dissolve
    show mum angry at right
    with dissolve

    pov "{i}*Gasp*{/i}"
    show pov embarrassed_talk at left
    show sis smirk at Position(xpos=1300)
    show mum angry at right
    if winc == 0:
        pov "Oh gods, I think I almost saw Jesus!"
        show pov confused at left
        show sis confused at Position(xpos=1300)
        show mum angry_talk at right
        mum "What took you so long?!"
        show pov confused_talk at left
        show sis sad at Position(xpos=1300)
        show mum angry at right
        pov "[missus], I literally started walking here the moment we finished talking on the phone!"
    else:
        pov "Oh gods, I think I almost saw Grandma!"
        show pov confused at left
        show sis confused at Position(xpos=1300)
        show mum angry_talk at right
        mum "What took you so long?!"
        show pov confused_talk at left
        show sis confused at Position(xpos=1300)
        show mum angry at right
        pov "M-Mom, I literally started walking here the moment we finished talking on the phone!"
    show pov embarrassed_talk at left
    show sis smirk at Position(xpos=1300)
    show mum angry at right
    pov "Effie walked with me home and we dragged on a bit by talking to calm us down!"
    show pov confused at left
    show sis sad at Position(xpos=1300)
    show mum angry_talk at right
    mum "You still took too long for such a short stretch!"
    show pov sad at left
    show sis sad_talk at Position(xpos=1300)
    show mum angry at right
    if winc == 0:
        sis "[missus], it’s alright."
    else:
        sis "Mom, it’s alright."
    sis "He is home and safe - you can stop freaking out now."
    show pov sad at left
    show sis sad at Position(xpos=1300)
    show mum sad_talk at right
    mum "R-Right…"
    mum "It’s fine. You are both fine…"
    show pov sad_talk at left
    show sis sad at Position(xpos=1300)
    show mum sad at right
    if winc == 0:
        pov "Sit down before you pass out, [missus]."
    else:
        pov "Sit down before you pass out, Mom."
    pov "Focus on your breathing."
    show pov sad at left
    show sis sad at Position(xpos=1300)
    show mum sad_talk at right
    mum "I-I have to go lay down."
    show pov shocked at left
    show sis shocked at Position(xpos=1300)
    show mum shocked_talk at right
    mum "I cannot believe this is happening! We're in danger."
    mum "We're not safe anymore!"
    show pov confused at left
    show sis confused at Position(xpos=1300)
    show mum confused_talk at right
    if winc == 0:
        mum "[dadname] said this is a safe town but not anymore."
        mum "I can't- I can't- I- I can't-"
        show pov sad at left
        show sis sad_talk at Position(xpos=1300)
        show mum confused at right
        sis "It’s okay, [missus]. We're okay. See?"
        sis "Come on, we’ll help you up."
        show pov sad at left
        show sis sad at Position(xpos=1300)
        show mum confused_talk at right
        mum "I’ll call [dadname] later. Better to keep him informed."
        show pov sad_talk at left
        show sis sad at Position(xpos=1300)
        show mum confused at right
        pov "Don't worry about him, I'm sure he's well informed already."
        pov "Let’s get you in bed, [missus]."
    else:
        mum "Your father said this is a safe town but not anymore."
        mum "I can't- I can't- I- I can't-"
        show pov sad at left
        show sis sad_talk at Position(xpos=1300)
        show mum confused at right
        sis "It’s okay, Mom. We're okay. See?"
        sis "Come on, we’ll help you up."
        show pov sad at left
        show sis sad at Position(xpos=1300)
        show mum confused_talk at right
        mum "I’ll call your dad later. Better to keep him informed."
        show pov sad_talk at left
        show sis sad at Position(xpos=1300)
        show mum confused at right
        pov "Don't worry about him, I'm sure he's well informed already."
        pov "Let’s get you in bed, Mom."

    $ main_story = 56

    $ townmap_enabled = 1

    jump lbl_quite_the_town
