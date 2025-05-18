## Underaged Drinking ##
label lbl_underaged_drinking:

    scene bg nightclub_night
    with fade
    show sis smirk_talk flip at Position(xpos=600)
    with dissolve
    show pov embarrassed at left
    with dissolve
    show ste neutral at right
    with dissolve
    call lbl_nightclub_counter_check
    sis "Aye! Steve, ma' main man."
    show sis smirk flip at Position(xpos=600)
    show ste neutral_talk at right
    ste "What is good, [sister]? How is my p'avourite customer?"
    show sis neutral_talk flip at Position(xpos=600)
    show ste confused at right
    if winc == 0:
        sis "Not too shabby. Aye, this is my [povsisrole]. You might have seen him in here before."
    else:
        sis "Not too shabby. Aye, this is my brother. You might have seen him in here before."
    if steve_path >= 1:
        show sis neutral flip at Position(xpos=600)
        show ste smirk_talk at right
        if winc == 0:
            ste "Yeah, yeah, I know that p'ace. I didn't know he was your [povsisrole]."
        else:
            ste "Yeah, yeah, I know that p'ace. I didn't know he was your brother."
        show sis neutral_talk flip at Position(xpos=600)
        show ste neutral at right
        if winc == 0:
            sis "[povsisrole]s. Yeah, trust me, we used to look more alike when we were younger."
        else:
            sis "Twin brother. Yeah, trust me, we used to look more alike when we were younger."
        show sis neutral flip at Position(xpos=600)
        show pov neutral at left
        show ste embarrassed_talk at right
        if winc == 0:
            ste "I'm so sorry I was so hard on you, brosep'. If I had known you two were [sisrole]s."
        else:
            ste "I'm so sorry I was so hard on you, brosep'. If I had known you two were related."
        show pov embarrassed_talk at left
        show ste embarrassed at right
        pov "It's all good. You're just doing your job, uh- Steve was it?"
        show pov neutral at left
        show ste neutral_talk at right
        ste "Precisely."
        show sis smirk_talk flip at Position(xpos=600)
        show pov embarrassed at left
        show ste smirk at right
        sis "Did he try to buy a drink?"
        show sis smirk flip at Position(xpos=600)
        show ste neutral_talk at right
        ste "One too many times, I'm ap'raid."
        show sis smirk_talk flip at Position(xpos=600)
        show pov bored at left
        show ste neutral at right
        sis "Tsk tsk tsk, [povname]. You know the law, you shouldn't be buying drinks at your age."
    else:
        show sis smirk flip at Position(xpos=600)
        show pov embarrassed at left
        show ste smirk_talk at right
        ste "Actually, no? Maybe. He might've been dancing on the dance floor but I've never seen him at this bar."
        $ steve_path = 1

