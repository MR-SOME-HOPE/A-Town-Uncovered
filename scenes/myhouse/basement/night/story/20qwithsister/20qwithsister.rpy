## 20Q with Sister ##
label lbl_20q_with_sister:
    default twentyqwithsister_q1 = 0
    default twentyqwithsister_q2 = 0
    default twentyqwithsister_q3 = 0
    default twentyqwithsister_q4 = 0
    default twentyqwithsister_q5 = 0
    default twentyqwithsister_q6 = 0
    default twentyqwithsister_q7 = 0
    default twentyqwithsister_q8 = 0
    default twentyqwithsister_q9 = 0
    default twentyqwithsister_q10 = 0
    default twentyqwithsister_q11 = 0
    default twentyqwithsister_q12 = 0
    default twentyqwithsister_q13 = 0
    default twentyqwithsister_q14 = 0
    default twentyqwithsister_q15 = 0
    default twentyqwithsister_q16 = 0
    default twentyqwithsister_q17 = 0
    default twentyqwithsister_q18 = 0
    default twentyqwithsister_q19 = 0
    default twentyqwithsister_q20 = 0
    default twentyqwithsister_qc = 0
    default twentyqwithsister_qsis = 0
    default twentyqwithsister_sispass = 0
    default twentyqwithsister_povpass = 0
    default twentyqwithsister_honest = 0
    default twentyqwithsister_camgurl = 0

    scene bg 20qwithsister_1
    with fade
    sis "Alright, why did you drag me down here for?"
    show bg 20qwithsister_2
    if winc == 0:
        pov "Does a [povsisrole] need a reason to want to spend time with his beloved [sisrole]?"
    else:
        pov "Does a brother need a reason to want to spend time with his beloved sister?"
    show bg 20qwithsister_1
    sis "When it's you, he does."
    show bg 20qwithsister_3
    pov "Ouchie."
    show bg 20qwithsister_4
    pov "But really, I just wanted to y'know. Hang out together. Play a little game."
    show bg 20qwithsister_5
    sis "You... you wanna play... doctor?"

    menu:
        "YES!":
            show bg 20qwithsister_3
            pov "YES!"
            show bg 20qwithsister_6
            sis "Hahaha, you're embarrassingly desperate, y'know that?"
            sis "Lucky that you're not being desperate in front of anyone else."
            show bg 20qwithsister_1
            sis "I was joking by the way, we ain't playing doctor tonight."
            show bg 20qwithsister_2
            pov "So another night?"
            show bg 20qwithsister_1
            sis "Shut up. [povname]."
            show bg 20qwithsister_2
            pov "Hehe, well anyway..."
        "Yeah.. but...":
            show bg 20qwithsister_7
            pov "Yeah.. but I had something else in mind."
            show bg 20qwithsister_5
            sis "Ohh? What is it?"
        "Not really.":
            show bg 20qwithsister_7
            pov "Not really, I have something else in mind."
            show bg 20qwithsister_6
            sis "Really? Not even a little bit interested? Hmm, alright, what do you have in mind?"
        "No...":
            show bg 20qwithsister_7
            pov "No..."
            show bg 20qwithsister_5
            sis "Wow, don't have to be so cold about it, even if I was joking, which I am."
            sis "Well, what ideas do you have?"
    show bg 20qwithsister_7
    pov "I was thinking we could play 20Q."
    show bg 20qwithsister_5
    sis "You mean, the game where either one of us has to think of a thing and the other has to guess what that thing is?"
    show bg 20qwithsister_7
    pov "Uh... the other... version?"
    show bg 20qwithsister_5
    sis "Explain?"
    show bg 20qwithsister_4
    pov "The one where we ask each other 20 questions?"
    show bg 20qwithsister_8
    sis "... Fair enough."
    show bg 20qwithsister_4
    pov "You in?"
    show bg 20qwithsister_6
    sis "Well, it's obviously not fun with one person."
    show bg 20qwithsister_8
    sis "But an extra rule. We are each allowed 5 passes at any time, no sub-questions asked."
    show bg 20qwithsister_1
    sis "Yes or no questions only. Any additional information is up to the person."
    show bg 20qwithsister_4
    pov "Sounds fair to me."
    show bg 20qwithsister_8
    sis "Youngest first, baby boy."

