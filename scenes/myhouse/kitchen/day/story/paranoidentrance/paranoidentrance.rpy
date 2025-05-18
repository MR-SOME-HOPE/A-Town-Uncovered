## Paranoid Entrance:
label lbl_paranoid_entrance:
    default paranoidentrance_sisknowstalker = 0

    scene bg mylivingroom_day
    with fade

    if skill_sta <= 8:
        show bg mylivingroom_day
        with hpunch

        if skill_sta >= 4:
            $ skill_sta -= 4
        else:
            $ skill_sta = 0
        $ renpy.notify("You Lost 4 Stamina Points from a Panicky Stumble")

        pov "Ow, fuck-"
        pov "Holy fuck, holy fuck, holy fuck, holy fuck, holy fuck!!"
        pov "I-It wasn’t a dream!"
        pov "I am being fucking hunted!"
        pov "B-By a fucking ghost chick thing from another dimension!"
        show sis shocked_talk at right
        with dissolve
        sis "What's going on?! It sounded like something fell over."
        show sis bored_talk at right
        sis "Oh- it's just you."
        show pov angry_talk at left
        with dissolve
        show sis confused at right
        pov "Don't give me that look! There was a thing on the floor... and I tripped."

        scene bg mykitchen_day
        with fade

        show pov sad at left
        with dissolve
        show sis confused_talk at right
        sis "What is up with you? Why are you being a weirdo?"

    else:
        show pov shocked_talk at left
        with dissolve
        pov "Holy fuck, holy fuck, holy fuck, holy fuck, holy fuck!!"
        pov "I-It wasn’t a dream!"
        pov "I am being fucking hunted!"
        pov "B-By a fucking ghost chick thing from another dimension!"

        scene bg mykitchen_day
        with fade

        show pov sad at left
        with dissolve
        show sis confused_talk at right
        sis "Hey, are you okay-"
        show pov shocked_talk at left
        show sis shocked at right
        pov "Ahhh!"
        show pov shocked at left
        show sis shocked_talk at right
        sis "Ahhh!"
        show pov shocked at left
        show sis angry_talk at right
        sis "Holy shit, the hell’s wrong with you?!"

    menu:
        "Nothing!":
            if skill_cha >= 2:
                $ skill_cha -= 2
                $ renpy.notify("You Used 2 Charisma Points")

                show pov embarrassed_talk at left
                show sis confused at right
                pov "Nothing!"
                pov "Nothing, [sister]. Absolutely nothing's wrong…"

            else:
                if sister_points >= 1:
                    $ sister_points -= 1
                else:
                    $ sister_points = 0
                $ renpy.notify("Relationship with [sister] Decreased")

                show pov sad_talk at left
                show sis confused at right
                pov "Nothing!"
                show pov angry_talk at left
                pov "Nothing, [sister]. Absolutely nothing's wrong…"
            show pov sad at left
            show sis confused_talk at right
            sis "Dude, you are shaking."
            sis "You are not okay."
            sis "What happened?"
            show pov shocked_talk at left
            show sis bored at right
            pov "N-Nothing!"
            show pov embarrassed_talk at left
            pov "J-Just, you know-"
            show pov embarrassed at left
            show sis bored_talk at right
            sis "[povname], do you need to sit down?"
            show pov embarrassed_talk at left
            show sis confused at right
            pov "No, no!"
            show sis confused at right
            pov "I just- I just need to lock myself in my room for a few hours if you don’t mind."
            show pov embarrassed at left
            show sis sad_talk at right
            sis "[povname], you are scaring me."
            show pov sad at left
            show sis angry_talk at right
            sis "Seriously, what’s wrong with you?"

        "I'm being followed.":
            if skill_cha >= 8:
                $ paranoidentrance_sisknowstalker = 2

                $ skill_cha -= 4
                $ renpy.notify("You Used 4 Charisma Points")

                show pov sad_talk at left
                show sis shocked at right
                pov "Someone’s following me."
                show pov sad at left
                show sis confused_talk at right
                sis "Really?"
                show sis confused at right
                sis "…"
                show pov shocked at left
                show sis smirk_talk at right
                sis "You’re pulling my leg."
                show pov angry_talk at left
                show sis smirk at right
                pov "Why would I joke about that?!"
                show pov sad_talk at left
                pov "How much more possible is it that I’m being followed after my nudes are leaked?"
                show pov sad at left
                show sis confused_talk at right
                sis "I mean, out of all people?"
                show pov bored at left
                show sis smirk_talk at right
                sis "You..?"

                if sister_points >= 4:
                    show pov embarrassed at left
                    show sis smirk_talk at right
                    sis "I’ve seen your dick and just because it’s that big, doesn’t really make you ‘stalk’ worthy."
                    show pov sad_talk at left
                    show sis smirk at right
                    pov "Well, fuck you. I am too ‘stalk’ worthy, and I fucking hate it."
                else:
                    show sis smirk_talk at right
                    sis "I can’t see why anyone would care enough to follow you home."

            else:
                show pov sad_talk at left
                show sis shocked at right
                pov "Someone’s following me."
                show pov sad at left
                show sis confused_talk at right
                sis "Really?"
                show sis confused at right
                sis "…"
                show pov embarrassed at left
                show sis sad_talk at right
                sis "Man, this is serious..."
                show pov sad at left
                show sis confused_talk at right
                sis "Should we notify.. someone?"
                show pov sad at left
                show sis sad_talk at right
                sis "Like- I'm not one to be a tattle-tale but this isn't a laughing matter."
                show pov sad_talk at left
                show sis sad at right
                pov "Yeah, no kidding."
                show sis confused at right
                pov "Though I don't think reporting the stalker would help."
                show pov sad at left
                show sis confused_talk at right
                sis "Why not? Do you recognize who it is?"

                menu:
                    "Yeah.":
                        $ paranoidentrance_sisknowstalker = 1

                        show pov sad_talk at left
                        show sis confused at right
                        pov "Yeah... but the thing is-"
                        pov "It's complicated."
                        show pov embarrassed_talk at left
                        show sis sad at right
                        pov "Don't worry about it, [sister]."
                        show sis embarrassed at right
                        pov "Thanks for having my back."

                        if sister_points <= 1:
                            $ sister_points += 1
                        else:
                            $ sister_points = 0
                        $ renpy.notify("Relationship with [sister] Increased")

                        show pov embarrassed at left
                        show sis embarrassed_talk at right
                        sis "You're still a loser but I care about you, [povname]."
                        sis "Because I know you'll have my back when I need you."

                    "No.":
                        show pov sad_talk at left
                        show sis sad at right
                        pov "No..."
                        show sis confused at right
                        pov "Not exactly."
                        pov "I- It's complicated."
                        show sis sad at right
                        pov "I think I gotta sort this out on my own."
                        show pov embarrassed_talk at left
                        pov "Thanks for the suggestion though."
                        show pov embarrassed at left
                        show sis sad_talk at right
                        sis "You sure about this?"
                        show pov embarrassed_talk at left
                        show sis sad at right
                        pov "Yeah, it'll be okay. I hope."

        "What do you think?":
            if sister_points >= 1:
                $ sister_points -= 1
            else:
                $ sister_points = 0
            $ renpy.notify("Relationship with [sister] Decreased")

            show pov angry_talk at left
            show sis shocked at right
            pov "What do you think?"
            show pov bored at left
            show sis confused_talk at right
            sis "Jeez, man. Take a pill-chill, Chill-Bill."
            show sis smirk_talk at right
            sis "Don’t tell me your nudes have been leaked online!"
            show pov bored_talk at left
            show sis smirk at right
            pov "I know you’re joking, but in the off chance that you’re not..."
            pov "No."
            show pov bored at left
            show sis bored_talk at right
            sis "Then my guess is as good as yours."
            show pov angry_talk at left
            show sis bored at right
            pov "Erm, no. Your guess is {i}not{/i} as good as mine because I know what’s wrong and you don’t!"
            show pov angry at left
            show sis confused_talk at right
            sis "Someone rolled out the wrong side of the lake."
            show sis smirk at right
            sis "…"
            show sis smirk_talk at right
            sis "Get it?"
            sis "Because you were nude at the-"
            show pov bored_talk at left
            show sis neutral at right
            pov "[sister]. Do me a favour and shove a dick."
            show pov angry at left
            show sis neutral_talk at right
            sis "I have no idea what the fuck you mean by that, but I wish."

    if sister_path >= 11:
        show pov confused at left
        show sis confused_talk at right
        sis "You want to go to the twin fort?"
        show pov embarrassed at left
        show sis embarrassed_talk at right
        if sister_points >= 7:
            sis "W-We could slowly grind and talk if that’s what you need."
        elif sister_points >= 4:
            sis "W-We could cuddle and talk if that’s what you need."
        else:
            sis "W-We could just talk if that’s what you need."
        show sis smirk_talk at right
        sis "Maybe it will help you calm down?"
        show pov embarrassed_talk at left
        show sis neutral at right
        pov "I-I…"
        show pov embarrassed at left
        show sis neutral_talk at right
        if sister_points >= 7:
            sis "I can bring down some snacks, and my laptop - watch a Webflick and chill?"
        else:
            sis "I can bring down some snacks, and my laptop - watch a movie together?"
        show pov embarrassed_talk at left
        show sis confused at right
        pov "T-that sounds really nice and all, [sister], but I really just need to casually lock myself in my room for a while."
        show pov embarrassed at left
        show sis confused_talk at right
        sis "I- can’t tell if you’re joking. You're not one to refuse an offer like this."
        show sis embarrassed_talk at right
        sis "Come on, it’ll be fun!"
        sis "Seems like you need it too."
        show pov sad_talk at left
        show sis embarrassed at right
        pov "I…"
        show pov embarrassed_talk at left
        show sis sad at right
        pov "Raincheck? Alright?"
        show pov sad_talk at left
        pov "I really just need to... be alone for a while."
        show pov embarrassed at left
        show sis sad_talk at right
        sis "[povname]...?"

    show pov embarrassed_talk at left
    show sis sad at right
    pov "R-Really, I am fine!"
    pov "Tip top shape!"
    pov "No problems here!"
    show pov embarrassed at left
    show sis bored_talk at right
    sis "Dude, you are rambling and stuttering like a mofo."
    if winc == 0:
        show pov shocked at left
        show sis confused_talk at right
        sis "Should I call [missus]?"
        show pov sad_talk at left
        show sis confused at right
        pov "No! Don’t call [missus]!"
        show pov bored at left
        show sis shocked_talk at right
        sis "[missus]! [povname]'s going through puberty!"
    else:
        show pov shocked at left
        show sis confused_talk at right
        sis "Should I call [missus]?"
        show pov sad_talk at left
        show sis confused at right
        pov "No! Don’t call [missus]!"
        show pov bored at left
        show sis shocked_talk at right
        sis "Moooom! [povname]'s going through puberty!"

    if paranoidentrance_sisknowstalker == 1:
        pass
    else:
        show sis confused_talk at right
        sis "Seriously, what happened?"
        sis "Did you get beat up at university, over the whole nudity thing or something?"
        show pov angry_talk at left
        show sis confused at right
        pov "Shut up about that!"
        show pov embarrassed at left
        show sis sad_talk at right
        sis "What has you so scared?"
        if paranoidentrance_sisknowstalker == 2:
            $ paranoidentrance_sisknowstalker = 0

            show pov angry_talk at left
            show sis sad at right
            pov "I told you already! There's a stalker stalking me!"
            show pov angry at left
            show sis sad_talk at right
            sis "{i}*Sigh*{/i}"
            sis "If you're not going to be serious with me then-"
            show pov bored at left
            show sis sad at right
            sis "..."
            show sis sad_talk at right
            sis "I don't know. I'm trying, [povname]."

            if sister_points >= 1:
                $ sister_points -= 1
            else:
                $ sister_points = 0
            $ renpy.notify("Relationship with [sister] Decreased")

        else:
            show pov embarrassed_talk at left
            show sis confused at right
            pov "S-Scared?"
            pov "Me?"
            if winc == 0:
                pov "Don’t you know nothing scares your [povsisrole]? Heart of a lion and nerves of pure steel!"
            else:
                pov "Don’t you know nothing scares your bro? Heart of a lion and nerves of pure steel!"
            show pov bored at left
            show sis smirk_talk at right
            sis "You snuck into bed with me back when we were little because you thought the boogeyman was constantly watching from next door."
            show pov bored_talk at left
            show sis smirk at right
            pov "I was little back then."
            show pov bored at left
            show sis smirk_talk at right
            sis "You did it until you turned ten!"
            if winc == 0:
                sis "[dadname] had you with a night light the rest of the year!"
            else:
                sis "Dad had you with a night light the rest of the year!"
            show pov bored_talk at left
            show sis neutral at right
            pov "How was I supposed to know that old man Jerkins had a cardboard cutout of his past wife propped up against the window?"
            show pov confused_talk at left
            pov "That dude alone was scary as hell and he stared at me with his crazy eye everytime we rode our bikes down the street!"
            show pov embarrassed at left
            show sis bored_talk at right
            sis "He has a glass eye because lost his real one during the war and he gave you a daggering stare because you were the weird kid that cried boogeyman every time you rode past!"
            show pov embarrassed_talk at left
            show sis smirk at right
            if winc == 0:
                pov "Yes, yes, yes. Precious household memories and all of that."
            else:
                pov "Yes, yes, yes. Precious family memories and all of that."

    show pov embarrassed_talk at left
    show sis confused at right
    pov "Oh, look at the time!"
    pov "Sorry, gotta bounce!"
    hide pov embarrassed_talk
    $ renpy.pause()
    show sis confused_talk at right
    sis "[povname]...?!"
    show sis confused at right
    sis "…"
    show sis smirk_talk at right
    sis "Are you constipated again or something?!"

    menu:
        "Shut up!":
            show sis smirk at right
            pov "Shut up!"
            pov "Your face is constipated!"
        "Yes...":
            show sis smirk at right
            pov "… Yes, now leave me be or embrace the smell."
            show sis shocked_talk at right
            sis "Ew, Jesus, [povname]. Don’t make me puke."

    $ main_story = 47

    jump lbl_the_mother_obstacle
