## Getting Back Home
label lbl_getting_back_home:
    scene black
    with fade
    scene bg mylivingroom_day
    show sis confused at right
    show mum confused at Position(xpos=1300)
    with fade
    show pov neutral at left
    with dissolve
    #"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    #if winc == 1:
    #    "You arrive home to find Mom and Sister in the living room."
    #else:
    #    "You arrive home to find [missus] and [sister] in the living room."
    show pov neutral_talk at left
    pov "I'm home."
    show pov neutral
    show mum neutral_talk at Position(xpos=1300)
    mum "Welcome back, sweetie!"
    show mum neutral at Position(xpos=1300)
    show sis bored_talk at right
    sis "About time!"
    sis "What have you been up to?"
    show sis bored
    show pov neutral_talk

    if kidnapping_assembly_crossroad == 1:#mainstory_62_crossroads_hangout == 1:
        pov "Helped Effie clean the coffee shop a bit after it got vandalized, then we went to the mall for some drinks and to chill."
        show sis sad_talk
        sis "You know, you could have at least called and asked if I wanted anything!"
        show sis sad
        show pov bored_talk
        pov "I am not going to walk all the way from the mall with another tube of ice cream for you, after last time!"
        pov "By the time I came back, it was already soup, and you went apeshit on me."
        show sis angry_talk
        sis "Aw, come on!"
        if winc == 1:
            sis "What happened to brotherly love, [povname]?"
        else:
            sis "What happened to [povsisrole] love, [povname]?"
        sis "Besides, that's what you get for taking the long way home from the mall!"
        sis "Why don’t you use the shortcut through the park?"
        show sis angry
        show pov shocked_talk
        pov "I, uh…"
        pov "...rather avoid the park as much as I can right now."
        show pov neutral_talk
        pov "Anyway, I'm back. Sorry to keep you guys waiting."
        show mum neutral_talk
        mum "As long as you are home safe, [povname]."
        mum "Speaking of which: I wanted to talk to the two of you about something serious."
        mum "Let’s go to the dining room."
        show mum neutral
        show sis confused_talk
        sis "Why the dining room?"
        show sis confused
        show mum neutral_talk
        mum "I want to try using it more often, for serious family talks."
        mum "Now, come on, you two."

    elif kidnapping_assembly_crossroad == 2:#mainstory_62_crossroads_stay == 1:
        pov "Some paranoid jackass started spreading rumors about me in uni."
        pov "I stayed behind to try and do some damage control before I became a social outcast or people started chasing me with pitchforks."

        show sis smirk_talk
        if winc == 1:
            sis "I feel you, bro."
        else:
            sis "I feel you, [povname]."
        show sis angry_talk
        sis "Some people were giving me the stink eye when I was on my way to work."
        sis "I was about to flip them off, before Hazel stopped me. "
        show sis neutral
        show pov neutral_talk
        pov "Best not to make things worse."
        show pov neutral
        show sis smirk_talk
        sis "Yeah, no kidding. "
        show sis neutral
        show mum neutral_talk
        mum "Speaking of all of this, I need to talk to the both of you about something important."
        mum "Come on to the dining room."
        show mum neutral
        show sis confused_talk
        sis "Why talk there?"
        show sis confused
        show mum neutral_talk
        mum "It's a serious talk, [sister]."
        mum "Now come on."
        show mum neutral
        show sis confused_talk
        sis "Alright, alright."
        sis "Don't put your panties in a bunch."

    $ main_story = 66

    jump lbl_safety_and_home_life