label lbl_20q_with_sister_pov1:                      # Do you parttake in livecamming?

    menu:
        "Do you parttake in livecamming?" if twentyqwithsister_q1 == 0:
            $ twentyqwithsister_q1 = 1
            if (day == 6 or sister_points <= 7) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_9
                sis "Pass."
            elif twentyqwithsister_qc <= 15:
                $ twentyqwithsister_camgurl = 1
                show bg 20qwithsister_9
                sis "I have... partaken?"
                show bg 20qwithsister_10
                pov "Really now?"
                show bg 20qwithsister_9
                sis "I've answered your question, let's move on."
            else:
                $ twentyqwithsister_camgurl = 1
                show bg 20qwithsister_9
                sis "I... do."
                show bg 20qwithsister_11
                pov "So you DO livecam!"
                show bg 20qwithsister_5
                sis "What do you mean, I DO livecam? How did you know that I was even involved with that?"
                show bg 20qwithsister_12
                pov "That is for me to know and for you to find out?"
                show bg 20qwithsister_13
                sis "[povname]!"
                show bg 20qwithsister_12
                if winc == 0:
                    pov "Keep your voice down, [missus] and [dadname] are sleeping."
                else:
                    pov "Keep your voice down, Mom and Dad are sleeping."
                show bg 20qwithsister_13
                sis "[povname]... how did you know I livecammed? You don't just ask a girl that out of the blue."
                show bg 20qwithsister_12
                pov "..."
                pov "I found out about it from a scrunched up note you had in your room."
                show bg 20qwithsister_13
                sis "You fucker, you were in my room?!"
                show bg 20qwithsister_12
                pov "Shhhhh!"
                pov "Look, I'm sorry about that but-"
                show bg 20qwithsister_1
                if winc == 0:
                    pov "But- we're [sisrole]s. There shouldn't be any secrets between us."
                else:
                    pov "But- we're twins. There shouldn't be any secrets be'twin' us."
                show bg 20qwithsister_2
                sis "Lets-"
                sis "Let's just get on with the game. We'll discuss this another time."
                show bg 20qwithsister_13
                sis "And don't you fucking dare tell a single fucking soul or I will hate you for eternity."
                sis "I'm not kidding."
                show bg 20qwithsister_12
                pov "Alright, alright. You can trust me."
                show bg 20qwithsister_1
                pov "You should be trusting me, y'know?"
                sis "..."

            jump lbl_20q_with_sister_sisq
        "Did you lose your v-card at an early age?" if twentyqwithsister_q2 == 0:
            $ twentyqwithsister_q2 = 1
            if (day == 5 or sister_points <= 3) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_1
                sis "Pass."
            else:
                show bg 20qwithsister_8
                sis "I lost it first year of highschool."
                show bg 20qwithsister_7
                pov "With who?"
                show bg 20qwithsister_6
                sis "Too many questions, it's my turn."

            jump lbl_20q_with_sister_sisq
        "Are you okay?" if twentyqwithsister_q3 == 0:
            $ twentyqwithsister_q3 = 1
            if day == 0 and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_5
                sis "Pass."
            else:
                show bg 20qwithsister_5
                sis "Yeah? Was that your question?"
                show bg 20qwithsister_2
                pov "Yeah, was that yours?"
                show bg 20qwithsister_1
                sis "Don't be a smart-fuck. It's still my turn."

            jump lbl_20q_with_sister_sisq
        "Do you wish you'd have went to university?" if twentyqwithsister_q4 == 0:
            $ twentyqwithsister_q4 = 1
            if day == 1 and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_1
                sis "Pass."
            else:
                show bg 20qwithsister_8
                sis "Nope. I think I'd be in a mentally draining situation if I was."
                sis "It's just so freeing to not be there."
                show bg 20qwithsister_6
                sis "No 'ragrets', am I right?"

            jump lbl_20q_with_sister_sisq
        "Have you done drugs?" if twentyqwithsister_q5 == 0:
            $ twentyqwithsister_q5 = 1
            if (day == 4 or sister_points <= 2) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_1
                sis "Pass."
            else:
                show bg 20qwithsister_1
                sis "Nope, and I don't plan on it."
                show bg 20qwithsister_2
                pov "You don't wanna get in with the cool kids?"
                show bg 20qwithsister_1
                sis "I couldn't give 3 shits about that at this point."

            jump lbl_20q_with_sister_sisq

label lbl_20q_with_sister_pov2:                      # Can you feel the love tonight?

    menu:
        "Can you feel the love tonight?" if twentyqwithsister_q6 == 0:
            $ twentyqwithsister_q6 = 1
            if day == 2 and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_5
                sis "Pass."
            else:
                show bg 20qwithsister_6
                sis "Between you and me? Hah, nope."
                show bg 20qwithsister_3
                pov "I detect a liar in our presence."
                show bg 20qwithsister_6
                sis "Fuck off, you little shit. Of course I love your snarky ass."

            jump lbl_20q_with_sister_sisq
        "Do you have a crush on someone at the moment?" if twentyqwithsister_q7 == 0:
            $ twentyqwithsister_q7 = 1
            if (day == 3 or sister_points <= 2) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_5
                sis "Pass."
            else:
                show bg 20qwithsister_5
                sis "I don't really have ‘crushes' anymore. That's really such a childish term."
                show bg 20qwithsister_3
                pov "So there isn't any person that you have a sexual or romantic interest in?"
                show bg 20qwithsister_6
                sis "I didn't say that at all."

            jump lbl_20q_with_sister_sisq
        "Have you sexually fantasized about me?" if twentyqwithsister_q8 == 0:
            $ twentyqwithsister_q8 = 1
            if (day == 2 or sister_points <= 6) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_9
                sis "Pass."
            else:
                show bg 20qwithsister_10
                sis "..."
                show bg 20qwithsister_9
                if winc == 0:
                    sis "Yes- But hear me out. What curious human being hasn't thought about [povsisrole] like that before?!"
                else:
                    sis "Yes- But hear me out. What curious human being hasn't thought about a sibling like that before?!"
                show bg 20qwithsister_13
                sis "It's just normal to curiously wonder, okay? Don't fuckin' hold that against me."

            jump lbl_20q_with_sister_sisq
        "Are you bisexual?" if twentyqwithsister_q9 == 0:
            $ twentyqwithsister_q9 = 1
            if (day == 1 or sister_points <= 4) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_5
                sis "Pass."
            else:
                show bg 20qwithsister_5
                sis "Are you asking because of Effie?"
                show bg 20qwithsister_3
                pov "She's contacted you?"
                show bg 20qwithsister_6
                sis "Yes... and yes. Moving on."

            jump lbl_20q_with_sister_sisq
        "Do you honestly like this new town?" if twentyqwithsister_q10 == 0:
            $ twentyqwithsister_q10 = 1
            if day == 3 and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_1
                sis "Pass."
            else:
                show bg 20qwithsister_6
                sis "Y'know. It's not perfect, but it does have a charm about it. I'll say yeah."
                show bg 20qwithsister_7
                pov "You thinking of staying for a long time though?"
                show bg 20qwithsister_5
                sis "What did I say about no sub-questions? It's my turn."

            jump lbl_20q_with_sister_sisq

