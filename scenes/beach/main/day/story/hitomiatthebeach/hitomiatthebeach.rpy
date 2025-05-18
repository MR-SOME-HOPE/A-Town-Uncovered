## Hitomi At The Beach ##
## GEESEKI NOTE: THIS SECTION OF THE GAME HAS A MORE THAN GOOD CHANCE OF BEING REMOVED LATER.
label lbl_hitomibeach_1_0:
    ## Hitomi Beach Choices
    $ hitomibeach_understandthat = 0
    $ hitomibeach_tryitonce = 0
    $ hitomibeach_takenoff = 0
    $ hitomibeach_littletan = 0
    $ hitomibeach_bondingexperience = 0
    $ hitomibeach_findthenerve = 0
    $ hitomibeach_contradicting = 0
    $ hitomibeach_youre50 = 0
    $ hitomibeach_livealittle = 0
    $ hitomibeach_stareatyou = 0
    $ hitomibeach_safeplace = 0
    $ hitomibeach_completelynormal = 0
    $ hitomibeach_yoursenses = 0
    $ hitomibeach_meneither = 0
    $ hitomibeach_beautifulday = 0
    $ hitomibeach_stayingornot = 0
    $ hitomibeach_staywithyou = 0
    $ hitomibeach_passingby = 0
    $ hitomibeach_beacharound = 0
    $ hitomibeach_staysinrome = 0
    $ hitomibeach_tryit = 0
    $ hitomibeach_stripdown = 0
    $ hitomibeach_walkaround = 0
    $ hitomibeach_halfnaked = 0
    show pov neutral_talk at left
    with dissolve
    show hit embarrassed at right
    with dissolve
    pov "Hey, Hitomi! how's it going?"
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "Hey, [povname]. I'm doing good. What brings you here?"
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "I was about to ask you the same thing - just thought I'd drop by and see what's new."
    show pov confused_talk at left
    pov "Who's running the store?"
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "Oh, I asked Kev to 'watch over our kingdom' for me, while I'm on break."
    show hit neutral_talk at right
    hit "Since it's such a beautiful day today; I thought I'd visit the beach today."
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "Haha, yeah. I like coming here often. First time I came, the lifeguard called me out for wearing clothes so..."
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "Yeah.. about that. I'm a bit.. well... I'm not really used to being naked in public."
    $ hitomi_path = 2

    jump lbl_hitomibeach_1_menu

label lbl_hitomibeach_1_1:
    show pov neutral_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    pov "Hey Hitomi. Nice seeing you here again."
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "Yeah, well. I do work just up the hill; so it never hurts to stop by and get some vitamin D."
    show pov smirk_talk at left
    show hit bored at right
    pov "Vitamin D?"
    show pov smirk at left
    show hit embarrassed_talk at right
    hit "...ANYWAY."
    show pov neutral at left
    hit "I figured, coming here would help me face my fear of public nudity. I'm still not used to it."

    jump lbl_hitomibeach_1_menu

