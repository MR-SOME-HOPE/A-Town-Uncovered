## Mother Main Story Throwaway Conversations Kitchen ##
label lbl_mykitchen_day_mother_wake_up_sister:
    show pov bored at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    if winc == 0:
        mum "Shouldn't you be waking up your [sisrole]?"
    else:
        mum "Shouldn't you be waking up [sister]?"
    show mum neutral at right
    show pov bored_talk at left
    pov "Yeah, yeah, I was about to get onto that."

    jump lbl_mykitchen_day

label lbl_mykitchen_day_mother_sexworld_0:
    show pov sad_talk at left
    with dissolve
    hide btn mykitchen_day_mother_idle
    show mum confused at right
    with dissolve
    pov "Mom? Are you feeling okay? Why are you acting like that?"
    show pov sad at left
    show mum confused_talk at right
    mum "Hmm? I'm fine. What are you talking about?"
    show pov sad_talk at left
    show mum confused at right
    if winc == 0:
        pov "Y'know... with [dadrole]?"
    else:
        pov "Y'know... with Dad?"
    show pov sad at left
    show mum smirk_talk at right
    mum "He just loves me, [povname]."
    show pov embarrassed at left
    mum "It seems that I should be asking if YOU'RE the one that's okay."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "Umm.. I think I am. I'll just head to uni."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Alright, sweetie. I love you."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "Love you too.."

    jump lbl_mykitchen_day
