label lbl_investigations_effie:
    ##-Mc approaches the coffee stand to see Effie working there-
    default investigations_effie = 0

    if investigations_effie != 0:
        show btn cafeinside_day_effie_idle
        pov "{i}I already talked to her. I'll leave her alone for now.{/i}"
    else:

        scene bg cafeinside_day
        show btn cafeinside_day_effie_idle
        with fade
        show pov embarrassed_talk at left
        with dissolve
        show effw shocked at right
        call lbl_cafeinside_counter_check
        with dissolve
        pov "Um, Effie?"
        show pov embarrassed at left
        show effw embarrassed_talk at right
        eff "Hey dude, whats up?"
        show effw confused_talk at right
        eff "Came for some coffee or just to spend time with little ol’ me?"
        show pov shocked at left
        show effw sad_talk at right
        eff "Please tell me it’s the second, I am soooo bored."
        show pov embarrassed_talk at left
        show effw sad at right
        pov "Y-Yeah, about that..."
        show effw smirk at right
        pov "H-Hey, um… Can we talk for a bit?"
        show pov embarrassed at left
        show effw smirk_talk at right
        eff "Always dude, you know I always have time for you."
        show pov confused at left
        show effw confused_talk at right
        eff "Is something wrong?"
        show pov confused_talk at left
        show effw confused at right
        pov "Well…"
        show pov embarrassed_talk at left
        pov "It’s a bit of a long story."
        show pov embarrassed at left
        show effw bored_talk at right
        eff "Is it now?"
        show effw shocked_talk at right
        eff "You have been looking rather shaken up lately."
        show effw smirk_talk at right
        eff "Finally ready to have a heart to heart with me?"
        show pov embarrassed_talk at left
        show effw smirk at right
        pov "Sort of. Actually, I have some questions I was told from a few people that you could answer."
        show pov embarrassed at left
        show effw bored_talk at right
        eff "That so?"
        show effw smirk_talk at right
        eff "Well, depends on what you want to know I guess."
        show pov shocked at left
        show effw angry_talk at right
        eff "But damn, what sort of reputation do I have for people to send you directly to me?"
        show pov sad at left
        show effw confused_talk at right
        eff "Don’t want people to start comparing me to gossip queen Meghan or something."
        show pov embarrassed at left
        show effw bored_talk at right
        eff "What is it you want to know?"
        show pov embarrassed_talk at left
        show effw bored at right
        pov "Well…"
        pov "It’s about the…"
        show pov confused_talk at left
        show effw shocked at right
        pov "The strange things going on around town…"
        show pov embarrassed at left
        show effw confused_talk at right
        eff "Okay?"
        eff "Are you going to elaborate on it or just assume I immediately know what you are talking about?"
        show pov embarrassed_talk  at left
        show effw confused at right
        pov "R-Right, sorry! It’s just that I’m not really sure how to bring this topic up with you."
        show pov confused at left
        show effw bored_talk at right
        eff "Well, I hear that using your words its quite an effective method of letting people know stuff."
        show pov confused_talk at left
        show effw smirk at right
        pov "Okay, okay, I see I caught you in full sass mode."
        show pov shocked at left
        show effw smirk_talk at right
        eff "Wrong! I’m always in full sass mode."
        eff "Never to miss a witty comeback."
        show pov smirk at left
        show effw neutral_talk at right
        eff "You just gotta learn to love me that way~"
        show pov smirk_talk at left
        show effw neutral at right
        pov "I’m well aware of that."
        show pov smirk at left
        show effw smirk_talk at right
        eff "Which is why you are my favorite goober."

        ##-If player has had sex with Effie-
        show pov smirk at left
        show effw smirk_talk at right
        eff "Well, that and another few reasons~"

        ##=RESULT END=
        show pov neutral at left
        show effw confused_talk at right
        eff "Anyway, are you going to tell me what's eating ya or not?"
        show pov embarrassed_talk  at left
        show effw confused at right
        pov "Well…"
        pov "It’s about the town and everything going on."
        show pov embarrassed at left
        show effw confused_talk at right
        eff "What about it?"
        show effw smirk_talk at right
        eff "Don’t tell me you are also here to ask about what my dad said on the news!"
        show pov confused at left
        show effw bored_talk at right
        eff "God, he is so embarrassing."
        show effw angry_talk at right
        eff "Everytime he gets any attention from the community he just goes full redneck on public media!"
        show pov embarrassed at left
        show effw smirk_talk at right
        eff "And he wonders why I don’t want him to come to school events, ugh…"
        show pov embarrassed_talk at left
        show effw confused at right
        pov "N-No, it’s not about that."
        show pov confused_talk at left
        pov "Effie… What do you know about town mysteries?"
        show pov confused at left
        show effw bored_talk at right
        eff "… Okay, you got me, I wasn't expecting you to come out and ask that."
        show pov embarrassed at left
        show effw smirk_talk at right
        eff "Not gonna lie, I was kind of betting with myself whether or not you would ask me to meet you in the backroom or something."
        show pov smirk_talk at left
        show effw confused at right
        pov "Weirdly enough, you are not the first girl to say that to me today."
        show pov smirk at left
        show effw confused_talk at right
        eff "Well, aren’t you quite the active lady killer?"
        show pov smirk_talk at left
        show effw smirk at right
        pov "Back on point, please."
        show pov bored_talk at left
        show effw smirk at right
        pov "Look, I’ve heard that you used to be quite into this sort of stuff."
        show pov bored at left
        show effw smirk_talk at right
        eff "Getting invited to the backroom?"
        show pov shocked at left
        show effw confused_talk at right
        eff "Not a good thing to accuse a lady, you know?"
        show pov shocked_talk at left
        show effw confused at right
        pov "Effie!"
        pov "I mean the whole weird shit about the town."
        show pov bored_talk at left
        show effw smirk at right
        pov "And yes, I mean before the kidnapping and my whole nudity thing, before you ask."
        show pov bored at left
        show effw smirk_talk at right
        eff "You did beat me to it."
        show effw bored_talk at right
        eff "Look, [povname], that was just a phase I was going through alright?"
        show effw angry_talk at right
        eff "Don’t look too deeply into it."
        show pov bored_talk at left
        show effw bored at right
        pov "Effie please."
        show pov angry_talk at left
        show effw smirk at right
        pov "Look, I’ll be honest with you here, some weird shit has been going on around me and I really need some answers before I downright lose it."
        show pov bored at left
        show effw smirk_talk at right
        eff "Weird time to finally decide to be honest when Jacob and I have been asking you for days what's wrong with you, don’t you think?"
        show pov embarrassed_talk at left
        show effw bored at right
        pov "L-Look, I’m really sorry about that, but I really need your help here."
        show pov sad_talk at left
        show effw smirk at right
        pov "Isn’t there anything you can tell me that may help me?"
        show pov bored at left
        show effw smirk_talk at right
        eff "[povname], I told you already all of that was just a phase I was into."
        show pov confused at left
        show effw angry_talk at right
        eff "Can’t you get off my back?"
        show pov bored at left
        show effw bored_talk at right
        eff "I clearly don’t want to talk about it."
        show pov bored_talk at left
        show effw bored at right
        pov "I can see that, but I can’t help but be pushy about this."
        show pov embarrassed_talk at left
        show effw angry at right
        pov "Please, it’s really important."
        show pov embarrassed at left
        show effw angry_talk at right
        eff "Ugh, gimme a break here…"
        show pov angry_talk at left
        show effw confused at right
        pov "I’m telling you that I can’t afford to do that."
        show effw shocked at right
        pov "I’m not asking for much here, what’s the big deal?"
        show pov bored at left
        show effw bored_talk at right
        eff "[povname], please."
        show pov angry at left
        show effw smirk_talk at right
        eff "I’m asking nicely here, I don’t want to talk about it, nor do I want to keep talking to you right now if you don’t understand that."
        show pov angry_talk at left
        show effw angry at right
        pov "Why do you keep avoiding the subject?"
        show pov bored_talk at left
        show effw shocked at right
        pov "I wouldn’t be asking you this if it wasn’t important."
        show pov angry_talk at left
        show effw bored at right
        pov "Look, I just need you to tell me if-"
        show pov shocked at left
        show effw bored_talk at right
        eff "I said no, [povname]!"
        show pov angry at left
        eff "N. O."
        show effw angry_talk at right
        eff "Do you understand that?!"

        ##-The sudden outburst has the entire cafe go quiet as everyone stares at you and Effie-

        ##-The Mc looks rather shocked as well but Effie remains headstrong and upset-
        show pov shocked at left
        show effw confused_talk at right
        eff "Look… You better leave, I really don’t want to see your face right now…"
        show pov shocked_talk at left
        show effw confused at right
        pov "So that’s it?"
        show pov angry_talk at left
        show effw bored at right
        pov "Just like that, I’m asking you for help and you just shut me out completely, no explanation, no nothing?"
        show pov smirk_talk at left
        pov "That’s just how it is?"
        show pov smirk at left
        show effw bored_talk at right
        eff "Yeah."
        eff "Yeah, that’s exactly how it is."
        show pov bored at left
        show effw angry_talk at right
        eff "It doesn’t make me happy, but it's where I draw the line."
        show pov smirk at left
        show effw bored_talk at right
        eff "I’m not going to apologize about it."
        show pov smirk_talk at left
        show effw bored at right
        pov "Wow…"
        pov "Just… Wow."
        show pov angry_talk at left
        show effw angry at right
        pov "I thought we-"
        show pov shocked at left
        show effw angry_talk at right
        eff "Well, you thought wrong!"
        show pov angry_talk at left
        show effw bored at right
        pov "..."
        show pov angry at left
        show effw bored_talk at right
        eff "P-Please get out of here and don’t make it even harder than it is."
        show pov angry_talk at left
        show effw angry at right
        pov "…"
        show pov bored_talk at left
        show effw sad at right
        pov "Fine…"
        pov "Goodbye..."

        ##-Mc leaves upset and a crack on Effie’s face is visible from the way he says goodbye-


        ##=SCENE END=

        $ investigations_effie = 1
        #$ townmap_enabled = 1
        #$ main_story = 84.5

    jump lbl_cafeinside_day_setup