## $ steve_path = 2
    show sis neutral flip at Position(xpos=600)
    show ste neutral_talk at right
    ste "Honestly, I find it sooo hilarious t'at your country's legal drinking age is 21."
    show sis bored flip at Position(xpos=600)
    show ste smirk_talk at right
    ste "I t'ought it was a joke at p'irst."
    show ste neutral_talk at right
    ste "Hahahaha!"
    show ste bored_talk at right
    ste "But no..."
    show sis bored_talk flip at Position(xpos=600)
    show ste smirk at right
    sis "Yeah, yeah. Land of the free. Hey, listen-"
    show sis smirk_talk flip at Position(xpos=600)
    show pov confused at left
    show ste smirk at right
    sis "Would you mind hooking us up with some... y'know... ‘gum'?"
    show sis neutral_talk flip at Position(xpos=600)
    sis "One each for the both of us to start of with- and uh, one for yourself."
    show sis neutral flip at Position(xpos=600)
    show ste neutral_talk at right
    ste "Appreciated, [sister]. Coming right up!"

    scene bg underageddrinking_1
    with fade
    pov "‘Gum'? Aren't we drinking?"
    show bg underageddrinking_2
    sis "It's our little ode-cay word for ots-shay."
    show bg underageddrinking_3
    sis "omprende-cay?"
    show bg underageddrinking_4
    pov "I ink-thay..."
    show bg underageddrinking_5
    with dissolve
    $ renpy.pause()
    show bg underageddrinking_6
    if winc == 0:
        sis "Bottoms up, little [povsisrole]."
    else:
        sis "Bottoms up, little bro."
    show bg underageddrinking_7
    $ renpy.pause(1,hard=True)
    show bg underageddrinking_8
    $ renpy.pause(0.5,hard=True)
    show bg underageddrinking_7
    with hpunch
    $ renpy.pause()
    show black
    with fade
    $ renpy.pause()
    "A few shots later..."

    scene bg underageddrinking_9
    with fade
    pov "An- an- an an- then- he was all lik'..."
    show bg underageddrinking_10
    pov "F- fuccck you!"
    show bg underageddrinking_9
    pov "I was all like... NO...!"
    show bg underageddrinking_10
    pov "F- fuccck you!"
    show bg underageddrinking_9
    pov "And he- he said t- to me...."
    show bg underageddrinking_10
    pov "F- fuccckk you!"
    show bg underageddrinking_9
    pov "And I was like- nooooooo...!"
    show bg underageddrinking_10
    pov "Fuckyouuuuuuuuuuuuuuuuuu!"
    show bg underageddrinking_11
    pov "An- an- an- and then we became best buds..."
    show bg underageddrinking_12
    pov "..."
    show bg underageddrinking_13
    pov "Y'know what I mean?!"
    show bg underageddrinking_14
    sis "That is such an interesting story, [povname]. I didn't know you had such a cool relationship with your doctor."
    show bg underageddrinking_15
    sis "All my doctor does is tell me to lift up my shirt."
    show bg underageddrinking_16
    pov "Noooo... honest to Jebus?!"
    show bg underageddrinking_17
    sis "Like I swear to God, all they wanna do is tit-fuck me."
    show bg underageddrinking_10
    pov "Hell, fuckin' yeah, girrrrrrl! Your TITS are fucking amaaahaaaeehaeeyzing."
    sis "But no... they just wanna check my heart beat or so they say."
    show bg underageddrinking_9
    if winc == 0:
        pov "Like I know I'm like youuur [povsisrole] an' all. But FUCK you g-got big fucking tits!"
    else:
        pov "Like I know I'm like youuur bro-bro an' all. But FUCK you g-got big fucking tits!"
    sis "Like that's such bullshit, right?"
    show bg underageddrinking_10
    pov "Such b- {i}*hiccup*{/i} u-ulll shit!"
    show bg underageddrinking_9
    sis "I bet she's a closet lesbian or something."
    show bg underageddrinking_11
    pov "H- have you asked her to lift HER shirt up?!"
    show bg underageddrinking_17
    sis "[povname]... be real with me."
    show bg underageddrinking_14
    sis "Why are you such a fucking genius?!"
    show bg underageddrinking_18
    pov "I don'- I don'- knowww!"
    show bg underageddrinking_19
    sis "I don't know what it is about alcohol but it's made you into such a smart, interesting, funny person."
    show bg underageddrinking_20
    sis "I like you a lot better like this."
    show bg underageddrinking_11
    pov "Nawwwww, naww?"
    pov "Yo- you really mean thaa', [sister]?"
    show bg underageddrinking_17
    sis "Cross my heart and hope to die."
    show bg underageddrinking_10
    pov "Well, I like you too! An- an- an- and I'm not just saaaayin' that ‘cause yooouu said it!"
    show bg underageddrinking_11
    if winc == 0:
        pov "Hahahahaha! Besties!"
    else:
        pov "Hahahahaha! Twinsies!"
    pov "Hahahaha!"
    pov "Maaaaan! Whooo the fuccckk waaants to wait until they're tweenn'y one?!"
    show bg underageddrinking_9
    pov "Hahaha! I don't!"
    show bg underageddrinking_10
    pov "Drinking is sooo m-much fun!"
    show bg underageddrinking_9
    idk "{i}*Clears throats*{/i}"
    show bg underageddrinking_21
    mina "What was that you said?"
    sis "Sorry, I know he sounds a little tipsy at the moment. He said and I quote."
    show bg underageddrinking_22
    if winc == 0:
        sis "'Hahahahaha! Besties!'"
    else:
        sis "'Hahahahaha! Twinsies!'"
    show bg underageddrinking_23
    mina "No, after that."
    show bg underageddrinking_22
    sis "He said, 'Drinking is sooo much fun!'"
    show bg underageddrinking_23
    mina "No, before that."
    show bg underageddrinking_22
    sis "He said, “Hahahahaha, I don't!”"
    show bg underageddrinking_23
    mina "A little bit more before that."
    show bg underageddrinking_21
    if winc == 0:
        sis "'Best-‘"
    else:
        sis "'Twin-'"
    mina "Nope again, keep going."
    sis "'Who the fuck wants to wait until they're twenty one? I don't?'"
    show bg underageddrinking_23
    mina "That's the ticket."
    mina "Can I see some ID from the both of you?"
    show bg underageddrinking_22
    sis "Yes, we're over 18, hahahaha! Barely though."
    show bg underageddrinking_24
    sis "But no thank you. We're not looking for a prostitute at the moment."
    if winc == 0:
        sis "Just wanna enjoy some bev with my [povsisrole] over here."
    else:
        sis "Just wanna enjoy some bev with my brov over here."
    show bg underageddrinking_21
    mina "Hey, Steve?"
    show bg underageddrinking_25
    with dissolve
    ste "Yes, ma'am?"
    ste "A- am I in trouble?"
    show bg underageddrinking_26
    mina "Depends. Did you know you were serving these {i}kids{/i}?"
    show bg underageddrinking_27
    ste "I swear, the p'irst time I asked for t'eir IDs, it said t'ey were over 21."
    show bg underageddrinking_25
    ste "T'ey must have given me p'ake IDs- Hey! How is about a drink on the house?!"
    ste "Eh? Eeeh? On me-!"
    show bg underageddrinking_28
    ste "Well... I mean not {i}ON{/i} me, p'ysically but-"
    show bg underageddrinking_29
    mina "Not right now, I'm on duty again."
    mina "C'mon, you two. You're coming with me."
    show bg underageddrinking_30
    sis "Jesus, Steve. Can you tell this lady that we're not interested in her."
    show bg underageddrinking_31
    ste "I think you better go, Miss."
    show bg underageddrinking_32
    pov "Ahhh! Shittt! I just remembered!"
    pov "Right b-fore I said fuck you to him...!"
    pov "He saaaid fucckkkk you!"
    show bg underageddrinking_33
    mina "How many shots did this kid have?"
    show bg underageddrinking_34
    sis "It's an embarrassingly low amount, he's not used to drinking."
    mina "Mmmmhmm."
    show black
    with fade
    $ renpy.pause()
    $ sister_path = 20
    $ gtime = 3

    jump lbl_sibling_jail_time
