## Crush on Allaway ##
label lbl_crush_on_allaway:
    default crushonallaway_time = 0

    scene bg cafeoutside_day
    with fade
    if gtime == 0:
        $ crushonallaway_time = 0

        jump lbl_crush_on_allaway_brock
    else:
        $ crushonallaway_time = 1

        jump lbl_crush_on_allaway_effie

label lbl_crush_on_allaway_brock:
    show pov confused at left
    with dissolve
    show brow neutral_talk at right
    with dissolve
    bro "Hey, dude."
    bro "How was your date with Miss TILF."
    show pov confused_talk at left
    show brow neutral at right
    pov "TILF?"
    show pov confused at left
    show brow smirk_talk at right
    bro "Teacher I'd-"
    show pov bored_talk at left
    show brow neutral at right
    pov "Okay, I get it."

    menu:
        "It was fun.":
            show pov neutral_talk at left
            show brow neutral at right
            pov "It was fun."
            show pov neutral at left
            show brow smirk_talk at right
            bro "Did you get a second date?"
            show pov confused_talk at left
            show brow confused at right
            pov "Um... not a clearly planned one. But I'm sure we'll get a chance another time."
            show pov confused at left
            show brow confused_talk at right
            bro "Tsk tsk tsk, you should've asked, bro. If I were you, I'd be going home with her right now."
            show pov bored at left
            show brow smirk_talk at right
            bro "Close the curtains, turn up the heat and-"

            menu:
                "Don't talk about her that way.":
                    show pov angry_talk at left
                    show brow shocked at right
                    pov "Don't frikkin talk about her that way, dude. She's mine."
                    show pov angry at left
                    show brow shocked_talk at right
                    bro "Whoa, bro. Chill."
                    bro "I'm just speaking hypothetically."
                    show pov confused at left
                    show brow smirk_talk at right
                    bro "She's not really my type anyway. I like them girls petite and soft."
                    show brow confused_talk at right
                    bro "Allaway's got a surprising bite to her."
                "No need to get into anymore details.":
                    show pov bored_talk at left
                    show brow neutral at right
                    pov "Hahaha... yeah, I get it, no need to get into anymore details."
                    show pov bored at left
                    bro "..."
                    show brow smirk_talk at right
                    bro "And we'd fuck the night away."
                    show pov angry at left
                    show brow smirk at right
                    bro "..."
                    show pov angry at left
                    show brow embarrassed_talk at right
                    bro "But it's all good, dude. You don't need to cry about it tonight."
                    show pov confused at left
                    show brow smirk_talk at right
                    bro "Allaway's not really my type anyway."
        "It was alright.":
            show pov confused_talk at left
            show brow neutral at right
            pov "It was alright."
            show pov confused at left
            show brow neutral_talk at right
            bro "Alright's better than terrible by far, my dude."
            show pov bored at left
            show brow embarrassed_talk at right
            bro "Don't be too down about it, man. First dates aren't always the best, doesn't mean that it's always going to be like that forever."
            show pov confused at left
            show brow neutral_talk at right
            bro "You just gotta... feel her up as does she to you."
            show brow neutral_talk at right
            bro "You know what I mean?"
            show brow neutral at right
            pov "..."
            show pov confused_talk at left
            show brow bored at right
            pov "You mean feel her out?"
            show pov bored at left
            show brow confused_talk at right
            bro "Uh- yeah, whatever works for you, bro."
        "It could've gone better.":
            show pov embarrassed_talk at left
            show brow confused at right
            pov "It could've gone better."
            show pov confused at left
            show brow bored_talk at right
            bro "That's just the nice guy's way of saying it sucked."
            show pov bored at left
            show brow confused_talk at right
            bro "Don't be a nice guy, bro. Say it sucked."
            show pov shocked at left
            show brow angry_talk at right
            bro "Say it!"
            show pov confused_talk at left
            show brow bored at right
            pov "Alright, dude. It sucked. Don't need to go agro on me."
            show pov bored at left
            show brow bored_talk at right
            bro "... It couldn't have sucked that much, dude."
            show brow neutral_talk at right
            bro "You two looked as if you were getting along pretty rad."
            show pov embarrassed at left
            show brow smirk_talk at right
            bro "Don't give up on her, man. Not everyone will get a chance to sleep with their teacher."
            bro "You're going to be every boy's hero and role model."
            bro "Trust me, I know what I'm talking about."
    show pov confused at left
    show brow confused_talk at right
    bro "Look, man. Bro to bro."
    show pov shocked at left
    show brow smirk_talk at right
    bro "I'm rooting for you to get into her pants."
    show pov confused at left
    show brow confused_talk at right
    bro "Let me give you some insight on your target, give you the upper hand on this hunt for that sweet ass."
    show pov confused_talk at left
    show brow confused at right
    pov "Why would you help me?"
    show pov bored at left
    show brow neutral_talk at right
    bro "Because my purpose in this world is to help those who aren't as big and chiselled as me with the ladies."
    show brow neutral at right
    pov "..."
    show pov bored_talk at left
    show brow neutral at right
    pov "You know, she did mention you and how much she has the hots for you. She likes the fact that you're the biggest and strongest in the fight club."
    show pov angry at left
    show brow smirk_talk at right
    bro "Oh?! She does?! Ooooh, maybe I should go after her, aye?"
    bro "May the best man win."
    show brow smirk at right
    pov "..."
    show brow smirk_talk at right
    bro "I'm joking, dude. I know she has the hots for me."
    bro "Don't look at me like that, man. I can't help that I have the body of Hercules and the Strength of also Hercules."
    show pov bored_talk at left
    show brow confused at right
    pov "Did you and her...?"
    show pov bored at left
    bro "Hm?"
    show pov bored_talk at left
    pov "Y'know?"
    show pov bored at left
    show brow confused_talk at right
    bro "Did we bang? Her and I? Me and her?"
    show brow smirk_talk at right
    bro "Tune in next week for the answer to that question!"
    bro "Epic cliffhange-"
    show pov bored_talk at left
    show brow neutral at right
    pov "C'mon, man!"
    show pov bored at left
    show brow neutral_talk at right
    bro "Fine, fine. I'm just playing around."
    show pov confused at left
    show brow neutral_talk at right
    bro "No, she and I never did nothing."
    show brow confused_talk at right
    bro "We're just close acquaintances, she stops by the cafe every weekend and we talk."
    show brow neutral_talk at right
    bro "Lovely gal. But other than that, nothing else."
    show pov embarrassed at left
    show brow bored_talk at right
    bro "I don't even know where she is during the fight club, I never see her in the gym."
    show pov embarrassed_talk at left
    show brow shocked at right
    pov "She's actually watching from outside the door."
    show pov embarrassed at left
    show brow confused_talk at right
    bro "Really? Huh... learnt something new today."
    show pov confused_talk at left
    show brow confused at right
    pov "Speaking of learning. The insight on Miss Allaway?"
    show pov bored at left
    show brow neutral_talk at right
    bro "Oh! Right, nearly forgot."
    show pov confused at left
    bro "We've actually talked about it already. She has the hots for me, right?"
    show pov confused_talk at left
    show brow neutral at right
    pov "Right."
    show pov confused at left
    show brow neutral_talk at right
    bro "She likes tough guys. Bad boys."
    show pov bored_talk at left
    show brow neutral at right
    pov "I guess I kinda figured that out already."
    show pov bored at left
    show brow smirk_talk at right
    bro "The fact that I'm denying her desires for me is making her soaking wet in the panties."
    bro "Sue me."
    show pov bored_talk at left
    show brow neutral at right
    pov "Y'know, I kinda wished you didn't keep mentioning that she would sleep with you in a split second."
    pov "This kinda makes you my archenemy."
    show pov bored at left
    show brow smirk_talk at right
    bro "Whaat? Hell naww, bro. We bros, dude. I'm here for you and cross my heart, I won't sleep with her ever."
    show pov confused at left
    bro "You trust me?"

    menu:
        "Yeah, I do.":
            if brock_points <= 9:
                $ brock_points += 1
            else:
                $ brockpoints = 10
            $ renpy.notify("Your relationship with Brock has increased")
            show pov embarrassed_talk at left
            show brow neutral at right
            pov "Yeah. Yeah, I do."
            show pov embarrassed at left
            show brow neutral_talk at right
            bro "Sweet! Bros before hoes, dude. They didn't make that a bibrocal rule for nothing."
            show pov neutral at left
        "I don't think I can.":
            if brock_points >= 1:
                $ brock_points -= 1
            else:
                $ brockpoints = 0
            $ renpy.notify("Your relationship with Brock has decreased")
            show pov confused_talk at left
            show brow bored at right
            pov "I don't think I can."
            show pov confused at left
            show brow confused_talk at right
            bro "Alright, I see how it is then. I guess I have nothing else to say about this."
    bro "Best I get back inside, my little break's over."
    show pov neutral at left
    show brow neutral_talk at right
    bro "Good luck with it all, dude."
    $ missallaway_path = 7

    jump lbl_cafeoutside_day_setup

