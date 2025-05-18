## Effie Post Sex (with clothes) ##
label lbl_effie_post_sex_clothed:
    show pov sad_talk at left
    with dissolve
    show eff bored at right
    with dissolve
    pov "I guess I should head home now."
    show pov bored at left
    show eff neutral_talk at right
    eff "Yeah, I don't think so."
    show pov confused_talk at left
    show eff neutral at right
    pov "Wait, what? Why not?"
    show pov confused at left
    show eff smirk_talk at right
    eff "Believe me, I'm not trying to hold you captive or anything but my dad's home."
    show pov confused_talk at left
    show eff smirk at right
    pov "And? Isn't that a reason for me to skidaddle?"
    show pov confused at left
    show eff bored_talk at right
    eff "He doesn't know you're here. Trust me, you don't wanna risk getting caught by him."
    show pov confused_talk at left
    show eff bored at right
    pov "Is he THAT bad?"
    show pov confused at left
    show eff bored_talk at right
    eff "Well... only to guys."
    show pov sad at left
    eff "Any guys I bring home really. It doesn't matter if you're my boyfriend or a study buddy."
    eff "He'll literally beat the shit out of you if he catches you."
    show pov sad_talk at left
    show eff bored at right
    pov "Oh my God. Has that happened before?"
    show pov sad at left
    show eff bored_talk at right
    eff "Nine times out of ten he does. The last time I had a guy over, he gave him three black eyes."
    show pov confused_talk at left
    show eff bored at right
    pov "Three?"
    show pov sad at left
    show eff bored_talk at right
    eff "Yeah, one on each of his eyes plus another black eye on top of his first black eye."
    show eff angry_talk at right
    eff "I nearly threw up looking at it."
    show pov bored_talk at left
    show eff bored at right
    pov "... Is he still alive."
    show pov sad at left
    show eff neutral_talk at right
    eff "I think he escaped wishing he had died instead."
    eff "So yeah. I guess we'll be sleeping together tonight."
    show pov confused_talk at left
    show eff neutral at right
    pov "Can't I climb through the window?"
    show pov bored at left
    show eff neutral_talk at right
    eff "Yeah, about that. It won't budge. Guess you have no choice."

    scene black
    with fade
    $ main_story = 14
    $ gtime = 0
    if day <= 5:
        $ day += 1
    else:
        $ day = 0
    call lbl_next_date
    $ skill_int_times = 0
    $ skill_sta_times = 0
    $ skill_luc_times = 0
    $ hitomibeach_day = 0
    call lbl_skill_items

    jump lbl_effieroom_day_setup
