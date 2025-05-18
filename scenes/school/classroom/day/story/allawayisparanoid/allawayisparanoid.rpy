## Allaway is Paranoid ##
label lbl_allaway_is_paranoid:

    scene bg classroom_day
    with fade
    show pov neutral_talk at left
    with dissolve
    show mis shocked at right
    with dissolve
    pov "Hey, Miss Allaway."
    pov "How's it going?"
    show pov neutral at left
    show mis shocked_talk at right
    mis "W-what do you mean?"
    show pov smirk_talk at left
    show mis shocked at right
    pov "I'm just asking if you're alright."
    show pov confused at left
    show mis embarrassed_talk at right
    mis "W-why wouldn't I be?"
    mis "I'm totally alright, why wouldn't I be alright."
    show mis sad_talk at right
    mis "Are you alright?!"
    show pov shocked at left
    show mis shocked_talk at right
    mis "Don't answer that."
    show mis shocked at right
    pov "..."
    show pov embarrassed_talk at left
    show mis angry at right
    pov "Really, are you okay? You seem a little antsy."
    show pov shocked at left
    show mis sad_talk at right
    mis "Look, [povname]. Nothing happened between us. Okay?"
    mis "It was just a tutoring session."
    show pov sad_talk at left
    show mis sad at right
    pov "I wasn't-"
    show pov shocked at left
    show mis bored_talk at right
    mis "I- I need to get some marking done, [povname]. If you'll excuse m-"
    show pov confused_talk at left
    show mis bored at right
    pov "Are you trying to avoid me? You can say so if you are."
    show mis sad at right
    pov "I won't take it personal."
    show pov sad_talk at left
    pov "Yes, I will. How can I not."
    show pov sad at left
    show mis sad_talk at right
    mis "Please, [povname]. Don't make a scene. I feel like someone's watching us very closely."
    show pov confused at left
    show mis sad at right
    pov "..."
    show pov sad_talk at left
    pov "I guess, I'll leave you to your marking."
    pov "...Bye."
    $ missallaway_path = 11

    jump lbl_classroom_day_setup
