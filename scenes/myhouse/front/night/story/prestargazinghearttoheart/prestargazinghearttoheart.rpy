## Pre Stargazing Heart to Heart ##
label lbl_pre_stargazing_heart_to_heart:

    scene bg myhousefront_night
    with fade
    show pov neutral at left
    with dissolve
    show sis neutral_talk at right
    with dissolve
    sis "Hey! Ready to go?"
    show pov neutral_talk at left
    show sis neutral at right
    pov "On your mark, [sister]."
    show pov neutral at left
    show sis neutral_talk at right
    if winc == 0:
        sis "Great! Let's get going, [missus]'s letting us stay there a while but she wants us back as soon as we can."
        show pov smirk at left
        show sis smirk_talk at right
        sis "I told her we would also get dinner out so that got us an extra hour."
        show pov smirk_talk at left
        show sis shocked at right
        pov "Sweet! Want me to drive?"
        show pov bored at left
        show sis smirk_talk at right
        sis "No offense, [povname] but I'm not in the mood for a heart attack right now."
    else:
        sis "Great! Let's get going, Mom's letting us stay there a while but she wants us back as soon as we can."
        show pov smirk at left
        show sis smirk_talk at right
        sis "I told her we would also get dinner out so that got us an extra hour."
        show pov smirk_talk at left
        show sis shocked at right
        pov "Sweet! Want me to drive?"
        show pov bored at left
        show sis smirk_talk at right
        sis "No offense, baby-bro but I'm not in the mood for a heart attack right now."
    show pov bored_talk at left
    show sis smirk at right
    pov "Very funny, [sister]."
    show pov neutral at left
    show sis smirk_talk at right
    sis "I know! Now come on! I want to get there before it starts!"

    jump lbl_stargazing_heart_to_heart
