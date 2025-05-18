## Mom Stay With Me ##
label lbl_mom_stay_with_me:
    if winc == 0:
        jump lbl_mom_stay_with_me_winc0
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Morning, honey. How was your sleep?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was good. Yours?"
    show pov neutral at left
    show mum bored_talk at right
    mum "Mine was good."
    if momfallenasleep_kiss == 1:
        show mum confused_talk at right
        mum "What happened last night?"

        menu:
            "You got drunk.":
                show pov neutral_talk at left
                show mum smirk at right
                pov "You got drunk."
                show pov neutral at left
                show mum smirk_talk at right
                mum "Oh, did I now? Hehehe... sorry about that. That must've been an embarrassing sight."
                show pov smirk_talk at left
                show mum smirk at right
                pov "Nope, not one little bit."
                show pov neutral at left
                show mum neutral_talk at right
                mum "Hmmm, good boy. Thank you for doing as I asked."
            "We cuddled on the sofa and talked.":
                show pov neutral_talk at left
                show mum neutral at right
                pov "We cuddled on the sofa and talked."
                show pov neutral at left
                show mum smirk_talk at right
                mum "Oh, did we? That sounded like an amazing night."
                show pov neutral_talk at left
                show mum smirk at right
                pov "It actually was. I'm glad I came downstairs."
                show pov bored at left
                show mum smirk_talk at right
                mum "Um... did you... you... ‘came downstairs'."
                show pov sad_talk at left
                show mum smirk at right
                pov "No, no! Mom! Why do you have to turn that into something lewd."
                show pov embarrassed at left
                show mum neutral_talk at right
                mum "Shhh, I'm only joking. Hahaha!"
            "Nothing much.":
                show pov neutral_talk at left
                show mum confused at right
                pov "Nothing much."
                show pov bored at left
                show mum confused_talk at right
                mum "Really? I could've sworn that we did something on the sofa."
                show pov bored_talk at left
                show mum confused at right
                pov "Um..."
                show pov neutral at left
                show mum confused_talk at right
                mum "We cuddled and talked, duh."
                show pov shocked_talk at left
                show mum confused at right
                pov "Oh! Right."
                show pov embarrassed at left
                show mum confused_talk at right
                mum "Did you forget or something?"
                show pov embarrassed_talk at left
                show mum smirk at right
                pov "I just... didn't think it was necessary to bring it up."
                show pov embarrassed at left
                show mum embarrassed_talk at right
                mum "I guess it's not. I just wanted to make sure that it wasn't a dream."
                show pov smirk_talk at left
                show mum embarrassed at right
                pov "And if it was?"
                show pov smirk at left
                show mum embarrassed_talk at right
                mum "Then you'd be looking at me like a stranger."
                mum "You're no stranger to me, are you, [povname]?"
                show pov smirk_talk at left
                show mum neutral at right
                pov "Nope."
                show pov neutral at left
                show mum smirk_talk at right
                mum "Good."

    elif momfallenasleep_kiss == 0 and momfallenasleep_goodbye == 1:
        show pov embarrassed at left
        show mum neutral_talk at right
        mum "Thanks for waking me up to cuddle last night."
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "I enjoyed every bit of it."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "Me too, honey. You really did turn my day upside down when I saw you watching over me in the livingroom."
        show mum neutral_talk at right
        mum "Like an angel in the blue sky."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Jeez, Mom. How much cheese did you eat with that statement."
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Hahaha, enough to make you want to hide into a ball."
    elif momfallenasleep_kiss == 0 and momfallenasleep_goodbye == 0:
        show pov embarrassed at left
        show mum bored_talk at right
        mum "I'm just gonna come right out and say this but let's just pretend last night didn't happen. Okay?"
        show pov sad_talk at left
        show mum bored at right
        pov "I'm... sorry I said what I said."
        show pov sad at left
        show mum bored_talk at right
        mum "No. Let's just pretend it didn't happen."
        show pov sad at left
        show mum bored at right
        pov "..."
        show pov embarrassed_talk at left
        show mum bored at right
        pov "Alright..."
        show pov sad at left
        show mum bored_talk at right
        mum "I thought we could bond together for the little time we have before you leave for college but I guess last night was not the night for that."
        show pov sad_talk at left
        show mum sad at right
        pov "Mom..."
        show pov embarrassed at left
        show mum sad_talk at right
        mum "[povname]. As your mother, can you please grant me this one request?"
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "..."
    show pov confused at left
    show mum embarrassed_talk at right
    mum "I was wondering if you could stay home this afternoon?"
    show pov confused_talk at left
    show mum embarrassed at right
    pov "Why?"
    show pov confused at left
    show mum embarrassed_talk at right
    mum "I want you to stay with me in the living room for the rest of the day."
    mum "Just uh... some mother-son time together?"
    mum "We could watch a movie, talk, whatever you want."

    menu:
        "Sure, we can do that.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show pov neutral_talk at left
            show mum neutral at right
            pov "Sure, we can do that."
            show pov neutral at left
            show mum neutral_talk at right
            mum "Yay! I can't wait. Thank you, honey. I love you so much."
            show pov neutral_talk at left
            show mum neutral at right
            pov "Hehe, I love you too, Mom."
            show pov neutral at left
            show mum smirk_talk at right
            mum "Don't forget okay?"
            show pov neutral_talk at left
            show mum neutral at right
            pov "I won't."
        "I'm busy today, how about tomorrow?":
            show pov confused_talk at left
            show mum bored at right
            pov "I'm actually a little busy today. How about tomorrow?"
            show pov confused at left
            mum "..."
            show pov sad at left
            show mum bored_talk at right
            mum "I was actually hoping today? You can do what you want tomorrow."
            mum "You're still a teenager but also as an adult, you need to start getting your priorities straight, okay?"
            show pov sad_talk at left
            show mum bored at right
            pov "Okay..?"
            show pov sad at left
            show mum confused_talk at right
            mum "What's more important? Your own mother, or whatever other crap going on in your life?"

            menu:
                "You are.":
                    if mum_points <= 9:
                        $ mum_points += 1
                        $ renpy.notify("Your relationship with Mom has increased")
                    else:
                        $ mum_points = 10
                    show pov embarrassed_talk at left
                    show mum smirk at right
                    pov "You are."
                    show pov embarrassed at left
                    show mum smirk_talk at right
                    mum "Good boy. I raised you so well."
                    show mum bored_talk at right
                    mum "Don't you dare forget. Mother-son time starts before the sun sets."
                    show mum angry_talk at right
                    mum "Got it?"
                    show pov embarrassed_talk at left
                    show mum neutral at right
                    pov "Yes, Mom."
                "Other things.":
                    show pov sad_talk at left
                    show mum angry at right
                    pov "Other things, Mom."
                    show pov sad at left
                    mum "..."
                    show pov sad at left
                    show mum angry_talk at right
                    mum "You want to rethink your answer?"

                    menu:
                        "I mean you.":
                            show pov embarrassed_talk at left
                            show mum angry at right
                            pov "I mean... you, of course you."
                            show pov sad at left
                            show mum angry_talk at right
                            mum "It better be."
                            show mum bored_talk at right
                            mum "Anyways, don't forget; mother-son time starts before the sun sets."
                            show mum angry_talk at right
                            mum "Got it?"
                            show pov embarrassed_talk at left
                            show mum smirk at right
                            pov "Yes, Mom."
                        "No.":
                            if mum_points >= 1:
                                $ mum_points -= 1
                                $ renpy.notify("Your relationship with Mom has decreased")
                            else:
                                $ mum_points = 0
                            show pov angry_talk at left
                            show mum angry at right
                            pov "No, I'm standing by my decision."
                            show pov angry at left
                            show mum bored_talk at right
                            mum "Fine. You've made your choice."
                            show pov sad at left
                            show mum sad_talk at right
                            mum "Just forget about it. Go and live your life."
                            show pov sad_talk at left
                            show mum angry at right
                            pov "I still care abou-"
                            show pov shocked at left
                            show mum angry_talk at right
                            mum "Shut up, [povname]. I don't wanna hear another word from you."
                            $ mompastsunset_attend = 2
        "Sorry, I can't.":
            show pov embarrassed_talk at left
            show mum bored at right
            pov "Sorry, I can't. I've got other things to attend to."
            mum "..."
            show pov sad at left
            show mum bored_talk at right
            mum "That's it? You're not gonna try and reschedule your other plans?"
            show pov embarrassed_talk at left
            show mum bored at right
            pov "I could try to..."
            show pov sad at left
            show mum bored_talk at right
            mum "No, don't worry about it. Just forget I even mentioned this."
            show pov sad_talk at left
            show mum angry at right
            pov "Why are you mad at me all of a sudde-"
            show pov sad at left
            show mum angry_talk at right
            mum "You don't get it do you? You don't get how important this is for me."
            show pov embarrassed_talk at left
            show mum angry at right
            pov "I can try to understa-"
            show pov sad at left
            show mum angry_talk at right
            mum "Shut up, [povname]. Not another word from you."
            $ mompastsunset_attend = 2

    $ mum_path = 6
    $ townmap_enabled = 1

    jump lbl_mykitchen_day

