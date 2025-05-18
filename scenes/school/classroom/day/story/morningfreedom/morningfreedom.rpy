## Morning Freedom ##
label lbl_morning_freedom:

    scene black
    with fade
    "The next morning."

    scene bg classroom_dayempty
    show mis shocked_talk at right
    with hpunch
    mis "Wake up!"
    show mis neutral_talk at right
    show pov shocked at left
    with dissolve
    mis "The doors are unlocked!"
    show pov bored at left
    mis "We can go now."
    show pov bored_talk at left
    show mis neutral at right
    pov "Wh- what time is it?"
    show pov bored at left
    show mis neutral_talk at right
    mis "It's early morning, the university is pretty empty at the moment."
    mis "Let's leave before someone sees us."
    show pov bored_talk at left
    show mis neutral at right
    pov "Hmm- Mm.. right..."
    show mis bored at right
    pov "Leave..."
    show pov bored at left
    mis "..."
    show mis bored_talk at right
    mis "I don't have time to wait for you. I'm heading home to take a well-deserved shower."
    show mis smirk_talk at right
    mis "And have some pre-coffee before I get more coffee in the staff room."
    show mis confused at right
    pov "Mhmm..."
    show mis smirk_talk at right
    mis "Wake up, [povname]. You sleepy head."
    show mis confused_talk at right
    mis "I expect to see you in class later."
    show mis confused at right
    pov "..."

    scene bg schoolyard_dayweekend
    with fade
    show pov neutral_talk at left
    with dissolve
    show mis neutral at right
    with dissolve
    pov "See ya later, Miss."
    show mis shocked at right
    pov "Last night was... fun!"
    show pov neutral at left
    show mis angry_talk at right
    mis "Shut your mouth, [povname]. Do you want the whole world to hear."
    show pov neutral_talk at left
    show mis bored at right
    pov "I... forgot. Hush hush."
    $ missallaway_path = 9
    $ gtime = 0
    if day <= 5:
        $ day += 1
    call lbl_misc_restart
    call lbl_next_date
    call lbl_skill_items
    $ townmap_enabled = 0
    scene black with fade
    jump lbl_myhousefront_day_setup
