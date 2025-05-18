## I Become the Warrior ##
label lbl_i_become_the_warrior:

    scene bg schoolgymdoor_night
    with fade
    if ibecomethewarrior_beatbrock == 2:
        show pov smirk at left
        with dissolve
        show mis smirk_talk at right
        with dissolve
        mis "Hey, tough stuff."
        show pov smirk_talk at left
        show mis smirk at right
        pov "Hey, Miss-"
        scene bg ibecomethewarrior_1
        with hpunch
        $ renpy.pause()
        show bg ibecomethewarrior_2
        $ renpy.pause(0.6,hard=True)
        show bg ibecomethewarrior_1
        $ renpy.pause(0.4,hard=True)
        show bg ibecomethewarrior_2
        $ renpy.pause(0.6,hard=True)
        show bg ibecomethewarrior_1
        $ renpy.pause(0.4,hard=True)
        show bg ibecomethewarrior_2
        $ renpy.pause(0.6,hard=True)
        show bg ibecomethewarrior_3
        mis "I hope no one saw that."
        show bg ibecomethewarrior_4
        pov "No, neither do I."
        show bg ibecomethewarrior_5
        mis "..."
        show bg ibecomethewarrior_2
        $ renpy.pause(0.6,hard=True)
        show bg ibecomethewarrior_1
        $ renpy.pause(0.4,hard=True)
        show bg ibecomethewarrior_2
        $ renpy.pause(0.6,hard=True)
        show bg ibecomethewarrior_1
        $ renpy.pause(0.4,hard=True)
        show bg ibecomethewarrior_2
        $ renpy.pause(0.6,hard=True)
        scene bg schoolyard_night
        with fade
        $ missallaway_path = 13
    elif ibecomethewarrior_beatbrock == 1:
        show pov neutral at left
        with dissolve
        show mis smirk_talk at right
        with dissolve
        mis "Hey, [povname]."
        show pov embarrassed at left
        mis "What happened in there? I thought you were going to beat Brock."
        show pov embarrassed_talk at left
        show mis smirk at right
        pov "You saw the whole thing?"
        show pov embarrassed at left
        show mis confused_talk at right
        mis "I wish I didn't."
        show pov bored at left
        show mis smirk at right
        pov "..."
        show pov bored_talk at left
        pov "Don't worry about me, my jaw is still intact."
        show pov embarrassed_talk at left
        pov "I'll get him next time."
        show pov embarrassed at left
        show mis smirk_talk at right
        mis "I'll be here watching."
        $ missallaway_path = 12
    else:
        show pov confused at left
        with dissolve
        show mis smirk_talk at right
        with dissolve
        mis "Hey, [povname]. Did you forget about our little bet?"
        show pov confused_talk at left
        show mis confused at right
        pov "Nope, I just-"
        show pov confused at left
        show mis confused_talk at right
        mis "I best be off. Only wanted to see the fight between you and Brocky-boo."
        show pov bored_talk at left
        show mis smirk at right
        pov "Why don't you ask him out if you're so in love with him?"
        show pov shocked at left
        show mis smirk_talk at right
        mis "I did."
        show pov embarrassed at left
        show mis bored_talk at right
        mis "He said I wasn't his type."
        show mis sad_talk at right
        mis "His rejection made me sooo..."
        show pov shocked at left
        show mis embarrassed_talk at right
        mis "Fucking horny!"
        show pov embarrassed at left
        show mis shocked_talk at right
        mis "Oops. Was that too loud? I'll be going."
        $ missallaway_path = 12
    $ townmap_enabled = 1

    jump lbl_schoolyard_night_setup
