## Effie Mentions Sister ##
label lbl_effie_mentions_sister:
    default effiementionsister_revealed = 0
    if winc == 0:
        jump lbl_effie_mentions_sister_winc0
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    eff "Hey, [povname]! Where are you off to?"
    show pov neutral_talk at left
    show eff neutral at right
    pov "Maybe work, maybe not. I like to live my life spontaneously."
    show pov confused at left
    show eff smirk_talk at right
    eff "Ahh. Got to earn the paper to keep your girl happy, huh?"
    show pov confused_talk at left
    show eff smirk at right
    pov "Huh?"
    show pov shocked at left
    show eff smirk_talk at right
    eff "Jacob told me about your girlfriend. She's really pretty. I saw her."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "Oh! Well, actually..."

    menu:
        "I'm a really lucky guy.":
            show pov neutral_talk at left
            show eff embarrassed at right
            pov "She's gorgeous, huh? I'm really lucky."
            show pov embarrassed at left
            show eff confused_talk at right
            eff "Yeah, you are. I was just surprised you hadn't mentioned her before."
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Oh, well, it didn't really matter when it came to us."
            show pov embarrassed at left
            show eff neutral_talk at right
            eff "Yeah. Okay, that makes sense."
            show pov smirk_talk at left
            show eff neutral at right
            pov "Are you jeal-"
            show pov shocked at left
            show eff bored_talk at right
            eff "Sh- She doesn't know about me, does she?"
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Not really.."
            show pov confused at left
            show eff embarrassed_talk at right
            eff "Like you guys aren't into-, y'know."
            show pov embarrassed at left
            eff "I guess I should keep my mouth shut about us then, huh?"
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Well..."
            show pov embarrassed at left
            show eff neutral_talk at right
            eff "Don't worry, dude."
            show pov shocked at left
            show eff smirk_talk at right
            eff "And hey, if ever you guys are into adding another person into your sex life."
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "We're cool, yeah?"
            show eff neutral_talk at right
            eff "Well, of course she's gotta be okay with me, hahaha."
            eff "Anyway, I've got to go. But I'll see you later!"
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Uh yeah, for sure. Bye, Effie."
            hide eff neutral
            $ effiementionsister_revealed = 0
        "She's my twin sister.":
            show pov neutral_talk at left
            show eff shocked at right
            pov "Jacob was totally wrong. She's not my girlfriend, she's my twin sister."
            show pov neutral at left
            show eff shocked_talk at right
            eff "What?!"
            show pov smirk_talk at left
            show eff neutral at right
            pov "You know how he is. He never listens to anything anyone tries to tell him."
            show pov smirk at left
            show eff embarrassed_talk at right
            eff "Ugh, he really doesn't. He was going on and on about the two of you."
            show pov neutral_talk at left
            show eff embarrassed at right
            pov "Obviously making stuff up."
            show pov neutral at left
            show eff smirk_talk at right
            eff "Obviously."
            show pov neutral at left
            show eff neutral_talk at right
            eff "Hey, could you introduce me to your twin?"
            show pov neutral_talk at left
            show eff neutral at right
            pov "Yeah, sure. Anytime."
            show pov confused at left
            show eff embarrassed_talk at right
            eff "Does she..."
            show pov confused_talk at left
            show eff smirk at right
            pov "Does she what?"
            show pov shocked at left
            show eff smirk_talk at right
            eff "Does she swing both ways?"
            show pov confused_talk at left
            show eff neutral at right
            pov "Are you asking me if she likes girls?"
            show pov embarrassed at left
            show eff smirk_talk at right
            eff "C'mon, don't be as dense as Jacob."
            show pov embarrassed_talk at left
            show eff smirk at right
            pov "I don't know, actually. We've never talked about it. What plans do you have with my sister?"
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "I just thought maybe you could put in a good word for me."
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "A good word? To [sister]? About you?"
            show eff embarrassed at right
            pov "So you can make a move on her?"
            show pov bored at left
            show eff smirk_talk at right
            eff "Aha! You pieced it all together."
            show pov shocked at left
            show eff embarrassed_talk at right
            eff "To put it bluntly, I find her just as attractive as you."
            show pov confused at left
            show eff neutral_talk at right
            eff "I guess it makes sense, you being twins and all."
            show pov confused_talk at left
            show eff neutral at right
            pov "We don't look that much alike."
            show pov confused at left
            show eff neutral_talk at right
            eff "They say that if you see a clone of yourself in real life, you won't be able to recognise them."
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Possibly?"
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "Please... For a friend?"
            $ effiementionsister_revealed = 1

            menu:
                "I guess I can do it.":
                    show pov embarrassed_talk at left
                    show eff neutral at right
                    pov "I have never had to play wingman for [sister] before. But, uh... I guess I can do it for a... friend."
                    show pov embarrassed at left
                    show eff neutral_talk at right
                    eff "You're the best! Thank you so much."
                    show pov shocked at left
                    show eff smirk_talk at right
                    eff "She looks like a bubble ready to be popped, if you know what I mean."
                    show pov embarrassed_talk at left
                    show eff smirk at right
                    pov "Uh- yeah?"
                    show pov embarrassed at left
                    show eff neutral_talk at right
                    eff "Anyway, I'll see you around!"
                    hide eff neutral_talk
                "I thought we were...":
                    show pov embarrassed_talk at left
                    show eff confused at right
                    pov "I thought we were uh- y'know..."
                    show pov sad at left
                    show eff confused_talk at right
                    eff "In a relationship?"
                    show pov embarrassed_talk at left
                    show eff shocked at right
                    pov "No, more like... exclusive."
                    show pov embarrassed at left
                    show eff embarrassed_talk at right
                    eff "Oh! Uh- well, this is awkward, isn't it?"
                    eff "I thought we were transparent about sleeping around and having multiple friends with benefits."
                    show pov sad at left
                    show eff embarrassed at right
                    pov "..."
                    show pov embarrassed_talk at left
                    show eff embarrassed at right
                    pov "I mean- yeah I guess. It doesn't make sense if we're locked together, doesn't it?"
                    pov "..hahaha."
                    show pov embarrassed at left
                    show eff embarrassed_talk at right
                    eff "You're sweet, [povname]. But we're young and wild. Spread your wings."
                    show eff neutral_talk at right
                    eff "I'll be spreading eagle for quite some time before I settle down."
                    show eff sad at right
                    pov "..."
                    show eff embarrassed_talk at right
                    eff "Look, real talk, dude. If you can win me over, I'll be loyal to you and only you."
                    show pov embarrassed at left
                    eff "Cool?"
                    show pov embarrassed_talk at left
                    show eff neutral at right
                    pov "Cool..."
                    show pov embarrassed at left
                    show eff neutral_talk at right
                    eff "Cool! Then, I guess you'll hook me up?"
                    show pov embarrassed_talk at left
                    show eff neutral at right
                    pov "Uh- yeah. Sure. I'll mention you."
                    show pov embarrassed at left
                    show eff embarrassed_talk at right
                    eff "Thank you, [povname]. Glad we can come to an understanding."
                    hide eff embarrassed_talk at right
    show pov bored at left
    pov "{i}Great, that ended well. I really thought I'd be her only one.{/i}"
    show pov sad at left
    pov "Didn't think my competition would be my own sister."
    $ sister_path = 7

    jump lbl_schoolyard_day_setup