label lbl_20q_with_sister_pov3:                      # Have you ever done it in a public place?

    menu:
        "Have you ever done it in a public place?" if twentyqwithsister_q11 == 0:
            $ twentyqwithsister_q11 = 1
            if (day == 0 or sister_points <= 3) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_5
                sis "Pass."
            else:
                show bg 20qwithsister_5
                sis "Does the public toilets count? If so, then yeah."
                show bg 20qwithsister_7
                pov "Sorta, not really though? It's kind of a grey area."
                show bg 20qwithsister_8
                sis "Well, you can decide that for yourself."

            jump lbl_20q_with_sister_sisq
        "Hello... is it me you're looking for?" if twentyqwithsister_q12 == 0:
            $ twentyqwithsister_q12 = 1
            if day == 4 and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_1
                sis "Pass."
            else:
                show bg 20qwithsister_5
                sis "I can see it in your eyes?"
                show bg 20qwithsister_2
                pov "You didn't answer the question."
                show bg 20qwithsister_1
                sis "No, my answer is no. Great question, now it's my turn."

            jump lbl_20q_with_sister_sisq
        "Do you ever regret your previous life decisions?." if twentyqwithsister_q13 == 0:
            $ twentyqwithsister_q13 = 1
            if (day == 6 or sister_points <= 2) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_1
                sis "Pass."
            else:
                show bg 20qwithsister_1
                sis "Don't we all. Whatever my answer is, it won't change the past."
                show bg 20qwithsister_2
                pov "That's deep."
                show bg 20qwithsister_6
                sis "Deep for your pre-pubescent brain, borderline shallow for mine."

            jump lbl_20q_with_sister_sisq
        "Have you ever seen Mom or Dad naked in the past 5 years?" if twentyqwithsister_q14 == 0 and winc == 1:
            $ twentyqwithsister_q14 = 1
            if (day == 5 or sister_points <= 3) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_5
                sis "Pass."
            else:
                show bg 20qwithsister_14
                sis "I have. I've seen them going at it. It's..."
                if mum_path >= 7:
                    show bg 20qwithsister_11
                    pov "I know... me too."
                    show bg 20qwithsister_15
                    sis "You too?! They... need to turn it down like 100 notches."
                else:
                    show bg 20qwithsister_10
                    pov "Ew... just, no. Shut up. Forget I asked that."
                    show bg 20qwithsister_9
                    sis "Ditto, but that question still counts as 1."

            jump lbl_20q_with_sister_sisq
        "Have you ever seen [missus] or [dadname] naked in the past 5 years?" if twentyqwithsister_q14 == 0 and winc == 0:
            $ twentyqwithsister_q14 = 1
            if (day == 5 or sister_points <= 3) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_5
                sis "Pass."
            else:
                show bg 20qwithsister_14
                sis "I have. I've seen them going at it. It's..."
                if mum_path >= 7:
                    show bg 20qwithsister_11
                    pov "I know... me too."
                    show bg 20qwithsister_15
                    sis "You too?! They... need to turn it down like 100 notches."
                else:
                    show bg 20qwithsister_10
                    pov "Ew... just, no. Shut up. Forget I asked that."
                    show bg 20qwithsister_9
                    sis "Ditto, but that question still counts as 1."

            jump lbl_20q_with_sister_sisq
        "Are you proud of your job?" if twentyqwithsister_q15 == 0:
            $ twentyqwithsister_q15 = 1
            if (day == 4 or sister_points <= 6) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_9
                sis "Pass."
            else:
                show bg 20qwithsister_14
                sis "... No. I'm not proud of it."
                show bg 20qwithsister_10
                pov "Is that why you don't share what your job is with me?"
                show bg 20qwithsister_16
                sis "Mhmm."

            jump lbl_20q_with_sister_sisq

