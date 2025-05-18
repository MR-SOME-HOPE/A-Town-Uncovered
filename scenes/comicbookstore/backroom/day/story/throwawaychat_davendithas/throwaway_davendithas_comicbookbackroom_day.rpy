## Throwaway Davendithas Comic Book Back Room Day Conversation ##
label lbl_comicbookbackroom_day_davendithas:
    show btn_comicbookbackroom_day_crugeon_idle2
    show btn_comicbookbackroom_day_davendithas_idle2
    show btn_comicbookbackroom_day_lordkev_idle2
    $ renpy.pause(0.001)
    hide btn_comicbookbackroom_day_davendithas_idle2
    jump lbl_comicbookbackroom_day_davendithas_convo

label lbl_comicbookbackroom_day_davendithas_convo:

    ## 1 - 2 because he's speechless
    if gtime == 0:
        jump lbl_comicbookbackroom_day_davendithas_1
    else:
        jump lbl_comicbookbackroom_day_davendithas_2

## The Only Ones
label lbl_comicbookbackroom_day_davendithas_1:
    show pov neutral_talk at left
    with dissolve
    show dav neutral at right
    with dissolve
    pov "Hey, how are things with you, dude?"
    show pov neutral at left
    show dav neutral at right
    dav "..."
    show pov neutral_talk at left
    show dav neutral at right
    pov "Cool cool. I hear ya loud and clear."
    show pov neutral at left
    show dav neutral at right
    dav "..."
    show pov neutral_talk at left
    show dav neutral at right
    pov "Doing good, myself."
    show pov neutral_talk at left
    show dav neutral at right
    pov "I shall be off, but it's nice talking to you."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_davendithas_2:
    show pov neutral_talk at left
    with dissolve
    show dav bored at right
    with dissolve
    pov "Hey, man. What's been happening?"
    show pov neutral at left
    show dav bored at right
    dav "..."
    show pov neutral_talk at left
    show dav bored at right
    pov "Oh shit, sorry to hear that, man."
    show pov neutral at left
    show dav bored at right
    dav "..."
    show pov neutral_talk at left
    show dav bored at right
    pov "I'm sure things will come around soon, I'm here for you."
    show pov neutral_talk at left
    show dav bored at right
    pov "I'll catch up with you soon, gotta bounce."

    jump lbl_comicbookbackroom_day
