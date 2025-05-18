## A Stranger Morning ##
label lbl_a_stranger_morning:
    if winc == 0:
        jump lbl_a_stranger_morning_winc0
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Morning, honey."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Morning, Mom."
    show pov neutral at left
    show mum smirk_talk at right
    mum "Did you get home safe last night? You were out pretty late."
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "Oh, yeah. Sorry about that. I just ran to catch up with someone."
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "Did you get some last night?"
    show pov confused_talk at left
    show mum smirk at right
    pov "Hmm? Sorry?"
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "Did you get some action? Some fun? Y'know, did you get down and dirty?"

    menu:
        "I went to the park.":
            show pov embarrassed_talk at left
            show mum smirk at right
            pov "I just went to the park to meet Effie."
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Though she didn't show up."
            show pov embarrassed at left
            show mum bored_talk at right
            mum "Oh, that's a shame, sorry to hear that. There are plenty of other girls out there to bang."
        "Too much information.":
            #if mum_points >= 1:
            #    $ mum_points -= 1
            #    $ renpy.notify("Your relationship with Mom has decreased by 1")
            #else:
            #    $ mum_points = 0
            show pov confused_talk at left
            show mum confused at right
            pov "Too much information, Mom."
            show pov confused at left
            show mum confused_talk at right
            mum "What? I'm just asking if you fucked anyone last night. Sheesh, Mr. Grumpy-Pants."
        "It was eventful.":
            #if mum_points <= 9:
            #    $ mum_points += 1
            #    $ renpy.notify("Your relationship with Mom has increased")
            #else:
            #    $ mum_points = 10
            show pov embarrassed_talk at left
            show mum neutral at right
            pov "It was eventful, I'll tell you that."
            show pov confused at left
            show mum smirk_talk at right
            mum "Oooh, I'd like to hear the juicy details later, okay?"
    show pov confused_talk at left
    show mum confused at right
    pov "Mom... are you drunk or something? It's not really something we should talk about."
    show pov confused at left
    show mum confused_talk at right
    mum "What? I'm not drunk, I'm fine. And you're my son. There's nothing in the world that you should hide from me."
    show pov sad at left
    show mum angry_talk at right
    mum "There isn't anything you're hiding from me, is there?"

    menu:
        "No.":
            show pov embarrassed_talk at left
            show mum confused at right
            pov "No, everything you need to know, you already know."
            show pov embarrassed at left
            show mum confused_talk at right
            mum "Hmm... You're not just saying that because you're afraid of what I'll do?"

            menu:
                "Kinda yeah.":
                    #if mum_points >= 1:
                    #    $ mum_points -= 1
                    #    $ renpy.notify("Your relationship with Mom has decreased by 1")
                    #else:
                    #    $ mum_points = 0
                    show pov embarrassed_talk at left
                    show mum angry at right
                    pov "Kinda yeah."
                    show pov sad at left
                    show mum angry_talk at right
                    mum "What did I do to deserve this kind of treatment? I thought we were honest and open with one another."
                "Not at all.":
                    #if mum_points <= 9:
                    #    $ mum_points += 1
                    #    $ renpy.notify("Your relationship with Mom has increased")
                    #else:
                    #    $ mum_points = 10
                    show pov neutral_talk at left
                    show mum confused at right
                    pov "No, not at all."
                    show pov neutral at left
                    show mum confused_talk at right
                    mum "I hope so. I trust you, [povname]."
        "Actually..":
            #if mum_points <= 9:
            #    $ mum_points += 1
            #    $ renpy.notify("Your relationship with Mom has increased")
            #else:
            #    $ mum_points = 10
            show pov embarrassed_talk at left
            show mum confused at right
            pov "Actually, there is something that you should know..."
            show pov embarrassed at left
            show mum confused at right
            mum "Oh? What is it?"

            menu:
                "I have strange feelings for you.":
                    pass
                "I saw a girl drown last night.":
                    pass
                "I went to the hospital last night.":
                    pass
    hide mum confused
    hide mum angry talk
    hide mum confused talk
    show pov embarrassed_talk at left
    show dad neutral at Position(xpos=1300)
    show mum confused at right
    pov "I-"
    show pov bored at left
    show dad neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Oh, hold that thought for just a second."
    mum "Morning, sweetie."
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "Morning, hon."
    show pov confused at left
    show dad neutral_talk at Position(xpos=1300)
    show mum smirk at right
    dad "Last night was a.maz.ing."
    show dad neutral at Position(xpos=1300)
    show mum smirk_talk at right
    mum "Hehe, it really was. Who knew you could still surprise me with new moves after all these years."
    show pov sad at left
    show dad neutral_talk at Position(xpos=1300)
    show mum smirk at right
    dad "Learnt them at work."
    show pov sad at left
    show dad neutral at Position(xpos=1300)
    show mum smirk_talk at right
    mum "One of the best benefits of working there."

    menu:
        "I'm right here.":
            show pov bored_talk at left
            show dad neutral at Position(xpos=1300)
            show mum neutral at right
            pov "I'm right here."
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            show mum neutral at right
            dad "Oh! [povname]! Uhm.. Hey! [povname]. Good morning to you too."
            show pov confused at left
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "S-sorry about that, I.. just... couldn't help but let your mother know how unbelievably beautiful she is."
            show pov bored at left
            show dad neutral at Position(xpos=1300)
            show mum smirk_talk at right
            mum "Oh, stop it. Don't make me rip your clothes off."
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "I love it when you want it now."
            dad "But..."
        "What's going on?":
            show pov confused_talk at left
            show dad neutral at Position(xpos=1300)
            show mum neutral at right
            pov "What's going on?"
            show pov confused at left
            show dad neutral_talk at Position(xpos=1300)
            dad "Oh my God. [povname]! Uh- good morning! Haha... I bet you already know these moves. You kids and your internet porn.. hehe."
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            dad "How could you not have seen someone try them before."
            show pov confused_talk at left
            show dad neutral at Position(xpos=1300)
            show mum confused at right
            pov "Why are you talking to me about this...? It's weird."
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "Oh- don't be like that.. Just because I'm your dad, doesn't mean I can't get in with the new stuff you kids are into these days."
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            dad "No matter how old they are, all these girls deserve to be treated the best way possible."
            show pov confused at left
            show dad neutral at Position(xpos=1300)
            show mum smirk_talk at right
            mum "But I'm the most fuckable, right?"
            show pov angry at left
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "Y-yeah! Of course dear. But don't tell [povname] that. He'll get jealous of me, again."
            show pov bored at left
            show dad neutral at Position(xpos=1300)
            show mum smirk_talk at right
            mum "Don't worry about him, he's behaving. Right, [povname]?"

            menu:
                "Uhh..?":
                    show pov confused_talk at left
                    show dad neutral at Position(xpos=1300)
                    show mum smirk at right
                    pov "Uhhh...?"
                    show pov confused at left
                    show dad neutral at Position(xpos=1300)
                    show mum smirk_talk at right
                    mum "Don't worry about him, boys will be boys."
                "Sure..":
                    show pov confused_talk at left
                    show dad neutral at Position(xpos=1300)
                    show mum smirk at right
                    pov "Sure..."
                    show pov confused at left
                    show dad neutral at Position(xpos=1300)
                    show mum smirk_talk at right
                    mum "See? Only on special occasions."
        "Stay silent":
            show pov angry at left
            show dad neutral at Position(xpos=1300)
            show mum neutral at right
            pov "..."
            show dad neutral_talk at Position(xpos=1300)
            show mum neutral at right
            dad "[povname]? [povname]! Morning, [povname]! How's university going for you? Are they teaching you properly?"
            show pov angry_talk at left
            show dad neutral at Position(xpos=1300)
            pov "I guess so?"
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "Good. Good. Always master the basics because they are the foundations of healthy, active life."
            show pov confused_talk at left
            show dad neutral at Position(xpos=1300)
            pov "W-Wha-?"
            show pov confused at left
            show dad neutral_talk at Position(xpos=1300)
            dad "Isn't that right, hon?"
            show pov bored at left
            show dad neutral at Position(xpos=1300)
            show mum smirk_talk at right
            mum "Listen to your dad, he definitely knows what he's talking about."
    show pov bored at left
    show dad neutral_talk at Position(xpos=1300)
    show mum embarrassed at right
    dad "I've got to head off now, I'm running pretty late."
    show mum smirk at right
    dad "As much as I'd like to have your mom for breakfast. I can't miss work."
    dad "Love you."
    show dad neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Take care today, dear."
    show pov confused at left
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "Have a good day today, [povname]."

    menu:
        "Thanks..":
            if dad_points <= 9:
                $ dad_points += 1
                if winc == 0:
                    $ renpy.notify("Your relationship with [dadname] has increased")
                else:
                    $ renpy.notify("Your relationship with Dad has increased")
            else:
                $ dad_points = 10

            show pov bored_talk at left
            show dad neutral at Position(xpos=1300)
            show mum bored at right
            pov "Thanks, Dad.."
        "Stay silent":
            show pov angry at left
            show dad neutral at Position(xpos=1300)
            show mum bored at right
            pov "..."
    hide dad neutral
    show pov angry at left
    show mum bored_talk at right
    mum "I think it's about time you got to university as well, [povname]."
    show pov angry_talk at left
    show mum bored at right
    pov "Alright, Mom."
    show mum confused at right
    pov "But wait. What the hell is going on?"
    show pov angry at left
    show mum confused_talk at right
    mum "Well, you're going to be late for university if you don't hurry your ass out the door - that's what."
    show pov sad_talk at left
    show mum bored at right
    pov "No, with the whole conversation. Why are you all of a sudden so... y'know."
    show pov angry_talk at left
    show mum embarrassed at right
    pov "And Dad?! What happened to hi-"
    show pov angry at left
    show mum embarrassed_talk at right
    mum "You should've seen him last night, [povname]. He pinned me down so hard and took my breath away."

    menu:
        "I'll see myself out.":
            show pov angry_talk at left
            show mum bored at right
            pov "I'll see myself out."
            show pov angry at left
            show mum embarrassed_talk at right
            mum "Take care, baby. Love you."
            $ main_story = 29
            $ townmap_enabled = 1
            $ renpy.notify("New Objective: Go to University")

            jump lbl_mykitchen_day
        "What is fuck is happening?":
            show pov angry_talk at left
            show mum confused at right
            pov "What the fuck is happening around here."
            show pov angry at left
            show mum smirk_talk at right
            mum "If you come home early, I'll teach you how he did it."
            show pov bored at left
            show mum smirk at right
            pov "..."
            show pov bored_talk at left
            pov "Bye, Mom."
            show pov bored at left
            show mum smirk_talk at right
            mum "Well, aren't you in a rush to get through the day, haha. I love you, baby."
            $ main_story = 29
            $ townmap_enabled = 1
            $ renpy.notify("New Objective: Go to University")

            jump lbl_mykitchen_day

