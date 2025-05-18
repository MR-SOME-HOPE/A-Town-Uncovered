## Twin Scolding ##
label lbl_twin_scolding:
    if winc == 0:
        jump lbl_twin_scolding_winc0

    scene bg mylivingroom_night
    with fade
    show sis sad flip at Position(xpos=600)
    with dissolve
    show pov neutral at left
    with dissolve
    show mumc angry at right
    with dissolve
    mum "..."
    show pov shocked at left
    show sis shocked flip at Position(xpos=600)
    show mumc angry_talk at right
    with hpunch
    mum "I- just- can't believe the two of you."
    show pov neutral at left
    show sis sad_talk flip at Position(xpos=600)
    show mumc angry at right
    sis "We said we're sorry..."
    show pov smirk at left
    show sis smirk_talk flip at Position(xpos=600)
    sis "I mean, really though. What's the big deal about drinking at our age when most other countries-"
    show pov shocked at left
    show sis angry flip at Position(xpos=600)
    show mumc angry_talk at right
    with hpunch
    mum "You're not in other countries, [sister]!"
    if siblingjailtime_hj == 1:
        show pov confused at left
        show sis confused flip at Position(xpos=600)
        mum "And not only that!"
        show pov neutral at left
        show sis sad flip at Position(xpos=600)
        mum "That- that- thing you did in the cell with your brother?!"
        mum "I shouldn't be the one to tell you that you are NOT supposed to be doing that to him."
        show pov smirk at left
        show sis bored flip at Position(xpos=600)
        mum "You two are related to each other for chrissakes, it's not natural."
        if momfallenasleep_lovewithsister == 1:
            show pov shocked at left
            show sis shocked flip at Position(xpos=600)
            show mumc sad_talk at right
            mum "A-are... are you two in an incestuous relationship with each other?!"
            scene bg mylivingroom_night
            with hpunch
            show mumc angry_talk at right
            mum "Tell me the truth! NOW!"

            menu:
                "We are...":
                    if sister_points <= 8:
                        $ sister_points += 2
                        $ renpy.notify("Your relationship with [sister] has increased by 2")
                    else:
                        $ sister_points = 10
                    if mum_points >= 2:
                        $ mum_points -= 2
                        $ renpy.notify("Your relationship with Mom has decreased by 2")
                    else:
                        $ mum_points = 0
                    $ renpy.pause(3,hard=True)
                    show pov smirk_talk at left
                    show mumc shocked at right
                    pov "W-we are..."
                "We are not.":
                    if mum_points <= 7:
                        $ mum_points += 3
                    else:
                        $ mum_points = 10
                    $ renpy.notify("Your relationship with Mom has increased by 3")
                    show pov smirk_talk at left
                    show sis embarrassed flip at Position(xpos=600)
                    show mumc angry at right
                    pov "W-we are not..."
                    pov "{i}*Burp*{/i}"
                    show pov bored_talk at left
                    show sis bored flip at Position(xpos=600)
                    show mumc bored at right
                    pov "...Related."
            show pov bored at left
            show sis embarrassed_talk flip at Position(xpos=600)
            show mumc angry at right
            sis "D-don't listen to him, Mom. He's still very much drunk up the head."
            show pov smirk at left
            show sis angry flip at Position(xpos=600)
            show mumc angry_talk at right
            mum "And so are you, missy."
    show pov neutral at left
    show sis sad flip at Position(xpos=600)
    show mumc sad_talk at right
    mum "I don't even know why I'm trying to argue with you in the state you two are in."
    show pov sad at left
    mum "{i}*Sigh*{/i}"
    mum "You two are supposed to look out for each other, not get each other into trouble!"
    show pov bored at left
    show sis shocked flip at Position(xpos=600)
    show mumc angry_talk at right
    mum "Both of you, get to your rooms. I'm going to talk to your dad about this."
    show sis shocked_talk flip at Position(xpos=600)
    show mumc angry at right
    sis "What?! N- no! Please don't bring Dad into this."
    show pov neutral_talk at left
    show sis sad flip at Position(xpos=600)
    pov "Y-yeaaah, Mommy. Pwetty pweaase."
    show pov sad_talk at left
    show mumc bored at right
    pov "Look how sad I am."
    show pov sad at left
    show mumc sad_talk at right
    mum "He's your father and he deserves the right to know how troublesome you both have been."
    mum "Times like this is when punishment is best left to him."
    show pov confused at left
    show sis sad_talk flip at Position(xpos=600)
    show mumc angry at right
    sis "I'm begging you, mo-"
    show pov embarrassed_talk at left
    show sis sad flip at Position(xpos=600)
    pov "She's begging!"
    show pov shocked at left
    show sis angry flip at Position(xpos=600)
    show mumc angry_talk at right
    with hpunch
    mum "That is enough! Get to your rooms!"
    hide sis angry
    with dissolve
    show mumc angry at right
    $ renpy.pause()

    scene black
    with fade
    $ renpy.pause()

    scene bg mybedroom_night
    with fade
    $ sister_path = 22
    $ townmap_enabled = 0

    jump lbl_mybedroom_night_setup

