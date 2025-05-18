## Naked Yoga
label lbl_naked_yoga_revisit:
    $ renpy.pause()
    "The next morning..."

    scene bg campsite_3
    with fade

    ## SPRITEWORK

    pov "{i}*Streeetch*{/i}"
    show povn neutral_talk at left
    with dissolve
    pov "Ughhhoood- morning."
    pov "Ya’ll are up early."

    show povn neutral
    show sisn neutral at Position(xpos=1300)
    show mumn neutral_talk at right
    with dissolve
    mum "Yup! We gotta make the most of being in the outdoors."
    mum "Not everyday can you roll out of bed and immediately get a hit of the freshest air the Earth can offer."

    show povn neutral
    show sisn neutral_talk
    show mumn neutral
    sis "I was feeling a little hungry to be honest, my grumbly tummy woke me up."
    sis "Good thing we have plenty of eggs to fry."

    show povn neutral
    show sisn embarrassed
    show mumn smirk_talk
    mum "A little hungry?"
    mum "Little Miss Hungry over here was eating me out this morning."
    show povn smirk
    mum "Hungry and horny, the most dangerous combination."

    show povn neutral
    show sisn smirk_talk
    show mumn smirk
    sis "Well, it’s better than me jumping on top of you like when I was little right?"

    show povn smirk
    show sisn embarrassed
    show mumn bored_talk
    mum "Even when you were little, it hurt."
    show povn neutral
    show sisn smirk
    show mumn smirk_talk
    mum "So many times I nearly gave you a good spanking because of it."
    
    show povn neutral
    show sisn smirk_talk
    show mumn neutral
    sis "Hehehehe."

    show povn neutral_talk
    show sisn neutral
    show mumn neutral
    pov "Did you finish her off, [sister]?"

    show povn shocked
    show sisn smirk_talk
    show mumn smirk
    sis "Naaah, just a little fun to get her day started."

    show povn confused_talk
    show sisn neutral
    show mumn neutral
    pov "Is that why you’re doing yoga?"

    show povn smirk
    show sisn neutral
    show mumn smirk_talk
    mum "I’m doing yoga because I can."
    show mumn neutral_talk
    mum "I’ve heard doing naked yoga is great for the body, mind, and spirit."

    show povn smirk_talk
    show mumn neutral
    pov "It’s definitely a magnificent view for me to wake up to."

    show povn shocked
    show mumn smirk_talk
    mum "Well, I’m still pretty wet, honey."
    mum "Come and give me your hard morning wood."
    show povn smirk
    mum "I need my daily, morning, vitamin D."

    hide povn
    show povne smirk_talk at left
    show mumn smirk
    if winc == 0:
        pov "Oh, as you please, [missus]..."
    else:
        pov "Oh, as you please, mom..."

    show povne smirk
    show sisn neutral_talk
    show mumn smirk
    sis "You guys have fun, eggs will be ready by the time you’re both done."

    show povne neutral
    show sisn neutral
    show mumn neutral_talk
    mum "Sounds great, baby. Thank you for cooking."

    show sisn neutral_talk
    show mumn neutral
    sis "No biggie!"

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

label lbl_naked_yoga_revisit_hscene_revisit:
    scene img_nakedyoga_1
    with fade
    $ renpy.pause()
    show img_nakedyoga_2
    $ renpy.pause()
    show img_nakedyoga_3
    $ renpy.pause()
    show white
    with dissolve
    $ renpy.pause(2,hard=True)
    scene bg nakedyoga_4
    with dissolve
    $ renpy.pause()
    
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

image img_nakedyoga_1:
    "bg nakedyoga_1"
    pause 0.3
    "bg nakedyoga_2"
    pause 0.1
    "bg nakedyoga_3"
    pause 0.1
    "bg nakedyoga_4"
    pause 0.2
    "bg nakedyoga_5"
    pause 0.2
    repeat

image img_nakedyoga_2:
    "bg nakedyoga_1"
    pause 0.3
    "bg nakedyoga_3"
    pause 0.1
    "bg nakedyoga_4"
    pause 0.2
    "bg nakedyoga_5"
    pause 0.2
    repeat

image img_nakedyoga_3:
    "bg nakedyoga_1"
    pause 0.2
    "bg nakedyoga_4"
    pause 0.1
    "bg nakedyoga_5"
    pause 0.2
    repeat