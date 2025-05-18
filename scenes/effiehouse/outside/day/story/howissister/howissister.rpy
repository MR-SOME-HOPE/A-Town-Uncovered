## How is Sister ##
label lbl_how_is_sister:
    default howissister_suggestion_castle = 0
    default howissister_suggestion_clown = 0
    default howissister_suggestion_chris = 0

    scene bg effiehouseoutside_day
    "{i}*Knock knock knock*{/i}"
    pov "..."
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    eff "Oh, hey, [povname]."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Hey, Effie. How are you?"
    show pov neutral at left
    show eff neutral_talk at right
    eff "I'm good, thanks for asking. But I'm sure you're not here for me."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "H-How is [sister]?"
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "I'm not going to lie to you, man."
    show pov sad at left
    show eff sad_talk at right
    eff "She isn't doing well..."
    eff "She barely slept last night, not to mention she barely touched her food."
    eff "She is taking this very hard."
    eff "I don't think I have ever seen her like this."
    show pov embarrassed_talk at left
    show eff sad at right
    pov "You think I could-"
    show pov sad at left
    show eff sad_talk at right
    eff "No."
    eff "She barely even talks to me without tearing up."
    eff "I don't think she is ready to see any of you anytime soon."
    eff "I hope you understand that. The family that broke her isn't one that she wants comforting her at the moment."

    menu:
        "This is the asshole's fault.":
            show pov angry_talk at left
            show eff embarrassed at right
            pov "This is all that asshole's fault!"
            show pov angry at left
            show eff embarrassed_talk at right
            eff "I'm sure she knows that, [povname]."
            show pov sad at left
            show eff embarrassed_talk at right
            eff "But until she gets over it on her own I doubt there is much we can do without hurting her even more."
            show pov sad_talk at left
            show eff embarrassed at right
            pov "Yeah, but-"
            show pov sad at left
            show eff embarrassed_talk at right
            eff "Dude, what happened, happened."
            show eff sad_talk at right
            if winc == 0:
                eff "Not much we can do about it now and regardless of how much of a dickhole your [dadrole] is, pointing fingers and complaining isn't going to solve anything."
            else:
                eff "Not much we can do about it now and regardless of how much of a dickhole your Dad is, pointing fingers and complaining isn't going to solve anything."
            show pov sad_talk at left
            show eff embarrassed at right
            pov "{i}*Sigh*{/i} You're right."
            show pov sad at left
            show eff confused_talk at right
            if winc == 0:
                eff "Your [sisrole] has made it perfectly clear to me that she is sick of talking about her [dadrole]."
            else:
                eff "[sister] has made it perfectly clear to me that she is sick of talking about her dad."
            eff "That was not a fun conversation at all."
            show pov sad_talk at left
            show eff confused at right
            pov "I don't doubt that for a second. How bad was it?"
            show pov shocked at left
            show eff shocked_talk at right
            eff "It went from her sobbing to blowing up at me faster than I could blink."
            show pov embarrassed at left
            show eff sad_talk at right
            eff "Never seen her that mad before."
            show eff embarrassed_talk at right
            eff "Really something I would rather not see again if I have the choice about it."
            show pov embarrassed_talk at left
            show eff embarrassed at right
            pov "You and I both, girlfriend."
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "Anyway, [sister] is really fragile right now, man."
            show pov embarrassed at left
            show eff sad_talk at right
            eff "We have to do something about it."
            show pov embarrassed_talk at left
            show eff embarrassed at right
            pov "Like what? Put her in a box full of shipping peanuts and send her off to Dinseyland?"
            show pov confused at left
            show eff confused_talk at right
            eff "I think it's about time we intervened."
        "It's all my fault.":
            show pov sad_talk at left
            show eff sad at right
            pov "It's all my fault, Effie. It's all my fault."
            pov "If I hadn't-"
            show pov sad at left
            show eff sad_talk at right
            eff "You can't blame yourself for what happened, man."
            eff "Everything went to hell real fast according to her, there wasn't much that you could do."
            show pov sad_talk at left
            show eff sad at right
            pov "Yeah, but..."
            if fortdestroyed_engage == 1:
                pov "I just wish I hadn't made things worse with how I handled things."
                show pov angry_talk at left
                pov "I was mad, and angry, and furious, and all the other synonyms."
                pov "I hated him so much for what he's done and wanted him to feel his jaw break."
                show pov sad at left
                show eff embarrassed_talk at right
                if winc == 0:
                    eff "Dude, you stood up to your own [dadrole] when he was going on a rampage."
                else:
                    eff "Dude, you stood up to your own dad when he was going on a rampage."
                show pov embarrassed at left
                eff "That takes balls."
                eff "I mean, sure it didn't helped things along but at least you came up with something."
                show pov sad at left
                eff "I'm not sure what other option was there to handle a situation like that."
                show pov embarrassed_talk at left
                show eff embarrassed at right
                pov "There are options... I just chose the wrong one."
                show pov sad_talk at left
                show eff sad at right
                pov "It fuckin' pains me whenever I replay what happened in my head."
                pov "Like what the fuck would've gone differently if I hadn't lashed out so violently."
                show pov sad at left
                show eff sad_talk at right
                eff "Dude, what else could you have done?"
                show eff embarrassed_talk at right
                eff "Doubt he would have calmed down if you had offered some lemonade and a backrub."
                show pov embarrassed_talk at left
                show eff embarrassed at right
                pov "If that option was given to me, I would've done it."
                show pov sad_talk at left
                pov "If it meant for a better outcome, I would have tried."
                show pov embarrassed at left
                show eff embarrassed_talk at right
                eff "Maybe next time, aye, Rocko?"
                show pov embarrassed_talk at left
                show eff embarrassed at right
                pov "Rocko Balboba? Fuck off, I love that movie..."
            else:
                show pov sad_talk at left
                show eff embarrassed at right
                pov "I just wished I had done something..."
                pov "Anything, for that matter."
                show pov angry_talk at left
                show eff sad at right
                pov "I just stood there like a deer in the headlights."
                show pov sad at left
                show eff sad_talk at right
                eff "What could you have done?"
                show eff confused_talk at right
                eff "Were you going to jump him or hit him upside the head with a pipe?"
                show pov confused at left
                if winc == 0:
                    eff "Not only is that actually fucked up but the chances of getting arrested for assault, charged by your own [dadrole] is pretty high."
                else:
                    eff "Not only is that actually fucked up but the chances of getting arrested for assault, charged by your own father is pretty high."
                show pov smirk_talk at left
                show eff confused at right
                pov "Yeah, but think about it. He can't press charges if he doesn't wake up."
                show pov embarrassed at left
                show eff bored_talk at right
                eff "Bruh, as I said. Fucked. Up."
                show pov smirk_talk at left
                show eff smirk at right
                pov "Look who's the party pooper now."
                show pov embarrassed at left
                show eff smirk_talk at right
                eff "Call me when 'The Purging' happens."
                show eff embarrassed_talk at right
                eff "You did the smart thing, and that's what matters."
                eff "You didn't escalated things."
                eff "It takes any idiot to throw a punch but it takes someone with brains to know when to pull 'em."
                show pov confused_talk at left
                show eff smirk at right
                pov "That phrase sounds familiar. Ghandi?"
                show pov smirk at left
                show eff embarrassed_talk at right
                eff "Just a DET Talk."
                show pov embarrassed at left
                eff "Been watching some videos on coping with pain and the likes to help [sister] get through this."
                show eff confused_talk at right
                eff "Actually the quote was from some guy who stopped showering for a year but that's not the point."
                eff "Which now that I mention it, we should really start talking about what to do with her."
                show pov sad at left
                show eff sad_talk at right
                eff "She is doing worse."
        "It all happened so fast.":
            show pov sad_talk at left
            show eff sad at right
            pov "It all happened so fast..."
            show pov sad at left
            show eff sad_talk at right
            eff "So from what [sister] managed to convey to me through all the sobbing and saliva bridges."
            show eff confused_talk at right
            eff "He really just came out of nowhere and started breaking shit?"
            show pov sad_talk at left
            show eff confused at right
            pov "From my perspective, that's what happened."
            pov "I just heard screaming downstairs and there he was."
            show pov angry_talk at left
            show eff embarrassed at right
            pov "The big fucking bad wolf coming to knock our house down like it was 2012 on the Mayan Calendar."
            show pov angry at left
            show eff sad_talk at right
            eff "Fuck.."
            show eff confused_talk at right
            eff "What do you think made him snap like that?"
            show pov bored_talk at left
            show eff confused at right
            pov "Who knows?"
            pov "Maybe something at work or just stress..."
            if main_story >= 35:
                show pov angry_talk at left
                show eff confused at right
                if winc == 0:
                    pov "Or that he's not even my real [dadrole], but a fucking imposter!"
                else:
                    pov "Or that he's not even my real dad, but a fucking imposter!"
                show pov angry at left
                show eff confused_talk at right
                eff "Wai- what?!"
                show pov angry at left
                show eff confused at right
                pov "..."
                show pov embarrassed_talk at left
                show eff embarrassed at right
                pov "I- I'm just kidding.. Sorry. Tried to lighten the mood."
            else:
                show pov bored_talk at left
                show eff embarrassed at right
                pov "He has always been a bit stern and perhaps even cold at times, but nowadays I don't even recognize him."
                show eff sad at right
                pov "It's like he turned into a completely different person."
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "Whatever the reason, we all unanimously agree that he's a fucker and literally worst than Hitlar."
            if winc == 0:
                eff "Let's focus on getting your [sisrole] back to normal so you guys can come up with some way to deal with this."
                show pov confused at left
                show eff sad_talk at right
                eff "Speaking of, your [sisrole] isn't doing good at all..."
            else:
                eff "Let's focus on getting [sister] back to normal so you guys can come up with some way to deal with this."
                show pov confused at left
                show eff sad_talk at right
                eff "Speaking of, your sister isn't doing well at all..."
            show pov sad at left
            eff "In fact, I think she is getting even worse the more she remembers what happened."
    show pov sad_talk at left
    show eff confused at right
    pov "What do you think we should do then?"
    show pov confused_talk at left
    pov "I've given her some time and space, I'm sure she's vented enough to you."
    show pov sad at left
    show eff confused_talk at right
    eff "She's vented. But I don't think all of it is out."
    show pov shocked at left
    show eff sad_talk at right
    eff "I can tell that it's too painful for her to talk about. It's not just what happened to the box fort but all the years prior."
    show pov sad at left
    eff "You should have heard her, [povname]."
    show eff sad_talk at right
    eff "She was trying so hard not to cry her eyes out and every sob that managed to escape her lips made her feel even worse."
    eff "I'm worried what she might do if we allow her like this for too long."
    show pov sad_talk at left
    show eff sad at right
    pov "You-"
    show eff shocked at right
    pov "You're not actuall suggesting that she'll-"
    show pov shocked at left
    show eff shocked_talk at right
    eff "What?! No!"
    show pov embarrassed at left
    eff "Oh, good God, no!"
    show pov sad at left
    show eff sad_talk at right
    eff "But she may decide she needs an even bigger distance from you guys and maybe run away for real."
    eff "Depending on how bad she feels if she decides that she might not even give me a warning, so we have to come up with something."
    show pov embarrassed_talk at left
    show eff confused at right
    pov "I'm all ears."
    show pov shocked at left
    show eff embarrassed_talk at right
    eff "Actually, I was hoping for you to have some ideas."
    show pov embarrassed_talk at left
    show eff embarrassed at right
    pov "Right. I can do that too."
    pov "Um.. hehe.."
    pov "I'm more used to arguing with her over the dumbest of things than I am at making her feel better."
    show pov smirk_talk at left
    pov "Then again, the times I did try to cheer her up involved hugs and ice cream."
    show pov embarrassed at left
    show eff smirk_talk at right
    eff "Yeah, I don't think she needs any more hugs and ice cream than what she has available here."
    show pov shocked at left
    show eff neutral_talk at right
    eff "I gave her a nice full body massage the other day though. She seemed to like that."
    show pov smirk_talk at left
    show eff confused at right
    pov "Something sensua-?"
    show pov embarrassed at left
    show eff bored_talk at right
    eff "{i}Something{/i} to ease her mind and body. Excuse you, pervert."
    show eff bored at right
    eff "..."
    show pov shocked at left
    show eff embarrassed_talk at right
    eff "But yes.."
    show pov smirk_talk at left
    show eff confused at right
    pov "Man, I can't tell if I'm aroused or jealous and if I was, jealous of who in what-who-knows-what way."
    show pov smirk at left
    eff "..."
    show pov shocked at left
    show eff confused_talk at right
    eff "You're.. not suggesting that you have a 'thing-thing' with [sister], right?"
    show eff confused at right
    pov "..."

    menu:
        "What?! Eww!":
            if sister_points <= 4:
                show pov angry_talk at left
                show eff confused at right
                pov "What? Eww! Dude, what's wrong with you?."
                show pov bored_talk at left
                show eff smirk at right
                pov "You should be ashamed with that sicko mind of yours."
                show eff shocked at right
                pov "Maybe in your dreams."
            else:
                show pov embarrassed_talk at left
                show eff confused at right
                pov "What?! Ewww! Effie, really? Me and [sister]?"
                pov "Haha, no. Pssh."
                show eff smirk at right
                pov "You're dirty, you know that? Girrrrrrl-"
        "I love her.":
            if sister_points <= 4:
                show pov confused_talk at left
                show eff confused at right
                if winc == 0:
                    pov "I love her like a [sisrole] if that's what you mean."
                else:
                    pov "I love her like a sister if that's what you mean."
                show pov shocked at left
                show eff smirk_talk at right
                eff "Uh-huh."
                show pov angry at left
                eff "Okay, [povname]. Okaie dokie, [povname]."
            else:
                show pov embarrassed_talk at left
                show eff smirk at right
                pov "I mean.. I love her-"
                show pov shocked_talk at left
                if winc == 0:
                    pov "Like a [sisrole]! That is-"
                else:
                    pov "Like a sister! That is-"
                show pov embarrassed at left
                pov "Like not in the wrong way! Fucking silly- youuu-"
        "That's fucked.":
            if sister_points <= 4:
                show pov bored_talk at left
                show eff smirk at right
                pov "That's fucked, Effie."
                pov "Get your mind out of the gutter."
                show pov bored at left
                show eff smirk_talk at right
                eff "Hey, I'm just teasing you."
            else:
                show pov embarrassed_talk at left
                show eff smirk at right
                pov "Whaat? Effie! That's fucked."
                pov "I can't even believe that you would even think of such indecency."
                show eff confused at right
                pov "I thought you were a good Christian girl."
                show pov embarrassed at left
                show eff smirk_talk at right
                eff "The fuck made you think that?"
    show pov embarrassed at left
    show eff confused_talk at right
    eff "It's just that you too are really close."
    show eff embarrassed_talk at right
    eff "Not saying that that's wrong at all."
    eff "Just... closer than normal."
    show pov shocked at left
    show eff smirk_talk at right
    eff "Besides, [sister]'s said some titalating things about you."
    show pov shocked_talk at left
    show eff smirk at right
    pov "Did... she... now...?"
    show pov shocked at left
    show eff smirk_talk at right
    eff "Don't worry, [povname]. It's between me and her."
    show pov bored at left
    show eff smirk_talk at right
    eff "Wink."
    show pov bored_talk at left
    show eff smirk at right
    pov "Did you just say wink?"
    show pov embarrassed at left
    show eff bored_talk at right
    eff "Wanna fight?"
    show pov embarrassed_talk at left
    show eff smirk at right
    pov "No, thanks."
    show pov confused_talk at left
    show eff confused at right
    pov "Hmm. How's about a chick flick marathon?"
    show pov smirk_talk at left
    pov "Girls do that when they are sad, right?"
    show pov embarrassed at left
    show eff confused_talk at right
    eff "That's for breakups and it's mostly to make fun of them."
    show eff smirk_talk at right
    eff "That and determine how much we would be willing to give it to the male leads."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "Really?"
    show pov embarrassed at left
    show eff smirk_talk at right
    eff "Yeah, why do you think we watch them in the first place?"
    eff "I can tell you, it's not for the plot most of the time."
    show eff neutral_talk at right
    eff "Especially when the guy is taking his shirt off."
    show pov embarrassed_talk at left
    show eff smirk at right
    pov "Conversation for a different time that I'm not sure I want to hear in the first place."
    show eff shocked at right
    if winc == 0:
        pov "Can we focus back on my [sisrole], please?"
    else:
        pov "Can we focus back on [sister], please?"
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "Right!"
    eff "Sorry."
    show pov confused at left
    show eff confused_talk at right
    eff "I mean- do you have any more ideas?"
    show pov smirk at left
    eff "What do you usually do whenever you want to cheer up a girl?"
    show pov smirk_talk at left
    show eff confused at right
    pov "Would you be surprised if I told you that getting food and oversized gifts are the two main things men think of to fix an issue with a woman?"
    show pov smirk at left
    show eff bored_talk at right
    eff "In all honesty, no."
    show pov bored at left
    eff "Would explain a lot."
    show pov smirk_talk at left
    show eff bored at right
    pov "Hey, by the end of it we are supporting the giant gifts economy so that's making someone happy."
    show pov shocked at left
    show eff bored_talk at right
    eff "Stop joking about capitalism and focus!"
    show pov embarrassed at left
    show eff confused_talk at right
    if winc == 0:
        eff "We already know more ice cream isn't going to work and I really doubt getting her a giant teddy bear will stop her from being pissed at your [dadrole], what else have you got?"
    else:
        eff "We already know more ice cream isn't going to work and I really doubt getting her a giant teddy bear will stop her from being pissed at your dad, what else have you got?"