### NO WINC ###
label lbl_effie_mentions_sister_winc0:
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    eff "Hey, [povname]! Where are you off to?"
    show pov neutral_talk at left
    show eff neutral at right
    pov "Maybe work, maybe not. I like to live my life spontaneously."
    show pov confused at left
    show eff smirk_talk at right
    eff "Ahh. Got to earn the paper to keep your girl happy, huh?"
    show pov confused_talk at left
    show eff smirk at right
    pov "Huh?"
    show pov shocked at left
    show eff smirk_talk at right
    eff "Jacob told me about your girlfriend. She's really pretty. I saw her."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "Oh! Well, actually..."

    menu:
        "I'm a really lucky guy.":
            show pov neutral_talk at left
            show eff embarrassed at right
            pov "She's gorgeous, huh? I'm really lucky."
            show pov embarrassed at left
            show eff confused_talk at right
            eff "Yeah, you are. I was just surprised you hadn't mentioned her before."
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Oh, well, it didn't really matter when it came to us."
            show pov embarrassed at left
            show eff neutral_talk at right
            eff "Yeah. Okay, that makes sense."
            show pov smirk_talk at left
            show eff neutral at right
            pov "Are you jeal-"
            show pov shocked at left
            show eff bored_talk at right
            eff "Sh- She doesn't know about me, does she?"
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Not really.."
            show pov confused at left
            show eff embarrassed_talk at right
            eff "Like you guys aren't into-, y'know."
            show pov embarrassed at left
            eff "I guess I should keep my mouth shut about us then, huh?"
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Well..."
            show pov embarrassed at left
            show eff neutral_talk at right
            eff "Don't worry, dude."
            show pov shocked at left
            show eff smirk_talk at right
            eff "And hey, if ever you guys are into adding another person into your sex life."
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "We're cool, yeah?"
            show eff neutral_talk at right
            eff "Well, of course she's gotta be okay with me, hahaha."
            eff "Anyway, I've got to go. But I'll see you later!"
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Uh yeah, for sure. Bye, Effie."
            hide eff neutral
            $ effiementionsister_revealed = 0
        "She's my [sisrole].":
            show pov neutral_talk at left
            show eff shocked at right
            pov "Jacob was totally wrong. She's not my girlfriend, she's my [sisrole]."
            show pov neutral at left
            show eff shocked_talk at right
            eff "What?!"
            show pov smirk_talk at left
            show eff neutral at right
            pov "You know how he is. He never listens to anything anyone tries to tell him."
            show pov smirk at left
            show eff embarrassed_talk at right
            eff "Ugh, he really doesn't. He was going on and on about the two of you."
            show pov neutral_talk at left
            show eff embarrassed at right
            pov "Obviously making stuff up."
            show pov neutral at left
            show eff smirk_talk at right
            eff "Obviously."
            show pov neutral at left
            show eff neutral_talk at right
            eff "Hey, could you introduce me to your [sisrole]?"
            show pov neutral_talk at left
            show eff neutral at right
            pov "Yeah, sure. Anytime."
            show pov confused at left
            show eff embarrassed_talk at right
            eff "Does she..."
            show pov confused_talk at left
            show eff smirk at right
            pov "Does she what?"
            show pov shocked at left
            show eff smirk_talk at right
            eff "Does she swing both ways?"
            show pov confused_talk at left
            show eff neutral at right
            pov "Are you asking me if she likes girls?"
            show pov embarrassed at left
            show eff smirk_talk at right
            eff "C'mon, don't be as dense as Jacob."
            show pov embarrassed_talk at left
            show eff smirk at right
            pov "I don't know, actually. We've never talked about it. What plans do you have with my [sisrole]?"
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "I just thought maybe you could put in a good word for me."
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "A good word? To my [sisrole]? About you?"
            show eff embarrassed at right
            pov "So you can make a move on her?"
            show pov bored at left
            show eff smirk_talk at right
            eff "Aha! You pieced it all together."
            show pov shocked at left
            show eff embarrassed_talk at right
            eff "To put it bluntly, I find her just as attractive as you."
            show pov confused at left
            show eff neutral_talk at right
            eff "I guess it makes sense, you being [povsisrole]s and all."
            show pov confused_talk at left
            show eff neutral at right
            pov "We don't look that much alike."
            show pov confused at left
            show eff neutral_talk at right
            eff "They say that if you see a clone of yourself in real life, you won't be able to recognise them."
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "Possibly?"
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "Please... For a friend?"
            $ effiementionsister_revealed = 1

            menu:
                "I guess I can do it.":
                    show pov embarrassed_talk at left
                    show eff neutral at right
                    pov "I have never had to play wingman for my [sisrole] before. But, uh... I guess I can do it for a... friend."
                    show pov embarrassed at left
                    show eff neutral_talk at right
                    eff "You're the best! Thank you so much."
                    show pov shocked at left
                    show eff smirk_talk at right
                    eff "She looks like a bubble ready to be popped, if you know what I mean."
                    show pov embarrassed_talk at left
                    show eff smirk at right
                    pov "Uh- yeah?"
                    show pov embarrassed at left
                    show eff neutral_talk at right
                    eff "Anyway, I'll see you around!"
                    hide eff neutral_talk
                "I thought we were...":
                    show pov embarrassed_talk at left
                    show eff confused at right
                    pov "I thought we were uh- y'know..."
                    show pov sad at left
                    show eff confused_talk at right
                    eff "In a relationship?"
                    show pov embarrassed_talk at left
                    show eff shocked at right
                    pov "No, more like... exclusive."
                    show pov embarrassed at left
                    show eff embarrassed_talk at right
                    eff "Oh! Uh- well, this is awkward, isn't it?"
                    eff "I thought we were transparent about sleeping around and having multiple friends with benefits."
                    show pov sad at left
                    show eff embarrassed at right
                    pov "..."
                    show pov embarrassed_talk at left
                    show eff embarrassed at right
                    pov "I mean- yeah I guess. It doesn't make sense if we're locked together, doesn't it?"
                    pov "..hahaha."
                    show pov embarrassed at left
                    show eff embarrassed_talk at right
                    eff "You're sweet, [povname]. But we're young and wild. Spread your wings."
                    show eff neutral_talk at right
                    eff "I'll be spreading eagle for quite some time before I settle down."
                    show eff sad at right
                    pov "..."
                    show eff embarrassed_talk at right
                    eff "Look, real talk, dude. If you can win me over, I'll be loyal to you and only you."
                    show pov embarrassed at left
                    eff "Cool?"
                    show pov embarrassed_talk at left
                    show eff neutral at right
                    pov "Cool..."
                    show pov embarrassed at left
                    show eff neutral_talk at right
                    eff "Cool! Then, I guess you'll hook me up?"
                    show pov embarrassed_talk at left
                    show eff neutral at right
                    pov "Uh- yeah. Sure. I'll mention you."
                    show pov embarrassed at left
                    show eff embarrassed_talk at right
                    eff "Thank you, [povname]. Glad we can come to an understanding."
                    hide eff embarrassed_talk at right
    show pov bored at left
    pov "{i}Great, that ended well. I really thought I'd be her only one.{/i}"
    show pov sad at left
    pov "Didn't think my competition would be my own [sisrole]."
    $ sister_path = 7

    jump lbl_schoolyard_day_setup
