## Camgurl Substitute Favour ##
label lbl_camgurl_substitute_favour:
    default camgurlsubstitutefavour_ask = 0
    if camgurlsubstitutefavour_ask == 0:
        pass
    else:
        jump lbl_camgurl_substitute_favour_1

    scene bg mybedroom_day
    show sis neutral_talk at right
    with hpunch
    sis "Hey! [povname]... you awake?"
    $ camgurlsubstitutefavour_ask = 1

    menu:
        "Yeah?":
            show povn bored_talk at left
            with dissolve
            show sis neutral at right
            pov "Yeah?"
            show povn bored at left
            show sis neutral_talk at right
            sis "Awesome."
        "Don't you ever knock?":
            show povn bored_talk at left
            with dissolve
            show sis neutral at right
            pov "Don't you ever knock?"
            show povn bored at left
            show sis smirk_talk at right
            sis "You gotta have {i}some{/i} spontaneity in your life."
        "Here for a morning quickie?" if sister_points >= 7:
            show povn smirk_talk at left
            with dissolve
            show sis neutral at right
            pov "Here for a morning quickie?"
            show povn bored at left
            show sis confused_talk at right
            sis "Not this morning, no."
    show povn confused at left
    show sis confused_talk at right
    sis "Why are you still naked?"
    show povn confused_talk at left
    show sis bored at right
    pov "I just got out of bed."
    show povn smirk at left
    show sis bored_talk at right
    sis "Well, can't you get changed?"
    show povn neutral_talk at left
    show sis neutral at right
    pov "I will."
    show povn smirk_talk at left
    show sis bored at right
    pov "After you tell me what's up."
    show povn smirk at left
    show sis smirk at right
    sis "..."
    show sis embarrassed_talk at right
    sis "Hehehe, it's funny..."
    sis "I was so ready to ask you this and-"
    show povn confused at left
    sis "I even hyped myself up and slapped my face a few times."
    show povn smirk_talk at left
    show sis embarrassed at right
    pov "Yeah, it does look a little tender."
    show povn confused at left
    show sis sad_talk at right
    sis "I uh-"
    show sis embarrassed_talk at right
    sis "I was hoping if you could..."
    show povn confused at left
    sis "Maybe I don't know if you want to..."
    show povn confused_talk at left
    show sis bored at right
    pov "Spit it out, [sister]."
    show povn neutral_talk at left
    pov "Like a bandaid."
    show povn neutral at left
    show sis bored_talk at right
    sis "Okay, first off; that doesn't even make any sense."
    show povn shocked at left
    show sis angry_talk at right
    sis "Second, don't put more pressure than what is already on me."
    show povn shocked at left
    show sis sad at right
    pov "..."
    show povn confused at left
    show sis embarrassed_talk at right
    sis "You see... I have my uhm... stream later in the afternoon. And-"
    show povn shocked at left
    sis "I was wondering if you..."
    show povn shocked_talk at left
    show sis shocked at right
    pov "Stop."
    show povn embarrassed_talk at left
    pov "I know what you're going to ask."
    show povn smirk_talk at left
    show sis bored at right
    pov "You want me to take over and host your webshow for you?"
    show povn smirk at left
    show sis bored_talk at right
    sis "What? No, that's stupid."
    show povn embarrassed_talk at left
    show sis bored at right
    pov "I'm just joking- nevermind terrible jok-"
    show povn sad_talk at left
    pov "Just proceed, I'll shut up."
    show povn embarrassed at left
    show sis sad_talk at right
    sis "{i}*Inhale*{/i}"
    sis "{i}*Exhale*{/i}"
    show povn shocked at left
    show sis embarrassed_talk at right
    sis "I was wondering if you wanted to stand in as one of my sex toys."

    menu:
        "Fuck. Yes.":
            show povn neutral_talk at left
            show sis smirk at right
            pov "Fuck. Yes."
            show povn neutral at left
            show sis smirk_talk at right
            sis "I knew you would say that."
            show sis confused_talk at right
            sis "Pervert-ass lookin' pervert-wannabe naked-ass-lookin' motherfuckin' naked-pervert-ass lookin' pervert."
            show povn embarrassed at left
            show sis bored_talk at right
            sis "Didn't even take a second to think about it, desperate-ass lookin' motherfuckin' naked-desperate-pervert-ass-"
            show povn confused_talk at left
            show sis confused at right
            pov "Oh. Kay. I get it. You don't have to rub it against me."
            show povn embarrassed_talk at left
            pov "So what are you saying? Was that all joke?"
            show povn shocked at left
            show sis confused_talk at right
            sis "Oh- no. I'm actually serious. I just didn't expect you to say ‘yes' so quickly. Kind of a turn off if you ask me."
            if sister_points >= 1:
                $ sister_points -= 1
                $ renpy.notify("Your relationship with [sister] has decreased by 1")
            else:
                $ sister_points = 0
            show povn bored at left
            sis "It's like you're skipping the foreplay all together."
            show povn confused at left
            sis "Anyway, I really need a body double for my Ben-Dover sex doll."
            show povn embarrassed at left
            show sis sad_talk at right
            sis "It was supposed to arrive today but Hazel told me that it was delayed for some shitty reason."
            show sis embarrassed_talk at right
            sis "You know how mail couriers are."
            show povn confused at left
            show sis smirk_talk at right
            sis "Probably some guy stranded on an island right now butt-fucking my Ben-Dover sex doll crying out ‘Wilson'!"
            show povn confused_talk at left
            show sis confused at right
            pov "That is weirdly specific, is that from a movie?"
            show povn bored at left
            show sis confused_talk at right
            sis "Ben-Dover? I think it was one of those gag-names that someone decided to make into a sex doll."
            show sis confused at right
            pov "..."
            show povn embarrassed at left
            show sis confused_talk at right
            sis "Anyhoosies, as you may know, the stream is in the afternoon."
            show povn neutral at left
            show sis neutral_talk at right
            sis "Meet me in my room later, alright?"
            show povn embarrassed at left
            show sis confused_talk at right
            sis "And if I were you, I'd jack off before the actual stream. I want you to last as long as possible, thanks."
            show povn smirk_talk at left
            show sis smirk at right
            pov "Jeez, so many demands. First day and I'm treated like a piece of meat."
            $ sister_path = 39
        "No, thanks.":
            show povn smirk_talk at left
            show sis smirk at right
            pov "No, thanks."
            show povn smirk at left
            show sis neutral_talk at right
            sis "Awesome, I knew you woul-"
            show povn confused at left
            show sis angry_talk at right
            sis "Wait, what did you say?"
            show povn confused_talk at left
            show sis shocked at right
            pov "No, thanks."
            pov "Not in the mood."
            show sis angry at right
            pov "Camera shy."
            pov "Take advantage of."
            pov "You didn't say the magic word."
            pov "Insert another excuse here."
            show povn neutral_talk at left
            pov "Yeah."
            show povn embarrassed at left
            sis "..."
            show povn shocked at left
            show sis angry_talk at right
            sis "What the fuck, man."
            sis "I fuck your back and you fuck mine."
            show povn embarrassed at left
            sis "I thought we had a thing going."
            show povn bored_talk at left
            show sis angry at right
            pov "First off, that doesn't make sense."
            show povn smirk_talk at left
            show sis shocked at right
            pov "And B, what do I get in return? Don't make me protest for equal pay."
            show povn confused at left
            show sis angry_talk at right
            sis "You're really gonna go there? You get your dick wet, isn't that enough?"
            show povn smirk_talk at left
            show sis angry at right
            pov "Hey, I'm not that desperate to get my bong hit."
            pov "There's plenty of fish in the-"
            if skinnydipping_fishbite == 1:
                show povn embarrassed_talk at left
                pov "The- the--"
                show povn shocked at left
                pov "..."
                show povn sad_talk at left
                show sis confused at right
                pov "Jesus... I just had a nasty flashback."
                show povn sad at left
                show sis bored_talk at right
                sis "Not even gonna ask."
                show povn embarrassed_talk at left
                show sis angry at right
                pov "Look, I'm just saying that you're not the only one who has a thing for my co-"
            if skill_cha >= 14:
                show povn confused at left
                show sis sad_talk at right
                sis "{i}*Sigh*{/i} Fuck you and your bullshit."
                show povn smirk at left
                sis "If you weren't such a good fuck I'd be so turned off right now."
                if sister_points <= 9:
                    $ sister_points += 1
                    $ renpy.notify("Your relationship with [sister] has increased")
                else:
                    $ sister_points = 10
                sis "Don't make me resort to begging..."
                show sis embarrassed_talk at right
                if winc == 0:
                    sis "C'mon. I'm your [sisrole] for Christ sake."
                else:
                    sis "C'mon. I'm your sister for Christ sake."
            else:
                show povn embarrassed at left
                show sis bored_talk at right
                sis "{i}*Sigh*{/i} Are you trying to make me jealous or something?"
                sis "Because it's not working."
                if sister_points >= 1:
                    $ sister_points -= 1
                else:
                    $ sister_points = 0
                $ renpy.notify("Your relationship with [sister] has decreased by 1")
                show povn sad at left
                sis " I could easily ask one of your friends for a fuck and you can watch from behind a computer screen like a sad little boy you are."

            menu:
                "Alright fine.":
                    show povn embarrassed_talk at left
                    show sis smirk at right
                    pov "Alright fine, I'll be your stand in body double sex toy- thing."
                    show povn embarrassed at left
                    show sis smirk_talk at right
                    sis "Good, knew you'd come around."
                    sis "Anyway, meet me in my room later this afternoon and we'll do a quick ‘de-briefing'."
                    sis "Little bit of adult entertainment humour for you there."
                    show povn smirk at left
                    sis "And I'll uh get straight ‘onto it', and you can get straight ‘into it'."
                    show povn bored at left
                    sis "Just another adult entertainment humour for you there. Keep the change, I'll be here all week."
                    show povn embarrassed at left
                    show sis confused_talk at right
                    sis "Don't try the veal, shit sucks chodes."
                    $ sister_path = 39
                "Sorry, I really am busy today.":
                    show povn embarrassed_talk at left
                    show sis sad at right
                    pov "Sorry, [sister]. Ask me next week. In all seriousness, I really am sorta busy today."
                    show sis sad_talk at right
                    sis "{i}*Sigh*{/i} Fine. I'll just tell the viewers that I can't use the Ben-Dover sex doll today."
                    sis "Wonder what old toy I can bring back today. Throwback Wednesday or whatever."
                    show sis bored_talk at right
                    sis "You better free up your schedule for next week, [povname]."
                    $ sister_path = 38.5

    jump lbl_camgurl_substitute_favour_end

