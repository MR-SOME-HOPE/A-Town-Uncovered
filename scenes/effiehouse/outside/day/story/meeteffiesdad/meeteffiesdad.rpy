## Meet Effie's Dad ##
label lbl_meet_effies_dad:
    default meeteffiesdad_dating = 0
    show pov neutral at left
    with dissolve
    show effdad bored_talk at right
    with dissolve
    effdad "Hello?"
    show pov neutral_talk at left
    show effdad bored at right
    if gtime == 0:
        pov "Good morning, sir."
    elif gtime == 1:
        pov "Good afternoon, sir."
    else:
        pov "Good evening, sir."
    pov "My name is [povname]. I'm a friend of Effie's and I-."
    show pov shocked at left
    show effdad confused_talk at right
    effdad "Are you two dating?"

    menu:
        "Yes.":
            show pov neutral_talk at left
            show effdad bored at right
            pov "Yes, we are."
            show pov embarrassed_talk at left
            show effdad bored_talk at right
            effdad "No, you're not."
            show pov embarrassed_talk at left
            show effdad bored at right
            pov "We.. are-?"
            show pov embarrassed at left
            show effdad bored_talk at right
            effdad "No. You are not."
            $ meeteffiesdad_dating = 1
        "No.":
            show pov neutral_talk at left
            show effdad bored at right
            pov "No, just friends."
            show pov confused at left
            show effdad bored_talk at right
            effdad "Pssh, yeah, that's what they all say."
            effdad "I was your age once, you can't fool me."
        "It's complicated.":
            show pov embarrassed_talk at left
            show effdad bored at right
            pov "Well, it's sort of a gray area between us-"
            show pov shocked at left
            show effdad bored_talk at right
            effdad "Look- Stop. Just- Shut up for a second."
            show pov embarrassed at left
            effdad "Whatever you have going on with my daughter, forget it."
            effdad " That's an order."
            $ meeteffiesdad_dating = 2
    show pov embarrassed_talk at left
    show effdad bored at right
    pov "Um..."
    show pov shocked at left
    show effdad angry_talk at right
    effdad "I told her a million times that she's too young to deal with boys like you."
    show pov confused_talk at left
    show effdad angry at right
    pov "Like me?"
    show pov confused at left
    show effdad bored_talk at right
    effdad "Look, kid. Don't get this the wrong way but Effie has a bright future ahead of herself."
    effdad "One that she is building up for herself."
    show pov bored at left
    show effdad bored_talk at right
    effdad "I don't want you boys fucking that up for her."
    show effdad bored at right
    pov "..."
    show pov shocked at left
    show effdad bored_talk at right
    effdad "Now I suggest you stop seeing my daughter."
    show pov confused_talk at left
    show effdad bored at right
    pov "With all due respects, sir-"
    show pov embarrassed_talk at left
    pov "We are at the very least friends and I can't just not cut contacts with her."
    pov "She's a great person to hang out with-"
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "As I said, I don't want you distracting her."
    show pov shocked at left
    effdad "No offence but she's too good for you and you know it."
    show pov angry at left
    effdad "Go chase someone in your own league."
    show effdad confused_talk at right
    effdad "It was good meeting you..."
    show pov angry_talk at left
    show effdad bored at right
    pov "[povname]."
    show pov angry at left
    show effdad bored_talk at right
    effdad "[povname]. But I hope that I don't see you around here again."
    effdad "This is my courtesy warning."
    effdad "Stay away from my daughter."
    hide effdad bored_talk
    show pov bored at left
    pov "{i}Jeez. Effie wasn't kidding about her dad not liking guys around.{/i}"
    show pov confused at left
    pov "{i}At least he didn't beat me up on the spot.{/i}"
    $ effiesdad_path = 1
    $ renpy.notify("New Contact: Effie's Dad")
    if gtime <= 1:
        jump lbl_effiehouseoutside_day_setup
    else:
        jump lbl_effiehouseoutside_night_setup
