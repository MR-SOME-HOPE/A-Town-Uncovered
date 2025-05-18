## Surprise Weekend Camping Getaway
label lbl_surprise_weekend_camping_getaway:
    scene bg mylivingroom_day
    with fade

    show pov confused at left
    show sis bored at Position(xpos=1300)
    show mum neutral_talk at right
    with dissolve
    mum "[povname]! Good, you’re here."

    show pov confused_talk at left
    show mum neutral at right
    pov "What’s up? Are we in trouble?"

    show pov confused at left
    show sis bored_talk at Position(xpos=1300)
    sis "She jumped me too in the kitchen. I just came down to grab a snack."

    show sis confused at Position(xpos=1300)
    show mum neutral_talk at right
    mum "I have some news that I wanted to share with you both."

    show sis confused_talk at Position(xpos=1300)
    show mum neutral at right
    sis "Uh-huh..?"
    sis "Feeling wary."

    show pov shocked at left
    show sis shocked at Position(xpos=1300)
    show mum neutral_talk at right
    mum "We’re gonna go on a weekend family camping trip!"

    show sis shocked_talk at Position(xpos=1300)
    show mum neutral at right
    sis "What?"

    show pov shocked_talk at left
    show sis shocked at Position(xpos=1300)
    show mum confused at right
    pov "What, tomorrow?!"
    pov "Why are you telling us this on such short notice."

    show pov confused at left
    show sis sad_talk at Position(xpos=1300)
    show mum bored at right
    sis "I had plans!"

    show pov smirk_talk at left
    show sis bored at Position(xpos=1300)
    pov "No, you didn’t."

    show pov smirk at left
    show sis angry_talk at Position(xpos=1300)
    sis "You don’t know!"

    show pov confused at left
    show sis bored at Position(xpos=1300)
    show mum shocked_talk at right
    mum "Kids, it’ll be fun. We haven’t done anything like this as a family in a long while."
    show mum embarrassed_talk at right
    mum "It’s about time we did."
    mum "You can spare a weekend, right?"

    show pov embarrassed_talk at left
    show mum sad at right
    pov "It’s not that I can’t-"
    pov "It’s just-"

    show pov sad at left
    show mum sad_talk at right
    mum "Just what?"

    show pov embarrassed_talk at left
    show mum neutral at right
    pov "Nothing."

    show pov embarrassed at left
    show sis bored_talk at Position(xpos=1300)
    show mum smirk at right
    sis "We don’t even camp. We never have."

    show sis bored at Position(xpos=1300)
    show mum smirk_talk at right
    mum "Well, tomorrow is a great time to start! Who knows, maybe you’ll actually enjoy yourself."

    show pov embarrassed at left
    show sis shocked_talk at Position(xpos=1300)
    show mum bored at right
    sis "Okay, but what if-"

    show pov confused at left
    show sis bored at Position(xpos=1300)
    show mum bored_talk at right
    mum "[sister]."
    mum "Enough with the attitude, we’re going."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "I already bought some camping supplies and a small tent for us."
    show pov shocked at left
    show mum smirk_talk at right
    mum "[povname] should be able to put it up for us. Aren’t you, sweetie?"

    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I mean- I guess."
    pov "If it’s small then it shouldn’t be that hard, right?"

    show pov shocked at left
    show mum confused_talk at right
    mum "See? Why can’t you be more like him?"

    show pov embarrassed at left
    show sis bored_talk at Position(xpos=1300)
    show mum neutral at right
    sis "*Groans*"
    sis "Whatever, fine."
    sis "I’d feel a little better about if you hadn’t dropped this on us so soon."

    show sis bored at Position(xpos=1300)
    show mum smirk_talk at right
    mum "I thought you liked surprises."

    show sis shocked_talk at Position(xpos=1300)
    show mum neutral at right
    sis "This-"
    show sis bored_talk at Position(xpos=1300)
    sis "Whatever."
    sis "I’ll go pack a bag."

    hide sis with dissolve

    show mum neutral_talk at right
    mum "Don’t pack too heavily, it’s just the weekend, remember."
    mum "We’re roughin’ it! Partly."

    show mum smirk at right
    sis "Don’t say that so excitedly!"

    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I’ll go pack a bag too."

    show pov neutral at left
    show mum neutral_talk at right
    mum "We’re leaving early tomorrow morning, okay?"

    show pov neutral_talk at left
    show mum neutral at right
    pov "Yup."

    $ mumsiscamp_path = 2

    jump lbl_mylivingroom_day_setup
