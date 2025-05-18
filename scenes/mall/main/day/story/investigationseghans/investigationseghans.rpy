label lbl_investigations_eghans:
    default investigations_eghans = 0
    show btn_mall_day_meghan_idle2
    show btn_mall_day_teghan_idle2
    show btn_mall_day_chieghan_idle2
    $ renpy.pause(0.001)

    if investigations_eghans != 0:
        pov "{i}I don't think they'll be of any help.{/i}"
    else:
        $ investigations_eghans = 1

        show pov neutral_talk at left
        with dissolve
        show teg neutral at right
        hide btn_mall_day_teghan_idle2
        with dissolve
        show chi neutral at Position(xpos=1300)
        hide btn_mall_day_chieghan_idle2
        with dissolve
        show meg confused at Position(xpos=1030)
        hide btn_mall_day_meghan_idle2
        with dissolve
        pov "Hey, girls. I was wondering if you could-"
        show pov neutral at left
        show teg neutral at right
        show chi neutral at Position(xpos=1300)
        show meg confused_talk at Position(xpos=1030)
        meg "No."
        show pov embarrassed_talk at left
        show teg neutral at right
        show chi neutral at Position(xpos=1300)
        show meg confused at Position(xpos=1030)
        pov "Uh… You didn’t even let me tell you-"
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        show meg angry_talk at Position(xpos=1030)
        meg "I don’t even want to hear you start."
        meg "Why are you wasting the oxygen around me, to begin with?"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi embarrassed at Position(xpos=1300)
        show meg angry at Position(xpos=1030)
        teg "Meg, that's a bit excessive…"
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        show meg angry at Position(xpos=1030)
        chi "A little bit…"
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        show meg angry_talk at Position(xpos=1030)
        meg "Are you two seriously taking his side now?!"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi embarrassed at Position(xpos=1300)
        show meg angry at Position(xpos=1030)
        teg "No one is taking anyone's side!"
        teg "I’m just saying, he hasn’t even said anything yet and-"
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        show meg angry_talk at Position(xpos=1030)
        meg "Ugh! Forget it!"
        meg "Fine. Talk to the nudist dork all you want. I’ll be ordering another latte while you do so."

        ##-Meghan leaves the conversation-
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        hide meg angry_talk
        show btn_mall_day_meghan_idle2 behind pov
        with dissolve
        pov "Uhhh, okay?"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi embarrassed at Position(xpos=1300)
        teg "Ugh, sorry about her, [povname]."
        teg "She is extra annoyed at the world, with all this stuff happening."
        teg "She becomes meaner, to deal with hard times."
        teg "Take it as a method of self-defense or something."
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        pov "Well, she is mean to me, in general, so I’ll have to take your word when it comes to that."
        show pov embarrassed at left
        show teg embarrassed at right
        show chi neutral_talk at Position(xpos=1300)
        chi "She is not so mean most of the time."
        show pov embarrassed at left
        show teg neutral_talk at right
        show chi neutral at Position(xpos=1300)
        teg "Yeah!"
        teg "She’s actually stopped and put an end to any rumors surrounding the comic book store geeks."
        teg "Figured, best to leave them alone while they deal with all this."
        show pov neutral_talk at left
        show teg neutral at right
        show chi neutral at Position(xpos=1300)
        pov "Oh, well."
        pov "That’s quite nice actually-"
        show pov neutral at left
        show teg neutral at right
        show chi embarrassed_talk at Position(xpos=1300)
        chi "She WAS the one who started them though."
        show pov neutral at left
        show teg embarrassed_talk at right
        show chi embarrassed at Position(xpos=1300)
        teg "R-Right. But she is learning not to kick people when they are down."
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        pov "It’s something, I guess…"
        show pov embarrassed at left
        show teg neutral_talk at right
        show chi embarrassed at Position(xpos=1300)
        teg "A-Anyway, what did you want to talk about, [povname]?"
        show pov confused_talk at left
        show teg neutral at right
        show chi neutral at Position(xpos=1300)
        pov "Oh, well I just wanted to ask if you know anything about town history in general or just weird and out of the norm stuff going on around town."
        show pov confused at left
        show teg confused_talk at right
        show chi confused at Position(xpos=1300)
        teg "You mean weirder than you just appearing naked in the middle of the park?"
        show pov embarrassed_talk at left
        show teg confused at right
        show chi confused at Position(xpos=1300)
        pov "Y-Yeah…"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi confused at Position(xpos=1300)
        teg "Hard time to ask about that with everything going on you know?"
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi confused at Position(xpos=1300)
        pov "Yeah, I know, but since you girls are always up to date with the latest gossip and all, I figured you may know something interesting."
        show pov embarrassed at left
        show teg confused_talk at right
        show chi embarrassed at Position(xpos=1300)
        teg "Well, there are a ton of things popping up all over town, but most relates to either the whole mess going on lately and your nude escapades."
        show pov embarrassed at left
        show teg confused at right
        show chi smirk_talk at Position(xpos=1300)
        chi "You being naked doesn’t come up as often though."
        show pov embarrassed_talk at left
        show teg confused at right
        show chi smirk at Position(xpos=1300)
        pov "Y-Yeah, I imagined something like that would be the case."
        pov "I was actually wondering more about stuff like other mysteries and general weirdness in town."
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi embarrassed at Position(xpos=1300)
        teg "That’s an awkward topic to just be asking around."
        teg "What for?"
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        pov "Well, I’m trying to get my mind off things and all, plus it gets me to know more about the town."
        show pov embarrassed at left
        show teg smirk_talk at right
        show chi smirk at Position(xpos=1300)
        teg "Well, aren’t you quite the curious little sausage?"
        teg "Though I suppose “Little Sausage” doesn’t exactly fit you, huh?"
        show pov embarrassed_talk at left
        show teg smirk at right
        show chi smirk at Position(xpos=1300)
        pov "W-What?"
        show pov shocked at left
        show teg smirk at right
        show chi smirk_talk at Position(xpos=1300)
        chi "She’s very thirsty!"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi smirk at Position(xpos=1300)
        teg "C-Chieghan, just don’t rat me out like that!"
        show pov embarrassed at left
        show teg embarrassed at right
        show chi smirk_talk at Position(xpos=1300)
        chi "But didn’t you say you wanted him to do-"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi smirk at Position(xpos=1300)
        teg "S-Shut it, girl!"
        teg "Sheesh, sometimes I think you are just pretending not to understand this sort of stuff."
        show pov embarrassed at left
        show teg embarrassed at right
        show chi smirk_talk at Position(xpos=1300)
        chi "Hehehe."
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi smirk at Position(xpos=1300)
        pov "Um, so-"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi neutral at Position(xpos=1300)
        teg "The beach!"
        teg "Try the beach!"
        teg "Violette used to say how some weird stuff happens there from time to time so you should go check there!"
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi neutral at Position(xpos=1300)
        pov "You guys know Violette?"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi neutral at Position(xpos=1300)
        teg "Y-Yeah, she is quite popular and is always around for parties and the like."
        teg "The guys tend to like having her around."
        show pov embarrassed at left
        show teg embarrassed at right
        show chi smirk_talk at Position(xpos=1300)
        chi "Do you like girls like that, [povname]?"
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi smirk at Position(xpos=1300)
        pov "I-I, um…"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi smirk at Position(xpos=1300)
        teg "T-That’s enough with you, missy!"
        teg "No need to interrogate him like that!"
        teg "E-Erm…"
        teg "But, well… Do you, [povname]?"
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi smirk at Position(xpos=1300)
        pov "That’s a bit-"
        show pov embarrassed at left
        show teg shocked at right
        show chi shocked at Position(xpos=1300)
        meg "Ugh, are you girls still talking to this creep?!"
        meg "Seriously, I assumed you bug would be done wasting our time by the time I returned with my Latte."
        meg "What do you want?"
        show pov embarrassed at left
        show teg shocked at right
        show chi shocked_talk at Position(xpos=1300)
        chi "He wants to know weird stuff about the town."
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        meg "Has he looked in the mirror recently?"
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        pov "Always a pleasure talking to you, Meghan."
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        meg "You wish you had the chance."
        meg "Seriously, I would assume you would be talking to Effie about boring town stuff with how obsessed she is about things like that."
        meg "But then again, guess I can’t blame her for not wanting to share stuff with the town weirdo."
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        pov "Effie used to ask around about this?"
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        meg "Yeah, didn’t you know?"
        meg "Effie used to be quite the snoop. Always asking stuff about the town and stuff like that, she was convinced something weird was going on but she suddenly stopped."
        meg "I just thought she outgrew that weirdo phase of hers, but she is still hanging out with losers like that blonde dork and you, so I guess old habits die hard."
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        pov "Wow, you manage to be both a super mean and condescending pain, yet somehow helpful at the same time."
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi embarrassed at Position(xpos=1300)
        teg "She is better once you get used to her."
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed_talk at Position(xpos=1300)
        chi "A real tsundere."
        show pov embarrassed at left
        show teg shocked at right
        show chi shocked at Position(xpos=1300)
        meg "Who are you calling a pain?!"
        meg "And who are you calling a tsundere, Chieghan?!"
        show pov embarrassed_talk at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        pov "I’ll keep in mind what you all told me, thanks a bunch!"
        show pov embarrassed at left
        show teg embarrassed at right
        show chi embarrassed at Position(xpos=1300)
        meg "Are you finally going away now?!"
        meg "And wait a second, who are you calling a pain?!"
        show pov embarrassed at left
        show teg embarrassed at right
        show chi smirk_talk at Position(xpos=1300)
        chi "Teghan looks great in a swimsuit, [povname] - but even better without it!"
        show pov embarrassed at left
        show teg embarrassed_talk at right
        show chi smirk at Position(xpos=1300)
        teg "W-What’s with you today!?"
        teg "N-Nevermind that. We’ll talk later, [povname]!"

    jump lbl_mall_day_setup
