## Meet Jacob's Dad ##
label lbl_meet_jacobs_dad:
    show pov neutral at left
    with dissolve
    show jacdad neutral_talk at right
    with dissolve
    jacdad "Hello, there. What can I do you for?"
    show pov neutral_talk at left
    show jacdad neutral at right
    if gtime == 0:
        pov "Good morning, sir."
    elif gtime == 1:
        pov "Good afternoon, sir."
    else:
        pov "Good evening, sir."
    pov "My name is [povname]."
    show jacdad smirk at right
    pov "I'm a friend of Jacob's and I'm just wondering if he's home at the moment."
    show pov neutral at left
    show jacdad smirk_talk at right
    jacdad "Oh, so you're the [povname] that he mentioned before."
    show jacdad neutral_talk at right
    jacdad "It's great to meet you, young lad."
    show pov embarrassed at left
    jacdad "He's actually said a lot of good things about you."
    show pov confused at left
    show jacdad confused_talk at right
    jacdad "You're not one of those medieval play-pretend friends, are you?"
    show pov embarrassed_talk at left
    show jacdad neutral at right
    pov "Uh- no. Not that kind of friend. I moved into town recently."
    show pov neutral at left
    show jacdad neutral_talk at right
    jacdad "Oh! Well then, welcome!"
    show pov embarrassed at left
    show jacdad smirk_talk at right
    jacdad "It's great to see Jacob make a new-{i}new{/i} friend."
    jacdad "Hehehe~"
    show pov confused at left
    show jacdad confused_talk at right
    jacdad "Anyways, I'm afraid Jacob's not in at the moment."
    if gtime == 0:
        if day <= 4:
            show pov neutral at left
            jacdad "He's already taken off for university."
        else:
            jacdad "He's out - and before you ask, he didn't say where."
            show pov neutral at left
            show jacdad smirk_talk at right
            jacdad "Your guess is as good as mine."
    elif gtime == 1:
        show pov neutral at left
        show jacdad neutral_talk at right
        jacdad "You may be able to find him at the comic book store near the beach."
        show pov embarrassed at left
        show jacdad smirk_talk at right
        jacdad "He likes hanging out there with his play buddies."
    else:
        show pov confused at left
        jacdad "I think he's out at another friend's house."
    show pov neutral_talk at left
    show jacdad neutral at right
    pov "Oh, okay. Thanks. I'll probably just catch up with him another time."
    show pov neutral at left
    show jacdad neutral_talk at right
    jacdad "Alrighty-roo!"
    jacdad "It was nice meeting you, [povname]."
    show pov neutral_talk at left
    show jacdad neutral at right
    pov "It's good meeting you too, sir."
    show pov neutral at left
    show jacdad smirk_talk at right
    jacdad "Have a good day now."
    show pov neutral_talk at left
    if gtime >= 2:
        show pov embarrassed at left
        jacdad "Well, I guess I should say, good night."
        jacdad "Hehehe~"
        show pov embarrassed_talk at left
    show jacdad smirk at right
    pov "You too, sir."
    hide jacdad smirk
    pov "{i}He seems alright - a little corny around the edges.{/i}"
    if effiesdad_path >= 1:
        show pov neutral at left
        show jacdad smirk_talk at right
        pov "{i}At least he's not like Effie's dad.{/i}"
    $ jacobsdad_path = 1
    $ add_contact("Jacob's Dad")
    if gtime <= 1:
        jump lbl_jacobhouseoutside_day_setup
    else:
        jump lbl_jacobhouseoutside_night_setup
