## Alanna Side Story Throwaway Conversations Mall ##
default mall_spareboxes = 0

## Spare Boxes
label lbl_mall_day_alanna_spareboxes:
    show pov embarrassed_talk at left
    with dissolve
    show ala bored at right
    with dissolve
    pov "Hey, Alanna. How's business?"
    show pov embarrassed at left
    show ala bored_talk at right
    ala "Slow day today. Wanna take over the counter?"
    show pov embarrassed_talk at left
    show ala confused at right
    pov "Not at the moment, I'm wondering if I can steal some boxes in the back."
    show pov embarrassed at left
    show ala confused_talk at right
    ala "Boxes? What boxes?"
    show pov embarrassed_talk at left
    show ala confused at right
    pov "Y'know, the ones made of cardboard."
    show pov shocked at left
    show ala confused_talk at right
    ala "Oh, those soggy, damp, smelly ones?"
    show ala confused at right
    ala "..."
    show pov embarrassed at left
    show ala confused_talk at right
    ala "Why do you want those?"
    show pov embarrassed_talk at left
    show ala bored at right
    pov "Well, I actually just changed my mind just now."
    show pov bored_talk at left
    pov "I don't remember them being as you described."
    show pov embarrassed at left
    show ala bored_talk at right
    ala "What do you expect when you work with icecream."
    show pov embarrassed_talk at left
    show ala bored at right
    pov "Right, silly me. I guess I'll catch you later."
    show pov bored at left
    show ala bored_talk at right
    ala "Whatever."

    $ mall_spareboxes = 1

    jump lbl_mall_day_setup
