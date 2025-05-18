label lbl_meet_luna:
    #GeeSeki Note: The creepy, horror-fanatic, taxidermy girl." Think of a female version of Norman Bates."
    #Anything involve stomach-flipping material, and blood, she’s there for sure." She makes Halloween look like Christmas."

    #-You walk up to hallway 2 when you suddenly feel a foreboding presence and you suddenly have the urge to get out of there as fast as possible-
    show pov shocked at left
    with dissolve
    show lun bored_talk at right
    hide btn_schoolhallway2_day_luna_idle2
    with dissolve
    lun "You are new!"
    show pov shocked_talk at left
    show lun bored at right
    pov "JESUS!"
    #-You are startled by the sudden appearance of a small girl next to you-
    show pov confused_talk at left
    show lun bored at right
    pov "God, you startled me!"
    pov "Where did you come from?!"
    show pov sad at left
    show lun angry_talk at right
    lun "I was already here - when you rudely cut me off where I was walking."
    show pov sad_talk at left
    show lun bored at right
    pov "O-Oh, did I?"
    pov "I am so sorry. I must still be adjusting to this new place, so I didn't notice you and-"
    show pov confused at left
    show lun bored_talk at right
    lun "That was actually a lie. I’ve been following you for a while, to be honest."
    show pov confused at left
    show lun bored at right
    pov "…"
    show pov confused_talk at left
    show lun neutral at right
    pov "I'm sorry, what..?"
    show pov confused at left
    show lun neutral_talk at right
    lun "Do you like stuffed animals?"
    show pov confused at left
    show lun neutral at right
    pov "W-Well, I suppose I do?"
    show pov confused at left
    show lun neutral_talk at right
    lun "I like the ones, hunters keep as trophies."
    show pov shocked at left
    show lun angry_talk at right
    lun "They are the real thing; not some pretend workshop garbage."
    show pov confused_talk at left
    show lun bored at right
    pov "I-Is that so?"
    show pov shocked at left
    show lun bored_talk at right
    lun "I think you would make a good stuffed figure."
    show pov confused at left
    show lun neutral_talk at right
    lun "You have a nice bone structure, fit of the finest of game."
    show pov confused_talk at left
    show lun bored at right
    pov "Thanks, I guess?"
    show pov confused at left
    show lun neutral_talk at right
    lun "Do you like scary movies?"
    show pov confused_talk at left
    show lun sad at right
    pov "Uh…"
    show pov confused at left
    show lun sad_talk at right
    lun "I am sorry - people often tell me I make them uncomfortable."
    lun "I am not really good with conversation."
    show pov embarrassed_talk at left
    show lun neutral at right
    pov "R-Really? Could have fooled me!"
    show pov embarrassed at left
    show lun neutral_talk at right
    lun "You are nice."
    lun "People usually run away by now."
    show pov shocked_talk at left
    show lun bored at right
    pov "I cannot seem to move my legs for some reason."
    pov "T-The conversation is too interesting!"
    pov "Hehe… He…"
    show pov neutral at left
    show lun bored_talk at right
    lun "My name is Luna."
    lun "My mom calls me ‘Moonbeam’, but I prefer Luna."
    show pov neutral_talk at left
    show lun angry at right
    pov "Moonbeam is nice."
    show pov embarrassed at left
    show lun angry_talk at right
    lun "I prefer Luna."
    show pov embarrassed_talk at left
    show lun bored at right
    pov "Noted."
    show pov neutral_talk at left
    show lun neutral at right
    pov "I am [povname]."
    pov "It’s nice to meet you."
    show pov neutral at left
    show lun bored_talk at right
    lun "I shall remember your name, [povname]."
    show pov embarrassed_talk at left
    show lun bored at right
    pov "Well, I still have to get a lot done today, so I guess I’ll see you later?"
    show pov sad at left
    show lun bored_talk at right
    lun "I’ll definitely see you, but you won’t see me."
    show pov shocked at left
    show lun neutral_talk at right
    lun "Not if I don’t want you to."
    #-She walks away creepily, leaving you alone in the hallway-
    hide lun
    show pov sad at left
    pov "…"
    show pov sad_talk at left
    pov "I am not sleeping tonight, am I?"
    $ luna_path = 1
    $ add_contact("Luna")
    pause 0.2
    jump lbl_schoolhallway2_day_setup