label lbl_20q_with_sister_pov4:                      # Do you think I'm a good brother?

    menu:
        "Do you think I'm a good brother?" if twentyqwithsister_q16 == 0 and winc == 1:
            $ twentyqwithsister_q16 = 1
            if (day == 3 or sister_points <= 2) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_6
                sis "Pass."
            else:
                show bg 20qwithsister_9
                if winc == 0:
                    sis "I think you're the best [povsisrole] I could ever ask for."
                else:
                    sis "I think you're the best brother I could ever ask for."
                sis "As unoriginal as that sounds, it's true."
                sis "My turn."

            jump lbl_20q_with_sister_sisq
        "Do you think I'm a good [povsisrole]?" if twentyqwithsister_q16 == 0 and winc == 0:
            $ twentyqwithsister_q16 = 1
            if (day == 3 or sister_points <= 2) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_6
                sis "Pass."
            else:
                show bg 20qwithsister_9
                if winc == 0:
                    sis "I think you're the best [povsisrole] I could ever ask for."
                else:
                    sis "I think you're the best brother I could ever ask for."
                sis "As unoriginal as that sounds, it's true."
                sis "My turn."

            jump lbl_20q_with_sister_sisq
        "Have you slept with more than 5 guys?" if twentyqwithsister_q17 == 0:
            $ twentyqwithsister_q17 = 1
            if (day == 2 or sister_points <= 4) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_5
                sis "Pass."
            else:
                show bg 20qwithsister_5
                sis "At the same time? Actually, don't answer that. My answer is yes."
                show bg 20qwithsister_3
                pov "Now I'm curious..."
                show bg 20qwithsister_6
                sis "To save you a question, no it wasn't."

            jump lbl_20q_with_sister_sisq
        "Would you consider living with me, if either of us move out?" if twentyqwithsister_q18 == 0:
            $ twentyqwithsister_q18 = 1
            if (day == 1 or sister_points <= 4) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_9
                sis "Pass."
            else:
                show bg 20qwithsister_8
                sis "I would. If you're alright with that idea."
                show bg 20qwithsister_9
                sis "I mean, it's not weird for us to do that right? It's just room-mating...?"
                show bg 20qwithsister_15
                sis "I didn't mean... matin- nevermind."

            jump lbl_20q_with_sister_sisq
        "Do you remember when we used to play doctor?" if twentyqwithsister_q19 == 0:
            $ twentyqwithsister_q19 = 1
            if (day == 0 or sister_points <= 3) and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_9
                sis "Pass."
            else:
                show bg 20qwithsister_6
                sis "Of course I have, I'm sure even if you're a kid, it's not something you'd forget."
                show bg 20qwithsister_4
                if winc == 0:
                    pov "Oh, the looks on [missus] and [dadname]'s face when they found out about our wrong doings."
                else:
                    pov "Oh, the looks on Mom and Dad's face when they found out about our wrong doings."
                show bg 20qwithsister_6
                sis "We didn't know it was wrong, did we? Don't answer that."

            jump lbl_20q_with_sister_sisq
        "Have you decided on your next plan?" if twentyqwithsister_q20 == 0:
            $ twentyqwithsister_q20 = 1
            if day == 5 and twentyqwithsister_sispass <= 4:
                $ twentyqwithsister_sispass += 1
                show bg 20qwithsister_9
                sis "Pass."
            else:
                show bg 20qwithsister_14
                sis "{i}*Sigh*{/i} Honestly, no. I'm too busy trying to get through each day at a time."
                sis "I don't have a long term answer."
                show bg 20qwithsister_9
                sis "I don't know if I even want to think about my future, scarily enough."

            jump lbl_20q_with_sister_sisq

label lbl_20q_with_sister_sisq:
    $ twentyqwithsister_qc += 1
    if twentyqwithsister_qsis == 0:
        if day == 0:
            $ twentyqwithsister_qsis = 1
        elif day == 1:
            $ twentyqwithsister_qsis = 4
        elif day == 2:
            $ twentyqwithsister_qsis = 7
        elif day == 3:
            $ twentyqwithsister_qsis = 10
        elif day == 4:
            $ twentyqwithsister_qsis = 14
        elif day == 5:
            $ twentyqwithsister_qsis = 17
        elif day == 6:
            $ twentyqwithsister_qsis = 19
    if twentyqwithsister_qsis == 1:
        jump lbl_20q_with_sister_sisq1
    elif twentyqwithsister_qsis == 2:
        jump lbl_20q_with_sister_sisq2
    elif twentyqwithsister_qsis == 3:
        jump lbl_20q_with_sister_sisq3
    elif twentyqwithsister_qsis == 4:
        jump lbl_20q_with_sister_sisq4
    elif twentyqwithsister_qsis == 5:
        jump lbl_20q_with_sister_sisq5
    elif twentyqwithsister_qsis == 6:
        jump lbl_20q_with_sister_sisq6
    elif twentyqwithsister_qsis == 7:
        jump lbl_20q_with_sister_sisq7
    elif twentyqwithsister_qsis == 8:
        jump lbl_20q_with_sister_sisq8
    elif twentyqwithsister_qsis == 9:
        jump lbl_20q_with_sister_sisq9
    elif twentyqwithsister_qsis == 10:
        jump lbl_20q_with_sister_sisq10
    elif twentyqwithsister_qsis == 11:
        jump lbl_20q_with_sister_sisq11
    elif twentyqwithsister_qsis == 12:
        jump lbl_20q_with_sister_sisq12
    elif twentyqwithsister_qsis == 13:
        jump lbl_20q_with_sister_sisq13
    elif twentyqwithsister_qsis == 14:
        jump lbl_20q_with_sister_sisq14
    elif twentyqwithsister_qsis == 15:
        jump lbl_20q_with_sister_sisq15
    elif twentyqwithsister_qsis == 16:
        jump lbl_20q_with_sister_sisq16
    elif twentyqwithsister_qsis == 17:
        jump lbl_20q_with_sister_sisq17
    elif twentyqwithsister_qsis == 18:
        jump lbl_20q_with_sister_sisq18
    elif twentyqwithsister_qsis == 19:
        jump lbl_20q_with_sister_sisq19
    elif twentyqwithsister_qsis == 20:
        jump lbl_20q_with_sister_sisq20

