## Throwaway Mother Parents Room Night Conversation ##
label lbl_parentsbedroom_night_mother:
    show btn parentsbedroom_night_mother_idle
    menu:
        "Talk":
            jump lbl_parentsbedroom_night_mother_convo
        "Give gift" if selecteditem != None:
            jump lbl_mum_giftgiving
        "I need some company":
            menu:
                "Trouble sleeping" if mum_path >= 31:
                    jump lbl_parentsbedroom_night_mother_hscene_redo
                "With [sister] down in the fort" if mumsis_path >= 13:
                    jump lbl_momxsisxmc_boxfort_premum
                "Have some fun?" if mum_path >= 31:
                    jump lbl_mom_mating_press_pre
                "Can you and [sister] come help me fall asleep?" if mumsis_path >= 13:
                    jump lbl_momxsisterxmc_cocksandwich
                "Nevermind":
                    jump lbl_parentsbedroom_night_mother
        "Nevermind":
            jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_convo:
    hide btn parentsbedroom_night_mother_idle

## 1 - 10 is evening exclusive
    if date == 1 or date == 11 or date == 23:
        jump lbl_parentsbedroom_night_mother_1
    elif date == 2 or date == 16 or date == 25:
        jump lbl_parentsbedroom_night_mother_2
    elif date == 3 or date == 17 or date == 29:
        jump lbl_parentsbedroom_night_mother_3
    elif date == 4 or date == 19 or date == 21:
        jump lbl_parentsbedroom_night_mother_4
    elif date == 5 or date == 20 or date == 22:
        if 27 <= sister_path <= 33:
            jump lbl_parentsbedroom_night_mother_4
        else:
            jump lbl_parentsbedroom_night_mother_5
    elif date == 6 or date == 12 or date == 30:
        jump lbl_parentsbedroom_night_mother_6
    elif date == 7 or date == 14 or date == 24:
        jump lbl_parentsbedroom_night_mother_7
    elif date == 8 or date == 18 or date == 26:
        jump lbl_parentsbedroom_night_mother_8
    elif date == 9 or date == 13 or date == 28:
        jump lbl_parentsbedroom_night_mother_9
    elif date == 10 or date == 15 or date == 27 or date == 31:
        if main_story >= 22:
            jump lbl_parentsbedroom_night_mother_10
        else:
            jump lbl_parentsbedroom_night_mother_1

label lbl_parentsbedroom_night_mother_sleep:
    pov "{i}She's sleeping, I shouldn't disturb her.{/i}"
    call screen scr_parentsbedroom_night

