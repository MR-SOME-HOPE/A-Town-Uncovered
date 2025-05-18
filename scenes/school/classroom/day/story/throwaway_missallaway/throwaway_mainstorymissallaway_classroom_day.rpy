## Miss Allaway Main Story Throwaway Conversations Classroom ##
label lbl_classroom_day_missallaway_sexworld_1:
    show pov embarrassed at left
    with dissolve
    show mis neutral_talk at right
    hide btn_classroom_day_missallaway_idle2
    with dissolve
    mis "Hey, [povname]. What can I do you for?"
    show pov embarrassed_talk at left
    show mis neutral at right
    pov "Nothing at the moment, I'm alright."
    show pov embarrassed at left
    show mis neutral_talk at right
    mis "Well, don't be a stranger. See me anytime you need to get off."
    show pov embarrassed at left
    pov "..."
    show pov embarrassed_talk at left
    show mis neutral at right
    pov "Thanks."
    show pov sad_talk at left
    show mis smirk at right
    pov "Wait- what?"
    show pov sad at left
    show mis embarrassed_talk at right
    mis "Well, actually.. do you mind if I just take my in-between class break?"
    mis "I had to deal with quite a few other students this morning."

    menu:
        "Go ahead.":
            show pov embarrassed_talk at left
            show mis neutral at right
            pov "No, go ahead. You deserve it."
            show pov embarrassed at left
            show mis neutral_talk at right
            mis "Thanks, [povname]. I promise that I'll get to you after class."
        "That's not fair.":
            show pov sad_talk at left
            show mis bored at right
            pov "Wait a second, that's not fair. I have the right to equal attention."
            show pov sad at left
            show mis bored_talk at right
            mis "[povname]. Please, I'm only human, not a robot. I promise that I'll get to you after class."

    jump lbl_classroom_day