### NO WINC ###
label lbl_a_stranger_morning_winc0:
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Morning, honey."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Morning, [missus]."
    show pov neutral at left
    show mum smirk_talk at right
    mum "Did you get home safe last night? You were out pretty late."
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "Oh, yeah. Sorry about that. I just ran to catch up with someone."
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "Did you get some last night?"
    show pov confused_talk at left
    show mum smirk at right
    pov "Hmm? Sorry?"
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "Did you get some action? Some fun? Y'know, did you get down and dirty?"

    menu:
        "I went to the park.":
            show pov embarrassed_talk at left
            show mum smirk at right
            pov "I just went to the park to meet Effie."
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Though she didn't show up."
            show pov embarrassed at left
            show mum bored_talk at right
            mum "Oh, that's a shame, sorry to hear that. There are plenty of other girls out there to bang."
        "Too much information.":
            #if mum_points >= 1:
            #    $ mum_points -= 1
            #    $ renpy.notify("Your relationship with [missus] has decreased by 1")
            #else:
            #    $ mum_points = 0
            show pov confused_talk at left
            show mum confused at right
            pov "Too much information, [missus]."
            show pov confused at left
            show mum confused_talk at right
            mum "What? I'm just asking if you fucked anyone last night. Sheesh, Mr. Grumpy-Pants."
        "It was eventful.":
            #if mum_points <= 9:
            #    $ mum_points += 1
            #    $ renpy.notify("Your relationship with [missus] has increased")
            #else:
            #    $ mum_points = 10
            show pov embarrassed_talk at left
            show mum neutral at right
            pov "It was eventful, I'll tell you that."
            show pov confused at left
            show mum smirk_talk at right
            mum "Oooh, I'd like to hear the juicy details later, okay?"
    show pov confused_talk at left
    show mum confused at right
    pov "[missus]... are you drunk or something? It's not really something we should talk about."
    show pov confused at left
    show mum confused_talk at right
    mum "What? I'm not drunk, I'm fine. And you're my [povmumrole]. There's nothing in the world that you should hide from me."
    show pov sad at left
    show mum angry_talk at right
    mum "There isn't anything you're hiding from me, is there?"

    menu:
        "No.":
            show pov embarrassed_talk at left
            show mum confused at right
            pov "No, everything you need to know, you already know."
            show pov embarrassed at left
            show mum confused_talk at right
            mum "Hmm... You're not just saying that because you're afraid of what I'll do?"

            menu:
                "Kinda yeah.":
                    #if mum_points >= 1:
                    #    $ mum_points -= 1
                    #    $ renpy.notify("Your relationship with [missus] has decreased by 1")
                    #else:
                    #    $ mum_points = 0
                    show pov embarrassed_talk at left
                    show mum angry at right
                    pov "Kinda yeah."
                    show pov sad at left
                    show mum angry_talk at right
                    mum "What did I do to deserve this kind of treatment? I thought we were honest and open with one another."
                "Not at all.":
                    if mum_points <= 9:
                        $ mum_points += 1
                        $ renpy.notify("Your relationship with [missus] has increased")
                    else:
                        $ mum_points = 10
                    show pov neutral_talk at left
                    show mum confused at right
                    pov "No, not at all."
                    show pov neutral at left
                    show mum confused_talk at right
                    mum "I hope so. I trust you, [povname]."
        "Actually..":
            #if mum_points <= 9:
            #    $ mum_points += 1
            #    $ renpy.notify("Your relationship with [missus] has increased")
            #else:
            #    $ mum_points = 10
            show pov embarrassed_talk at left
            show mum confused at right
            pov "Actually, there is something that you should know..."
            show pov embarrassed at left
            show mum confused at right
            mum "Oh? What is it?"

            menu:
                "I have strange feelings for you.":
                    pass
                "I saw a girl drown last night.":
                    pass
                "I went to the hospital last night.":
                    pass
    hide mum confused
    hide mum angry talk
    hide mum confused talk
    show pov embarrassed_talk at left
    show dad neutral at Position(xpos=1300)
    show mum confused at right
    pov "I-"
    show pov bored at left
    show dad neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Oh, hold that thought for just a second."
    mum "Morning, sweetie."
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "Morning, hon."
    show pov confused at left
    show dad neutral_talk at Position(xpos=1300)
    show mum smirk at right
    dad "Last night was a.maz.ing."
    show dad neutral at Position(xpos=1300)
    show mum smirk_talk at right
    mum "Hehe, it really was. Who knew you could still surprise me with new moves after all these years."
    show pov sad at left
    show dad neutral_talk at Position(xpos=1300)
    show mum smirk at right
    dad "Learnt them at work."
    show pov sad at left
    show dad neutral at Position(xpos=1300)
    show mum smirk_talk at right
    mum "One of the best benefits of working there."

    menu:
        "I'm right here.":
            show pov bored_talk at left
            show dad neutral at Position(xpos=1300)
            show mum neutral at right
            pov "I'm right here."
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            show mum neutral at right
            dad "Oh! [povname]! Uhm.. Hey! [povname]. Good morning to you too."
            show pov confused at left
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "S-sorry about that, I.. just... couldn't help but let your [mumrole] know how unbelievably beautiful she is."
            show pov bored at left
            show dad neutral at Position(xpos=1300)
            show mum smirk_talk at right
            mum "Oh, stop it. Don't make me rip your clothes off."
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "I love it when you want it now."
            dad "But..."
        "What's going on?":
            show pov confused_talk at left
            show dad neutral at Position(xpos=1300)
            show mum neutral at right
            pov "What's going on?"
            show pov confused at left
            show dad neutral_talk at Position(xpos=1300)
            dad "Oh my God. [povname]! Uh- good morning! Haha... I bet you already know these moves. You kids and your internet porn.. hehe."
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            dad "How could you not have seen someone try them before."
            show pov confused_talk at left
            show dad neutral at Position(xpos=1300)
            show mum confused at right
            pov "Why are you talking to me about this...? It's weird."
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "Oh- don't be like that.. Just because I'm your [povdadrole], doesn't mean I can't get in with the new stuff you kids are into these days."
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            dad "No matter how old they are, all these girls deserve to be treated the best way possible."
            show pov confused at left
            show dad neutral at Position(xpos=1300)
            show mum smirk_talk at right
            mum "But I'm the most fuckable, right?"
            show pov angry at left
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "Y-yeah! Of course dear. But don't tell [povname] that. He'll get jealous of me, again."
            show pov bored at left
            show dad neutral at Position(xpos=1300)
            show mum smirk_talk at right
            mum "Don't worry about him, he's behaving. Right, [povname]?"

            menu:
                "Uhh..?":
                    show pov confused_talk at left
                    show dad neutral at Position(xpos=1300)
                    show mum smirk at right
                    pov "Uhhh...?"
                    show pov confused at left
                    show dad neutral at Position(xpos=1300)
                    show mum smirk_talk at right
                    mum "Don't worry about him, boys will be boys."
                "Sure..":
                    show pov confused_talk at left
                    show dad neutral at Position(xpos=1300)
                    show mum smirk at right
                    pov "Sure..."
                    show pov confused at left
                    show dad neutral at Position(xpos=1300)
                    show mum smirk_talk at right
                    mum "See? Only on special occasions."
        "Stay silent":
            show pov angry at left
            show dad neutral at Position(xpos=1300)
            show mum neutral at right
            pov "..."
            show dad neutral_talk at Position(xpos=1300)
            show mum neutral at right
            dad "[povname]? [povname]! Morning, [povname]! How's university going for you? Are they teaching you properly?"
            show pov angry_talk at left
            show dad neutral at Position(xpos=1300)
            pov "I guess so?"
            show pov bored at left
            show dad neutral_talk at Position(xpos=1300)
            show mum smirk at right
            dad "Good. Good. Always master the basics because they are the foundations of healthy, active life."
            show pov confused_talk at left
            show dad neutral at Position(xpos=1300)
            pov "W-Wha-?"
            show pov confused at left
            show dad neutral_talk at Position(xpos=1300)
            dad "Isn't that right, hon?"
            show pov bored at left
            show dad neutral at Position(xpos=1300)
            show mum smirk_talk at right
            mum "Listen to your [povdadrole], he definitely knows what he's talking about."
    show pov bored at left
    show dad neutral_talk at Position(xpos=1300)
    show mum embarrassed at right
    dad "I've got to head off now, I'm running pretty late."
    show mum smirk at right
    dad "As much as I'd like to have your [mumrole] for breakfast. I can't miss work."
    dad "Love you."
    show dad neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Take care today, dear."
    show pov confused at left
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "Have a good day today, [povname]."

    menu:
        "Thanks..":
            if dad_points <= 9:
                $ dad_points += 1
                $ renpy.notify("Your relationship with Dad has increased")
            else:
                $ dad_points = 10
            show pov bored_talk at left
            show dad neutral at Position(xpos=1300)
            show mum bored at right
            pov "Thanks, [dadname].."
        "Stay silent":
            show pov angry at left
            show dad neutral at Position(xpos=1300)
            show mum bored at right
            pov "..."
    hide dad neutral
    show pov angry at left
    show mum bored_talk at right
    mum "I think it's about time you got to university as well, [povname]."
    show pov angry_talk at left
    show mum bored at right
    pov "Alright, [missus]."
    show mum confused at right
    pov "But wait. What the hell is going on?"
    show pov angry at left
    show mum confused_talk at right
    mum "Well, you're going to be late for university if you don't hurry your ass out the door - that's what."
    show pov sad_talk at left
    show mum bored at right
    pov "No, with the whole conversation. Why are you all of a sudden so... y'know."
    show pov angry_talk at left
    show mum embarrassed at right
    pov "And [dadname]?! What happened to hi-"
    show pov angry at left
    show mum embarrassed_talk at right
    mum "You should've seen him last night, [povname]. He pinned me down so hard and took my breath away."

    menu:
        "I'll see myself out.":
            show pov angry_talk at left
            show mum bored at right
            pov "I'll see myself out."
            show pov angry at left
            show mum embarrassed_talk at right
            mum "Take care, baby. Love you."
            $ main_story = 29
            $ townmap_enabled = 1
            $ renpy.notify("New Objective: Go to University")

            jump lbl_mykitchen_day
        "What is fuck is happening?":
            show pov angry_talk at left
            show mum confused at right
            pov "What the fuck is happening around here."
            show pov angry at left
            show mum smirk_talk at right
            mum "If you come home early, I'll teach you how he did it."
            show pov bored at left
            show mum smirk at right
            pov "..."
            show pov bored_talk at left
            pov "Bye, [missus]."
            show pov bored at left
            show mum smirk_talk at right
            mum "Well, aren't you in a rush to get through the day, haha. I love you, baby."
            $ main_story = 29
            $ townmap_enabled = 1
            $ renpy.notify("New Objective: Go to University")

            jump lbl_mykitchen_day
