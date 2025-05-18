## Allaway at the Cafe Date ##
label lbl_allaway_at_the_cafe_date:
    default allawayatthecafe_hobbymovie = 0

    scene bg allawayatthecafe_1
    with fade
    mis "..."
    show bg allawayatthecafe_2
    mis "So, [povname]. I guess tell me about yourself."
    show bg allawayatthecafe_3
    pov "Am I applying for an interview or something? Hahaha."
    show bg allawayatthecafe_4
    mis "I just want to get to know you more. That's all."
    show bg allawayatthecafe_5
    mis "What do you like to do for fun?"

    menu:
        "Video games.":
            $ allawayatthecafe_hobby = "play video games"
            show bg allawayatthecafe_6
            pov "Video games."
            show bg allawayatthecafe_2
            mis "Video games, I haven't played a video game since..."
            mis "Does solitaire count? I play that occasionally during class while you guys are doing stuff."
            show bg allawayatthecafe_3
            pov "Technically yeah but I wouldn't call you a gamer by any means."
            show bg allawayatthecafe_4
            mis "I wouldn't think so. There's too much going on for me to keep track of."
            show bg allawayatthecafe_3
            mis "Although I did enjoy watching my brother play on his N69 back in the day."
            show bg allawayatthecafe_7
            pov "Oh, you have a brother?"
            show bg allawayatthecafe_8
            mis "I have two brothers and a sister. I'm the youngest of the Brady Bunch."
            show bg allawayatthecafe_6
            if winc == 0:
                pov "That's cool. I don't have siblings but I have a female [sisrole]."
                show bg allawayatthecafe_9
                mis "A [sisrole]?! Who is she, maybe I know her."
                mis "You both aren't in the same class are you?"
                show bg allawayatthecafe_3
                pov "Hahaha, no. She dropped out at end of last year. University just wasn't for her."
                show bg allawayatthecafe_9
                mis "Oh, yeah? What does she do now?"
                if sister_path >= 19:
                    show bg allawayatthecafe_10
                    pov "Sh-she works..."
                    show bg allawayatthecafe_11
                    pov "In customer service."
                    pov "Is all I know, to be honest with you. We don't really talk about it that much, work is work."
                    show bg allawayatthecafe_12
                    mis "That's fair, I totally understand the struggle of getting a job you're proud of right out of studying."
                    show bg allawayatthecafe_13
                    mis "I wish her the best of luck in whatever career she aspires to be."
                else:
                    show bg allawayatthecafe_3
                    pov "She works at the mall, I believe."
                    show bg allawayatthecafe_14
                    mis "Wish I knew what she looks like so I know if I've seen her there or not."
                    show bg allawayatthecafe_15
                    mis "Actually, unless you two are clones, I can't assume you both look similar."
                    show bg allawayatthecafe_3
                    pov "We actually look a lot more similar that other [sisrole]s."
                    show bg allawayatthecafe_5
                    mis "That's common. Personal lifestyle changes one's body."
                    mis "I wish her the best of luck for her future career endeavours."
            else:
                pov "That's cool. I have a twin sister."
                show bg allawayatthecafe_9
                mis "A twin sister?! Who is she, maybe I know her."
                mis "You both aren't in the same class are you?"
                show bg allawayatthecafe_3
                pov "Hahaha, no. She dropped out at the end of last year. University just wasn't for her."
                show bg allawayatthecafe_9
                mis "Oh, yeah? What does she do now?"
                if sister_path >= 19:
                    show bg allawayatthecafe_10
                    pov "Sh-she works..."
                    show bg allawayatthecafe_11
                    pov "In customer service."
                    pov "Is all I know, to be honest with you. We don't really talk about it that much, work is work."
                    show bg allawayatthecafe_12
                    mis "That's fair, I totally understand the struggle of getting a job you're proud of right out of studying."
                    show bg allawayatthecafe_13
                    mis "I wish her the best of luck in whatever career she aspires to be."
                else:
                    show bg allawayatthecafe_3
                    pov "She works at the mall, I believe."
                    show bg allawayatthecafe_14
                    mis "Wish I knew what she looks like so I know if I've seen her there or not."
                    show bg allawayatthecafe_15
                    mis "Actually, unless you two are fraternal twins, I can assume you both look very similar."
                    show bg allawayatthecafe_3
                    pov "We used to look a lot more similar when we were younger."
                    show bg allawayatthecafe_5
                    mis "That's common. Personal lifestyle changes one's body."
                    mis "I wish her the best of luck for her future career endeavours."
        "Read books.":
            $ allawayatthecafe_hobby = "read"
            show bg allawayatthecafe_16
            pov "Read books."
            show bg allawayatthecafe_17
            mis "You actually read books?"
            show bg allawayatthecafe_18
            pov "Don't you?"
            show bg allawayatthecafe_19
            mis "Nope, I hate those boring suckers. No offence."

            menu:
                "I lied":
                    show bg allawayatthecafe_20
                    pov "I actually only said that because I thought you have the same interest."
                    show bg allawayatthecafe_21
                    mis "Firstly, I told you not to play games with me, and second, that's a stupid cliche."
                    show bg allawayatthecafe_19
                    mis "Just because I'm an introvert, doesn't mean I like to read."
                    show bg allawayatthecafe_21
                    mis "I don't know why people assume that that's the only activity you can do in your alone time."
                    show bg allawayatthecafe_20
                    mis "Ever heard of Webflicks?"
                    show bg allawayatthecafe_22
                    pov "Would you say you're a Webflicks addict then?"
                    show bg allawayatthecafe_23
                    mis "Addict is a strong term."
                    show bg allawayatthecafe_13
                    mis "So yeah."
                "None taken.":
                    show bg allawayatthecafe_11
                    pov "None taken."
                    show bg allawayatthecafe_6
                    pov "I prefer reading a story and visualizing it with my imagination, rather than it being shown to me through someone's eyes."
                    show bg allawayatthecafe_14
                    mis "That's great and all but one's imagination isn't always the superior medium."
                    show bg allawayatthecafe_5
                    mis "Think of your favourite movie, or show, or if you have a favourite director."
                    mis "The way the film captures your emotions and pulls on your strings is by the power of the director's vision, not yours."
                    show bg allawayatthecafe_4
                    mis "It's an emotional rollercoaster constructed by a visionary, a moment in time to feel lost in their world and the only thing you should do it ride it out."
                    show bg allawayatthecafe_5
                    mis "That is my kind of drug."
                    show bg allawayatthecafe_15
                    mis "That and caffeine."
                    show bg allawayatthecafe_5
                    mis "So in conclusion to my verbal essay, audiovisual media rules, books stinks."
        "Watch movies and TV shows.":
            $ allawayatthecafe_hobbymovie = 1
            $ allawayatthecafe_hobby = "watch movies and tv shows"
            show bg allawayatthecafe_16
            pov "Watch movies and TV shows."
            show bg allawayatthecafe_9
            mis "Oh, really? Then that's definitely something we have in common."
            if whyamiintrouble_fightclub == 1:
                show bg allawayatthecafe_5
                mis "I remember our little conversation about ‘Fight Club' after your little fight club."
            else:
                show bg allawayatthecafe_5
                mis "One of my favourite films is 'Fight Club'."
                show bg allawayatthecafe_19
                mis "Kind of like what you were doing in the gym when you caught me- I mean when I caught you!"
            show bg allawayatthecafe_8
            mis "Speaking of, do you still partake in that?"
            show bg allawayatthecafe_24
            pov "The fight club?"
            show bg allawayatthecafe_3
            pov "From time to time. It's not like its on my mind 24-7 though."
            pov "Just some exercise to make myself feel alive."
            show bg allawayatthecafe_8
            mis "That's some really intense form of exercise. Beating the living hell out of each other."
            show bg allawayatthecafe_14
            mis "I don't condone physical violence but between you and me."
            show bg allawayatthecafe_8
            mis "I love watching it. The 2nd hand adrenaline and the rush that you get turns me right on."
            mis "Turns me-"
            show bg allawayatthecafe_19
            mis "It makes me really excited."
        "Be active.":
            $ allawayatthecafe_hobby = "live an active lifestlye"
            show bg allawayatthecafe_16
            pov "Be active."
            show bg allawayatthecafe_15
            mis "Active? As in what, exercise and work out non-stop?"
            show bg allawayatthecafe_20
            pov "Not non-stop. It involves a lot of walking around, meeting new people, living life to the fullest with what I can."
            pov "That sort of ‘be active' lifestyle."
            show bg allawayatthecafe_8
            mis "Sounds like something that's very out of my comfort zone but it's also something that I'm trying to do more of."
            show bg allawayatthecafe_25
            pov "If you don't feel comfortable doing it, why do it?"
            show bg allawayatthecafe_26
            mis "That's exactly why I'm doing it, so I can turn my uncomfortableness into something comfortable."
            show bg allawayatthecafe_19
            mis "Besides, when you reach this age and you're mostly at home watching Webflicks alone, you have find the missing piece."
            show bg allawayatthecafe_20
            pov "And that missing piece is a partner?"
            show bg allawayatthecafe_13
            mis "Right on the money."
            show bg allawayatthecafe_1
            pov "..."
            show bg allawayatthecafe_16
            pov "Well, I'm here, and I'm free to take home if you want."
            show bg allawayatthecafe_13
            mis "You're cute, [povname]. But not my type. Thanks for the suggestion though."
            show bg allawayatthecafe_7
            pov "Really? Are you sure you're I'm not your type? What is your type."
            show bg allawayatthecafe_19
            mis "If I told you, you'd magically turn into one tomorrow."
            show bg allawayatthecafe_23
            mis "That's the type you are. One to do whatever it takes to win the girl."
        "Roam around finding stuff to do.":
            $ allawayatthecafe_hobby = "roam around"
            show bg allawayatthecafe_16
            pov "Roam around finding stuff to do."
            show bg allawayatthecafe_15
            mis "Is that how you came across me today?"
            show bg allawayatthecafe_11
            pov "I don't know why but you make it sound like I found you in a magical forest."
            show bg allawayatthecafe_12
            mis "What happened to you, [povname]? Not flirtatious anymore?"
            show bg allawayatthecafe_13
            mis "Have you hidden back into your shell?"
            show bg allawayatthecafe_7
            pov "I'm kind of surprised at how much more chill and awesome you are when you're not a teacher."
            show bg allawayatthecafe_19
            mis "I'm still your teacher, [povname]. I'm just teasing you."
            show bg allawayatthecafe_9
            mis "A little fun won't hurt as long as we don't cross the line between what are appropriate, harmless jokes and what aren't."
            show bg allawayatthecafe_16
            pov "Are we at the stage of our relationship where we're setting down the house rules?"
            pov "Should we come up with a safety word while we're at it?"
            show bg allawayatthecafe_17
            mis "For when we have sex or wha-"
            show bg allawayatthecafe_27
            mis "Wahh-aha-hahah-hahaha... I- I didn't mean..."
            mis "Don't... Think that we're..."
            show bg allawayatthecafe_28
            pov "Don't worry, Miss Allaway. I didn't hear a thing."
            show bg allawayatthecafe_26
            mis "Oh.. good... Hehe..."
    show bg allawayatthecafe_1
    mis "..."
    show bg allawayatthecafe_2
    mis "This cake is good."
    show bg allawayatthecafe_3
    pov "You do have a thing for coffee and coffee flavoured goods, it appears."
    show bg allawayatthecafe_4
    mis "If I said it once, I'll say it again, coffee is better than sex."
    show bg allawayatthecafe_8
    mis "I mean- y'know. Sex is good!"
    show bg allawayatthecafe_17
    mis "I have sex a lot!"
    mis "No, wait- what I meant to say is-"
    show bg allawayatthecafe_25
    pov "Okay, okay. Hold your horses, Miss. I don't want you spiralling into panic."
    show bg allawayatthecafe_29
    mis "..."
    show bg allawayatthecafe_8
    mis "I'm so sorry about that, [povname]..."
    show bg allawayatthecafe_30
    mis "Sometimes I wish I didn't catch myself saying such stupid things."
    mis "It is more embarrassing than letting it slip..."

    menu:
        "I find it cute.":
            if missallaway_points <= 9:
                $ missallaway_points += 1
            else:
                $ missallaway_points = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased")
            show bg allawayatthecafe_31
            pov "I find it cute."
            show bg allawayatthecafe_32
            mis "You're just saying that to make me feel better about it. I know it's weird and awkward to deal with."
            show bg allawayatthecafe_31
            pov "No, really. It's all the perfect imperfections in a girl that makes her special."
            show bg allawayatthecafe_33
            mis "Say that to me in bed and I'd kiss the shit out of you."
        "It's alright.":
            show bg allawayatthecafe_25
            pov "It's alright."
            show bg allawayatthecafe_26
            mis "I hope it doesn't ruin things or make things deathly awkward."
            show bg allawayatthecafe_31
            pov "No, don't worry, really. I'll just need to get used to it."
            show bg allawayatthecafe_32
            mis "I hope you don't get tired of me too quickly, I wanna see how far we go."
        "It's really weird.":
            if missallaway_points >= 1:
                $ missallaway_points -= 1
            else:
                $ missallaway_points = 0
            $ renpy.notify("Your relationship with Miss Allaway has decreased by 1")
            show bg allawayatthecafe_34
            pov "It's really weird how you do that."
            show bg allawayatthecafe_35
            mis "Hahaha.. Yeah, I know. My apologies for that and any future outbursts."
            show bg allawayatthecafe_36
            pov "You're good, it's just weird."
            show bg allawayatthecafe_37
            mis "Fuck me... he thinks I'm freaky. I can get freaky..."
    show bg allawayatthecafe_40
    pov "..."
    show bg allawayatthecafe_39
    pov "I'm sorry, what did you say?"
    show bg allawayatthecafe_40
    mis "..."
    show bg allawayatthecafe_27
    mis "I honestly don't know, and I'm too afraid to ask you."
    show bg allawayatthecafe_25
    pov "It's better if we just move on."
    show bg allawayatthecafe_35
    mis "... Thanks, [povname]. I bet it's really... dirty... and risque."
    show bg allawayatthecafe_41
    pov "Why is it that way?"
    show bg allawayatthecafe_42
    mis "Hm? Why is what way?"
    show bg allawayatthecafe_43
    pov "Why does most if not all your- uh... spontaneous outburst end up dirty and risque?"
    show bg allawayatthecafe_35
    mis "I-"
    show bg allawayatthecafe_27
    mis "Don't know."
    mis "Hahaha.. Funny, isn't it? You'd think I know, but I don't! Hahaha!"
    show bg allawayatthecafe_21
    mis "Of course I fucking know why! It's because I'm nervous as hell hole here with you."
    show bg allawayatthecafe_30
    mis "I just wanna-"
    show bg allawayatthecafe_21
    mis "Fuck.. fuck... fuck... nope. Nope. Stop it girl. Stop ruining my date- date- daaay!"
    show bg allawayatthecafe_30
    mis "Shit..."
    mis "I'm gonna shut the fuck up now."
    show bg allawayatthecafe_28
    pov "Hey, Miss?"
    show bg allawayatthecafe_25
    pov "Why don't we move onto another subject, hey?"
    pov "Not to sound narcissistic but let's talk about me, shall we?"
    show bg allawayatthecafe_24
    pov "What do you want to know?"
    show bg allawayatthecafe_8
    mis "{i}*mumbling*{/i} Dn't-ask-bou'-his-dic..."
    if gtime == 0:
        show bg allawayatthecafe_9
        mis "What do you think of Brock?"
        show bg allawayatthecafe_11
        pov "Brock?"
        show bg allawayatthecafe_12
        mis "Yeah, the guy inside the cafe, the one that attends the not-so-secret secret fight club."
        show bg allawayatthecafe_13
        mis "What do you think of him?"
        show bg allawayatthecafe_11
        pov "Him? Well..."

        menu:
            "He's really cool.":
                if brock_points <= 9:
                    $ renpy.notify("Your relationship with Brock has increased")
                    $ brock_points += 1
                else:
                    $ brock_points = 10
                show bg allawayatthecafe_16
                pov "He's really cool."
                show bg allawayatthecafe_4
                mis "Yeah? He's such a badass, and he really knows how to service a woman."
                show bg allawayatthecafe_17
                mis "I love him."
                show bg allawayatthecafe_27
                mis "But like, not love love, just dreamy love."
            "He's fine.":
                pov "He's fine."
                show bg allawayatthecafe_12
                mis "Just fine? I think he's a total stud. Just the way he makes coffee is so sexy."
                show bg allawayatthecafe_33
                mis "The way the steam makes his skin glisten. O.M.G."
            "I don't like him.":
                if brock_points >= 1:
                    $ brock_points -= 1
                    $ renpy.notify("Your relationship with Brock has decreased by 1")
                else:
                    $ brock_points = 0
                show bg allawayatthecafe_44
                pov "I don't like him."
                show bg allawayatthecafe_45
                mis "Really? Well, that's where we have different taste in men."
                show bg allawayatthecafe_42
                mis "Not that I'm saying you're into men, I can't assume that but damn.."
                show bg allawayatthecafe_19
                mis "He's such a hunk. I'd let him squeeze me to death in those arms."
        show bg allawayatthecafe_13
        mis "I'm not making you jealous, am I?"
        show bg allawayatthecafe_11
        pov "Seems like you're doing it on purpose to see if I break."
        show bg allawayatthecafe_3
        pov "Well, I'm not hiding anything, Miss Allaway. I do fancy you, it ain't no secret."
        show bg allawayatthecafe_8
        mis "Ain't no secret, hmm? I could spank you for that grammar."
        show bg allawayatthecafe_14
        mis "But I won't. Mainly because it'd look like I was harassing you on the security cameras."
        show bg allawayatthecafe_9
        mis "But in any case, you don't need to be so jealous, [povname]."
        show bg allawayatthecafe_12
        mis "I can see it in your face, hehehehe! I'm just kidding around."
        show bg allawayatthecafe_30
        mis "But seriously, uggh. I just love watching him fight. Everything goes into slow motion."
        show bg allawayatthecafe_18
        pov "... What if I beat him?"
        show bg allawayatthecafe_46
        mis "You can't beat him. No offence but have you even stood next to him? He's like Godzilla."
        mis "I bet he has a monster in his pants."
        show bg allawayatthecafe_47
        pov "Let's move the conversation onto something else, one last time!"
        show bg allawayatthecafe_48
        mis "Jealousy's in the air, everywhere you look around."
    else:
        show bg allawayatthecafe_9
        mis "What do you think of Effie?"
        show bg allawayatthecafe_7
        pov "Effie?"
        show bg allawayatthecafe_5
        mis "You know Effie! Don't tell me you forgot who Effie is!"
        show bg allawayatthecafe_7
        pov "Of course, I know Effie, what kind of friend do you think I am."

        menu:
            "She's really cool.":
                if effie_points <= 9:
                    $ effie_points += 1
                else:
                    $ effie_points = 10
                $ renpy.notify("Your relationship with Effie has increased")
                show bg allawayatthecafe_6
                pov "She's really cool."
                show bg allawayatthecafe_9
                mis "Yeah? I think she's wonderful. Great study, smart girl, ambitious."
                show bg allawayatthecafe_14
                mis "A lot more mature and down to Earth than any other student I came across."
            "She's fine.":
                show bg allawayatthecafe_6
                pov "She's fine."
                show bg allawayatthecafe_14
                mis "Just fine? Oh, c'mon. She's amazing. She's a hardworking, clever, beautiful, young girl."
                show bg allawayatthecafe_15
                mis "Any guy lining up for her is lucky to even get a chance to be in the queue."
            "She's a friend, nothing special.":
                if effie_points >= 1:
                    $ effie_points -= 1
                else:
                    $ effie_points = 0
                $ renpy.notify("Your relationship with Effie has decreased by 1")
                show bg allawayatthecafe_41
                pov "She's a friend, nothing special though."
                show bg allawayatthecafe_42
                mis "Nothing special? Maybe you need a little convincing."
                show bg allawayatthecafe_35
                mis "She's naturally gorgeous, she's witty, and mature. She's two jack-of-all-trades combined."
                show bg allawayatthecafe_9
                mis "She's the whole package and more."
        show bg allawayatthecafe_31
        pov "From the way you talk about her, it sounds like you have a little girl crush."
        show bg allawayatthecafe_35
        mis "Oh, don't be silly, [povname]. Girls in general are just a bit more affectionate with each other than guys are."
        show bg allawayatthecafe_32
        mis "Nothing to do with romantic love, just pure, unadulterated platonic love."
        show bg allawayatthecafe_27
        mis "I mean, besides all the fun experiments."
        show bg allawayatthecafe_18
        pov "What experiments?"
        show bg allawayatthecafe_17
        mis "Who said anything about experiments?"
        show bg allawayatthecafe_18
        pov "You did!"
        show bg allawayatthecafe_17
        mis "... That's..."
        show bg allawayatthecafe_27
        mis "I was about to say that it's a story for another time but, no."
        mis "Just ignore my rambling."
        show bg allawayatthecafe_31
        pov "Y'know, you're never a bore to listen to."
        show bg allawayatthecafe_8
        mis "I'm glad, otherwise being a teacher would've been a terrible career choice, hahaha!"
    show bg allawayatthecafe_1
    $ renpy.pause()
    show bg allawayatthecafe_5
    mis "{i}*Sigh*{/i}"
    mis "I love the cakes and pastries here. The best in town."
    show bg allawayatthecafe_4
    mis "It's good to treat yourself with comfort food after a stressful week."
    show bg allawayatthecafe_5
    mis "Comfort food, and a good movie wearing nothing but a big fluffy blanket in a mildly air conditioned room."
    mis "That's my perfect weekend."
    show bg allawayatthecafe_49
    mis "I could fall asleep just thinking about it."
    show bg allawayatthecafefoot_1
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawayatthecafefoot_2
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawayatthecafefoot_1
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawayatthecafefoot_2
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawayatthecafefoot_1
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawayatthecafefoot_2
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawayatthecafefoot_1
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawayatthecafefoot_2
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg allawayatthecafefoot_1
    with dissolve
    mis "What's that pushing against my feet?"
    show bg allawayatthecafefoot_2
    with dissolve
    mis "[povname], there's something on your chai-"
    show bg allawayatthecafefoot_1
    mis "Uh-"
    show bg allawayatthecafe_50
    with hpunch
    mis "Oh my God! Oh my God..."
    show bg allawayatthecafe_30
    mis "Oh, ma goodness, I'm sooo sorry, [povname]."
    show bg allawayatthecafe_30
    mis "I didn't mean to do that, I swear!"
    show bg allawayatthecafe_51
    pov "Oh, no really? I thought you were giving me a little tease."
    show bg allawayatthecafe_32
    mis "Jesus Christ, no. I maybe?"
    show bg allawayatthecafe_21
    mis "No! I mean no!"
    show bg allawayatthecafe_30
    mis "Oh shit, this is too... I- I gotta go..."
    show bg allawayatthecafe_21
    mis "Don't tell anyone about this, it was an accident, I swear."
    mis "I would never intentionally give you a footjob."
    show bg allawayatthecafe_27
    mis "Unless you want me to-"
    show bg allawayatthecafe_21
    mis "No! Shut up and get out of here. Right!"
    show bg allawayatthecafe_30
    mis "Bye, [povname]. See you..."
    show bg allawayatthecafe_52
    mis "..."
    show bg allawayatthecafe_53
    $ renpy.pause(0.5,hard=True)
    show bg allawayatthecafe_52
    $ renpy.pause()
    show bg allawayatthecafe_54
    mis "Fuck..."

    jump lbl_crush_on_allaway