label lbl_parentsbedroom_night_mother_1:
    if winc == 1:
        show pov neutral_talk at left
        with dissolve
        show mum neutral at right
        with dissolve
        pov "Hey, Mom. What's for dinner?"
        show pov bored at left
        show mum neutral_talk at right
        mum "Leftover night, baby."
        show pov bored_talk at left
        show mum bored at right
        pov "What leftovers are there to eat?"
        show pov bored at left
        show mum confused_talk at right
        mum "Check the fridge, I made some food last night."
        show pov sad_talk at left
        show mum bored at right
        pov "Ugh, but I hated last night's dinner."
        show pov bored at left
        show mum smirk_talk at right
        mum "You could also make yourself cereal."

        jump lbl_parentsbedroom_night
    else:
        show pov neutral_talk at left
        with dissolve
        show mum neutral at right
        with dissolve
        pov "Hey, [missus]. What's for dinner?"
        show pov bored at left
        show mum neutral_talk at right
        mum "Leftover night, baby."
        show pov bored_talk at left
        show mum bored at right
        pov "What leftovers are there to eat?"
        show pov bored at left
        show mum confused_talk at right
        mum "Check the fridge, I made some food last night."
        show pov sad_talk at left
        show mum bored at right
        pov "Ugh, but I hated last night's dinner."
        show pov bored at left
        show mum smirk_talk at right
        mum "You could also make yourself cereal."

        jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_2:
    if winc == 1:
        show pov neutral_talk at left
        with dissolve
        show mum neutral at right
        with dissolve
        pov "Whatcha' watching, momma?"
        show pov bored at left
        show mum neutral_talk at right
        mum "Tit-tanic."
        show pov confused_talk at left
        show mum embarrassed at right
        pov "That's the nth time you've watched that!"
        show pov neutral at left
        show mum smirk_talk at right
        mum "I love my Deonardo Lecaprio."

        jump lbl_parentsbedroom_night
    else:
        show pov neutral_talk at left
        with dissolve
        show mum neutral at right
        with dissolve
        pov "Whatcha' watching, [missus]?"
        show pov bored at left
        show mum neutral_talk at right
        mum "Tit-tanic."
        show pov confused_talk at left
        show mum embarrassed at right
        pov "That's the nth time you've watched that!"
        show pov neutral at left
        show mum smirk_talk at right
        mum "I love my Deonardo Lecaprio."

        jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_3:
    if winc == 1:
        show pov neutral_talk at left
        with dissolve
        show mum neutral at right
        with dissolve
        pov "Hey, mo-"
        show pov shocked at left
        pov "{i}*Sniff*{/i}"
        show pov sad at left
        show mum neutral at right
        mum "Hmm?"
        show pov sad_talk at left
        show mum confused at right
        pov "What's that smell."
        show pov confused_talk at left
        show mum embarrassed at right
        pov "Di-did you fart?!"
        show pov shocked at left
        show mum smirk_talk at right
        mum "I guess you came in at the wrong time, sweetie."
        show pov angry_talk at left
        show mum neutral at right
        pov "Jesus, Mom!"

        jump lbl_parentsbedroom_night
    else:
        show pov neutral_talk at left
        with dissolve
        show mum neutral at right
        with dissolve
        pov "Hey-"
        show pov shocked at left
        pov "{i}*Sniff*{/i}"
        show pov sad at left
        show mum neutral at right
        mum "Hmm?"
        show pov sad_talk at left
        show mum confused at right
        pov "What's that smell."
        show pov confused_talk at left
        show mum embarrassed at right
        pov "Di-did you fart?!"
        show pov shocked at left
        show mum smirk_talk at right
        mum "I guess you came in at the wrong time, sweetie."
        show pov angry_talk at left
        show mum neutral at right
        pov "Jesus, [missus]!"

        jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_4:
    show pov confused_talk at left
    with dissolve
    show mum neutral at right
    with dissolve
    pov "What day is it today?"
    show pov confused at left
    show mum confused_talk at right
    mum "It's.."
    mum "[day]...?"
    show mum shocked_talk at right
    mum "... Why? Did I forget to do something?"
    show pov confused_talk at left
    show mum angry at right
    pov "I don't know, you tell me."
    show pov smirk at left
    show mum angry_talk at right
    mum "... Stop blocking the TV, honey."

    jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_5:
    if winc == 1:
        show pov sad_talk at left
        with dissolve
        show mum bored at right
        with dissolve
        pov "Mom, [sister] was making fun of me!"
        show pov sad at left
        show mum confused_talk at right
        mum "Did she really? Or are you just trying to cause trouble?"
        show mum confused at right
        pov "..."
        show pov embarrassed_talk at left
        show mum bored at right
        pov "Y'know what? It's fine."
        pov "My heart doesn't hurt that much."

        jump lbl_parentsbedroom_night
    else:
        show pov sad_talk at left
        with dissolve
        show mum bored at right
        with dissolve
        pov "[missus], [sister] was making fun of me!"
        show pov sad at left
        show mum confused_talk at right
        mum "Did she really? Or are you just trying to cause trouble?"
        show mum confused at right
        pov "..."
        show pov embarrassed_talk at left
        show mum bored at right
        pov "Y'know what? It's fine."
        pov "My heart doesn't hurt that much."

        jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_6:
    if winc == 1:
        show pov confused_talk at left
        with dissolve
        show mum neutral at right
        with dissolve
        pov "Where's Dad?"
        show pov confused at left
        show mum neutral_talk at right
        mum "Still out with his co-workers."
        show pov confused_talk at left
        show mum bored at right
        pov "Why is he always out?"
        show pov confused at left
        show mum bored_talk at right
        mum "He's a workaholic, honey."
        show pov embarrassed at left
        mum "Promise me you won't become a workaholic."

        jump lbl_parentsbedroom_night
    else:
        show pov confused_talk at left
        with dissolve
        show mum neutral at right
        with dissolve
        pov "Where's [dadname]?"
        show pov confused at left
        show mum neutral_talk at right
        mum "Still out with his co-workers."
        show pov confused_talk at left
        show mum bored at right
        pov "Why is he always out?"
        show pov confused at left
        show mum bored_talk at right
        mum "He's a workaholic, honey."
        show pov embarrassed at left
        mum "Promise me you won't become a workaholic."

        jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_7:
    show pov bored at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Hey, [povname]."
    mum "Are you looking for something?"
    show pov bored_talk at left
    show mum confused at right
    pov "Yeah. A purpose."
    pov "I need to know where my life should take me."
    show pov bored at left
    show mum embarrassed_talk at right
    mum "That's too much hippie mumbo-jumbo for one day, don't you think?"

    jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_8:
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "What's up, honey?"
    mum "How's university going?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It's going."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Learn anything new?"
    show pov neutral_talk at left
    show mum bored at right
    pov "Not really."
    show pov neutral at left
    show mum bored_talk at right
    mum "Ah, okay. Nice talk."

    jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_9:
    if winc == 1:
        show pov bored at left
        with dissolve
        show mum confused_talk at right
        with dissolve
        mum "Did you put the rubbish out?"
        show pov bored_talk at left
        show mum confused at right
        pov "... Yes, Mom."
        show pov bored at left
        show mum confused_talk at right
        mum "Put the dry dishes away?"
        show pov bored_talk at left
        show mum confused at right
        pov "Yes, Mom."
        show pov bored at left
        show mum smirk_talk at right
        mum "Laundry?"
        show pov bored_talk at left
        show mum embarrassed at right
        pov "That's your job, Mom. I can't do {i}everything{/i}."

        jump lbl_parentsbedroom_night
    else:
        show pov bored at left
        with dissolve
        show mum confused_talk at right
        with dissolve
        mum "Did you put the rubbish out?"
        show pov bored_talk at left
        show mum confused at right
        pov "... Yes, [missus]."
        show pov bored at left
        show mum confused_talk at right
        mum "Put the dry dishes away?"
        show pov bored_talk at left
        show mum confused at right
        pov "Yes, [missus]."
        show pov bored at left
        show mum smirk_talk at right
        mum "Laundry?"
        show pov bored_talk at left
        show mum embarrassed at right
        pov "That's your job, [missus]. I can't do {i}everything{/i}."

        jump lbl_parentsbedroom_night

label lbl_parentsbedroom_night_mother_10:
    show pov embarrassed at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Hey, baby. How's work?"
    show pov embarrassed_talk at left
    show mum shocked at right
    pov "The usual. {i}*sniff*{/i}"
    show pov confused at left
    show mum sad_talk at right
    mum "Oh my God, you need to get some rest, you sound sick."
    show pov smirk_talk at left
    show mum embarrassed at right
    pov "No, no. I'm fine. I just like the smell of money in my pocket."

    jump lbl_parentsbedroom_night