### NO WINC ###
label lbl_twin_scolding_winc0:

    scene bg mylivingroom_night
    with fade
    show sis sad flip at Position(xpos=600)
    with dissolve
    show pov neutral at left
    with dissolve
    show mumc angry at right
    with dissolve
    mum "..."
    show pov shocked at left
    show sis shocked flip at Position(xpos=600)
    show mumc angry_talk at right
    with hpunch
    mum "I- just- can't believe the two of you."
    show pov neutral at left
    show sis sad_talk flip at Position(xpos=600)
    show mumc angry at right
    sis "We said we're sorry..."
    show pov smirk at left
    show sis smirk_talk flip at Position(xpos=600)
    sis "I mean, really though. What's the big deal about drinking at our age when most other countries-"
    show pov shocked at left
    show sis angry flip at Position(xpos=600)
    show mumc angry_talk at right
    with hpunch
    mum "You're not in other countries, [sister]!"
    if siblingjailtime_hj == 1:
        show pov confused at left
        show sis confused flip at Position(xpos=600)
        mum "And not only that!"
        show pov neutral at left
        show sis sad flip at Position(xpos=600)
        mum "That- that- thing you did in the cell with your [povsisrole]?!"
        mum "I shouldn't be the one to tell you that you are NOT supposed to be doing that to him."
        show pov smirk at left
        show sis bored flip at Position(xpos=600)
        mum "You two are [povsisrole]s to each other for chrissakes, it's not natural."
        if momfallenasleep_lovewithsister == 1:
            show pov shocked at left
            show sis shocked flip at Position(xpos=600)
            show mumc sad_talk at right
            mum "A-are... are you two in a sexual relationship with each other?!"
            scene bg mylivingroom_night
            with hpunch
            show mumc angry_talk at right
            mum "Tell me the truth! NOW!"

            menu:
                "We are...":
                    if sister_points <= 8:
                        $ sister_points += 2
                        $ renpy.notify("Your relationship with [sister] has increased by 2")
                    else:
                        $ sister_points = 10
                    if mum_points >= 2:
                        $ mum_points -= 2
                        $ renpy.notify("Your relationship with [missus] has decreased by 2")
                    else:
                        $ mum_points = 0
                    $ renpy.pause(3,hard=True)
                    show pov smirk_talk at left
                    show mumc shocked at right
                    pov "W-we are..."
                "We are not.":
                    if mum_points <= 7:
                        $ mum_points += 3
                    else:
                        $ mum_points = 10
                    $ renpy.notify("Your relationship with [missus] has increased by 3")
                    show pov smirk_talk at left
                    show sis embarrassed flip at Position(xpos=600)
                    show mumc angry at right
                    pov "W-we are not..."
                    pov "{i}*Burp*{/i}"
                    show pov bored_talk at left
                    show sis bored flip at Position(xpos=600)
                    show mumc bored at right
                    pov "...Related."
            show pov bored at left
            show sis embarrassed_talk flip at Position(xpos=600)
            show mumc angry at right
            sis "D-don't listen to him, Mom. He's still very much drunk up the head."
            show pov smirk at left
            show sis angry flip at Position(xpos=600)
            show mumc angry_talk at right
            mum "And so are you, missy."
    show pov neutral at left
    show sis sad flip at Position(xpos=600)
    show mumc sad_talk at right
    mum "I don't even know why I'm trying to argue with you in the state you two are in."
    show pov sad at left
    mum "{i}*Sigh*{/i}"
    mum "You two are supposed to look out for each other, not get each other into trouble!"
    show pov bored at left
    show sis shocked flip at Position(xpos=600)
    show mumc angry_talk at right
    mum "Both of you, get to your rooms. I'm going to talk to your [dadrole] about this."
    show sis shocked_talk flip at Position(xpos=600)
    show mumc angry at right
    sis "What?! N- no! Please don't bring [dadrole] into this."
    show pov neutral_talk at left
    show sis sad flip at Position(xpos=600)
    pov "Y-yeaaah, [missus]. Pwetty pweaase."
    show pov sad_talk at left
    show mumc bored at right
    pov "Look how sad I am."
    show pov sad at left
    show mumc sad_talk at right
    mum "He's your [dadrole] and he deserves the right to know how troublesome you both have been."
    mum "Times like this is when punishment is best left to him."
    show pov confused at left
    show sis sad_talk flip at Position(xpos=600)
    show mumc angry at right
    sis "I'm begging you-"
    show pov embarrassed_talk at left
    show sis sad flip at Position(xpos=600)
    pov "She's begging!"
    show pov shocked at left
    show sis angry flip at Position(xpos=600)
    show mumc angry_talk at right
    with hpunch
    mum "That is enough! Get to your rooms!"
    hide sis angry
    with dissolve
    show mumc angry at right
    $ renpy.pause()

    scene black
    with fade
    $ renpy.pause()

    scene bg mybedroom_night
    with fade
    $ sister_path = 22
    $ townmap_enabled = 0

    jump lbl_mybedroom_night_setup
