## Meet Lailah ##
label lbl_meet_lailah:
    show pov neutral at left
    with dissolve
    show lai smirk_talk at right
    with dissolve
    lai "Yes, can I help you?"
    show pov neutral_talk at left
    show lai smirk at right
    if gtime == 0:
        pov "Good morning."
    elif gtime == 1:
        pov "Good afternoon."
    else:
        pov "Good evening."
    show pov smirk_talk at left
    show lai shocked at right
    pov "You must be Jacob's sister."
    show pov smirk at left
    show lai neutral_talk at right
    lai "Oh- Hahahahaha!"
    show lai smirk_talk at right
    lai "I was not expecting that."
    show lai neutral_talk at right
    lai "I'm Lailah, his step-mom."
    show pov neutral_talk at left
    show lai neutral at right
    pov "It's nice to meet you."
    show lai smirk at right
    pov "I'm [povname], a friend of his from university."
    show pov confused_talk at left
    pov "I was just wondering if he's in at the moment."
    show pov shocked at left
    show lai smirk_talk at right
    lai "Oh, so you're the young boy that he was talking about."
    show pov embarrassed_talk at left
    show lai smirk at right
    pov "Did he say anything nice about me."
    show pov embarrassed at left
    show lai neutral_talk at right
    lai "Oh- you know how Jacob is. A positive spirit."
    show lai smirk_talk at right
    lai "Don't worry, you have nothing to worry about."
    show lai confused_talk at right
    lai "Erm..."
    show pov confused at left
    lai "I think he's in his room?"
    show pov shocked at left
    show lai angry_talk at right
    lai "JACOB?!"
    show pov embarrassed at left
    show lai bored_talk at right
    lai "GET YOUR BUTT DOWN HERE, YOUR FRIEND'S AT THE DOOR!"
    show lai confused at right
    lai "..."
    show lai embarrassed at right
    pov "..."
    show lai confused at right
    lai "..."
    show lai confused_talk at right
    lai "Yeah, he's out at the moment."
    show lai embarrassed_talk at right
    lai "Sorry about that, hon."
    if gtime == 0:
        if day <= 4:
            show pov neutral at left
            show lai neutral_talk at right
            lai "I'm sure you can catch him at the university."
            show lai smirk_talk at right
            lai "You did say you were in the same course, right?"
            show pov neutral_talk at left
            show lai smirk at right
            pov "Yup."
            show pov embarrassed_talk at left
            show lai smirk_talk at right
            lai "Yeah, university. Like a good boy."
        else:
            show lai confused_talk at right
            lai "I'm sure you can catch him... somewhere."
            show pov confused at left
            show lai confused_talk at right
            lai "I don't know where you kids go at this time of day."
            show lai bored_talk at right
            lai "Especially on a weekend."
    elif gtime == 1:
        show pov neutral at left
        show lai confused_talk at right
        lai "He goes to the comic book store a lot."
        show lai smirk_talk at right
        lai "Maybe you can find him there?"
        show pov embarrassed at left
        show lai confused_talk at right
        lai "If that even is a place you like going to..."
    else:
        show pov confused at left
        show lai smirk_talk at right
        lai "I think he's out on a playdate with a friend."
        show pov embarrassed at left
        show lai bored_talk at right
        lai "One of those cringey, nerdy fellas."
        show lai embarrassed_talk at right
        lai "I mean.. y'know. Nice boys, nice boys."
    show pov embarrassed_talk at left
    show lai neutral at right
    pov "Oh, okay. Thanks. It's nothing time-sensitive so I'll just see him when I see him."
    show pov neutral at left
    show lai neutral_talk at right
    lai "I'll be sure to tell him you stopped by anyway."
    show pov neutral_talk at left
    show lai confused at right
    pov "Thanks. Again, it was great meeting you, Mrs-"
    show pov shocked at left
    show lai smirk_talk at right
    lai "Oh, just call me Lailah, I'm not used to the whole 'Mrs', and 'ma'am' thing."
    show pov embarrassed_talk at left
    show lai smirk at right
    pov "You got it, Lailah."
    show pov embarrassed at left
    show lai smirk_talk at right
    lai "See you around, [povname]."
    hide lai smirk_talk
    show pov smirk at left
    pov "{i}She seems cool. Cougar vibes.{/i}"
    show pov confused at left
    pov "{i}Didn't know Jacob had a step-mom.{/i}"
    pov "{i}Wonder what happened to his real mom.{/i}"

    $ lailah_path = 1
    $ add_contact("Lailah")

    if gtime <= 1:
        jump lbl_jacobhouseoutside_day_setup
    else:
        jump lbl_jacobhouseoutside_night_setup
