label lbl_sister_comes_home:
    scene bg mylivingroom_day
    with fade
    ##"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."

    ##if winc == 0:
    ##    "You are relaxing with Mom in the couch downstairs after whatever it is the two of you decided to do together when [sister] comes homes."
    ##else:
    ##     "You are relaxing with [missus] in the couch downstairs after whatever it is the two of you decided to do together when [sister] comes homes."
    show sis sad_talk flip at left
    with dissolve
    if winc == 1:
        sis "Mom, I am home!"
    else:
        sis "[missus], I am home!"
    show sis sad flip
    show mum neutral_talk at center with dissolve
    mum "Oh, hi sweetie!"
    mum "How was your day?"
    show mum neutral
    show sis sad_talk flip
    sis "It was going well before a shit show happened when I tried to meet a friend at the university’s entrance."
    show sis shocked flip
    show mum angry_talk
    mum "Hey, watch the language!"
    show mum angry
    show sis bored_talk flip
    if winc == 1:
        sis "Sorry, Mom."
    else:
        sis "Sorry, [missus]."
    show sis confused_talk flip
    sis "Anyway, some asshole just left a drugged out girl in the middle of the street!"
    sis "The maniac started to masturbate and beg for someone to “Do her” until Officer Mina took her away."
    sis "Seems like she and the officer have some history too, seeing as she was calling her mistress and all that."
    show sis confused flip
    show mum shocked_talk
    mum "Oh my, that’s horrible!"
    show mum shocked
    show sis confused_talk flip
    sis "No kidding."
    sis "Also, have you seen [povname]?"
    sis "I didn’t see him among the crowd."
    show sis confused flip
    show pov neutral_talk flip at Position(xpos=1300) with dissolve
    pov "I am here, [sister]."
    show pov neutral flip
    ##if winc == 1:
    ##    "You reveal yourself to be laying on Mom's lap as she lovingly pets your head."
    ##else:
    ##    "You reveal yourself to be laying on [missus]'s lap as she lovingly pets your head."
    show sis confused_talk flip
    sis "You are home early?"
    sis "Now that’s surprising."
    show sis confused flip
    show pov neutral_talk flip
    pov "Well, I figured it wouldn’t do any good to worry you two more than I needed to, so I came back here as soon as uni ended."
    show pov neutral flip
    show sis embarrassed flip
    #+1 Sister Rp.
    $ add_points("sister_points",1)
    show sis embarrassed_talk flip
    sis "Aww, geez."
    sis "Thanks, [povname]."
    show sis embarrassed flip
    show pov bored_talk flip
    pov "Least I can do after worrying the two of you so much."
    show pov bored flip
    #-If Sister has been romanced-

    if sister_path >= 36:
        show sis bored_talk flip
        sis "I am not going to lie, I got a little scared when I didn’t see you amongst the crowd back there."
        show sis bored flip
        show pov bored_talk flip
        pov "Sorry about that, I figured you would have been home as well by the time I got here."
        show sis shocked_talk flip
        show pov bored flip
        sis "No, no. It’s fine!"
        sis "As long as you are home safe, it’s all good!"

        #=RESULT END#=
    show sis confused_talk flip
    sis "So, what have the two of you been doing all day?"
    show sis confused flip
        #-If Mom hasn’t been romanced-

    if mum_path <= 30:
        show mum bored_talk
        mum "Oh, you know."
        mum "Catching up with each other."
        mum "Talking, watching dramas."
        show mum neutral_talk
        #if winc == 1:
        #    mum "Your brother insisted on spending time with me so we had quite the fun day just spending some quality time together."
        #    mum "We haven’t done this since you two were children!"
        #    mum "It was so nice."
        #    show mum neutral
        #    show pov neutral_talk flip
        #    pov "I am glad you had a good time, Mom."
        #else:
        mum "Your [povsisrole] insisted on spending time with me so we had quite the fun day just spending some quality time together."
        mum "It was so nice."
        show mum neutral
        show pov neutral_talk flip
        pov "I am glad you had a good time, [missus]."


        show pov neutral flip
        show mum neutral_talk flip at Position(xpos=800) with dissolve
        mum "Oh, honey. It was just the best I’ve had in a good while!"
        mum "Thank you so much!"
        show mum neutral flip
        show sis neutral_talk flip
        sis "Sound’s like you two had fun!"
        sis "I’m sorry I missed it."
        show sis neutral flip
        show mum neutral_talk at center with dissolve
        mum "Oh, it’s alright, dear!"
        mum "There is always next time."

    #=RESULT END#=
    elif mum_path >= 31:
        if not homeearly_63c_fooledaround:
                #-If Mom is romanced but for some reason they didn’t pick the sex option-
            show mum smirk_talk
            #if winc == 1:
            #    mum "Oh, Your brother and I just had a wonderful time together."
            #    mum "He is such a dear, and helped me relax!"
            #    mum "We talked and watched some dramas and even drink some tea as well!"
            #    mum "He is so touching and considerate."
            #    mum "He even gave me a massage and I feel like heaven~"
            #    show mum smirk
            #    show pov smirk_talk flip
            #    pov "I am glad you enjoyed yourself, Mom."
            #    mum "Oh honey, I didn’t just enjoy myself."
            #    mum "You took me to cloud nine!"
            #    mum "Not even your father when he was younger, pampered me as much as you did today."
            #    mum "I kind of like being treated that way now!"
            #    mum "You made me feel like a goddess today."
            #else:
            mum "Oh, Your [povsisrole] and I just had a wonderful time together."
            mum "He is such a dear and helped me relax!"
            mum "We talked and watched some dramas and even drink some tea as well!"
            mum "He is so touching and considerate."
            mum "He even gave me a massage and I feel like heaven~"
            show mum smirk
            show pov smirk_talk flip
            pov "I am glad you enjoyed yourself, [Missus]."
            show pov smirk flip
            show mum smirk_talk
            mum "Oh honey, I didn’t just enjoy myself."
            mum "You took me to cloud nine!"
            mum "Not even your [dadrole] when he was younger, pampered me as much as you did today."
            mum "I kind of like being treated that way now!"
            mum "You made me feel like a goddess today."
            show mum smirk
            show sis bored_talk
            sis "Geez, [povname]."
            sis "Don’t spoil her too much, alright?"
            sis "What kind of adult do you expect her to turn into if you keep doing so?"
            show sis bored
            show mum bored_talk
            mum "Very funny!"

            #-If Sister has been romanced-
            if sister_path >= 36:
                show mum bored
                show sis angry_talk flip
                sis "And when exactly do you plan to pamper me, huh?"
                show sis angry flip
                show pov shocked_talk flip
                pov "Um…"
                show pov shocked flip
                show sis angry_talk flip
                sis "We are going to talk about this later, [povname]."
                show sis angry
                    #=RESULT END#=
            #=RESULT END#=

            #-If Mom has been romanced and the player chose to have sex with her just now-
        elif homeearly_63c_fooledaround:
            show sis confused_talk flip
            sis "The two of you look a bit winded."
            #if winc == 1:
            ##    "Missus gains a sultry look to her eye as she starts to tease the MC with her double meaning."

            #    mum "Oh, you know~"
            #    mum "Your brother and I felt the need for a good… Workout."
            #    sis "A workout?"
            #    mum "I needed to burn some calories and your brother just has quite the stamina to keep me going, you know?"
            #    pov "Uhh…"
            #    mum "He is an athletic guy, so I just asked him to help me with some exercises I saw on late night tv and a few internet sites."
            #    mum "Some Yoga poses meant to help with my circulation."
            #    sis "You two are doing yoga now?"
            #    pov "A-A type of yoga, I suppose…"
            #    mum "Your brother has a real talent for making me feel the burn in our exercises!"

            #else:
            ##    "[missus] gains a sultry look to her eye as she starts to tease the MC with her double meaning."
            show sis confused flip
            show mum embarrassed_talk
            mum "Oh, you know~"
            mum "Your [povsisrole] and I felt the need for a good… Workout."
            show mum embarrassed
            show sis confused_talk flip
            sis "A workout?"
            show sis confused flip
            show mum embarrassed_talk
            mum "I needed to burn some calories and your [povsisrole] just has quite the stamina to keep me going, you know?"
            show mum embarrassed
            show pov embarrassed_talk flip
            pov "Uhh…"
            show pov embarrassed flip
            show mum embarrassed_talk
            mum "He is an athletic guy, so I just asked him to help me with some exercises I saw on late night tv and a few internet sites."
            mum "Some Yoga poses meant to help with my circulation."
            show mum embarrassed
            show sis confused_talk flip
            sis "You two are doing yoga now?"
            show sis confused flip
            show pov embarrassed_talk flip
            pov "A-A type of yoga, I suppose…"
            show pov embarrassed flip
            show mum neutral_talk
            mum "Your [povsisrole] has a real talent for making me feel the burn in our exercises!"



            mum "We plan to go through the whole manual, although we like some exercises more than others."
            show mum smirk_talk flip at Position(xpos=800) with dissolve
            mum "What were they called, hun?"
            mum "The Amazon? The Hound? The Rider?"
            mum "I am rather fond of The Padlock, but I believe you were rather enthusiastic during The Supernova and The Sphinx."
            mum "Oh yes, you definitely let me feel your enthusiasm during The Sphinx~"
            show mum smirk flip
            show sis shocked_talk flip
            sis "What?"
            show mum shocked_talk at center with dissolve
            mum "The burn, I mean!"
            mum "This exercises really get you pumped up!"
            show mum shocked
            sis "I thought yoga was meant to help you relax?"
            show mum neutral_talk
            mum "Oh, I am relaxed, I’ll tell you that much."
            mum "Very relaxed, in fact."
            mum "I haven’t felt this good in ages!"

                    #-If Sister has been romanced-
            if sister_path >= 36:
                show mum neutral
                show sis angry_talk flip
                sis "Anything you want to tell me there, [povname]?"
                show sis angry flip
                show pov shocked_talk flip
                pov "Uhh…"
                show pov shocked flip
                show sis angry_talk flip
                sis "You and I are having a long chat later."
                show sis angry flip
                show pov shocked_talk flip
                pov "Yes, Ma’am…"
                show pov shocked
                    #=RESULT END#=
            #=RESULT END#=
    show mum bored_talk
    mum "Anyway!"
    mum "Now that the two of you are home, I have something important I want to talk to you two about."
    mum "Let’s go to the dining room."
    show mum bored
    show sis confused_talk flip
    sis "Why the dining room? I was hoping to get home and just chill on the sofa for a while."
    show sis confused flip
    show mum angry_talk
    mum "This is a serious talk, [sister]. So I want your full attention."
    mum "Now let’s go, you two. I won’t ask again."
    show mum angry
    show pov shocked_talk flip
    pov "We’re coming."
    show pov shocked flip
    show sis angry_talk flip
    sis "Ugh, fine. "
    sis "But I am requesting the TV after this."
    show sis angry flip

    #=SCENE END#=
    $ main_story = 66
    scene black with fade
    jump lbl_safety_and_home_life