### NO WINC ###
label lbl_mom_stay_with_me_winc0:
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Morning, honey. How was your sleep?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was good. Yours?"
    show pov neutral at left
    show mum bored_talk at right
    mum "Mine was good."
    if momfallenasleep_kiss == 1:
        show mum confused_talk at right
        mum "What happened last night?"

        menu:
            "You got drunk.":
                show pov neutral_talk at left
                show mum smirk at right
                pov "You got drunk."
                show pov neutral at left
                show mum smirk_talk at right
                mum "Oh, did I now? Hehehe... sorry about that. That must've been an embarrassing sight."
                show pov smirk_talk at left
                show mum smirk at right
                pov "Nope, not one little bit."
                show pov neutral at left
                show mum neutral_talk at right
                mum "Hmmm, good boy. Thank you for doing as I asked."
            "We cuddled on the sofa and talked.":
                show pov neutral_talk at left
                show mum neutral at right
                pov "We cuddled on the sofa and talked."
                show pov neutral at left
                show mum smirk_talk at right
                mum "Oh, did we? That sounded like an amazing night."
                show pov neutral_talk at left
                show mum smirk at right
                pov "It actually was. I'm glad I came downstairs."
                show pov bored at left
                show mum smirk_talk at right
                mum "Um... did you... you... ‘came downstairs'."
                show pov sad_talk at left
                show mum smirk at right
                pov "No, no! [missus]! Why do you have to turn that into something lewd."
                show pov embarrassed at left
                show mum neutral_talk at right
                mum "Shhh, I'm only joking. Hahaha!"
            "Nothing much.":
                show pov neutral_talk at left
                show mum confused at right
                pov "Nothing much."
                show pov bored at left
                show mum confused_talk at right
                mum "Really? I could've sworn that we did something on the sofa."
                show pov bored_talk at left
                show mum confused at right
                pov "Um..."
                show pov neutral at left
                show mum confused_talk at right
                mum "We cuddled and talked, duh."
                show pov shocked_talk at left
                show mum confused at right
                pov "Oh! Right."
                show pov embarrassed at left
                show mum confused_talk at right
                mum "Did you forget or something?"
                show pov embarrassed_talk at left
                show mum smirk at right
                pov "I just... didn't think it was necessary to bring it up."
                show pov embarrassed at left
                show mum embarrassed_talk at right
                mum "I guess it's not. I just wanted to make sure that it wasn't a dream."
                show pov smirk_talk at left
                show mum embarrassed at right
                pov "And if it was?"
                show pov smirk at left
                show mum embarrassed_talk at right
                mum "Then you'd be looking at me like a stranger."
                mum "You're no stranger to me, are you, [povname]?"
                show pov smirk_talk at left
                show mum neutral at right
                pov "Nope."
                show pov neutral at left
                show mum smirk_talk at right
                mum "Good."
    elif momfallenasleep_kiss == 0 and momfallenasleep_goodbye == 1:
        show pov embarrassed at left
        show mum neutral_talk at right
        mum "Thanks for waking me up to cuddle last night."
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "I enjoyed every bit of it."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "Me too, honey. You really did turn my day upside down when I saw you watching over me in the livingroom."
        show mum neutral_talk at right
        mum "Like an angel in the blue sky."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Jeez, [missus]. How much cheese did you eat with that statement."
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Hahaha, enough to make you want to hide into a ball."
    elif momfallenasleep_kiss == 0 and momfallenasleep_goodbye == 0:
        show pov embarrassed at left
        show mum bored_talk at right
        mum "I'm just gonna come right out and say this but let's just pretend last night didn't happen. Okay?"
        show pov sad_talk at left
        show mum bored at right
        pov "I'm... sorry I said what I said."
        show pov sad at left
        show mum bored_talk at right
        mum "No. Let's just pretend it didn't happen."
        show pov sad at left
        show mum bored at right
        pov "..."
        show pov embarrassed_talk at left
        show mum bored at right
        pov "Alright..."
        show pov sad at left
        show mum bored_talk at right
        mum "I thought we could bond together for the little time we have before you leave for college but I guess last night was not the night for that."
        show pov sad_talk at left
        show mum sad at right
        pov "[missus]..."
        show pov embarrassed at left
        show mum sad_talk at right
        mum "[povname]. As your [mumrole], can you please grant me this one request?"
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "..."
    show pov confused at left
    show mum embarrassed_talk at right
    mum "I was wondering if you could stay home this afternoon?"
    show pov confused_talk at left
    show mum embarrassed at right
    pov "Why?"
    show pov confused at left
    show mum embarrassed_talk at right
    mum "I want you to stay with me in the living room for the rest of the day."
    mum "Just uh... some [mumrole]-[povmumrole] time together?"
    mum "We could watch a movie, talk, whatever you want."

    menu:
        "Sure, we can do that.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show pov neutral_talk at left
            show mum neutral at right
            pov "Sure, we can do that."
            show pov neutral at left
            show mum neutral_talk at right
            mum "Yay! I can't wait. Thank you, honey. I love you so much."
            show pov neutral_talk at left
            show mum neutral at right
            pov "Hehe, I love you too, [missus]."
            show pov neutral at left
            show mum smirk_talk at right
            mum "Don't forget okay?"
            show pov neutral_talk at left
            show mum neutral at right
            pov "I won't."
        "I'm busy today, how about tomorrow?":
            show pov confused_talk at left
            show mum bored at right
            pov "I'm actually a little busy today. How about tomorrow?"
            show pov confused at left
            mum "..."
            show pov sad at left
            show mum bored_talk at right
            mum "I was actually hoping today? You can do what you want tomorrow."
            mum "You're still a teenager but also as an adult, you need to start getting your priorities straight, okay?"
            show pov sad_talk at left
            show mum bored at right
            pov "Okay..?"
            show pov sad at left
            show mum confused_talk at right
            mum "What's more important? Your own [mumrole], or whatever other crap going on in your life?"

            menu:
                "You are.":
                    if mum_points <= 9:
                        $ mum_points += 1
                        $ renpy.notify("Your relationship with [missus] has increased")
                    else:
                        $ mum_points = 10
                    show pov embarrassed_talk at left
                    show mum smirk at right
                    pov "You are."
                    show pov embarrassed at left
                    show mum smirk_talk at right
                    mum "Good boy. I raised you so well."
                    show mum bored_talk at right
                    mum "Don't you dare forget. [mumrole]-[povmumrole] time starts before the sun sets."
                    show mum angry_talk at right
                    mum "Got it?"
                    show pov embarrassed_talk at left
                    show mum neutral at right
                    pov "Yes, [missus]."
                "Other things.":
                    show pov sad_talk at left
                    show mum angry at right
                    pov "Other things, [missus]."
                    show pov sad at left
                    mum "..."
                    show pov sad at left
                    show mum angry_talk at right
                    mum "You want to rethink your answer?"

                    menu:
                        "I mean you.":
                            show pov embarrassed_talk at left
                            show mum angry at right
                            pov "I mean... you, of course you."
                            show pov sad at left
                            show mum angry_talk at right
                            mum "It better be."
                            show mum bored_talk at right
                            mum "Anyways, don't forget; [mumrole]-[povmumrole] time starts before the sun sets."
                            show mum angry_talk at right
                            mum "Got it?"
                            show pov embarrassed_talk at left
                            show mum smirk at right
                            pov "Yes, [missus]."
                        "No.":
                            if mum_points >= 1:
                                $ mum_points -= 1
                                $ renpy.notify("Your relationship with [missus] has decreased")
                            else:
                                $ mum_points = 0
                            show pov angry_talk at left
                            show mum angry at right
                            pov "No, I'm standing by my decision."
                            show pov angry at left
                            show mum bored_talk at right
                            mum "Fine. You've made your choice."
                            show pov sad at left
                            show mum sad_talk at right
                            mum "Just forget about it. Go and live your life."
                            show pov sad_talk at left
                            show mum angry at right
                            pov "I still care abou-"
                            show pov shocked at left
                            show mum angry_talk at right
                            mum "Shut up, [povname]. I don't wanna hear another word from you."
                            $ mompastsunset_attend = 2
        "Sorry, I can't.":
            show pov embarrassed_talk at left
            show mum bored at right
            pov "Sorry, I can't. I've got other things to attend to."
            mum "..."
            show pov sad at left
            show mum bored_talk at right
            mum "That's it? You're not gonna try and reschedule your other plans?"
            show pov embarrassed_talk at left
            show mum bored at right
            pov "I could try to..."
            show pov sad at left
            show mum bored_talk at right
            mum "No, don't worry about it. Just forget I even mentioned this."
            show pov sad_talk at left
            show mum angry at right
            pov "Why are you mad at me all of a sudde-"
            show pov sad at left
            show mum angry_talk at right
            mum "You don't get it do you? You don't get how important this is for me."
            show pov embarrassed_talk at left
            show mum angry at right
            pov "I can try to understa-"
            show pov sad at left
            show mum angry_talk at right
            mum "Shut up, [povname]. Not another word from you."
            $ mompastsunset_attend = 2
    $ mum_path = 6
    $ townmap_enabled = 1

    jump lbl_mykitchen_day
