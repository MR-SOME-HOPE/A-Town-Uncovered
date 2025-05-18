## Safety and Home Life
default told_mom_and_sis_about_sex_maniac = False

label lbl_safety_and_home_life:
    scene bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_confused_talk
    with fade
    #"You are then seated in the dining room with Mom and Sister, Mom is looking quite nervous and sister starts asking what's going on."
    if winc == 1:
        sis "Mom, if this is about what's happening around the town-"
    else:
        sis "[missus], if this is about what's happening around the town-"

    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show sisexpression postnewsbreakfast_confused
    mum "It’s not just about that I asked to talk to you two."
    show eyessis postnewsbreakfast_lookmum
    show sisexpression postnewsbreakfast_embarrassed
    mum "…"
    show eyespov postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_confused
    mum "Kids, I have been really struggling lately with feeling safe in this town."
    mum "After what happened, I have started feeling watched constantly everytime I go outside. "
    mum "Something that while I am particularly used to thanks to my…"
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_sad
    show sisexpression postnewsbreakfast_sad
    mum "Body shape…"
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    mum "It's no less reason to be concerned."
    if winc ==1:
        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        mum "So, after having a long conversation with your father, we agreed to reach a sort of middle ground regarding home security."
        show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_confused_talk
        sis "What does that mean?"
        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_bored_talk
        sis "Are we getting a guard dog or something?"
        show eyessis postnewsbreakfast_lookmum
        show sisexpression postnewsbreakfast_shocked
        mum "That was one of my suggestions actually."
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_confused
        mum "But your father was very firm in his 'no animals' rule, so that quickly went down the drain."
    else:
        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        mum "So, after having a long conversation with your [dadrole], we agreed to reach a sort of middle ground regarding home security."
        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        show sisexpression postnewsbreakfast_confused_talk
        sis "What does that mean?"
        sis "Are we getting a guard dog or something?"
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_confused
        mum "That was one of my suggestions actually."
        mum "But your [dadrole] was very firm in his 'no animals' rule, so that quickly went down the drain."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_angry
    mum "Ugh, it took me ages to convince him to agree to do anything to make this house feel safer and he still has the nerve of giving me an attitude about it!"
    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_angry_talk
    sis "Are you honestly surprised? That man lives in his office so he doesn't have to worry about safety in the house."
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_angry
    mum "Well, regardless of that, I managed to get him to agree in hiring someone to install a security system around the house."
    mum "Cameras, an alarm, some locks, the whole beeswax."
    mum "That’s what you kids say this days, right?"
    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_confused_talk
    sis "Uh..."
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show povexpression postnewsbreakfast_bored_talk
    show sisexpression postnewsbreakfast_confused
    pov "Right..."
    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyessis postnewsbreakfast_lookmum
    pov "So, is that all of what you wanted to talk about?"
    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_confused
    mum "Well, not exactly…"
    show eyespov postnewsbreakfast_lookmum
    mum "I wanted to check on the two of you and see how you were handling everything."
    show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_bored
    mum "I mean, we still haven’t really have a conversation about [povname]’s… “Park Incident” and how that is affecting him."

        #-If Mom caught you and sister in jail-
    if sister_path >= 20:
        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_embarrassed
        mum "Not to mention how the two of you got yourselves in jail…"
        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookmum
        show sisexpression postnewsbreakfast_embarrassed_talk
        sis "I was kinda hoping you had forgotten about that by now."

            #-If she caught you after the handjob-
        if siblingjailtime_hj == 1:
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_embarrassed
            mum "And don’t even get me started about what I caught the two of you doing in there"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_embarrassed
            pov "Well, she certainly didn’t forget…"

    #=RESULT END#=
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_confused
    pov "I still call myself a victim of circumstances, by the way."
    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_bored_talk
    sis "Not helping, [povname]."
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_shocked
    show sisexpression postnewsbreakfast_shocked
    mum "Anyway!"
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_confused
    mum "While there is still a lot we need to talk about as a family, I mainly called you both here because I want to know if there is anything you two feel like telling me."
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    mum "Right now, the two of you are the only real people I can trust, so I want to build an area of trust between us so you guys can feel safe in telling me if anything is bothering you or if you need to get something off your chest."
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused_talk
    show sisexpression postnewsbreakfast_confused
    pov "Uh…"
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_embarrassed_talk
    sis "Um…"
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show sisexpression postnewsbreakfast_embarrassed
    mum "Come on now, is there anything you guys would like to talk to me about?"
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    mum "Anything I should know or that you want to tell me?"
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_bored
    "As she says this, it’s clear she expects you to be the one opening up as both her and sister turn to look at you, expecting you to say something."
    show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_bored_talk
    pov "W-Well…"

    #=CHOICE#=
    menu menu_conversation_about_safety_and_home_life:
        "Talk about what happened at university" if mainstory_62_crossroads_home == 0 and not told_mom_and_sis_about_sex_maniac:
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_shocked
            pov "Well, some sex maniac at uni was arrested today?"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_bored
            mum "What?!"
            if winc == 1:
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
                show eyespov postnewsbreakfast_looksis
                show sisexpression postnewsbreakfast_shocked_talk
                sis "Damn, bro."
            else:
                show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
                show eyespov postnewsbreakfast_lookfood
                show sisexpression postnewsbreakfast_smirk_talk
                sis "Damn, [povname]."
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_smirk
            show sisexpression postnewsbreakfast_smirk_talk
            sis "Wait, it isn’t you this time, right?"
            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_smirk_talk
            show sisexpression postnewsbreakfast_smirk
            pov "Very funny, [sister]."
            show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
            show povexpression postnewsbreakfast_bored
            show sisexpression postnewsbreakfast_smirk_talk
            sis "Hey, “if the shoe fits” and all."
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookmum
            show sisexpression postnewsbreakfast_shocked
            mum "Can you two stop fighting and go back to the story?!"
            if winc == 1:
                show povexpression postnewsbreakfast_bored_talk
                show sisexpression postnewsbreakfast_bored_talk
                "[sister] & [povname]" "Sorry, Mom."
            else:
                show povexpression postnewsbreakfast_bored_talk
                show sisexpression postnewsbreakfast_bored_talk
                "[sister] & [povname]" "Sorry, [missus]."
            show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_bored_talk
            show sisexpression postnewsbreakfast_confused
            pov "Anyway as I was saying."
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show sisexpression postnewsbreakfast_shocked
            pov "Once the assembly ended and we finished up with classes, some girl was found outside covered in god-knows-what and masturbating like her life depended on it."
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_shocked_talk
            show sisexpression postnewsbreakfast_confused
            pov "She was begging for someone to fuck her and-"
            show povexpression postnewsbreakfast_shocked
            show sisexpression postnewsbreakfast_shocked
            mum "Language!"
            if winc == 1:
                show povexpression postnewsbreakfast_embarrassed_talk
                pov "Sorry mom, but that's what she said."
            else:
                show povexpression postnewsbreakfast_embarrassed_talk
                pov "Sorry [missus], but that's what she said."
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_shocked_talk
            show sisexpression postnewsbreakfast_confused
            pov "She was begging for someone to “Do her” until Officer Mina came in. "
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_bored
            pov "Apparently the two of them have a history since the girl started calling her Mistress and begging her to bring the guards and do… Other stuff to her, until Officer Mina took her away."
            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_confused_talk
            show sisexpression postnewsbreakfast_confused
            pov "She seemed to be on drugs or something, I didn’t really stick around once they put her in cuffs but it seemed people knew her."
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            pov "Apparently she disappeared two years ago and this is the first time anyone has seen her since."
            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_confused
            show sisexpression postnewsbreakfast_bored
            mum "How horrible it must be for the poor family to be notified of their daughter being found in such a state."
            mum "More so after the tragedy that happened!"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_bored
            show sisexpression postnewsbreakfast_confused_talk
            sis "Did you happen to hear what they are going to do to her?"
            show bg postnewsbreakfast_pov_eats_sis_eats_mum_eats
            show eyespov postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_confused
            pov "Not really, once Mina drove off with her, I got out of there before I somehow got myself in trouble."
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed
            mum "Good."
            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_smirk
            show sisexpression postnewsbreakfast_smirk_talk
            sis "Smart move!"
            sis "You are a trouble magnet after all."
            show bg postnewsbreakfast_pov_eats_sis_eats_mum_eats
            show eyespov postnewsbreakfast_looksis
            show povexpression postnewsbreakfast_bored_talk
            show sisexpression postnewsbreakfast_smirk
            pov "Gee, thanks…"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_bored
            mum "But this is exactly what I am talking about."
            show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
            show eyessis postnewsbreakfast_lookmum
            mum "Really weird things are happening around the town so I expect you guys to let me know if anything is happening in your lives that I should be aware of."
            $ told_mom_and_sis_about_sex_maniac = True
            jump menu_conversation_about_safety_and_home_life

        "Calm them down.":
            $ add_points("mum_points",1)
            $ add_points("sister_points",1)
            if winc == 1:
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
                show eyessis postnewsbreakfast_lookpov
                show povexpression postnewsbreakfast_embarrassed_talk
                show sisexpression postnewsbreakfast_embarrassed
                pov "Mom, I really don’t know what you want me to tell you."
            else:
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
                show eyessis postnewsbreakfast_lookpov
                show povexpression postnewsbreakfast_embarrassed_talk
                show sisexpression postnewsbreakfast_embarrassed
                pov "[missus], I really don’t know what you want me to tell you."

            show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_shocked
            show sisexpression postnewsbreakfast_smirk_talk
            sis "How about the truth about your whole nude escapade?"
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_shocked_talk
            show sisexpression postnewsbreakfast_smirk
            pov "What’s there to say I haven’t told you?"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show povexpression postnewsbreakfast_bored_talk
            pov "I got drugged, likely by some punks picking on the new kid, and the last thing I remember was waking up on the park naked."
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_shocked
            show sisexpression postnewsbreakfast_smirk
            mum "That still leaves a lot of questions, [povname]."
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_bored_talk
            pov "I wish I had more to tell you, but even I don’t remember where I could have been drugged."
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_smirk
            pov "So until something jogs my memory, I told you all I know."
            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            pov "(Liar.)"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed
            mum "…"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show sisexpression postnewsbreakfast_smirk
            sis "…"

                    #-If the player has a charisma of 7 to 10-
            if 7 <= skill_cha <= 10:
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
                show eyespov postnewsbreakfast_lookmum
                show eyessis postnewsbreakfast_lookfood
                show povexpression postnewsbreakfast_embarrassed_talk
                pov "Look, I know that it’s not much…"
                pov "But I am safe. That has to count for something, right?"
                show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
                show eyessis postnewsbreakfast_lookmum
                show povexpression postnewsbreakfast_embarrassed
                show sisexpression postnewsbreakfast_confused
                mum "Oh sweet heart, it counts for everything."
                mum "I’m sorry we keep bringing this up; there are just a lot of things regarding that night, I wish I had answers to."
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
                show eyespov postnewsbreakfast_lookfood
                show eyessis postnewsbreakfast_lookpov
                show povexpression postnewsbreakfast_bored_talk
                pov "You and me both."
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
                show eyessis postnewsbreakfast_lookmum
                show povexpression postnewsbreakfast_bored_talk
                pov "But sadly, I don’t have much, besides what I already told you."
                show eyespov postnewsbreakfast_lookfood
                show eyessis postnewsbreakfast_lookpov
                pov "And if it’s alright with you, I’d just rather forget it even happened, to be honest."
                show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
                pov "I already get reminded of it plenty at uni and around the town."
                show sisexpression postnewsbreakfast_embarrassed
                pov "I am just glad to be home safe."

                #+1 Mom and Sister Rp.
                $ add_points("mum_points",1)
                $ add_points("sister_points",1)
                show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
                show povexpression postnewsbreakfast_bored
                show sisexpression postnewsbreakfast_embarrassed_talk
                sis "We are glad you are safe, bro."
                show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
                show eyessis postnewsbreakfast_lookmum
                show povexpression postnewsbreakfast_embarrassed
                sis "We’ll tone it down with the questions."
                show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
                show eyessis postnewsbreakfast_lookpov
                show povexpression postnewsbreakfast_embarrassed_talk
                show sisexpression postnewsbreakfast_neutral
                pov "Thank you."
                show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
                show eyespov postnewsbreakfast_looksis
                show eyessis postnewsbreakfast_lookmum
                show povexpression postnewsbreakfast_bored
                show sisexpression postnewsbreakfast_confused
                mum "Well, what about you, [sister]?"
                mum "There are also a couple of things I want to ask you about."
                show bg postnewsbreakfast_pov_eats_sis_idle_mum_eats
                show eyessis postnewsbreakfast_lookpov
                show sisexpression postnewsbreakfast_confused_talk
                sis "Uhh…"
                show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
                show eyespov postnewsbreakfast_lookmum
                show eyessis postnewsbreakfast_lookfood
                show povexpression postnewsbreakfast_bored_talk
                show sisexpression postnewsbreakfast_bored
                pov "Well, if you don’t mind. I’ll head upstairs."
                pov "It’s been a really long day and I need to sleep."
                show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
                show eyespov postnewsbreakfast_looksis
                show eyessis postnewsbreakfast_lookpov
                show povexpression postnewsbreakfast_embarrassed
                show sisexpression postnewsbreakfast_confused
                mum "Go ahead, [povname]."
                show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
                show eyespov postnewsbreakfast_lookmum
                show eyessis postnewsbreakfast_lookmum
                mum "But next family talk, I expect you to stay for the whole thing."
                if winc == 1:
                    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
                    show eyessis postnewsbreakfast_lookpov
                    show povexpression postnewsbreakfast_embarrassed_talk
                    show sisexpression postnewsbreakfast_bored
                    pov "You got it, Mom."
                else:
                    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
                    show eyessis postnewsbreakfast_lookpov
                    show povexpression postnewsbreakfast_embarrassed_talk
                    show sisexpression postnewsbreakfast_bored
                    pov "You got it, [missus]."
            else:
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
                show eyespov postnewsbreakfast_lookfood
                show eyessis postnewsbreakfast_lookmum
                show povexpression postnewsbreakfast_bored_talk
                show sisexpression postnewsbreakfast_embarrassed
                pov "I’m going to my room now, it’s been a long day."
    #=OR#=
        "Change the subject.":
        #=CHOICE END#=
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_smirk_talk
            show sisexpression postnewsbreakfast_confused
            pov "There is the whole thing about the town being vandalized. How crazy is that, am I right?"
            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed
            mum "W-Well, yeah, of course."
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_shocked
            mum "But that’s not what I was hoping to talk abou-"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_shocked_talk
            show sisexpression postnewsbreakfast_shocked
            pov "The cafe, my friend Effie works at, also got trashed. Not to mention the beach and of course the university."
            show eyespov postnewsbreakfast_looksis
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_confused_talk
            sis "[povname], I don’t think she-"
            show eyespov postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_confused
            pov "Oh! They also told us to let you know that the police chief is making an interview later tonight and broadcasting it on the local network, so better keep an eye on the tv, right?"
            show eyespov postnewsbreakfast_looksis
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_bored
            mum "I-I’ll be sure to tune into it, but-"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_confused
            pov "Hey, have you done something to your hair?"
            if winc == 1:
                show povexpression postnewsbreakfast_embarrassed
                show sisexpression postnewsbreakfast_shocked_talk
                "Mom and sis" "[povname]!"
            else:
                show eyespov postnewsbreakfast_lookmum
                show povexpression postnewsbreakfast_embarrassed
                show sisexpression postnewsbreakfast_shocked_talk
                "[missus] and [sister]" "[povname]!"

            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_bored
            pov "What?!"
            show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_shocked
            mum "While all of that is important, it’s clearly not what I want to talk about right now!"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show povexpression postnewsbreakfast_angry_talk
            pov "And what do you want to talk about?!"
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_shocked
            show sisexpression postnewsbreakfast_angry_talk
            sis "Your whole “Night in the woods” deal!"
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_angry_talk
            show sisexpression postnewsbreakfast_bored
            pov "Something I clearly don’t want to talk about!"
            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show povexpression postnewsbreakfast_angry
            mum "[povname], please. There are still a lot questions in your story and-"
            if winc == 1:
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
                show eyespov postnewsbreakfast_lookmum
                show povexpression postnewsbreakfast_angry_talk
                show sisexpression postnewsbreakfast_shocked
                pov "Mom, please!"
            else:
                show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
                show eyespov postnewsbreakfast_lookmum
                show povexpression postnewsbreakfast_angry_talk
                show sisexpression postnewsbreakfast_shocked
                pov "[missus], please!"

            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_bored_talk
            show sisexpression postnewsbreakfast_confused
            pov "I woke up naked by the side of the lake unsure of what I actually did for twenty four hours."
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_angry_talk
            pov "And now I'm constantly reminded of it everywhere I go!"
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookmum
            show sisexpression postnewsbreakfast_bored
            pov "Can’t I catch a break at home at the very least?!"

            #-1 Mom and Sister Rp
            $ subtract_points("mum_points",1)
            $ subtract_points("sister_points",1)

            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_bored
            show sisexpression postnewsbreakfast_confused
            mum "…"
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_angry
            sis "…"
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_bored_talk
            show sisexpression postnewsbreakfast_bored
            pov "I’m going to my room now, it’s been a long day."

    $ main_story = 67

    scene bg mybedroom_day
    with fade

    jump lbl_mybedroom_day_setup
