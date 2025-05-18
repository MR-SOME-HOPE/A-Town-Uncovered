## Throwaway Dad Living Room Day Conversation ##
label lbl_mylivingroom_day_dad:
## Add after caught parents
## Add when dad goes on his business trip in mom's story
    show btn mylivingroom_day_dad_idle
    $ renpy.pause(0.01)
    jump lbl_mylivingroom_day_dad_convo

label lbl_mylivingroom_day_dad_convo:
## 1 - 5 is afternoon exclusive
## 6 - 10 is morning exclusive
## 11 - 15 is interchangable
    if date < 7:
        if day == 5:
            jump lbl_mylivingroom_day_dad_6
        elif day == 6:
            jump lbl_myhouse_day_dad_11
    elif date < 14:
        if day == 5:
            jump lbl_mylivingroom_day_dad_7
        elif day == 6:
            jump lbl_myhouse_day_dad_12
    elif date < 21:
        if day == 5:
            jump lbl_mylivingroom_day_dad_8
        elif day == 6:
            jump lbl_myhouse_day_dad_13
    elif date < 27:
        if day == 5:
            jump lbl_mylivingroom_day_dad_9
        elif day == 6:
            jump lbl_myhouse_day_dad_14
    elif date < 31:
        if day == 5:
            jump lbl_mylivingroom_day_dad_10
        elif day == 6:
            jump lbl_myhouse_day_dad_15
    #if date == 1 or date == 20 or date == 27 or date == 31:
    #    jump lbl_mylivingroom_day_dad_6
    #elif date == 2 or date == 15 or date == 29:
    #    jump lbl_mylivingroom_day_dad_7
    #elif date == 5 or date == 17 or date == 28:
    #    jump lbl_mylivingroom_day_dad_8
    #elif date == 8 or date == 13 or date == 26:
    #    jump lbl_mylivingroom_day_dad_9
    #elif date == 3 or date == 11 or date == 30:
    #    jump lbl_mylivingroom_day_dad_10
    #elif date == 7 or date == 12 or date == 25:
    #    jump lbl_myhouse_day_dad_11
    #elif date == 10 or date == 16 or date == 23:
    #    jump lbl_myhouse_day_dad_12
    #elif date == 6 or date == 18 or date == 24:
    #    jump lbl_myhouse_day_dad_13
    #elif date == 9 or date == 14 or date == 22:
    #    jump lbl_myhouse_day_dad_14
    #elif date == 4 or date == 19 or date == 21:
    #    jump lbl_myhouse_day_dad_15

## morning Exclusive
label lbl_mylivingroom_day_dad_6:
    show pov neutral_talk at left
    with dissolve
    hide btn parentsbedroom_day_dad_idle
    show dadc neutral at right
    with dissolve
    pov "What's on TV?"
    show pov bored at left
    show dadc angry_talk at right
    dad "Use your eyes, I'm watching the news."
    show pov bored_talk at left
    show dadc neutral at right
    pov "Alright, I was just asking, don't need to be snappy."
    show pov bored at left
    show dadc neutral_talk at right
    dad "Don't you have coursework to do by Monday?"
    show pov bored_talk at left
    show dadc neutral at right
    pov "Not this weekend."
    show pov neutral at left
    show dadc angry_talk at right
    dad "Then go do something productive where you're not bothering me."

    jump lbl_mylivingroom_day

