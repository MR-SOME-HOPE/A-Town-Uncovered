## Mom Mating Press Pre
label lbl_mom_mating_press_pre:
    show pov neutral_talk at left
    show mum neutral at right
    with dissolve
    if winc == 1:
        pov "Hey, mom. I was wondering if you wanted to have a little fun before bed."
    else:
        pov "Hey, [missus]. I was wondering if you wanted to have a little fun before bed."
    show pov smirk
    show mum smirk_talk
    mum "Oh~? What do you have in mind?"
    show pov smirk_talk
    show mum smirk
    pov "Come with me to my room, I have something planned."
    show pov smirk
    show mum smirk_talk
    mum "Ooh~ Surprises."

    scene bg mybedroom_night_lightson
    with fade
    show mum smirk_talk at right
    with dissolve
    mum "Well- what do you have in mind [povname]?"
    show povn neutral_talk at left
    show mum shocked at right
    pov "Tah-dah~!"
    show povn shocked
    show mum shocked_talk
    mum "[povname]!"
    show povn neutral
    mum "How did you get undressed so quick?!"
    show povn smirk
    show mum neutral_talk
    mum "That's amazing."
    mum "Hold on, let me catch up-"
    hide mum neutral_talk
    with dissolve
    $ renpy.pause(1,hard=True)
    show mumn smirk_talk at right
    with dissolve
    mum "There we go, just had to drop it off the shoulders, easy and quick."
    show povn neutral_talk
    show mumn smirk
    pov "You look gorgeous as ever, mom."
    show povn embarrassed
    show mumn smirk_talk
    mum "You always know the right things to say."
    show povn smirk
    mum "But do you know the right things to do?"
    show povn smirk_talk
    show mumn smirk
    pov "Let's see if I do-"

    jump lbl_mom_mating_press
