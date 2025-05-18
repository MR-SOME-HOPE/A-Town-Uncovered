## Lashley Cafeteria Doggy Pre
label lbl_lashley_cafeteria_doggy_pre:
    show pov neutral_talk at left
    with dissolve
    show pri neutral at right
    with dissolve
    pov "Hello, Director Lashley."
    show pov neutral at left
    show pri neutral_talk at right
    pri "[povname]. What can I do for you today?"
    show pov embarrassed_talk at left
    show pri confused at right
    pov "I was hoping we could try that new prayer technique later."
    show pov neutral at left
    show pri confused_talk at right
    pri "The one about vulnerability and being open to the Earth?"
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "Exactly, I feel that part of me needs to be more... attuned."
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "I understand complete, [povname]."
    show pri neutral_talk at right
    pri "We are only children of God and everyday is a learning experience."
    pri "After university, right after everyone leaves the premises-"
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "So we can have our privacy, of course."
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "I'll see you in the cafeteria, [povname]."
    show pri neutral_talk at right
    pri "Remember, the first step to vulnerability and openness is-"
    show pov smirk_talk at left
    show pri shocked at right
    pov "A big window, and the sun on your skin."
    show pov neutral at left
    show pri neutral_talk at right
    pri "God bless your sweet heart. I'll see you later."

    $ gtime = 1

    scene black
    with fade
    $ renpy.pause()
    "After university, at the cafeteria..."
    $ renpy.pause()

    jump lbl_lashley_cafeteria_doggy