label lbl_camgurl_substitute_favour_1:

    scene bg mybedroom_day
    show sis neutral_talk at right
    with hpunch
    sis "Hey! [povname]... you awake?"
    show povn bored_talk at left
    with dissolve
    show sis neutral at right
    pov "Ugh... What do you want now."
    show povn bored at left
    show sis smirk_talk at right
    sis "It's Wednesday, ma dude."
    show povn confused at left
    sis "So what'll be?"
    show povn confused_talk at left
    show sis embarrassed at right
    pov "Hmm? What are you talking about?"
    show povn shocked at left
    show sis embarrassed_talk at right
    sis "Are you gonna be my body double for my unarrive-and-probably-never-arrive Ben Dover sex doll?"

    menu:
        "Alright, sure.":
            show povn smirk_talk at left
            show sis neutral at right
            pov "Alright, sure. Fuck it."
            show povn neutral_talk at left
            show sis neutral at right
            pov "Let's fuck the shit out of each other on camera!"
            show povn neutral at left
            show sis neutral_talk at right
            sis "That's the spirit!"
            show povn smirk at left
            sis "Meet me in my room in the afternoon and we'll get straight into it."
            $ sister_path = 39
        "Can we please do next week.":
            show povn embarrassed_talk at left
            show sis sad at right
            pov "Can we please do next week?"
            pov "I really did try to free myself up for you but other plans get in the way."
            show povn shocked at left
            show sis sad_talk at right
            sis "{i}*Sigh*{/i} Don't worry, I know you don't love me in that way."
            show povn sad at left
            sis "You don't need to make excuses."
            show povn sad_talk at left
            show sis sad at right
            pov "[sister]..."
            show povn bored at left
            show sis smirk_talk at right
            sis "I'm fucking with you, [povname]. But seriously. My viewers are getting antsy."
            show povn embarrassed at left
            show sis neutral_talk at right
            sis "I'll keep asking you until you say yes."
            $ sister_path = 38.5

label lbl_camgurl_substitute_favour_end:
    jump lbl_mybedroom_day_setup