label lbl_mylivingroom_day_dad_7:
    if winc == 1:
        show pov smirk_talk at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        show dadc angry at right
        with dissolve
        pov "Hello, father. Good to see you're in a good mood."
        show dadc angry at right
        dad "..."
        show pov smirk at left
        show dadc angry_talk at right
        dad "Does it look like I'm in a good mood?"
        show pov smirk_talk at left
        show dadc angry at right
        pov "You want the honest answer or the funny answer?"
        show pov bored at left
        show dadc neutral_talk at right
        dad "Leave me alone, [povname]. Go be useful and get me a cup of coffee or something."
        show pov neutral_talk at left
        show dadc neutral at right
        pov "I'll pass on that offer, thanks."

        jump lbl_mylivingroom_day
    else:
        show pov smirk_talk at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        show dadc angry at right
        with dissolve
        pov "Hello, [dadrole]. Good to see you're in a good mood."
        show dadc angry at right
        dad "..."
        show pov smirk at left
        show dadc angry_talk at right
        dad "Does it look like I'm in a good mood?"
        show pov smirk_talk at left
        show dadc angry at right
        pov "You want the honest answer or the funny answer?"
        show pov bored at left
        show dadc neutral_talk at right
        dad "Leave me alone, [povname]. Go be useful and get me a cup of coffee or something."
        show pov neutral_talk at left
        show dadc neutral at right
        pov "I'll pass on that offer, thanks."

        jump lbl_mylivingroom_day

label lbl_mylivingroom_day_dad_8:
    if winc == 1:
        show pov neutral_talk at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "Dad, knock knock."
        show pov neutral at left
        show dadc angry_talk at right
        dad "What?"
        show pov confused_talk at left
        show dadc angry at right
        pov "Knock knock."
        show pov bored at left
        show dadc angry_talk at right
        dad "Knock knock what? Are you retarded?"
        show pov confused_talk at left
        show dadc angry at right
        pov "Orange..."
        show pov bored at left
        show dadc angry_talk at right
        dad "Go bother someone else, idiot."

        jump lbl_mylivingroom_day
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "[dadname], knock knock."
        show pov neutral at left
        show dadc angry_talk at right
        dad "What?"
        show pov confused_talk at left
        show dadc angry at right
        pov "Knock knock."
        show pov bored at left
        show dadc angry_talk at right
        dad "Knock knock what? Are you retarded?"
        show pov confused_talk at left
        show dadc angry at right
        pov "Orange..."
        show pov bored at left
        show dadc angry_talk at right
        dad "Go bother someone else, idiot."

        jump lbl_mylivingroom_day

label lbl_mylivingroom_day_dad_9:
    show pov confused at left
    with dissolve
    hide btn parentsbedroom_day_dad_idle
    show dadc neutral_talk at right
    with dissolve
    dad "What do you want?"
    show pov confused_talk at left
    show dadc neutral at right
    pov "I didn't even say anything."
    show pov neutral at left
    show dadc neutral_talk at right
    dad "Do you want your allowance?"
    show pov neutral_talk at left
    show dadc neutral at right
    pov "Uh- actually yeah, that'd be grea-."
    show pov bored at left
    show dadc neutral_talk at right
    dad "You better get your ass on the clock then. You have a job already."
    show pov bored_talk at left
    show dadc neutral at right
    pov "Yeah, whatever."

    jump lbl_mylivingroom_day

label lbl_mylivingroom_day_dad_10:
    if winc == 1:
        show pov confused at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        show dadc neutral_talk at right
        with dissolve
        dad "How's university?"
        show pov confused_talk at left
        show dadc neutral at right
        pov "Why do you care?"
        show pov bored at left
        show dadc neutral_talk at right
        dad "I don't. Your mother told me that I should try and talk to you more."
        show pov confused_talk at left
        show dadc neutral at right
        pov "...Uni's fine."
        show pov bored at left
        show dadc neutral_talk at right
        dad "Bloody amazing conversation, [povname]."
        show pov bored at left
        show dadc neutral_talk at right
        dad "You can bugger off now."

        jump lbl_mylivingroom_day
    else:
        show pov confused at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        show dadc neutral_talk at right
        with dissolve
        dad "How's university?"
        show pov confused_talk at left
        show dadc neutral at right
        pov "Why do you care?"
        show pov bored at left
        show dadc neutral_talk at right
        dad "I don't. Your [povmumrole] told me that I should try and talk to you more."
        show pov confused_talk at left
        show dadc neutral at right
        pov "...Uni's fine."
        show pov bored at left
        show dadc neutral_talk at right
        dad "Bloody amazing conversation, [povname]."
        show pov bored at left
        show dadc neutral_talk at right
        dad "You can bugger off now."

        jump lbl_mylivingroom_day