label lbl_20q_with_sister_sisq1:                     # Do you sexually fantasize about Mom?
    show bg 20qwithsister_6
    if winc == 0:
        sis "Do you sexually fantasize about [missus]?"
    else:
        sis "Do you sexually fantasize about Mom?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_3
            pov "Yes, it's natural, look up the oedipus complex."
            show bg 20qwithsister_6
            sis "I know what it is."
            sis "I'm not judging..."
        "No.":
            $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_3
            pov "No."
            show bg 20qwithsister_6
            sis "That's a lie and you know it. I know about the oedipus complex."
            show bg 20qwithsister_3
            pov "Ah... right... gotcha."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_3
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq2:                     # Have you ever touched another dude's dick?
    show bg 20qwithsister_6
    sis "Have you ever touched another dude's dick?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_3
            pov "Yes, accidentally...?"
            show bg 20qwithsister_6
            sis "I doubt it was accidentally."
            show bg 20qwithsister_3
            pov "Why would I even lie about touching another dude's dick."
        "No.":
            if sister_points <= 3:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_7
            pov "Nope, fortunately."
            show bg 20qwithsister_5
            sis "You've never felt another man's dick before?"
            show bg 20qwithsister_6
            sis "For all you know, your dick feels abnormal compared to everyone else's."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_3
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq3:                     # Are you happy with your dick size?
    show bg 20qwithsister_6
    sis "Are you happy with your dick size?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_4
            pov "Yes, I'm glad it's the size it is."
            show bg 20qwithsister_8
            sis "At least you're confident."
            show bg 20qwithsister_3
            pov "At least it's not a micro-penis, is all I'm saying."
        "No.":
            if skill_luc >= 12:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_2
            pov "Nope, wish it was bigger."
            show bg 20qwithsister_1
            sis "Of course you do. To compensate for your lack of personality."
            show bg 20qwithsister_6
            sis "Too bad you're pretty much done growing, I assume."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_7
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq4:                     # Do you jack off in the shower?
    show bg 20qwithsister_6
    sis "Do you jack off in the shower?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_3
            pov "Yes, and I shamelessly watch it go down the drain."
            show bg 20qwithsister_6
            sis "Like Alfie Hitchdick's Psycho."
            show bg 20qwithsister_4
            pov "A genocide of could-have-been mini-me's."
        "No.":
            if sister_points <= 1:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_2
            pov "Nope."
            show bg 20qwithsister_5
            sis "Really? I doubt that very much. I fucking do it."
            sis "It's like the cleanest place to do it."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_7
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq5:                     # Have you gotten laid in the past 24 hours?
    show bg 20qwithsister_6
    sis "Have you gotten laid in the past 24 hours?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            if skill_cha <= 7:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_7
            pov "Yes."
            show bg 20qwithsister_5
            sis "With who?"
            show bg 20qwithsister_2
            pov "Ahem? No sub-questions."
        "No.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_3
            pov "No..."
            show bg 20qwithsister_6
            sis "Naww, that's okay. Not everyone can be a stud."
            show bg 20qwithsister_3
            pov "Just because I haven't in the past 24 hours, doesn't mean I don't get any, you bitch."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_3
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq6:                     # Is your addiction to porn... excessive?
    show bg 20qwithsister_5
    sis "Is your addiction to porn... excessive?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            show bg 20qwithsister_2
            pov "Yes... I uh... really do try to stop. But boobs..."
            show bg 20qwithsister_5
            sis "Porn is great an all, but you should really get out more."
            show bg 20qwithsister_7
            pov "Don't body shame digital boobs. Hashtag free-the-boobs."
        "No.":
            pov "No? Why would you even assume I have an addiction to porn?"
            if inventory.has_item(Items.fbpwmag1):
                $ inventory.drop(Items.fbpwmag1)
                $ fbpwmag1 = 2
                $ twentyqwithsister_honest -= 1
                show bg 20qwithsister_5
                sis "Well, because I found a porno mag in your bag. Who even carries around a porno mag around these days anyway? Addicts I guess?"
                show bg 20qwithsister_7
                pov "Alright, first off. That's an invasion of privacy, and 2nd. I was holding it for a friend."
                show bg 20qwithsister_6
                sis "Mhmm, anyway..."
            else:
                $ twentyqwithsister_honest += 1
                show bg 20qwithsister_6
                sis "Just wondering how you'd react if I made assumptions, that's all."
                show bg 20qwithsister_3
                pov "You sly, asshoe."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_7
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq7:                     # Have you changed that nasty bedsheet of yours since we've moved here?
    show bg 20qwithsister_5
    sis "Have you changed that nasty bedsheet of yours since we've moved here?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            if sister_points <= 1:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_7
            pov "Yes."
            show bg 20qwithsister_13
            sis "Then why does it smell?"
            show bg 20qwithsister_2
            pov "Why are you smelling my bedsheets?"
        "No.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_12
            pov "Nope."
            show bg 20qwithsister_13
            sis "That's gross, dude. Fuckin' change it already."
            show bg 20qwithsister_2
            pov "It's only going to get nasty right away. Stop coming into my room if you hate the scent."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_2
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq8:                     # Did you know what you were doing when you poked me in the face with your dick when were in the tub as kids?
    show bg 20qwithsister_1
    sis "Did you know what you were doing when you poked me in the face with your dick when were in the tub as kids?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            if skill_int >= 13:
                $ twentyqwithsister_honest += 1
            show bg 20qwithsister_2
            pov "Yes, well, at least now I do."
            show bg 20qwithsister_1
            sis "You owe me an apology for that."
            show bg 20qwithsister_3
            pov "Bitch, please. You found it so hilarious you nearly slipped and fell from laughing so hard."
        "No.":
            if skill_int >= 6:
                $ twentyqwithsister_honest += 1
            show bg 20qwithsister_2
            pov "No... that was an oddly specific event in our lifetime."
            show bg 20qwithsister_5
            sis "Well, you did that. And from what I remember, you nudged me so hard that I nearly fell over and died."
            show bg 20qwithsister_2
            pov "I think you're being a little overdramatic. Trust me, I was an innocent kid doing what I thought were innocent things."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_2
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq9:                     # Do you consider yourself good with your tongue?
    show bg 20qwithsister_6
    sis "Do you consider yourself good with your tongue?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            if skill_sta <= 11:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_2
            pov "Yes, why? Do you want me to prove it?"
            show bg 20qwithsister_1
            sis "Boy, put your tongue away. I was asking curiously for the other girls' sake."
            show bg 20qwithsister_11
            pov "Don't hide your true intentions from me, missy. I'm joking, just jokes."
        "No.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_11
            pov "No."
            show bg 20qwithsister_6
            sis "Huh. Just no? Not even going to defend yourself?"
            show bg 20qwithsister_10
            pov "Not gonna lie, my dick is my strong suit."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_6
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq10:                    # Have you ever sexually fantasized about me?
    show bg 20qwithsister_9
    sis "Have you ever sexually fantasized about me?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_10
            if winc == 0:
                pov "Yes... I mean, you're a girl. Just because you're my [sisrole]- It's completely just my brain doing it's own thing, I swear."
            else:
                pov "Yes... I mean, you're a girl. Just because you're my sister- It's completely just my brain doing it's own thing, I swear."
            show bg 20qwithsister_9
            sis "No, I get ya. I totally understand. At least I know you're being honest about it."
            show bg 20qwithsister_10
            pov "It's just human nature- that's all. I've thought about a LOT of nasty things, doesn't mean that I like it..."
        "No.":
            $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_7
            pov "No.."
            show bg 20qwithsister_13
            sis "That's bullshit, and even I know that. As if you've never in your whole life thought about me like that."
            show bg 20qwithsister_6
            sis "I bet you're thinking about it right now since I brought it up. Tsk tsk tsk, pussy."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_10
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq11:                    # Is it uncomfortable having that thing between your legs when you walk?
    show bg 20qwithsister_5
    sis "Is it uncomfortable having that thing between your legs when you walk?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            if skill_cha <= 5:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_2
            pov "Yes. It's just soooo big and it likes to just flop around, y'know?"
            show bg 20qwithsister_6
            sis "Hashtag humble brag."
            show bg 20qwithsister_3
            pov "Just carrying it around between my legs really hurts my back, y'know?"
        "No.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_4
            pov "No. It's just something that us guys are used to, we make do with what we're given."
            show bg 20qwithsister_8
            sis "Must be great not having to wear a bra-like device for your dick."
            show bg 20qwithsister_1
            sis "Ugh, bras' are so fucking uncomfortable."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_7
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq12:                    # Do you think we'll make it through this year alive?
    show bg 20qwithsister_14
    sis "Do you think we'll make it through this year alive?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            show bg 20qwithsister_10
            pov "Yes, just take it one step at a time, I'm here if you need the help."
            show bg 20qwithsister_9
            sis "Thanks, [povname]."
            show bg 20qwithsister_3
            pov "I on the other hand am totally screwed for my finals. Hehehe."
        "No.":
            show bg 20qwithsister_9
            pov "No, we should find a nice place in the backyard to dig our graves."
            show bg 20qwithsister_8
            sis "I got dibs for under the tree."
            show bg 20qwithsister_3
            pov "Actually, just chop me up and make a corpse effigy out of me, I can act as a scarecrow."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_9
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq13:                    # Have you purposely searched for incest porn before?
    show bg 20qwithsister_6
    sis "Have you purposely searched for incest porn before?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            if sister_points >= 4:
                $ twentyqwithsister_honest += 1
            show bg 20qwithsister_7
            pov "Yes, but y'know... the step-family type stuff... they're all obviously fake."
            show bg 20qwithsister_6
            sis "Heh, you vanilla-ass pleb. I search for real incest to see who would actually do it."
            show bg 20qwithsister_1
            sis "Don't look at me like that, other people have searched for far worst."
        "No.":
            $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_3
            pov "No, I've stumbled upon it via suggested videos."
            show bg 20qwithsister_6
            sis "You've still clicked on them, haven't you?"
            show bg 20qwithsister_4
            pov "Totally out of curiosity though... They're very obviously scripted and fictional though, it's not like they're REAL family."
            show bg 20qwithsister_3
            pov "Only a fucking asswipe with a stick shoved so far up their asses would get butthurt over them and think they're real."
            pov "I don't know why faux incest driven porn narratives are getting so much flack and shit when it's not doing any harm to literally ANYONE."
            pov "Whatever floats your boat, whatever gets you off, right? If you don't like it, leave it alone for the people who do. Jesus fucking Christ."
            show bg 20qwithsister_11
            pov "Stop trying to be a SJW and trying to dictate, control, and censor us."
            pov "..."
            pov "Jeez... sorry, I don't know what came over me. I felt like the energy of several dying stars penetrating my body."
            show bg 20qwithsister_6
            sis "... I'm sure those dying stars have made many people's lonely night."
            show bg 20qwithsister_9
            pov "..."
            show bg 20qwithsister_4
            pov "{i}*Ahem*{/i} Moving on."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_6
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq14:                    # Why are you such a cuck? Yes or no?
    show bg 20qwithsister_6
    sis "Why are you such a cuck? Yes or no?"
    $ twentyqwithsister_qsis += 1
    show bg 20qwithsister_3
    pov "What the fuck kind of question is that? That's not even a real yes or no question."
    show bg 20qwithsister_1
    sis "Just answer the damn question."

    menu:
        "Yes.":
            if mum_path >= 7:
                if sister_points <= 9:
                    $ sister_points += 1
                    $ renpy.notify("Relationship with [sister] increased.")
                else:
                    $ sister_points = 10
            show bg 20qwithsister_3
            pov "Yes?"
            show bg 20qwithsister_6
            sis "Fucking cuck."
            show bg 20qwithsister_4
            pov "Fuck you, that's your dud question, my turn."
        "No.":
            if mum_path <= 6:
                $ sister_points += 1
                $ renpy.notify("Relationship with [sister] increased.")
            else:
                $ sister_points = 10
            show bg 20qwithsister_3
            pov "No."
            show bg 20qwithsister_6
            sis "Cuck in denial."
            show bg 20qwithsister_4
            pov "Fuck you, that's your dud question, my turn."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_3
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq15:                    # Do you want to have kids in the future?
    show bg 20qwithsister_8
    sis "Do you want to have kids in the future?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            show bg 20qwithsister_3
            pov "Yes, I wanna see little mini-me's running around."
            show bg 20qwithsister_6
            sis "Huh, I pictured you as a childless-bachelor all your life."
            show bg 20qwithsister_4
            pov "Maybe up until 30s or something, but kids would be great to have."
        "No.":
            show bg 20qwithsister_7
            pov "No, no kids for me please."
            show bg 20qwithsister_5
            sis "Not even one?"
            show bg 20qwithsister_9
            pov "Not even half a kid. I have my whole life to live."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_5
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq16:                    # Have you decided what you want to do with your life?
    show bg 20qwithsister_5
    sis "Have you decided what you want to do with your life?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_7
            pov "Yes.. I think?"
            show bg 20qwithsister_5
            sis "Oh, and what would that be?"
            show bg 20qwithsister_2
            pov "What are the rules again? No sub-questions? The turn is mine."
        "No.":
            $ twentyqwithsister_honest += 1
            show bg 20qwithsister_10
            pov "No, no clue."
            show bg 20qwithsister_9
            sis "I figured so. You're still too young to fully know."
            show bg 20qwithsister_10
            pov "I hope I have it figured out soon. I better have, I'll need to know what I even wanna major in."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_9
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq17:                    # Are you going to keep in touch with me after all this is over?
    show bg 20qwithsister_9
    sis "Are you going to keep in touch with me after all this is over?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Relationship with [sister] increased.")
            else:
                $ sister_points = 10
            show bg 20qwithsister_10
            pov "Yes.. I'll do my best to."
            show bg 20qwithsister_9
            sis "I really hope you do. As sad and cheesy as it sounds, I'll really miss your company."
            show bg 20qwithsister_10
            pov "You're literally my other half, can't remember a day without you."
        "No.":
            if sister_points >= 2:
                $ sister_points -= 2
            else:
                $ sister_points = 0
            $ renpy.notify("Relationship with [sister] decreased by 2")
            show bg 20qwithsister_12
            pov "No-"
            show bg 20qwithsister_13
            sis "No?! What do you mean ‘no'? Just straight up say that you don't want anything to do with me to my face?"
            show bg 20qwithsister_12
            pov "I meant, no idea, [sister]. I can only hope that we keep in touch..."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_16
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq18:                    # Do you even want to be an adult?
    show bg 20qwithsister_9
    sis "Do you even want to be an adult?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            if skill_int >= 11:
                $ twentyqwithsister_honest += 1
            show bg 20qwithsister_7
            pov "Yes.. I hate being treated like a kid. All the girls nowadays want a man with power and money."
            show bg 20qwithsister_9
            sis "Ehh, some girls. I think most girls just want someone who doesn't act like a child."
            show bg 20qwithsister_5
            sis "There's a difference between treated like a woman and treated like your mother."
        "No.":
            if skill_int <= 4:
                $ twentyqwithsister_honest += 1
            show bg 20qwithsister_10
            pov "No. Adulthood sucks. Too many responsibilities."
            show bg 20qwithsister_9
            sis "As much as I agree with you, I'd take these responsibilities over being a kid any day. Being in control of your life is nice to have."
            show bg 20qwithsister_10
            pov "The term ‘being in control' is a bit generous, wouldn't you say?"
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_5
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq19:                    # Have you ever fantasized about Dad?
    show bg 20qwithsister_6
    if winc == 0:
        sis "Have you ever fantasized about [dadname]?"
    else:
        sis "Have you ever fantasized about Dad?"
    $ twentyqwithsister_qsis += 1

    menu:
        "Yes.":
            show bg 20qwithsister_4
            pov "Yes."
            show bg 20qwithsister_6
            sis "You're fucking disgusting, [povname]! Seriously?"
            show bg 20qwithsister_3
            pov "I'm not gonna deny that my brain wants to think of some fucked up things against my conscious will."
        "No.":
            show bg 20qwithsister_11
            pov "No. That shit's fuckin' nasty pasty. I bet you have though."
            show bg 20qwithsister_13
            sis "Of course I have, every girl has. It's fucking embedded into our animalistic DNA."
            show bg 20qwithsister_3
            pov "Your DNA is fucking nasty pasty."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_3
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisq20:                    # Is it a curse that I'm your sister?
    show bg 20qwithsister_9
    if winc == 0:
        sis "Is it a curse that I'm your [sisrole]?"
    else:
        sis "Is it a curse that I'm your sister?"
    $ twentyqwithsister_qsis = 1

    menu:
        "Yes.":
            if sister_points <= 4:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_7
            pov "Yes."
            show bg 20qwithsister_5
            sis "Why so?"
            show bg 20qwithsister_16
            pov "No sub-questions. I just, think it's a curse. You don't need to know the reason..."
        "No.":
            if sister_points <= 2:
                $ twentyqwithsister_honest -= 1
            show bg 20qwithsister_10
            if winc == 0:
                pov "No. I like the fact that you're my [sisrole]."
            else:
                pov "No. I like the fact that you're my sister."
            show bg 20qwithsister_9
            sis "I hope you mean that genuinely and not sexually."
            show bg 20qwithsister_16
            pov "Why would you even go there, [sister]."
        "Pass." if twentyqwithsister_povpass <= 4:
            show bg 20qwithsister_16
            pov "Pass."
            $ twentyqwithsister_povpass += 1

    jump lbl_20q_with_sister_sisend

label lbl_20q_with_sister_sisend:
    if twentyqwithsister_qc == 1 or twentyqwithsister_qc == 5 or twentyqwithsister_qc == 9 or twentyqwithsister_qc == 13 or twentyqwithsister_qc == 17:
        jump lbl_20q_with_sister_pov2
    elif twentyqwithsister_qc == 2 or twentyqwithsister_qc == 6 or twentyqwithsister_qc == 10 or twentyqwithsister_qc == 14 or twentyqwithsister_qc == 18:
        jump lbl_20q_with_sister_pov3
    elif twentyqwithsister_qc == 3 or twentyqwithsister_qc == 7 or twentyqwithsister_qc == 11 or twentyqwithsister_qc == 15 or twentyqwithsister_qc == 19:
        jump lbl_20q_with_sister_pov4
    elif twentyqwithsister_qc == 4 or twentyqwithsister_qc == 8 or twentyqwithsister_qc == 12 or twentyqwithsister_qc == 16:
        jump lbl_20q_with_sister_pov1
    elif twentyqwithsister_qc == 20:
        jump lbl_sibling_first_kiss