label lbl_how_is_sister_suggestions:

    menu:
        "Bouncy castle?" if howissister_suggestion_castle == 0:
            show pov smirk_talk at left
            show eff smirk at right
            pov "A bouncy castle? So she can jump out of the hole of despair?"
            show pov smirk at left
            show eff embarrassed_talk at right
            eff "Dude, take this seriously."
            show pov neutral_talk at left
            show eff embarrassed at right
            pov "I am! We used to love them when we were kids."
            show pov embarrassed_talk at left
            show eff shocked at right
            pov "I hurt my ankle jumping from the top of our treehouse and into one and she wouldn't stop laughing for days."
            show eff smirk at right
            if winc == 0:
                pov "[missus] grounded me for the entire time I had the cast on the leg."
            else:
                pov "Mom grounded me for the entire time I had the cast on the leg."
            show pov smirk_talk at left
            pov "Jokes on her, it's not like I could go out anywhere anyway."
            show pov smirk at left
            show eff confused_talk at right
            eff "We are not throwing her a birthday party!"
            show pov confused at left
            show eff neutral_talk at right
            eff "What else you got?"
            $ howissister_suggestion_castle = 1

            jump lbl_how_is_sister_suggestions
        "A clown?" if howissister_suggestion_clown == 0:
            show pov confused_talk at left
            show eff shocked at right
            pov "A clown? To turn her frown..."
            show pov smirk at left
            show eff angry_talk at right
            eff "Don't you dare say-"
            show pov smirk_talk at left
            show eff bored at right
            pov "Upside down."
            show pov smirk at left
            eff "..."
            show eff angry_talk at right
            eff "As long as I live and breathe, you are NOT bringing one of those things to my house."
            show eff sad_talk at right
            eff "We are trying to help her, not scare her to death!"
            show pov smirk_talk at left
            show eff angry at right
            pov "I'm assuming this is a topic with a backstory you are not open to talk about."
            show pov smirk at left
            show eff angry_talk at right
            eff "It's a long story but the main point is that they freak me the fuck out."
            show pov confused at left
            show eff confused_talk at right
            eff "Anything else?"
            $ howissister_suggestion_clown = 1

            jump lbl_how_is_sister_suggestions
        "Chris Hemmingsworth" if howissister_suggestion_chris == 0:
            show pov smirk_talk at left
            show eff shocked at right
            pov "How about Chris Hemmingsworth."
            show pov smirk at left
            show eff shocked_talk at right
            eff "If you were capable of bringing him or Chris Ebans to my doorstep, I would suck you off so hard your balls would go back into your body as raisins."
            show pov confused_talk at left
            show eff shocked at right
            pov "Jesus, Effie. Like-"
            show eff neutral at right
            pov "In front of them?"
            show pov bored at left
            show eff neutral_talk at right
            eff "After them, you beautiful, silly cuck."
            show pov bored_talk at left
            show eff smirk at right
            pov "You know what, I totally understand where you're coming from."
            show pov embarrassed at left
            show eff smirk_talk at right
            if effie_points >= 3:
                eff "As If you wouldn't eat me out like an absolute savage if I got you a date with Scarlet Johansome or Nicky Mirage."
            else:
                eff "As If you wouldn't do anything if I got you a date with Scarlet Johansome or Nicky Mirage."
            show pov smirk_talk at left
            show eff smirk at right
            pov "Nicky Mirage? You have The God of Thunder, The Winter Soldier, The Sexy-ass Russian Spy, and... Nicky."
            show pov confused at left
            show eff smirk_talk at right
            eff "Pretty sure she was in Black Cougar."
            show pov bored_talk at left
            show eff confused at right
            pov "Pretty sure that's not the right film."
            show pov confused at left
            show eff confused_talk at right
            eff "But since I highly doubt of your ability of bringing either Chris' to me, I am going to ask that you think something else."
            $ howissister_suggestion_chris = 1

            jump lbl_how_is_sister_suggestions
        "I got nothing.":
            show pov bored_talk at left
            show eff bored at right
            pov "I've got nothing, sorry."
    show eff confused_talk at right
    eff "Well..."
    show pov confused at left
    eff "This whole deal started with the fort being destroyed, why don't you just build one back up?"
    show eff sad_talk at right
    if winc == 0:
        eff "Doubt that's going to flow well with your dickhead of a [dadrole] though..."
        show pov embarrassed_talk at left
        show eff confused at right
        pov "I wouldn't worry too much about him."
        pov "My [mumrole] pretty much kicked him out after that whole business."
        show pov bored_talk at left
        show eff neutral at right
        pov "He has been behaving like a real jerk and my [mumrole] is getting tired of his shit."
    else:
        eff "Doubt that's going to flow well with your dickhead of a dad though..."
        show pov embarrassed_talk at left
        show eff confused at right
        pov "I wouldn't worry too much about him."
        pov "Mom pretty much kicked him out after that whole business."
        show pov bored_talk at left
        show eff neutral at right
        pov "He has been behaving like a real jerk and my mom is getting tired of his shit."
    show pov confused_talk at left
    show eff embarrassed at right
    pov "I doubt she is going to stand him too much if he keeps like this."
    if mum_points >= 5:
        show pov embarrassed_talk at left
        show eff confused at right
        pov "That and some... other stuff in her life has her reevaluating her relationship lately..."
        show pov embarrassed at left
        show eff confused_talk at right
        eff "Stuff like what?"
        show pov shocked at left
        show eff shocked_talk at right
        eff "Is she seeing someone else?"

        menu:
            "It's private.":
                show pov embarrassed_talk at left
                show eff embarrassed at right
                pov "It's a private matter."
                if winc == 0:
                    pov "I-I really don't think I should start talking about my [mumrole]'s private life behind her back."
                else:
                    pov "I-I really don't think I should start talking about my mom's private life behind her back."
                show pov embarrassed at left
                show eff embarrassed_talk at right
                eff "Totally get ya."
                show pov confused at left
                show eff confused_talk at right
                eff "Still, that's harsh dude..."
                show pov embarrassed at left
                show eff sad_talk at right
                eff "I'm sorry you guys are going through such a shitty run lately."
                show pov embarrassed_talk at left
                show eff embarrassed at right
                pov "I-It's alright, really."
                pov "We have each other's backs so there is nothing to worry about."
                show pov neutral_talk at left
                show eff smirk at right
                pov "Not to mention we also have you. You've been so good to [sister]."
                show pov neutral at left
                show eff smirk_talk at right
                eff "Hell yeah, you do."
            "I don't know.":
                show pov embarrassed_talk at left
                show eff confused at right
                pov "O-Oh, I don't know."
                show pov confused_talk at left
                pov "Some guy, I assume."
                show eff embarrassed at right
                pov "Not really something I'm in the mood of discussing with everything that's going on, Effie."
                show pov embarrassed at left
                show eff embarrassed_talk at right
                eff "R-Right! Sorry for bringing it up man."
                show pov embarrassed_talk at left
                show eff embarrassed at right
                pov "Besides, its for the best. She is an adult and capable of making her own decisions."
        show pov embarrassed at left
        show eff embarrassed_talk at right
        eff "Still, I'm surprised you're taking it so well!"
        show pov embarrassed_talk at left
        show eff embarrassed at right
        if winc == 0:
            eff "Most people wouldn't be happy to know their [mumrole] is cheating on their dad behind their backs."
            pov "Well..."
            pov "I'm definitely not like most people."
            pov "And I really think this other guy is making her happier so that's what matters."
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "You must be really close with your [mumrole] to not let this bother you."
        else:
            eff "Most people wouldn't be happy to know their mom is cheating on their dad behind their backs."
            pov "Well..."
            pov "I'm definitely not like most people."
            pov "And I really think this other guy is making her happier so that's what matters."
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "You must be really close with your mom to not let this bother you."
        show pov embarrassed_talk at left
        show eff confused at right
        pov "You have no idea."
        show pov embarrassed at left
        show eff embarrassed_talk at right
        eff "Ominous but adorable nonetheless."
    show pov confused at left
    show eff embarrassed_talk at right
    eff "Maybe talk to her?"
    show eff neutral_talk at right
    eff "Wasn't there something about a mama bear always protecting her cubs?"
    show pov neutral at left
    show eff embarrassed_talk at right
    if winc == 0:
        eff "If she knew she might not see [sister] again, I'm sure she will do whatever to keep your [dadrole] at bay."
    else:
        eff "If she knew she might not see [sister] again, I'm sure she will do whatever to keep your dad at bay."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Worth a shot."
    show pov confused at left
    pov "If I'm going to rebuild the fort then I'm going to need a ton of boxes, any idea where I can find some?"
    show pov confused at left
    show eff confused_talk at right
    eff "I don't know, dude. I'm sure you can ask some of the stores around. They always have products coming in."
    show pov confused_talk at left
    show eff neutral at right
    pov "Guess I'll ask around town."
    show pov embarrassed_talk at left
    pov "Keep me updated on her condition, okay?"
    show pov embarrassed at left
    show eff neutral_talk at right
    eff "You got it, dude."
    show pov confused at left
    show eff embarrassed_talk at right
    eff "Oh, and [povname], for the record..."
    show pov embarrassed at left
    show eff smirk_talk at right
    if winc == 0:
        eff "You're an awesome [povsisrole] for caring this much about her, I am sure she thinks so as well."
    else:
        eff "You're an awesome brother for caring this much about her, I am sure she thinks so as well."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "Thanks, Effie."
    show pov neutral_talk at left
    show eff neutral at right
    pov "I won't let her down."
    $ sister_path = 29
    $ renpy.notify("New Objective: Find Some Boxes")

    jump lbl_effiehouseoutside_day_setup