label lbl_crush_on_allaway_effie:
    show pov neutral at left
    with dissolve
    show effw smirk_talk at right
    with dissolve
    eff "Hey there, big shot."
    eff "How was your date with Allaway?"
    show pov neutral_talk at left
    show effw smirk at right
    pov "Oh, hey Effie."

    menu:
        "It was fun.":
            show pov neutral_talk at left
            show effw neutral at right
            pov "It was fun."
            show pov neutral at left
            show effw neutral_talk at right
            eff "That's great to here. I saw you too getting along quite well through the window."
            show pov embarrassed_talk at left
            show effw neutral at right
            pov "You were watching us?"
            show pov smirk at left
            show effw confused_talk at right
            eff "Not watching... observing... occasionally."
            show pov neutral_talk at left
            show effw neutral at right
            pov "Haha, yeah, Miss Allaway is fun to talk to."
            show pov confused_talk at left
            show effw smirk at right
            pov "Surprisingly more down to Earth than I thought she would be when she's not in her uniform."
            show pov neutral at left
            show effw neutral_talk at right
            eff "She's a person like everyone else. Some people forget about that."
            show pov smirk_talk at left
            show effw neutral at right
            pov "And you're definitely not one of them. She likes you a lot."
            show pov neutral at left
            show effw neutral_talk at right
            eff "Yeah, we're pretty good friends, in and out of uni hours."
            show effw embarrassed_talk at right
            eff "It's weird how it turned out like that, doesn't it?"
            show pov neutral_talk at left
            show effw neutral at right
            pov "That's totally one in a million."
        "It was alright.":
            show pov neutral_talk at left
            show effw confused at right
            pov "It was alright."
            show pov neutral at left
            show effw confused_talk at right
            eff "Just alright?"
            show pov embarrassed_talk at left
            show effw neutral at right
            pov "It was a first for me. I've never sat down and had a full-on personal conversation with my teacher before."
            show pov embarrassed at left
            show effw neutral_talk at right
            eff "I say it's a little weird for you because you're still only seeing her as a teacher and not as a regular person with a life outside of uni."
            show pov embarrassed_talk at left
            show effw neutral at right
            pov "Hahaha, yeah. I guess I need to get used to that idea."
        "It could've gone better.":
            show pov embarrassed_talk at left
            show effw confused at right
            pov "It could've gone better."
            show pov embarrassed at left
            show effw confused_talk at right
            eff "Huh? Why did something bad happen between you two?"

            menu:
                "Not exactly bad.":
                    show pov embarrassed_talk at left
                    show effw confused at right
                    pov "Not exactly bad."
                    pov "It was just... there was some misunderstanding..."
                    show pov embarrassed at left
                    show effw embarrassed_talk at right
                    eff "Oh, damn, dude. I'll talk to her for you. Make sure things are alright between the both of you."
                    show pov embarrassed_talk at left
                    show effw neutral at right
                    pov "You don't need to do that, it wasn't that big a deal. Just hoped things would've gone more smoothly."
                    pov "The brunch was... rememberable. Let's put it that way."
                "She gave me an under the tablet footjob.":
                    show pov embarrassed_talk at left
                    show effw shocked at right
                    pov "She... accidentally gave me an under the table footjob."
                    show pov embarrassed at left
                    show effw confused_talk at right
                    eff "Accidentally?"
                    show pov confused_talk at left
                    show effw confused at right
                    pov "Yeah, she must've put her feet up onto my chair without thinking and didn't realise until a bit later on."
                    show pov confused at left
                    show effw confused_talk at right
                    eff "Well, that's a first."
                    eff "You sure it was an accident?"
                    show pov confused_talk at left
                    show effw confused at right
                    pov "She panicked about it."
                    show pov embarrassed at left
                    show effw confused at right
                    eff "Mhmm...?"
    show pov embarrassed at left
    show effw neutral_talk at right
    eff "Well, hey. I'm sure a second date between you guys is just around the corner."
    show effw neutral at right
    pov "..."
    show effw smirk_talk at right
    eff "Oh, come now, [povname]. There's no hiding the fact that you like her."
    eff "Literally, you suck at hiding your feelings for her, whether it'd be romantically or lustfully."
    show effw smirk at right
    pov "..."
    show pov embarrassed_talk at left
    pov "It's hormonal."
    show pov embarrassed at left
    show effw smirk_talk at right
    eff "Hahahaha, yeah, [povname]. The hormones."
    eff "C'mon, we both agree that she's a gorgeous woman with a dark, dark secret."
    show pov confused at left
    show effw confused_talk at right
    eff "She could be a vampire, or a serial killer, or a really weird santa-teddy collector."
    show effw smirk_talk at right
    eff "We'd still sleep with her."
    show pov confused_talk at left
    show effw neutral at right
    pov "We? Why we?"
    show pov shocked at left
    show effw smirk_talk at right
    eff "Oh, come now, you can't have her all to yourself."
    show effw neutral_talk at right
    eff "I'm joking, hahahaha! Or am I?"
    show effw bored_talk at right
    eff "We've done stuff."
    show effw neutral_talk at right
    eff "But enough about me and her."
    show pov embarrassed at left
    eff "Let's talk about your chances with her. Being honest with you, you have a great chance with her."
    show pov embarrassed_talk at left
    show effw neutral at right
    pov "You think so?"
    show pov embarrassed at left
    show effw neutral_talk at right
    eff "I really do. I know her very well and I can totally see you and her being a thing."
    show effw bored_talk at right
    eff "But [povname]. As her friend and as your friend. You must keep it very low key."
    eff "She's still your teacher and any news about you and her in any sort of relationship can and will be bigger than an oil spill."
    eff "It will ruin her career and reputation and I know her longer than I know you."
    show pov shocked at left
    show effw angry_talk at right
    eff "So if you fuck things up, I will fuck you up."
    show effw bored_talk at right
    eff "Brock and I are on pretty good terms, I'm sure you don't wanna deal with him."
    show effw bored at right
    pov "..."
    show pov embarrassed_talk at left
    show effw shocked at right
    pov "Fuck me, Effie. That's quite the threat you just gave me."
    show pov embarrassed at left
    show effw embarrassed_talk at right
    eff "Oh my God. I'm so sorry. I think a little bit of Allaway slipped into me. My dark side creeped out a little."
    show pov shocked at left
    show effw angry_talk at right
    eff "But seriously, [povname]. Don't ruin her life."
    eff "If you can't handle the pressure, there's plenty of other girls at uni for you to stick your dick in."
    show effw sad_talk at right
    eff "{i}*Sigh*{/i}"
    show pov embarrassed at left
    show effw sad at right
    pov "..."
    show effw neutral_talk at right
    eff "Okay, I'm done. Now to give you a little tid-bit about her that may help you."
    show pov neutral at left
    eff "You obviously know about her spontaneous dark, and frequently risque outbreaks, right?"
    show pov neutral_talk at left
    show effw neutral at right
    pov "It's a very strong trait about her, yes."
    show pov shocked at left
    show effw smirk_talk at right
    eff "Well, she's very much aware of it and sometimes she fakes it."
    show pov shocked_talk at left
    show effw neutral at right
    pov "She what?"
    show pov shocked at left
    show effw neutral_talk at right
    eff "She fakes it. Sometimes."
    show pov shocked_talk at left
    show effw neutral at right
    pov "Fakes it? LIke she intentionally says something and plays it off like one of her accidental dark confessions."
    show pov shocked at left
    show effw smirk_talk at right
    eff "B-b-b-b-b-bingo."
    show pov confused_talk at left
    show effw neutral at right
    pov "Wow... I actually never thought of that."
    show pov confused at left
    show effw neutral_talk at right
    eff "I've gotten pretty good at knowing when she is and isn't aware of what dark, horny thoughts she splurts out of her mouth."
    show effw smirk_talk at right
    eff "Don't tell her this but she's really such a closet whore."
    show pov shocked at left
    eff "And between you and me. I help her get off sometimes."
    show pov shocked_talk at left
    show effw smirk at right
    pov "Yoooouuu..."
    show pov shocked at left
    show effw neutral_talk at right
    eff "Shhh... I better go. My break is over."
    show pov embarrassed at left
    eff "See you around, [povname]."
    show pov embarrassed_talk at left
    show effw neutral at right
    pov "See you, Effie. Thanks for the talk, I'll think about what you said."
    show pov neutral at left
    show effw neutral_talk at right
    eff "Good luck with everything, dude."
    $ missallaway_path = 7

    jump lbl_cafeoutside_day_setup
