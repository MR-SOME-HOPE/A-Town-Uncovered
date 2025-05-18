## Allaway Drive You Home ##
label lbl_allaway_drive_you_home:

    scene bg allawaydriveyouhome_1
    with fade
    if missallawayscolding_newcar == 0:
        show pov neutral_talk at left
        with dissolve
        show miso neutral at right
        with dissolve
        pov "Hey, you decided to keep your dad's car?"
        show pov neutral at left
        show miso embarrassed_talk at right
        mis "Yeah, it's hard for me to part ways with me, plus I took your suggestion at heart."
        mis "Remember? When you told me to keep it."
        show pov neutral_talk at left
        show miso embarrassed at right
        pov "Nothing wrong with keeping something sentimental."
        show pov neutral at left
        show miso confused_talk at right
        pov "Everyone's always looking for new, best thing."
        show miso bored_talk at right
        mis "And the best is either too expensive or too stupid-looking."
        show pov smirk_talk at left
        show miso smirk at right
        pov "Took the words out of my mouth."
        show pov smirk at left
        show miso embarrassed_talk at right
        mis "Besides, the new car smell gives me a headache."
        show miso bored_talk at right
        mis "Reminds me of a hospital in a plane."
        show pov neutral at left
        show miso confused_talk at right
        mis "Too... factory."
    else:
        show pov confused_talk at left
        with dissolve
        show miso confused at right
        with dissolve
        pov "You decided to keep this rust bucket?"
        show pov confused at left
        mis "..."
        show pov embarrassed_talk at left
        show miso bored at right
        pov "Or is THIS the new car?"
        show pov embarrassed at left
        show miso bored_talk at right
        mis "Nope, this is the same one that's been breaking down on me occasionally."
        show pov embarrassed_talk at left
        show miso bored at right
        pov "Why didn't you just get a new car if it keeps breaking down?"
        show pov shocked at left
        show miso angry_talk at right
        mis "Because it means something to me, [povname]."
        show pov embarrassed at left
        show miso sad_talk at right
        mis "I told you it was my dad's car. I just- can't let go of it."
        show miso embarrassed_talk at right
        mis "Not yet anyways. It's still fighting."
    show pov neutral at left
    show miso embarrassed_talk at right
    mis "Anyway, you'll have to direct me to your house."
    show pov neutral_talk at left
    show miso neutral at right
    pov "Of course."
    show pov embarrassed_talk at left
    show miso embarrassed at right
    pov "And Miss, as long as you're happy with the truck, it doesn't matter what I say."
    show pov embarrassed at left
    show miso embarrassed_talk at right
    mis "Thanks."

    scene black
    with fade
    $ renpy.pause()
    "After a few minutes drive..."

    jump lbl_parking_with_allaway