label lbl_hitomibeach_1_menu:

    menu:
        "I can understand that." if hitomibeach_understandthat == 0:
            show pov neutral_talk at left
            show hit embarrassed at right
            pov "I can understand that; it's not necessarily everyone's cup of tea."
            pov "But it's not that bad, I promise."
            show pov embarrassed at left
            show hit embarrassed_talk at right
            hit "I don't know.."

            menu:
                "Try it once." if hitomibeach_tryitonce == 0:
                    show pov neutral_talk at left
                    show hit embarrassed at right
                    pov "Just try it once - maybe you'll find a freeing feeling that you've never felt before."
                    show pov embarrassed at left
                    show hit embarrassed_talk at right
                    hit "I believe that it's definitely a freeing feeling, but that's what clothes are made for."
                    hit "To restrict us and protect our bodies."

                    menu:
                        "Clothes are made to be taken off." if hitomibeach_takenoff == 0:
                            show pov neutral_talk at left
                            show hit embarrassed at right
                            pov "Just like rules, clothes are made to be taken off."
                            show pov embarrassed at left
                            show hit embarrassed_talk at right
                            hit "When no one's looking, [povname]."
                            $ hitomibeach_takenoff = 1

                            jump lbl_hitomibeach_1_end
                        "You would do good with a little tan." if hitomibeach_littletan == 0:
                            show pov neutral_talk at left
                            show hit embarrassed at right
                            pov "You're quite pale-toned. A little tan would make you look really nice."
                            show pov embarrassed at left
                            show hit bored_talk at right
                            hit "I don't really like that tan look on me. I think I look cuter without it."
                            show hit embarrassed_talk at right
                            hit "Nothing against those who do prefer a tan. I'm just sayin."
                            show pov embarrassed_talk at left
                            show hit embarrassed at right
                            pov "No don't worry. I got ya."
                            $ hitomibeach_littletan = 1

                            jump lbl_hitomibeach_1_end
                        "Think of it as a bonding experience." if hitomibeach_bondingexperience == 0:
                            show pov neutral_talk at left
                            show hit bored at right
                            pov "Think of it as a bonding expeirence between us: It'll bring us closer."
                            show pov neutral at left
                            show hit neutral_talk at right
                            hit "You know what? Now that you say that, I think I will!"
                            show pov neutral_talk at left
                            show hit neutral at right
                            pov "Really?!"
                            show pov sad at left
                            show hit angry_talk at right
                            hit "No you fucking pervert."
                            if hitomi_points >= 1:
                                $ hitomi_points -= 1
                            else:
                                $ hitomi_points = 0
                            $ renpy.notify("Your relationship with Hitomi has decreased")
                            $ hitomibeach_bondingexperience = 1

                            jump lbl_hitomibeach_1_end_2
                "Maybe next time you'll find the nerve to do it." if hitomibeach_findthenerve == 0:
                    show pov embarrassed_talk at left
                    show hit embarrassed at right
                    pov "It's alright, maybe next time you'll find the nerve to run nude."
                    show pov embarrassed at left
                    show hit bored_talk at right
                    hit "Maybe. But you do know that I can potentially put this off indefinitely."

                    menu:
                        "You're contradicting yourself." if hitomibeach_contradicting == 0:
                            show pov neutral_talk at left
                            show hit bored at right
                            pov "There! You're contradicting yourself!"
                            show pov smirk_talk at left
                            show hit embarrassed at right
                            pov "Somewhere deep inside you, you do want to do it."
                            show pov bored at left
                            show hit bored_talk at right
                            hit "Trust me, I wish I could go on a killing spree, but something inside my head is telling me 'no'."
                            $ hitomibeach_contradicting = 1

                            jump lbl_hitomibeach_1_end
                        "You'll regret this when you're 50." if hitomibeach_youre50 == 0:
                            show pov embarrassed_talk at left
                            show hit bored at right
                            pov "You'll regret it when you're 50."
                            show pov smirk_talk at left
                            pov "You're young and this is the only time you'll have the sexiest body to flaunt."
                            show pov neutral at left
                            show hit neutral_talk at right
                            hit "You know what? Now that you say that, I think I will!"
                            show pov neutral_talk at left
                            show hit neutral at right
                            pov "Really?!"
                            show pov sad at left
                            show hit angry_talk at right
                            hit "No you fucking pervert."
                            if hitomi_points >= 1:
                                $ hitomi_points -= 1
                            else:
                                $ hitomi_points = 0
                            $ renpy.notify("Your relationship with Hitomi has decreased")
                            $ hitomibeach_youre50 = 1

                            jump lbl_hitomibeach_1_end_2
                        "Live a little." if hitomibeach_livealittle == 0:
                            show pov smirk_talk at left
                            show hit bored at right
                            pov "Hey, just live a little."
                            show pov embarrassed at left
                            show hit angry_talk at right
                            hit "For you to say that choosing not to strip down isn't living is.. just.."
                            show pov sad at left
                            hit "Why don't you get a life pervert."
                            if hitomi_points >= 1:
                                $ hitomi_points -= 1
                            else:
                                $ hitomi_points = 0
                            $ renpy.notify("Your relationship with Hitomi has decreased")
                            $ hitomibeach_livealittle = 1

                            jump lbl_hitomibeach_1_end_2
                "No one will stare at you." if hitomibeach_stareatyou == 0:
                    show pov embarrassed_talk at left
                    show hit embarrassed at right
                    pov "Everyone's naked, no one will stare at you."
                    show pov neutral at left
                    show hit embarrassed_talk at right
                    hit "I guess that is the case of if everyone's doing it, it becomes the norm."

                    menu:
                        "This is a safe place to be naked." if hitomibeach_safeplace == 0:
                            show pov neutral_talk at left
                            show hit embarrassed at right
                            pov "This is a safe place to be naked; everyone respects each other's boundaries."
                            show pov neutral at left
                            show hit embarrassed_talk at right
                            hit "How safe is it though.."
                            show pov neutral_talk at left
                            show hit sad at right
                            pov "Extremely safe, there's a single lifeguard and many guys around to protect you if something happens."
                            show pov embarrassed at left
                            show hit sad_talk at right
                            hit "Uh.... on second thought."
                            $ hitomibeach_safeplace = 1

                            jump lbl_hitomibeach_1_end
                        "Exactly, completely normal." if hitomibeach_completelynormal == 0:
                            show pov neutral_talk at left
                            show hit embarrassed at right
                            pov "Exactly, completely normal, nothing unethical here."
                            show pov confused at left
                            show hit bored_talk at right
                            hit "[povname], so was slavery may I say in a dark turn."
                            show pov confused_talk at left
                            show hit bored at right
                            pov "Jesus, Hitomi. Didn't see that coming."
                            $ hitomibeach_completelynormal = 1

                            jump lbl_hitomibeach_1_end
                        "Now you're coming along to your senses." if hitomibeach_yoursenses == 0:
                            show pov neutral_talk at left
                            show hit bored at right
                            pov "Now you're coming to your senses."
                            show pov embarrassed at left
                            show hit confused_talk at right
                            hit "Wait, so what I said earlier about not wanting to do it meant that I was being stupid?"
                            show pov sad_talk at left
                            show hit angry at right
                            pov "What... no? I didn't mean it lik-"
                            show pov sad at left
                            show hit angry_talk at right
                            hit "Save it, [povname]."
                            if hitomi_points >= 1:
                                $ hitomi_points -= 1
                            else:
                                $ hitomi_points = 0
                            $ renpy.notify("Your relationship with Hitomi has decreased")
                            $ hitomibeach_yoursense = 1

                            jump lbl_hitomibeach_1_end_2
        "Don't worry, me neither." if hitomibeach_meneither == 0:
            show pov embarrassed_talk at left
            show hit embarrassed at right
            pov "Don't worry, I don't like getting naked in public either."
            show pov embarrassed at left
            show hit smirk_talk at right
            hit "Then why are you here...?"

            menu:
                "It's a beautiful day." if hitomibeach_beautifulday == 0:
                    show pov neutral_talk at left
                    show hit neutral at right
                    pov "Like you said earlier, it's a beautiful day to visit the beach."
                    show pov neutral at left
                    show hit confused_talk at right
                    hit "Are you going to stay long or are you just stopping by?"

                    menu:
                        "Depends on whether you're staying or not." if hitomibeach_stayingornot == 0:
                            show pov neutral_talk at left
                            show hit neutral at right
                            pov "It depends on whether you're staying or not."
                            pov "If you're not staying than I don't really have a reason to stay myself."
                            show pov neutral at left
                            show hit embarrassed_talk at right
                            hit "Well, aren't you a sweet one."
                            show pov embarrassed at left
                            hit "I'm actually kind of embarrassed that you're here all of a sudden because I didn't think I'd see anyone I knew here."
                            show pov embarrassed_talk at left
                            show hit embarrassed at right
                            pov "I'll go if you want. I don't want to push you."
                            show pov embarrassed at left
                            show hit embarrassed_talk at right
                            hit "Yeah, I'll actually be heading back myself. See you, [povname]."
                            if hitomi_points >= 1:
                                $ hitomi_points -= 1
                            else:
                                $ hitomi_points = 0
                            $ renpy.notify("Your relationship with Hitomi has decreased")
                            $ hitomibeach_stayingornot = 1

                            jump lbl_hitomibeach_1_end_2
                        "Do you want me to stay with you?" if hitomibeach_staywithyou == 0:
                            show pov neutral_talk at left
                            show hit embarrassed at right
                            pov "Do you want me to stay with you? Keep you company."
                            show pov embarrassed at left
                            show hit embarrassed_talk at right
                            hit "Well actually, I'm shyer now that you're here. I didn't think I'd see anyone I knew here."
                            show pov embarrassed_talk at left
                            show hit embarrassed at right
                            pov "I'll go if you want - I don't want to push you."
                            show pov embarrassed at left
                            show hit embarrassed_talk at right
                            hit "Yeah, I'll actually be heading back myself. See you, [povname]."
                            if hitomi_points >= 1:
                                $ hitomi_points -= 1
                            else:
                                $ hitomi_points = 0
                            $ renpy.notify("Your relationship with Hitomi has decreased")
                            $ hitomibeach_staywithyou = 1

                            jump lbl_hitomibeach_1_end_2
                        "I'm just passing by." if hitomibeach_passingby == 0:
                            show pov neutral_talk at left
                            show hit neutral at right
                            pov "I'm just passing by here. I'll be off now."
                            show pov neutral at left
                            show hit neutral_talk at right
                            hit "Oh, alright, I'll see you around Hendai's sometime."
                            if hitomi_points >= 1:
                                $ hitomi_points -= 1
                            else:
                                $ hitomi_points = 0
                            $ renpy.notify("Your relationship with Hitomi has decreased")
                            $ hitomibeach_passingby = 1

                            jump lbl_hitomibeach_1_end_2
                "It's the only beach around." if hitomibeach_beacharound == 0:
                    show pov embarrassed_talk at left
                    show hit neutral at right
                    pov "It's the only beach around. It just happens to also be a nudist beach."
                    show pov embarrassed at left
                    show hit embarrassed_talk at right
                    hit "Yeah, it's a shame isn't it. Not all of us are okay with stripping down."
                    show pov embarrassed_talk at left
                    show hit embarrassed at right
                    pov "Totally. Although..."

                    menu:
                        "What happens in Rome, stays in Rome." if hitomibeach_staysinrome == 0:
                            show pov neutral_talk at left
                            show hit bored at right
                            pov "What happens in Rome, stays in Rome. As the saying goes."
                            show pov neutral at left
                            show hit bored_talk at right
                            hit "We're not in Rome."
                            show pov neutral_talk at left
                            show hit neutral at right
                            pov "You know what I mean."
                            show pov neutral at left
                            show hit confused_talk at right
                            hit "Y'know, I never quite understood what that meant. What did they do in Rome that stayed there?"
                            show pov smirk_talk at left
                            show hit neutral at right
                            pov "If we knew, it wouldn't have been accurate."
                            show pov embarrassed at left
                            show hit embarrassed_talk at right
                            hit "I don't know, I'm still not comfortable with it. Just because what ever happens here stays here, doesn't mean I'll like it."
                            $ hitomibeach_staysinrome = 1

                            jump lbl_hitomibeach_1_end
                        "You can't knock it until you try it.":
                            show pov neutral_talk at left
                            show hit embarrassed at right
                            pov "You can't knock it until you try it."
                            show pov neutral at left
                            show hit embarrassed_talk at right
                            hit "That is true.. that's a hard reason to argue against."
                            show pov neutral_talk at left
                            show hit embarrassed at right
                            pov "Really?! I did it! I mean..."
                            show pov embarrassed at left
                            show hit confused_talk at right
                            hit "What?"
                            show pov smirk_talk at left
                            show hit confused at right
                            pov "Huh?"
                            show pov smirk at left
                            show hit embarrassed_talk at right
                            hit "Why not, right?"
                            show pov neutral at left
                            hit "Don't knock it until you try it. I have lived in this town all my life and have never once been brave enough to attend this beach."
                            show pov neutral_talk at left
                            show hit embarrassed at right
                            pov "Let's do it! Just for a short while to get a feel for it."
                            ## WINNING BRANCH ##

                            jump lbl_hitomibeach_2
                        "It can't hurt to strip down once." if hitomibeach_stripdown == 0:
                            show pov embarrassed_talk at left
                            show hit embarrassed at right
                            pov "It won't hurt to strip down once here. Everyone's already seen plenty of naked bodies."
                            show pov sad at left
                            show hit embarrassed_talk at right
                            hit "Yeah, but.. it's a little embarrassing now that you're here."
                            hit "I would've maybe.. MAYBE done it if I didn't know anyone personally here."
                            show pov embarrassed_talk at left
                            show hit embarrassed at right
                            pov "Oh, well, isn't that a little unlucky for me? Hehe."
                            show pov sad at left
                            show hit embarrassed_talk at right
                            hit "Nothing personal, [povname]. But maybe another time?"
                            show pov embarrassed at left
                            hit "We're at that stage where we're neither strangers, nor good enough friends."
                            $ hitomibeach_stripdown = 1

                            jump lbl_hitomibeach_1_end
                "Just wanted to take a walk around town." if hitomibeach_walkaround == 0:
                    show pov neutral_talk at left
                    show hit neutral at right
                    pov "I just wanted to take a walk around town, see what's up with the neighbourhood."
                    show pov neutral at left
                    show hit neutral_talk at right
                    hit "Ahh, I see. No work or uni?"
                    show pov neutral_talk at left
                    show hit neutral at right
                    pov "Not right now, that's later."
                    pov "Anyway, I'll see you later?"
                    show pov neutral at left
                    show hit neutral_talk at right
                    hit "Sure, nice seeing you again, [povname]."
                    show pov neutral_talk at left
                    show hit neutral at right
                    pov "You too."
                    $ hitomibeach_walkaround = 1

                    jump lbl_hitomibeach_1_end_2
        "I'm sure you can go half-naked." if hitomibeach_halfnaked == 0:
            show pov neutral_talk at left
            show hit embarrassed at right
            pov "I'm sure you can go half-naked - I think they'll understand."
            show pov bored at left
            show hit confused_talk at right
            hit "Didn't you just say that the lifeguard scolded you for having clothes on?"
            show pov embarrassed_talk at left
            show hit confused at right
            pov "Well.. yeah, but only because she thinks I have some sort of genitalia infection."
            show pov embarrassed at left
            hit "..."
            show hit confused_talk at right
            hit "Do you?"
            show pov confused_talk at left
            show hit bored at right
            pov "What?! No. I got naked. It just took me surprise when I came here for the first time."
            show pov bored at left
            show hit bored_talk at right
            hit "Right. Never the less, this isn't my scene."
            show pov neutral_talk at left
            show hit neutral at right
            pov "No worries. Respect, respect."
            $ hitomibeach_halfnaked = 1

            jump lbl_hitomibeach_1_end

