## Deep Park Talk with Allaway ##
label lbl_deep_park_talk_with_allaway:

    scene bg deepparktalkwithallaway_1
    with fade
    mis "..."
    mis "When I was a young girl, I used to think there was a creature in this lake."
    mis "Not like the Lochness Monster."
    mis "More like... a mermaid."
    mis "And not even a beautiful one."
    mis "Like... all wrinkly from being in the water for too long."
    show bg deepparktalkwithallaway_2
    mis "Sorta like grandma's nutsack with a dolphin for a butt."

    menu:
        "I saw a ghost here before.":
            show bg deepparktalkwithallaway_4
            pov "I saw a ghost here before, standing on the water's surface."
            if main_story >= 33:
                mis "I remember you mentioning that to me."
                pov "I did? I remember telling the ‘you' in the other world."
                mis "..."
                mis "I vividly remember you coming into class in a panicky manner and you told me about a drowning girl."
                mis "Am I mistaken?"
                pov "..."
                show bg deepparktalkwithallaway_2
                pov "I'm so confused right now."
                mis "Maybe it's the Mandela Effect. Or reverse Deja vu..."
                show bg deepparktalkwithallaway_1
                mis "Or some other magical phenomenon."
            else:
                mis "A girl? Are you sure you didn't hit your head and saw Jesus?"
                pov "I'm very sure it was a girl. Long, white nightgown. Long, black hair."
                show bg deepparktalkwithallaway_3
                mis "Sounds like you saw the girl from 'The Ring'."
                show bg deepparktalkwithallaway_1
                pov "My guess is as good as yours. I just know what I saw."
                mis "Well good, I have a disobedient mouth and you have deceitful eyes."
        "There's another world in the lake." if main_story >= 33:
            pov "There's a whole ‘nother world at the bottom of that lake."
            show bg deepparktalkwithallaway_1
            mis "I think you're mistaking it for the sea, [povname]."
            mis "The lake shouldn't be {i}that{/i} deep."
            mis "Yeah, it's a deep but not ‘another world' type deep."
            show bg deepparktalkwithallaway_3
            pov "No, that's not what I meant, like literally another parallel universe!"
            mis "..."
            mis "I've been here in this town all my life. There isn't another parallel universe."
            mis "Actually, you know what?"
            mis "..."
            show bg deepparktalkwithallaway_4
            mis "I'll play along to your fun, hypothetical story."
            pov "It's not hypothetical, it's real!"
            mis "Alright, big cat. It's ‘reaal'."
            mis "Tell me, what happens in this hypothetic-"
            mis "I mean, parallel universe?"
            pov "It's exactly the same but everyone has sex!"
            show bg deepparktalkwithallaway_3
            mis "I-"
            show bg deepparktalkwithallaway_4
            mis "I don't know if your previous school taught you sex-ed properly but listen, [povname]."
            mis "Sex is completely normal in life. Everyone has sex, it's part of evolutio-"
            pov "No, no. That's not what I mean."
            pov "I meant like- everyone... has sex.. Just as part of their daily life."
            show bg deepparktalkwithallaway_3
            mis "..."
            mis "As I said, sex is norm-"
            show bg deepparktalkwithallaway_1
            pov "Nevermind, forget I mentioned it."
            pov "Stupid isn't it? I have a dirty imagination, hahaha..."
            mis "Don't worry, [povname]. Some guys are just late bloomers."
            show bg deepparktalkwithallaway_2
            mis "You'll lose your virginity soo-oo-oon.."
            show bg deepparktalkwithallaway_1
            pov "..."
            show bg deepparktalkwithallaway_3
            pov "Why'd you hesitate with that last word?"
            mis "Nothing."
        "A grandma's nutsack...?":
            show bg deepparktalkwithallaway_3
            pov "A grandma's nutsack with a dolphin for a butt, huh?"
            pov "You've got a knack for descriptive language."
            mis "Just trying to paint the perfect picture for you."
            show bg deepparktalkwithallaway_1
            pov "I'd love to see that in real life."
            mis "No, you wouldn't. It has already haunted my dreams."
            mis "Who knows what my psyche would be like if I saw it in the flesh."
            pov "Touche."
    show bg deepparktalkwithallaway_1
    mis "..."
    show bg deepparktalkwithallaway_2
    mis "Hey, can ask you a question?"
    show bg deepparktalkwithallaway_4
    mis "Not really a question but, I guess permission."
    pov "Sure, what is it?"
    mis "Can I be your friend for tonight?"
    pov "A friend? I don't see why not."
    show bg deepparktalkwithallaway_3
    mis "It's ‘cause, with tonight starting off wrong..."
    mis "I just feel like I'm not worth shit to people."
    show bg deepparktalkwithallaway_4
    mis "I was hoping you'd be a friend for me tonight."
    mis "I... really need one."

    menu:
        "Of course.":
            pov "Of course, Miss. I'll be here for you."
            pov "I'll be here at your lowest and your highest."
            show bg deepparktalkwithallaway_3
            mis "... I really wish I can believe you, [povname]."
            show bg deepparktalkwithallaway_4
            mis "N-not that I'm saying you won't try your best..."
            mis "But the age difference... and you have no idea where your life will end up."
            show bg deepparktalkwithallaway_3
            mis "It could be out of town in the next few months for all I know."
            mis "{i}*Sigh*{/i}"
            show bg deepparktalkwithallaway_4
            mis "Let's make it just for tonight..."
            mis "I don't want to get too attached to you..."
            show bg deepparktalkwithallaway_3
            mis "Not anymore than what I already have."
        "Friends... with benefits?":
            pov "Friends... with benefits?"
            show bg deepparktalkwithallaway_3
            mis "..."
            show bg deepparktalkwithallaway_1
            pov "S-sorry..."
            mis "{i}*Sigh*{/i}"
            mis "It's fine. At least you're here and not my date."
            mis "..."
            mis "Do you always rush things?"
            show bg deepparktalkwithallaway_3
            pov "Not always..."
            mis "Because you're really eager to get some action, aren't you?"
            show bg deepparktalkwithallaway_1
            pov "Can you blame me?"
            mis "Nope, no I cannot."
            mis "You're right. Growing boys have evolutionary needs."
            show bg deepparktalkwithallaway_2
            mis "Maybe you're still too immature to see the value of patience."
            show bg deepparktalkwithallaway_4
            pov "I understand patience!"
            show bg deepparktalkwithallaway_3
            mis "Mhmm, yeah... my mistake then."
        "I want to be more than friends.":
            if skill_cha >= 5:
                if missallaway_points >= 7:
                    if missallaway_points <= 9:
                        $ missallaway_points += 1
                    else:
                        $ missallaway_points = 10
                    $ skill_cha -= 5
                    $ renpy.notify("You used 5 Charisma Points\nYour relationship with Miss Allaway has increased")
            pov "I want to be more than just your friend."
            show bg deepparktalkwithallaway_3
            mis "To tell you the truth..."
            show bg deepparktalkwithallaway_4
            mis "And I'm only telling you now because I don't see any other perfect time to do so."
            mis "I- I want that too. For us to... y'know."
            show bg deepparktalkwithallaway_3
            mis "But you know that won't happen. Ever."
            mis "It-"
            mis "It's far too risky for us, [povname]."
            show bg deepparktalkwithallaway_1
            mis "Hell, being seen here with you alone is risky enough."
            mis "There's going to be headlines with my face on it all over social media and all the news sites."
            mis "‘University lecturer arrested for being in a relationship with her student'."
            show bg deepparktalkwithallaway_2
            mis "No."
            show bg deepparktalkwithallaway_1
            mis "I can't let that happen."
            pov "I understand how you feel."
            pov "There's no point trying to convince you that you're wrong and we should take things further."
            show bg deepparktalkwithallaway_3
            pov "Because you're 100 percent right about the risks."
            pov "And I know it's riskier for you."
            show bg deepparktalkwithallaway_1
            pov "But I do want you to know that I would do anything to have moments with you."
    show bg deepparktalkwithallaway_1
    mis "..."
    mis "Can I ask you why?"
    pov "Why what?"
    show bg deepparktalkwithallaway_3
    mis "Why me? Why do you have this strong interest in me?"
    show bg deepparktalkwithallaway_4
    mis "You have all these young, pretty girls all over university, and you pick the teacher with some strange mental illness and glasses."
    pov "Hey!"
    pov "Glasses are so fucking sexy."
    show bg deepparktalkwithallaway_3
    mis "... Then what is it?"

    menu:
        "I think you're really beautiful.":
            if skill_cha >= 5:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ skill_cha -= 3
                $ renpy.notify("You used 3 Charisma Points\nYour relationship with Miss Allaway has increased")
            pov "I think you're really beautiful."
            show bg deepparktalkwithallaway_4
            mis "You don't really think that, do you?"
            pov "I do, all the time."
            pov "When I get distracted in class, it's because of you."
            show bg deepparktalkwithallaway_3
            mis "I really wanna barf at how cheesy that was."
            show bg deepparktalkwithallaway_4
            mis "But thanks, [povname], really. I appreciate what you said."
        "I think your personality is quite charming.":
            if skill_int >= 5:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ skill_int -= 3
                $ renpy.notify("You used 3 Intelligence Points\nYour relationship with Miss Allaway has increased")
            pov "I think your personality is quite charming."
            show bg deepparktalkwithallaway_4
            mis "My personality is probably the least strongest feature about me..."
            mis "And that's saying something when you're talking about a frikkin human being."
            show bg deepparktalkwithallaway_1
            pov "Normal people are boring."
            show bg deepparktalkwithallaway_3
            pov "Talking to you keeps me on my toes, and I like that."
            mis "Doesn't mean it's always a good thing."
            show bg deepparktalkwithallaway_4
            mis "But thanks, [povname], really. I appreciate what you said."
        "I think it's because we have similar interest.":
            pov "I think it's because we have similar interests."
            if allawaydatecoldfeet_movie == 1:
                if missallaway_points >= 1:
                    $ missallaway_points -= 1
                else:
                    $ missallaway_points = 0
                $ renpy.notify("Your relationship with Miss Allaway has decreased")
                show bg deepparktalkwithallaway_4
                mis "If movies are such your thing, why'd we skip out on it?"
                pov "I-"
                show bg deepparktalkwithallaway_3
                mis "Rest my case."
            elif allawayatthecafe_hobbymovie == 1:
                show bg deepparktalkwithallaway_4
                mis "Yeah, we definitely do."
                show bg deepparktalkwithallaway_2
                pov "Girls these days..."
                if sitwithmissallaway_introvert == 1:
                    if missallaway_points <= 9:
                        $ missallaway_points += 1
                    else:
                        $ missallaway_points = 10
                    $ renpy.notify("Your relationship with Miss Allaway has increased")
                    pov "They just want to go shopping, and party."
                else:
                    pov "They're all just the same."
                show bg deepparktalkwithallaway_1
                pov "I just wanna sit back and enjoy a good movie."
                mis "Or a good TV show."
                pov "Naked."
                show bg deepparktalkwithallaway_2
                mis "..."
                show bg deepparktalkwithallaway_1
                mis "Not that I hate being here but I sooo wanna do that right now."
            else:
                mis "Not really..."
                pov "We both go to UNI?"
                show bg deepparktalkwithallaway_4
                mis "Hahaha, yeah but I think that's more of a responsibility than an interest."
                pov "It's an interest for you, it's your career."
                show bg deepparktalkwithallaway_3
                mis "But it's not yours, that's what I'm getting at."
                show bg deepparktalkwithallaway_4
                mis "But thanks, [povname], really. I appreciate the thought of it."
        "I think I'm just attracted to mature women.":
            if skill_cha >= 5:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ skill_cha -= 3
                $ renpy.notify("You used 3 Charisma Points\nYour relationship with Miss Allaway has increased")
            pov "I think I'm just naturally attracted to more mature women."
            pov "You're so... much better than girls my age."
            show bg deepparktalkwithallaway_4
            mis "More... experienced?"
            pov "In all kinds of ways."
            show bg deepparktalkwithallaway_3
            mis "I- I feel like I'm a little out of touch though."
            show bg deepparktalkwithallaway_4
            mis "But thanks, [povname], really. I appreciate what you said."
        "I think I'm just doing it for fun.":
            pov "I think I'm just doing it for the fun of it."
            if skill_luc >= 14:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ skill_luc -= 8
                $ renpy.notify("You Used 8 Luc Points")
                $ renpy.pause(1,hard=False)
                $ renpy.notify("Your relationship with Miss Allaway has increased")
                mis "Honestly, I'm not surprised."
                show bg deepparktalkwithallaway_4
                mis "And surprisingly, I don't mind."
                show bg deepparktalkwithallaway_3
                mis "The fact that we can't be emotionally with each other, as much as it hurts a little..."
                mis ".."
                mis "..."
                show bg deepparktalkwithallaway_4
                mis "Thanks, [povname], really. I appreciate what you said."
            else:
                if missallaway_points >= 2:
                    $ missallaway_points -= 2
                else:
                    $ missallaway_points = 0
                $ renpy.notify("Your relationship with Miss Allaway has decreased by 2")
                mis "I knew it."
                mis "You boys are all the same."
                mis "I guess it's a good thing that I sort of accepted that as a fact before I made assumptions about you."
                pov "I- It's not like we could've-"
                show bg deepparktalkwithallaway_4
                mis "Yeah, don't worry. It's okay."
    show bg deepparktalkwithallaway_4
    mis "We should head home."
    pov "It's getting pretty late, but it's not like I still have a curfew."
    mis "You don't have a curfew? Oooh, big boy with big boy pants."
    show bg deepparktalkwithallaway_2
    pov "I'm not a kid anymore."
    show bg deepparktalkwithallaway_1
    mis "Heh."
    mis "It's always fun hearing young, kid-adults say that."
    show bg deepparktalkwithallaway_2
    mis "C'mon."
    mis "I'll drive you home myself."
    show bg deepparktalkwithallaway_4
    mis "I have my truck parked closeby."
    pov "Really? You don't mind that?"
    mis "It's late and I don't want you getting shanked."
    mis "Not after having... this."
    show bg deepparktalkwithallaway_3
    mis "Whatever you call what we're doing."
    pov "A date?"
    show bg deepparktalkwithallaway_4
    mis "It is no-"
    show bg deepparktalkwithallaway_3
    mis "Not a date."
    show bg deepparktalkwithallaway_1
    pov "I love how much you're in denial. You really don't know how to feel about all this."
    mis "I don't, I'm so lost."
    show bg deepparktalkwithallaway_2
    mis "Listen to your brain, listen to your heart. My brain and heart are both on the fence."
    show bg deepparktalkwithallaway_4
    mis "I-"
    show bg deepparktalkwithallaway_3
    mis "Let's head to my truck."
    mis "We'll talk some more on the way home."

    jump lbl_allaway_drive_you_home
