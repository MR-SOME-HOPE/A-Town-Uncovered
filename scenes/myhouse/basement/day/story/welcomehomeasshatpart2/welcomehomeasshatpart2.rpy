## Welcome Home Asshat Part 2 ##
label lbl_welcome_home_asshat_part2:
    if sister_path >= 33:
        scene bg mybasement_lightson2
        with fade
        "You stand outside the boxfort and talk to [sister] through the box walls."
    elif sister_path >= 11:
        scene bg mybasement_lightson
        with fade
        "You stand outside the boxfort and talk to [sister] through the box walls."
    else:
        scene bg mybasement_lightsonmessy
        with fade
        "You stand there, far enough away from [sister] who is standing in a corner of the room."

    menu:
        "Can we talk?":
            show pov embarrassed_talk at left
            show sis confused at right
            with dissolve
            pov "Can we talk about this?"
            show pov embarrassed at left
            show sis bored_talk at right
            sis "..."
            show pov confused at left
            show sis bored at right
            pov "C'mon, I'm trying to understand why you're so upset with me."
        "Don't be like this.":
            show pov embarrassed_talk at left
            show sis bored at right
            with dissolve
            pov "Don't be like this, [sister]."
            show pov shocked at left
            show sis confused_talk at right
            sis "Oh, so now I'm the problem?!"
            show pov confused_talk at left
            show sis angry at right
            pov "No, that's not what I mea-"
        "Can I come in?" if sister_path >= 11:
            show pov embarrassed_talk at left
            show sis bored at right
            with dissolve
            pov "Can I come in and talk to you face to face?"
            show pov shocked at left
            show sis angry_talk at right
            sis "No! Stay out there where I can't see you."
            show pov embarrassed at left
            show sis bored at right
            pov "Fine. Then talk to me, [sister]."
    show pov confused at left
    show sis smirk_talk at right
    with dissolve
    sis "Do you even know how worried I was?! "
    show pov shocked at left
    show sis angry_talk at right
    if winc == 0:
        sis "God, I was awoken by [missus] in the middle of the night asking if I know where you were."
    else:
        sis "God, I was awoken by Mom in the middle of the night asking if I know where you were."
    show sis confused_talk at right
    sis "I gave you the benefit of the doubt and said that you were probably at your friends house or something."
    show pov confused at left
    show sis smirk_talk at right
    sis "After a couple of calls, nothing."
    show pov shocked at left
    show sis confused_talk at right
    sis "No one had seen you nor knew where you were."
    show sis shocked_talk at right
    if winc == 0:
        sis "[missus] was bawling with tears and I went out looking for you."
    else:
        sis "Mom was bawling with tears and I went out looking for you."
    show pov bored at left
    show sis bored_talk at right
    sis "I invited every single person I could convince, to help me look."
    show pov sad at left
    show sis smirk_talk at right
    sis "I probably sounded like a random prank call stranger to most of them."
    show pov embarrassed_talk at left
    show sis angry at right
    pov "I'm really sorry I put you through that, [sister]."
    show pov shocked_talk at left
    show sis bored at right
    pov "I didn't think this would affect you so much!"
    show pov shocked at left
    show sis confused_talk at right
    sis "How did you think I would take this!?"
    show pov bored at left
    show sis angry_talk at right
    sis "Goddammit, [povname]! Do you have any idea how scared I was?!"
    show pov embarrassed at left
    show sis shocked_talk at right
    sis "I thought my heart would explode."
    sis "And now here you are. You didn't think I'd be in the least bit upset?!"
    show pov sad at left
    show sis angry_talk at right
    sis "Are you that much of an idiot?!"
    show pov sad_talk at left
    show sis shocked at right
    pov "Yeah, I've been told that a lot today."
    show pov sad at left
    show sis confused_talk at right
    sis "..."
    show sis bored_talk at right
    sis "Just... Just give me some space. Right now."
    show pov bored at left
    show sis sad_talk at right
    sis "I... I need to be alone at the moment."

    menu:
        "Ask for forgiveness":
            show pov embarrassed_talk at left
            show sis confused at right
            with dissolve
            pov "[sister], I-"
            show pov bored at left
            show sis shocked_talk at right
            sis "I said leave me alone!"
            show pov sad_talk at left
            show sis angry at right
            pov "..."
            pov "Alright..."
            show pov bored at left
            pov "..."
        "Leave":
            pass

    jump lbl_mybasement_day_setup

## Welcome Home Asshat Part 2.2
label lbl_welcome_home_asshat_part2_2:
    show pov embarrassed at left
    show sis confused at right
    with dissolve
    sis "[povname]..?"
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "Hm- Yes?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "..."
    sis "I-"
    show pov confused at left
    show sis neutral_talk at right
    sis "..."
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "I missed you..."

    menu:
        "I missed you too.":
            show pov smirk_talk at left
            show sis embarrassed at right
            pov "I missed you too."
        "I know.":
            show pov smirk at left
            pov "I know."
            if skill_cha >= 14:
                $ skill_cha -= 6
                if sister_points <= 9:
                    $ sister_points += 1
                    $ renpy.notify("You used 6 Charisma Points\nYour relationship with [sister] has increased")
                else:
                    $ sister_points = 10
            else:
                pass

    $ main_story = 41

    jump lbl_mylivingroom_day_setup
