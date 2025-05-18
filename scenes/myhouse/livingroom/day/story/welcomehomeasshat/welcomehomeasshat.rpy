## Welcome Home Asshat ##
label lbl_welcome_home_asshat:
    $ townmap_enabled = 1

    scene bg welcomehomeasshat_1
    with fade
    $ renpy.pause()
    show bg welcomehomeasshat_2
    pov "Huh..."
    pov "I wonder who could've put that up."
    pov "..."
    if winc == 0:
        pov "{i}Seriously, was it [sister] or [dadname]?{/i}"
    else:
        pov "{i}Seriously, was it [sister] or Dad?{/i}"
    show bg welcomehomeasshat_3
    with vpunch
    pov "Ooww!!" with dissolve
    scene bg mylivingroom_day
    show pov confused_talk at left
    with fade
    show sis angry at right with dissolve
    pov "What did you punch me in the arm for?!"
    if sister_points <= 5 or sister_path <= 25:
        show pov confused at left
        show sis angry_talk at right
        sis "That's for making me look around all around town for your stupid face!"
        show pov embarrassed_talk at left
        show sis angry at right
        if winc == 0:
            pov "N-Nice to see you too, [sister]."
        else:
            pov "N-Nice to see you too, sis."
        show pov embarrassed at left
        show sis smirk_talk at right
        sis "Yeah, likewise."
        show pov shocked at left
        sis "So, is this a new thing for you? Dancing around naked in the middle of the night and passing out in the park?"
        show pov bored at left
        sis "If you're a closet exhibitionist, you can tell me."
        show pov angry_talk at left
        show sis smirk at right
        pov "I-I wasn't dancing around naked!"
        show pov sad at left
        show sis smirk_talk at right
        sis "Right, sure. Okay, [povname]. Uh-huh. I believe you."
        show pov bored_talk at left
        show sis embarrassed at right
        pov "Oh, fuck off, [sister]. I've had a very uncomfortable 24 hours in a cell."
        show sis confused at right
        pov "I don't need this from you right now."
        show pov bored at left
        show sis confused_talk at right
        sis "Just don't scare us like that again."
        "{i}*Whaap*{/i}"
        with hpunch
        show pov shocked_talk at left
        show sis neutral at right
        pov "Owww! You just punched me in the same frikkin spot!"
        show pov angry at left
        show sis neutral_talk at right
        sis "I know."
        show sis neutral at right
        pov "..."
        show pov sad_talk at left
        pov "I can see why I deserve it."
        show pov sad_talk at left
        show sis embarrassed at right
        pov "I'm sorry for making you worry, [sister]."
        show pov embarrassed at left
        show sis sad_talk at right
        if winc == 0:
            sis "Just don't do it again, okay? I may give you a ton of shit but you're still my [povsisrole]."
            show sis embarrassed_talk at right
            sis "My baby [povsisrole]."
            show sis smirk_talk at right
            sis "My wittle-bittle bab-by [povsisrole]"
        else:
            sis "Just don't do it again, okay? I may give you a ton of shit but you're still my brother."
            show sis embarrassed_talk at right
            sis "My baby brother."
            show sis smirk_talk at right
            sis "My wittle-bittle bab-by bro-bro-"
        show pov embarrassed_talk at left
        show sis smirk at right
        pov "Yeah, yeah. You can stop with the irritating sounds coming from that hole in your face."
        show pov embarrassed at left
        show sis smirk_talk at right
        sis "Hehehe. I love you too, [povname]."
        $ main_story = 41

        jump lbl_mylivingroom_day_setup
    else:
        show pov shocked at left
        show sis bored_talk at right
        sis "It's quite more than what your stupid face deserves..."
        show pov embarrassed_talk at left
        show sis bored at right
        pov "Oh hey, [sister]."
        show sis shocked at right
        pov "What's up?"
        show pov embarrassed at left
        show sis confused_talk at right
        sis "What's up..?"
        show sis angry_talk at right
        sis "What is up?"
        "{i}*Whaap*{/i}"
        with hpunch
        show pov angry_talk at left
        show sis angry at right
        pov "Owww! You just punched me in the same frikkin spot!"
        show pov shocked at left
        show sis angry_talk at right
        sis "What's up with ME?! What's up with YOU?!"
        show sis sad_talk at right
        sis "You fucking asshole!"
        hide sis sad_talk
        "[sister] leaves for the basement."
        show pov sad at left
        pov "{i}She's definitely upset with me. I should make things right with her.{/i}"
        pov "{i}She's down in the basement.{/i}"
        $ main_story = 40.5

        jump lbl_welcome_home_asshat_part2