label lbl_hitomibeach_1_end:
    show pov embarrassed at left
    show hit embarrassed_talk at right
    hit "Look, [povname], maybe I'll come by another time and feel things out myself"
    hit "Hopefully I'll be able to get over my fear of public exposure."
    show pov embarrassed_talk at left
    show hit embarrassed at right
    pov "So do I."
    show pov embarrassed at left
    show hit confused at right
    hit "Hmm?"
    show pov embarrassed_talk at left
    pov "Nothing."
    show pov embarrassed at left
    show hit neutral_talk at right
    hit "I guess I'll see you around."
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "See you, Hitomi."

    jump lbl_hitomibeach_1_end_2

label lbl_hitomibeach_1_end_2:
    if (hitomibeach_takenoff and hitomibeach_littletan and hitomibeach_bondingexperience) == 1:
        $ hitomibeach_tryitonce = 1
    if (hitomibeach_contradicting and hitomibeach_youre50 and hitomibeach_livealittle) == 1:
        $ hitomibeach_findthenerve = 1
    if (hitomibeach_safeplace and hitomibeach_completelynormal and hitomibeach_yoursenses) == 1:
        $ hitomibeach_stareatyou = 1
    if (hitomibeach_tryitonce and hitomibeach_findthenerv and hitomibeach_stareatyou) == 1:
        $ hitomibeach_understandthat = 1
    if (hitomibeach_stayingornot and hitomibeach_staywithyou and hitomibeach_passingby) == 1:
        $ hitomibeach_beautifulday = 1
    if (hitomibeach_staysinrome and hitomibeach_tryit and hitomibeach_stripdown) == 1:
        $ hitomibeach_beacharound = 1
    if (hitomibeach_beautifulday and hitomibeach_beacharound and hitomibeach_walkaround) == 1:
        $ hitomibeach_meneither = 1
    $ hitomibeach_day = 1

    jump lbl_beachmain_day_setup

