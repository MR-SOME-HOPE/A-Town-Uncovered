## Outside Effie's House ##
label lbl_outside_effies_house:
    stop music fadeout 5.0
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    eff "Ooh, so you did show up."
    show pov bored_talk at left
    show eff neutral at right
    pov "Well, I mean. You did ask me to come."
    show pov neutral at left
    show eff neutral_talk at right
    eff "I didn't really {i}ask{/i} you to come, per se. But I'm really happy you're here."
    show pov confused at left
    show eff neutral_talk at right
    eff "Oh hey, remember Jacob from Uni?"
    show pov confused_talk at left
    show eff neutral at right
    pov "The weird blonde kid with the sunglasses on his head?"
    show pov shocked at left
    show eff embarrassed_talk at right
    eff "Yeah, he lives right next door to me."
    show pov shocked_talk at left
    show eff smirk at right
    pov "Like right-right next door?"
    show pov confused at left
    show eff smirk_talk at right
    eff "As right next door as one possibly can live."
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "That's really why we're friends, childhood friends. If it wasn't for that, I don't think we'd ever have gotten along."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "The world works in mysterious ways."
    show pov shocked at left
    show eff smirk_talk at right
    eff "Anyway, wanna come inside?"
    show pov embarrassed_talk at left
    show eff confused at right
    pov "Is this going to take long?"
    show pov bored at left
    show eff smirk_talk at right
    eff "Why? Do you have somewhere to be?"
    show pov bored_talk at left
    show eff smirk at right
    if winc == 0:
        pov "My [mumrole] wants me to be home. She doesn't like it when I stay up past midnight."
        show pov bored at left
        show eff smirk_talk at right
        eff "That's so cute, you get more adorable by the second."
    else:
        pov "My mom wants me to be home. She doesn't like it when I stay up past midnight."
        show pov bored at left
        show eff smirk_talk at right
        eff "You're such a momma's boy, you get more adorable by the second."
    show pov sad_talk at left
    show eff smirk at right
    pov "Can we just..?"
    show pov sad at left
    show eff bored_talk at right
    eff "Alright, come on in. Just be like super quiet in case my dad's home. I'm serious. You do NOT want to meet my dad."
    show pov sad_talk at left
    show eff bored at right
    pov "Is he scary?"
    show pov sad at left
    show eff embarrassed_talk at right
    eff "Let's just say, he's protective."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Good enough reason to me."
    show pov neutral at left
    show eff neutral_talk at right
    eff "Now, shut the hell up and follow me. Capisce?"
    show pov smirk_talk at left
    show eff neutral at right
    pov "Oui oui."
    $ main_story = 12
    $ townmap_enabled = 0

    jump lbl_effiehousehallway_night_setup

###############
## Outside Effie's House Again ##
label lbl_outside_effies_house_again:
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    eff "Hey, [povname]. Ready to have some fun?"
    show pov smirk_talk at left
    show eff neutral at right
    pov "Ready doesn't even describe it."

    jump lbl_effieroom_night_setup
