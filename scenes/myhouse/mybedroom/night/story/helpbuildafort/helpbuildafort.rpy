## Help Build a Fort ##
label lbl_help_build_a_fort:

    scene black
    with fade
    sis "Hey, [povname]."
    pov "Mm..."
    sis "Wake up, [povname]."
    pov "Mhm..."
    sis "Wakey wakey."

    menu:
        "Wake up":
            scene bg helpbuildafort_1
            with dissolve
            $ renpy.pause(1,hard=True)
            show bg helpbuildafort_2
            with dissolve
            $ renpy.pause(1,hard=True)
            show bg helpbuildafort_3
            $ renpy.pause()
        "Ignore her":
            scene bg helpbuildafort_4
            with vpunch
            sis "I SAID WAKE UP!"
    show bg helpbuildafort_5
    sis "Oh, good, you're awake. Sorry, did I disturb you?"
    show bg helpbuildafort_6
    pov "W-"
    pov "What do you want?"

    menu:
        "What time is it?":
            pov "What time is it?"
            show bg helpbuildafort_7
            sis "No idea, c'mon. I need your help."
        "Just suck me off already.":
            show bg helpbuildafort_8
            pov "If you're going to suck me off, just do it already."
            show bg helpbuildafort_9
            sis "I'm gonna pretend that you're still half asleep and that you think I'm that girlfriend of yours."
    show bg helpbuildafort_7
    sis "Get up, we're sneaking into the basement."
    show bg helpbuildafort_6
    pov "Can't this wait till the morning?"
    show bg helpbuildafort_7
    sis "No. I'm bored and can't sleep. I'm too excited."
    show bg helpbuildafort_6
    pov "W-what is it that you want to do again?"
    show bg helpbuildafort_7
    sis "Help me build that fort."
    show bg helpbuildafort_8
    pov "Ugh..."
    show bg helpbuildafort_10
    sis "I'll give you a reward."
    show bg helpbuildafort_11
    pov "A reward?"
    show bg helpbuildafort_12
    sis "..."
    show bg helpbuildafort_13
    $ renpy.pause(0.6,hard=True)
    show bg helpbuildafort_14
    $ renpy.pause(0.1,hard=True)
    show bg helpbuildafort_15
    sis "Hey.. what the fuck. Why is your-"
    show bg helpbuildafort_16
    sis "[povname], did you seriously just get aroused from the word ‘reward'?"
    sis "I meant I was gonna buy you some food or something."
    show bg helpbuildafort_15
    sis "Jeez, dude."
    show bg helpbuildafort_16
    sis "You really just jabbed me in a place you really shouldn't be jabbing with a thing you shouldn't be jabbing me with."
    show bg helpbuildafort_17
    pov "S-sorry.. W-what?"
    show bg helpbuildafort_16
    sis "Fuckin' get up or I'll drop kick your dick like a bobblehead."
    show bg helpbuildafort_18
    pov "Fine. Fine. I'm up. Get off me, I need to put some clothes on."
    show bg helpbuildafort_19
    sis "You can come down to the basement naked if you want."
    sis "Your 'friend' may shribble from the cold though."
    if peekingsister_steam == 0:
        sis "Not like I haven't seen that before though."
    else:
        pass

    menu:
        "Get changed":
            show bg helpbuildafort_20
            pov "I'ma get changed."
            show bg helpbuildafort_21
            sis "Alright, I'll meet you downstairs in the basement."
            show bg helpbuildafort_20
            pov "Yeah, just gimme... like... 10 minut-"
            show bg helpbuildafort_16
            sis "Now."
            show bg helpbuildafort_17
            pov "Fine."
            show bg helpbuildafort_22
            with fade
            pov "{i}I'm totally whipped.{/i}"
            scene bg mybedroom_night
            with fade
        "Go down naked":
            scene bg mybedroom_night
            with fade
            show povne neutral at left
            with dissolve
            show sis smirk_talk at right
            with dissolve
            sis "No shame, huh?"
            show povne smirk_talk at left
            show sis neutral at right
            pov "You know me."
            show povne smirk at left
            show sis neutral_talk at right
            sis "Well, as much as I know how you love to flop your junk around like you own the place."
            show povne confused at left
            show sis bored_talk at right
            sis "It's fucking distracting and makes me a little uncomfortable with how comfortable you are."
            sis "Ironically."
            show povne embarrassed at left
            show sis angry_talk at right
            sis "Put some pants on and meet me downstairs, loser."
            scene bg mybedroom_night
    $ sister_path = 10
    $ gtime = 3
    $ renpy.pause()
    "After putting your clothes on."
    $ townmap_enabled = 0

    jump lbl_mybedroom_night_setup