label lbl_hitomibeach_2:

    scene black
    with fade
    "You and Hitomi both get changed in the same changing room."

    scene bg beachmain_day
    show povn neutral at left
    show hitn embarrassed_talk at right
    hit "Well... here we are..."
    hit "Naked."
    show povn neutral_talk at left
    show hitn embarrassed at right
    pov "Yup."
    show povn neutral at left
    pov "..."
    show povn embarrassed_talk at left
    pov "How are you feeling?"
    show povn embarrassed at left
    show hitn embarrassed_talk at right
    hit "I mean, it's as uncomfortable as I imagined it would be, but at least I faced my fear, right?"
    show povn neutral_talk at left
    show hitn embarrassed at right
    pov "Yeah, one step towards true freedom!"
    show povn embarrassed_talk at left
    pov "Relax, Hitomi. Give it a few more minutes and you'll soon consider this place a second home."
    show povn embarrassed at left
    show hitn embarrassed_talk at right
    hit "I wouldn't go that far, but thanks, [povname]."
    show hitn embarrassed at right
    hit "..."
    show povn smirk at left
    show hitn embarrassed_talk at right
    hit "Your.. um.. you're that big, huh?"
    show povn smirk_talk at left
    show hitn embarrassed at right
    pov "It's pretty flaccid at the moment. I'm a lot bigger when I'm 'excited'."
    show povn smirk at left
    show hitn embarrassed_talk at right
    hit "Oh, really? It's just that I couldn't really imagine how big or small it would be."
    show povn smirk_talk at left
    show hitn embarrassed at right
    pov "So you've tried to imagine me naked, huh?"
    show povn smirk at left
    show hitn sad_talk at right
    hit "W-What?! No... I didn't mean it like that."
    show hitn angry_talk at right
    hit "We're all sexual animals! It's normal! You've imagined me naked as well, don't lie to me."
    show povn smirk_talk at left
    show hitn angry at right
    pov "I didn't say nor deny it."

    menu:
        "But yes, I have.":
            show hitn embarrassed at right
            pov "But yes, I have imagined you naked. I'm not even sorry."
            if skill_cha >= 3:
                show povn smirk at left
                show hitn smirk_talk at right
                hit "Oh, really, well, I guess we're even then."
                show povn neutral_talk at left
                show hitn embarrassed at right
                pov "Look at it this way. There's not much left to the imagination."
                show povn smirk_talk at left
                pov "Well, except for what's down there."
                show povn smirk at left
                show hitn smirk_talk at right
                hit "You're quite forward, aren't you? You're going to have to wait another time. There's too many people here."
                show povn neutral_talk at left
                show hitn smirk at right
                pov "So there's guaranteed another time?"
                show povn smirk at left
                show hitn smirk_talk at right
                hit "Don't make me change my mind."
                show povn neutral at left
                show hitn bored_talk at right
                hit "Oh! I should be getting back to the store. I'll see you later, [povname]."
                show hitn smirk_talk at right
                hit "You know where to find me."
                show povn smirk_talk at left
                show hitn neutral at right
                pov "See ya, Hitomi. It was really nice to finally see you."
                if hitomi_points <= 8:
                    $ hitomi_points += 2
                else:
                    $ hitomi_points = 10
                $ skill_cha -= 3
                $ hitomi_path = 3
                $ beach_naked = 1
                $ renpy.notify("You used 3 Charisma Points\nYour relationship with Hitomi has increased by 2")

                jump lbl_beachmain_day_setup
            else:
                show povn smirk at left
                show hitn angry_talk at right
                hit "Oh, so you're a pervert."
                show povn smirk_talk at left
                show hitn angry at right
                pov "By your logic, you're a pervert too."
                show povn smirk at left
                hit "..."
                show povn embarrassed at left
                show hitn bored_talk at right
                hit "Look, [povname]. It was a big step for me to get naked in front of you and all these people all of a sudden, don't fuckin' push it."
                show povn sad_talk at left
                show hitn bored at right
                pov "Alright, alright. Sorry, pushed too far, gotcha."
                show povn embarrassed at left
                show hitn bored_talk at right
                hit "Well, I gotta get back to work. That's enough public nudity for me for one day. Don't wanna get a full-body sunburn."
                show povn embarrassed_talk at left
                show hitn bored at right
                pov "Yeah, no kidding."
                show povn embarrassed at left
                show hitn bored_talk at right
                hit "See you, [povname]."
                $ renpy.notify("You needed 3 Charisma Points")
                $ hitomi_path = 3
                $ beach_naked = 1

                jump lbl_beachmain_day_setup
        "But no, I haven't, honest.":
            show povn neutral_talk at left
            show hitn bored at right
            pov "But no, I haven't imagined you naked, honest."
            if skill_cha >= 1:
                show povn neutral at left
                show hitn bored_talk at right
                hit "Hmm.. Realistically, that's hard to believe."
                show hitn neutral_talk at right
                hit "But thanks for saving my dignity, somewhat."
                show povn smirk_talk at left
                show hitn smirk at right
                pov "No worries. And hey, it's fine if you imagine me naked. I know I have the body of a God."
                show povn smirk at left
                show hitn smirk_talk at right
                hit "Haha, you wish."
                show povn neutral at left
                show hitn bored_talk at right
                hit "Oh! I should be getting back to the store. I'll see you later, [povname]."
                show hitn neutral_talk at right
                hit "You know where to find me."
                show povn neutral_talk at left
                show hitn neutral at right
                pov "See ya, Hitomi. It was really nice to finally see you."
                if hitomi_points <= 9:
                    $ hitomi_points += 1
                    $ skill_cha -= 1
                    $ renpy.notify("You used a Charisma Point\nYour relationship with Hitomi has increased")
                else:
                    $ hitomi_points = 10
                $ hitomi_path = 3
                $ beach_naked = 1

                jump lbl_beachmain_day_setup
            else:
                show povn bored at left
                show hitn confused_talk at right
                hit "What...? Am I not attractive enough to imagine naked."
                show povn confused_talk at left
                show hitn angry at right
                pov "Wha-?"
                show povn sad at left
                show hitn angry_talk at right
                hit "Are my boobs too small for you to care?"
                show povn sad_talk at left
                show hitn angry at right
                pov "I wasn't really implyin-"
                show povn embarrassed at left
                show hitn angry_talk at right
                hit "I have the tightest pussy you'll probably never get to experience!"
                hit "So suck on that!"
                show hitn angry at right
                pov "..."
                show hitn sad at right
                hit "..."
                show hitn embarrassed_talk at right
                hit "Sorry. I don't know what came over me."
                hit "I guess with the sun and my lack of clothes and everyone's naked around me, I'm not thinking straight."
                show povn embarrassed_talk at left
                show hitn sad at right
                pov "T-That's alright. I hear ya."
                show povn embarrassed at left
                show hitn embarrassed_talk at right
                hit "I better just head back to the store. Thanks for pushing me out of my comfort zone."
                hit "Whether or not this was for the better or the worst, at least I tried it once."
                show povn embarrassed_talk at left
                show hitn embarrassed at right
                pov "Alright, and no sweat. It's not for everyone."
                show povn sad at left
                show hitn embarrassed_talk at right
                hit "See ya."
                $ renpy.notify("You needed 1 Charisma Point")
                $ hitomi_path = 3
                $ beach_naked = 1

                jump lbl_beachmain_day_setup
