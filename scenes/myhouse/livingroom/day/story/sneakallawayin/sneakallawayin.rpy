## Sneak Allaway In
label lbl_sneak_allaway_in:
    scene bg mylivingroom_day
    with fade
    show pov smirk at left
    with dissolve
    pov "{i}The coast is clear, I'll just wait for-{/i}"
    "{i}*Tap tap tap*{/i}"
    pov "{i}Speak of the devil.{/i}"
    show mis embarrassed at right
    with dissolve
    show pov smirk_talk at left
    pov "Hey, Miss Allaway."
    show pov smirk at left
    show mis embarrassed_talk at right
    mis "Hi.."
    show pov smirk at left
    show mis embarrassed_talk at right
    mis "Are- your parents home?"
    show pov confused_talk at left
    show mis shocked at right
    pov "My mum is at least, but the coast is clear up to my room."
    pov "I think..."
    show pov shocked at left
    show mis angry_talk at right
    mis "{i}*Whisper Shout*{/i} There are other people here?!"
    show pov smirk_talk at left
    show mis bored at right
    pov "Don't worry, let's just get to my room lickity split and get to some fun."
    show pov smirk at left
    show mis sad at right
    mis "..."

    scene bg sneakallawayin_1
    if skill_luc >= 12:
        pov ".."
        mis ".."
        pov "..."
        mis "..."
        pov "...."
        mis "................."
        show bg sneakallawayin_4
        pov "I think the coast is clear, let's hurry but keep a light foot."
        scene black
        with fade
        $ renpy.pause()
        "You have successfully snuck Miss Allaway into your bedroom."
        "A few hot minutes later..."

        $ skill_luc -= 8
        $ renpy.notify("You used 8 Luck Points")

        $ allawaybedroomsex_sneakherin = 0

        jump lbl_allaway_bedroom_sex

    else:
        pov ".."
        mis ".."
        pov "..."
        mis "..."
        "{i}*Fluuuuuushhhhhhh*{/i}"
        show bg sneakallawayin_2
        "{i}*Water tap turns on*{/i}"
        show bg sneakallawayin_3
        pov "Fuck- retreat! Retreat!"
        scene black
        with fade
        $ renpy.pause()
        "Miss Allaway ran out of the house in a panic."

        if skill_luc >= 4:
            $ skill_luc -= 4
        else:
            $ skill_luc = 0
            $ renpy.notify("You lost 4 Luck Points")

        $ allawaybedroomsex_sneakherin = 0

        scene bg mylivingroom_day
        with fade

        jump lbl_mylivingroom_day_setup
