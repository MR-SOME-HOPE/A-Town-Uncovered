## Under Cardboard Stars ##
label lbl_under_cardboard_stars:
    default undercardboardstars_cuddle = 1
    default undercardboardstars_silent = 0
    default undercardboardstars_sisterknowsabouteye = 0

    scene bg undercardboardstars_1
    with fade
    $ renpy.pause()
    show bg undercardboardstars_2
    sis "..."
    sis "{i}*Sigh*{/i}"
    show bg undercardboardstars_3
    pov "..."
    show bg undercardboardstars_4
    pov "Something wrong?"
    show bg undercardboardstars_3
    sis "{i}*Sigh*{/i}"
    sis "..."
    show bg undercardboardstars_5
    pov "[sister]?"
    show bg undercardboardstars_6
    sis "Hm? Did you say something?"
    show bg undercardboardstars_7
    pov "I said, is there something wrong?"
    show bg undercardboardstars_8
    sis "Oh, no. I'm fine. Just exhausted and just... I'm too tired to move."
    show bg undercardboardstars_9
    pov "Hehe, I was pretty sleepy myself a while ago. But now I'm just so awake."
    show bg undercardboardstars_10
    sis "I gave you some of my energy levels."
    show bg undercardboardstars_11
    pov "Yes, you did. Too bad this wasn't the best time to do that."
    show bg undercardboardstars_12
    sis "Hehehe, I'm sorry."
    show bg undercardboardstars_13
    sis "..."
    show bg undercardboardstars_14
    sis "I'm really sorry."
    show bg undercardboardstars_15
    pov "There's no need to apologise?"
    show bg undercardboardstars_16
    sis "No, like, I'm sorry for having woken you up. You're probably gonna be falling asleep all day tomorrow."
    show bg undercardboardstars_17
    pov "I think I can manage."
    show bg undercardboardstars_18
    sis "But thank you, for coming down here with me."
    show bg undercardboardstars_12
    sis "I-I had fun."
    show bg undercardboardstars_19
    pov "I'm glad you forced me down here."
    show bg undercardboardstars_10
    sis "You didn't have to call it ‘force'."
    show bg undercardboardstars_20
    pov "You forced me."
    show bg undercardboardstars_21
    sis "Tsk, whatever."
    show bg undercardboardstars_1
    pov "..."
    pov "I should be thanking you."
    pov "I've been so stressed lately. There's just so many things to do. So many errands to run."
    pov "So many people to meet and-"
    pov "I don't wanna let anyone down."
    sis "You spend too much time taking care of others, you forget how to take care of yourself, [povname]."
    pov "Yeah, well. I live my life thinking the only way to succeed is to be liked by as many people."
    sis "..."
    sis "Not to sound like I'm a whole hell wiser than you; but after I finished highschool-"
    sis "-I've just realised how much you don't NEED to please everyone."
    sis "Only the ones that mean something to you."
    sis "Looking back, there were so many fake assholes, plastic bitches, fuckin' flake-out ‘friends'."
    sis "As much as I miss the few good friends back there."
    sis "I'm glad we've gotten a chance to make a new life for ourselves here."
    show bg undercardboardstars_22
    sis "We're still young, yet old enough to have an idea of who we want to portray ourselves as."
    show bg undercardboardstars_23
    pov "..."

    menu:
        "I like listening to you being serious.":
            show bg undercardboardstars_9
            pov "Y'know. As weird as it is for me to say, I kinda like listening to you being serious."
            show bg undercardboardstars_12
            sis "I'm just tired..."
            sis "It's honestly a lot of bullshit coming out from my mou-"
            show bg undercardboardstars_17
            pov "No, no. Really, I like it. It makes sense what you said."
            show bg undercardboardstars_18
            sis "I wouldn't say it's my job to take care of you."
            if winc == 0:
                sis "But it's my job to make sure you turn out alright. Let your big [sisrole] lead the way and fall before you do."
                show bg undercardboardstars_24
                pov "You really think so highly of yourself because you're a tad older, don't you? Hahaha."
            else:
                sis "But it's my job to make sure you turn out alright. Let your big sister lead the way and fall before you do."
                show bg undercardboardstars_24
                pov "You really think so highly of yourself because you pushed past me in Mom's womb, don't you? Hahaha."
        "I reckon it doesn't apply to everyone.":
            show bg undercardboardstars_25
            pov "I'll keep that in mind, though I reckon it doesn't apply to every single one of us."
            pov "We have our own paths to carve and we have to hustle in whatever way we can, even if that means putting on a face."
            show bg undercardboardstars_26
            sis "You say that now but you'd feel a lot better about yourself if you just tone it down a bit."
            sis "It's not good for you to lie through your whole life."
            sis "You'll forget who you really are."
            show bg undercardboardstars_27
            sis "That's probably the most hippie thing that's ever come out of my mouth."
            show bg undercardboardstars_28
            pov "Hahaha. That's what middle-of-the-night talks are all about."
            show bg undercardboardstars_24
            pov "It's funny, why is it that just because you're older by a few minutes that you're qualified to give me life advice."
        "That was just a bunch of bullhonkey.":
            show bg undercardboardstars_25
            pov "I think that was just a bunch of bullhonkey that came out of your mouth just then."
            show bg undercardboardstars_12
            sis "Hahaha... haha.. Yeah."
            sis "I guess I'm just really sleepy all of a sudden. My brain is working to it's full... full- uh.. capacity."
            show bg undercardboardstars_29
            pov "Did you just say ‘Kappa-titty'?"
            show bg undercardboardstars_6
            sis "What the hell are you talking about?"
            show bg undercardboardstars_31
            pov "Nevermind."
            show bg undercardboardstars_24
            pov "Wait- why is it that just because you're older by a few minutes that you're qualified to give me life advice."
    show bg undercardboardstars_32
    sis "It's one of the few things I can take advantage of."
    show bg undercardboardstars_33
    sis "There's too many other things that you have the upper hand with."
    show bg undercardboardstars_34
    pov "Hmm?"
    show bg undercardboardstars_35
    pov "Like what?"
    show bg undercardboardstars_34
    sis "..."
    show bg undercardboardstars_36
    if winc == 0:
        sis "Being the more favourable [povdadrole], more likely to end up more financially successful, generally, life is being kinder to you."
    else:
        sis "Being the more favourable child, more likely to end up more financially successful, generally, life is being kinder to you."
    show bg undercardboardstars_37
    pov "..."
    show bg undercardboardstars_38
    pov "You really think all that?"
    show bg undercardboardstars_39
    sis "I have eyes, [povname]."
    sis "I'm not gonna sugar coat the fact that I feel like a background character in someone else's story."
    sis "There isn't much going on for me."
    sis "That's my fear."
    show bg undercardboardstars_40
    pov "What is?"
    show bg undercardboardstars_41
    sis "That I've peaked already. And that my peak is nowhere near as high as yours."

    menu:
        "You're giving me too much credit.":
            show bg undercardboardstars_1
            pov "You're giving me too much credit, you know that."
            pov "I'm not better than you. But with the off chance that what you say does turn out to be true."
            sis "Which it is."
            pov "..."
            if winc == 0:
                pov "I'm not going to leave you behind. You're my [sisrole]."
            else:
                pov "I'm not going to leave you behind. You're my sister."
            pov "Older or younger, it doesn't matter."
        "You're not giving yourself enough credit.":
            show bg undercardboardstars_1
            pov "You're not giving yourself enough credit. You haven't peaked already, [sister]."
            pov "Your life is only just beginning. You have a head start on me."
            if winc == 0:
                pov "And I'm not talking about being born first."
            else:
                pov "And I'm not talking about you coming out of Mom first."
            pov "You need to let that go."
            sis "Hehe, never."
            pov "But seriously, you have your whole life to go climb your mountain. So to speak."
            pov "I'll be there to support you."
    if winc == 0:
        pass
    else:
        pov "We're family."
        pov "Ohana means family. Remember that show we used to watch on Dinsey Channel?"
        sis "Ohana means family, right."
        sis "You're not just saying that because it's a good quote right?"
        pov "It's a good quote because it has a whole-hearted meaning behind it."
    pov "Have I ever let you down?"
    show bg undercardboardstars_6
    sis "Remember that time, in- I think it was 5th or 6th grade?"
    show bg undercardboardstars_30
    pov "..."
    show bg undercardboardstars_42
    sis "You punched that guy, Felix."
    show bg undercardboardstars_43
    pov "Oh, yeah! That was the first time I got detention. That dude was a straight up asshole."
    show bg undercardboardstars_29
    pov "What does that have to do with letting you down?"
    show bg undercardboardstars_44
    sis "I had a huge crush on him for a year and you totally ruined all my chances with him."
    show bg undercardboardstars_45
    pov "Reeaaally? I didn't know that."
    show bg undercardboardstars_46
    sis "I didn't tell you I had a crush on him because firstly, you'd make fun of me."
    sis "And second, I honestly thought you and him were enemies."
    show bg undercardboardstars_47
    sis "..."
    show bg undercardboardstars_48
    sis "Between the both of you, I didn't want to side against you, no matter how much I hated you at the time."
    show bg undercardboardstars_49
    pov "..."
    if winc == 0:
        pass
    else:
        show bg undercardboardstars_12
        sis "Ohana means family."
        show bg undercardboardstars_9
        pov "Heh.. brought it home, sister."
    show bg undercardboardstars_50
    pov "I'm guessing now's as any good time to apologise for back then-"
    show bg undercardboardstars_10
    sis "Oh, don't worry about it. He really turned out to be a huge spazz later on."
    show bg undercardboardstars_51
    sis "I heard he got expelled last year for causing major damage to a classroom."
    show bg undercardboardstars_52
    pov "Really? What the fuck did he do?"
    show bg undercardboardstars_53
    sis "My friend's friend had a friend that had a friend that was in the class at the time-"
    sis "And she told her friend that told her friend that told my friend that told me-"
    sis "That he went spastic and like threw chairs and desks around, smashing windows and the teacher's computer."
    show bg undercardboardstars_54
    pov "Jesus. I hope I didn't fuck up his brain in grade 6."
    show bg undercardboardstars_55
    sis "Hahaha, I don't think you did. I think it was all those drugs he was taking."
    show bg undercardboardstars_56
    sis "..."
    show bg undercardboardstars_57
    sis "Have you done drugs before?"

    menu:
        "Yeah.":
            pass
        "No.":
            pass
        "Have you?":
            pass
    sis "Don't."
    show bg undercardboardstars_59
    sis "..."
    show bg undercardboardstars_60
    sis "I'm serious, [povname]."
    sis "You know me, I'm pretty chill with a lot of things. Drugs just ain't one of them."
    sis "Not to sound like such a negative, depressing bitch but my life is fucked enough."
    show bg undercardboardstars_61
    sis "I don't need myself or anyone close to me getting caught up in that scene."
    show bg undercardboardstars_62
    sis "For real, I will kick your fucking ass if I find out you're an addict."
    show bg undercardboardstars_63
    sis "..."
    show bg undercardboardstars_39
    sis "I care about you."
    show bg undercardboardstars_64
    pov "...I won't let you down, [sister]."
    show bg undercardboardstars_65
    pov "...What about alcohol?"
    show bg undercardboardstars_32
    sis "Oh, alcohol is majorly fun. Don't be so square."
    show bg undercardboardstars_28
    pov "Haha, well that's good to know then."
    show bg undercardboardstars_66
    sis "You know the nightclub?"
    show bg undercardboardstars_67
    pov "Yeah?"
    show bg undercardboardstars_68
    if winc == 0:
        sis "This is between you and me, but I see [dadrole] going in there every night."
    else:
        sis "This is between you and me, but I see Dad going in there every night."
    sis "Not just to drink but to hang in the VIP lounge."
    show bg undercardboardstars_52
    pov "The VIP lounge?"
    show bg undercardboardstars_51
    sis "You didn't hear this from me."
    show bg undercardboardstars_52
    pov "I- I have so many question-"
    show bg undercardboardstars_51
    sis "I'd rather leave it at that. I think I revealed too much to you already."
    show bg undercardboardstars_54
    pov "Not enough if you ask me."
    show bg undercardboardstars_57
    if winc == 0:
        sis "I'm not asking you, [povname]. I just thought I'd let you know that [dadname]-"
        show bg undercardboardstars_69
        sis "Isn't the same [dadname] as he was back before we moved here."
    else:
        sis "I'm not asking you, [povname]. I just thought I'd let you know that Dad-"
        show bg undercardboardstars_69
        sis "Isn't the same Dad as he was back before we moved here."
    show bg undercardboardstars_1
    sis "Like, don't you think so too? It's not just me, right?"
    if main_story >= 36:
        pov "Y'know... I actually think I know what's going on with that."
        sis "...Really?"
        sis "Are you a psychologist now?"
        pov "No, well. The thing is, if I tell you what I know, you wouldn't believe me."
        sis "I want to know what you know."

        menu:
            "Tell her":
                pov "Fine. But just know that I'm 100 percent being serious here."
                sis "Noted."
                pov "There's an alternate universe that is accessible through the lake or the beach-"
                pov "And everything is the same except for the fact that sex is a totally normal everyday thing."
                pov "And not like, like ‘yeah, sex is natural' kind of thing. I mean, like it's treated as commonly and as normally as eating."
                pov "LIke you would see everyone just banging away and it's ‘just the norm'. No morals are broken."
                pov "Everyone is going about their day... but with mixed in."
                sis "Wa-wa-wa-wa-wait a second there, mister."
                if winc == 0:
                    sis "What the hell does this perverted world have anything to do with [dadname]?"
                    pov "I was about to get to that."
                    pov "Anyway, long-story short. I think our [dadname] from this reality has swapped places with [dadname] from that reality."
                else:
                    sis "What the hell does this perverted world have anything to do with Dad?"
                    pov "I was about to get to that."
                    pov "Anyway, long-story short. I think our dad from this reality has swapped places with Dad from that reality."
                pov "Why do I think this you ask?"
                pov "..."
                sis "..."
                pov "Go on, ask-"
                sis "Will you just tell me already!"
                pov "Okay, okay! Sorry. Well, when I met HIM in the morning, he was... like I remembered he used to be."
                pov "Except he looked.. Confused..."
                pov "As if he knew something was wrong with me. Like he knew I didn't belong in that reality."
                sis "I really wanna believe you there, [povname]."
                sis "But I'm not as gullible as you think I am anymore."
                pov "{i}*Sigh*{/i} See? I told you that you wouldn't believe me."
                sis "It was a quite a visual journey you took me on though."
                sis "Anyway, what was I saying?"
            "Keep it to yourself":
                pov "No, no matter how much I try to convince you. You'll end up thinking I'm making a joke of the situation."
                sis "{i}*Sigh*{/i} At least you're persistent with the whole trolling me aspect of it."
                pov "Whatever."
                sis "Anyway, what was I saying?"
    else:
        pov "No, I totally see it too."
    if winc == 0:
        sis "He was a lot more- [dadrole]ly? Like a good [dadrole]."
    else:
        sis "He was a lot more- fatherly? Like a good father."
    sis "And now it's like he's a totally different person."
    pov "I'm 100 percent with you on that."
    sis "By now, I'm just too scared to even ask him about it."
    sis "It's not like we have to deal with it any longer though."
    if winc == 0:
        pov "True, though I'm sorta worried about [missus]. Unless she files for a divorce-"
        pov "Which I do not wish for them to go through."
    else:
        pov "True, though I'm sorta worried about Mom. Unless she files for a divorce-"
        pov "Which I do not wish for the family to go through."
    show bg undercardboardstars_40
    pov "... I worry that she'd be mistreated by him."
    if bathwithmom_eyereveal == 1:
        show bg undercardboardstars_70
        if winc == 0:
            pov "Maybe if he does anything to [missus] again, I would be for that divorce ide-"
        else:
            pov "Maybe if he does anything to Mom again, I would be for that divorce ide-"
        show bg undercardboardstars_71
        sis "'Again'? What do you mean again?"
        show bg undercardboardstars_72
        pov "..."
        show bg undercardboardstars_73
        if winc == 0:
            sis "Don't just look at me. Did [dadname] hurt [missus]?!"
        else:
            sis "Don't just look at me. Did Dad hurt Mom?!"
        if healedeye_tellsister == 1:
            $ undercardboardstars_sisterknowsabouteye = 1
            show bg undercardboardstars_74
            pov "Uh.. yeah."
            pov "He did."
            show bg undercardboardstars_75
            pov "But please, pleaaase. Don't make a big fuss about it."
            show bg undercardboardstars_76
            if winc == 0:
                sis "How could I not make a big fuss about it?! This is our [mumrole] we're talking about."
            else:
                sis "How could I not make a big fuss about it?! This is our mother we're talking about."
            show bg undercardboardstars_75
            pov "She didn't want you to worry, and please don't get mad at her but she didn't want you to know about it."
            pov "She knew how worked up you'd get and she said that it was an accident in the moment."
            show bg undercardboardstars_76
            sis "You're actually somewhat sticking up for that prick?"
            show bg undercardboardstars_77
            pov "What? No! I told her that if he did it again, I'd beat the shit out of him."
            show bg undercardboardstars_78
            sis "You better beat the shit out of him if he does it again."
            show bg undercardboardstars_79
            sis "..."
            show bg undercardboardstars_80
            if winc == 0:
                sis "As much as I'm fucking furious right now. I'll do [missus] a favour and keep it bottled up."
            else:
                sis "As much as I'm fucking furious right now. I'll do Mom a favour and keep it bottled up."
            show bg undercardboardstars_81
            sis "For now."
            show bg undercardboardstars_82
            sis "..."
            show bg undercardboardstars_83
            sis "Ican'tfuckinbelievethisfuckin'- {i}*murmurring*{/i}"
        else:
            show bg undercardboardstars_45
            pov "No, no. Sorry. Freudian slip."
            pov "I was thinking of something else in the background."
            show bg undercardboardstars_44
            sis "Hmm, well alright, if you say so."
    else:
        show bg undercardboardstars_70
        if winc == 0:
            pov "I swear to God, if he did anything to [missus]. I'm going to beat the shit outta him."
        else:
            pov "I swear to God, if he did anything to Mom. I'm going to beat the shit outta him."
        show bg undercardboardstars_32
        sis "I'll be there to record the action and put it on MeTube."
        show bg undercardboardstars_55
        if winc == 0:
            sis "Think of the views. ‘Crazy kid beats up [dadrole] in front of [mumrole] over video games.'"
        else:
            sis "Think of the views. ‘Crazy kid beats up dad in front of mom over video games.'"
        show bg undercardboardstars_54
        pov "What the hell does the video games have anything to do with it?"
        show bg undercardboardstars_55
        sis "MeTube is like 50 percent gaming related. Duh."
        show bg undercardboardstars_9
        pov "If you start making money off that, I'm grabbing a share."
        show bg undercardboardstars_21
        sis "Hehehe, how exciting. Be sure to let me know when the fight is though. Don't wanna miss the money shot."
        show bg undercardboardstars_24
        pov "I'll notify you with plenty of time in advance, mark it on your calendar."
        pov "But don't le-"
        show bg undercardboardstars_32
        if winc == 0:
            sis "-Let [dadname] see. Hehehehe~"
        else:
            sis "-Let Dad see. Hehehehe~"
        show bg undercardboardstars_2
        sis "{i}*Gentle sigh*{/i}"
        pov "{i}*Gentle sigh*{/i}"
    show bg undercardboardstars_1
    sis "..."
    sis "[povname]?"
    sis "I'm sleepy."
    sis "We should get to sleep. Shall we?"
    pov "That's a good idea."
    sis "It's a little chilly in here."

    menu:
        "We should get back to bed.":
            pov "We should get back upstairs and into bed then."
            sis "Whaat? No."
            pov "No?"
            sis "Yeah, no. I wanna stay down here."
            pov "Didn't you say you were cold?"
            sis "It is. But The journey to my bedroom will be colder."
            pov "Wouldn't your warm bed be a grand reward for your weary travels?"
            sis "Hrrmm..."

            menu:
                "I'm going to bed.":
                    $ undercardboardstars_cuddle = 0
                    if sister_points >= 1:
                        $ sister_points -= 1
                    else:
                        $ sister_points = 0
                    $ renpy.notify("Your relationship with [sister] has decreased")
                    pov "Well, I'm going to bed."
                    sis "Naww don't say that. You're not just going to leave me here, are you?"
                    pov "If I go, you'd have no choice but to go to your own room and sleep in a cozy bed yourself."
                    show bg undercardboardstars_7
                    pov "I don't want you to catch a cold."
                    show bg undercardboardstars_57
                    sis "You're desthhh-picable "
                    show bg undercardboardstars_84
                    pov "Goodnight, [sister]. I'll see you in the morning."
                    $ sister_path = 13
                    scene bg mybedroom_night
                    with fade
                    $ renpy.pause()

                    jump lbl_mybedroom_night_sleep
                "I guess we'll stay down here.":
                    show bg undercardboardstars_31
                    pov "Alright, I guess we'll just stay down here. In the cold. Cold."
                    show bg undercardboardstars_85
                    sis "Yay."
        "Should I get a blanket?":
            pov "Do you want me to get a blanket?"
            sis "..."
            sis "No."
            pov "I won't take more than a second."
            sis "No."
            sis "Stay here."
            pov "..."
            sis "If you leave."
            sis "T-then..."
            sis "All the warmth will vanish into thin air."
            pov "But in the long run, we'll be warme-"
            sis "Don't argue with me, mister."
            pov "Don't talk to me like that, missy. You are definitely tired."
            sis "{i}*Growl* {/i} Don't leave the Fortress."
            sis "Or I'll smack you on the tooshie."

            menu:
                "I'll go get one.":
                    show bg undercardboardstars_31
                    pov "I'll go get one anyway."
                    show bg undercardboardstars_85
                    sis "You're not going anywhere. You're my heater."
                "I'll stay.":
                    show bg undercardboardstars_31
                    pov "Alright, I'll stay. Not because of you, but for the sake of the plumpness of my tooshie."
                    show bg undercardboardstars_85
                    sis "Yay."
        "Cuddle?":
            pov "You wanna sleep down here together?"
            if skill_cha >= 3:
                if sister_points <= 9:
                    $ sister_points += 1
                    $ renpy.notify("You used 3 Charisma Points\nYour relationship with [sister] has increased")
                else:
                    $ sister_points = 10
                $ skill_cha -= 3
                show bg undercardboardstars_24
                pov "I can be your source of warmth if you want. I'm at a healthy body temperature."
                show bg undercardboardstars_28
                pov "I'm actually dropping my semi-hot mixtape next year, ‘Source of Warmth'."
                show bg undercardboardstars_32
                sis "I can't wait to get a signed copy of it."
            else:
                show bg undercardboardstars_50
                pov "I guess like.. If you want, you can-"
                show bg undercardboardstars_85
                sis "I'll just cuddle up with you if you don't mind."
    show bg undercardboardstars_86
    if winc == 0:
        sis "Hehe~ Goodnight, [povname]."
    else:
        sis "Hehe~ Goodnight, baby brother."
    show bg undercardboardstars_87
    pov "Goodnight, [sister]."
    show bg undercardboardstars_1
    with fade
    $ renpy.pause()

    scene black
    with fade
    $ renpy.pause()
    "A few minutes later..."
    show bg undercardboardstars_88
    with fade
    $ renpy.pause(5,hard=True)
    show bg undercardboardstars_89
    $ renpy.pause()
    sis "{i}*Chu*{/i}"
    show bg undercardboardstars_90
    sis "{i}*Chu chup*{/i}"
    show bg undercardboardstars_91
    sis "Mmm.. {i}*Tchup-*{/i}"
    show bg undercardboardstars_92
    sis "{i}*Chuuuuuu-*{/i}"

    menu:
        "[sister]?":
            show bg undercardboardstars_95
            pov "[sister]?"
            show bg undercardboardstars_96
            sis "I-"
            sis "I love you, [povname]."
            sis "I don't say that often enough."

            menu:
                "I love you too.":
                    show bg undercardboardstars_97
                    pov "I love you too, [sister]."
                "I know you do.":
                    show bg undercardboardstars_97
                    pov "It's okay. I know you do."
            show bg undercardboardstars_98
            sis "Goodnight."
            show bg undercardboardstars_94
        "Stay silent":
            $ undercardboardstars_silent = 1
            pov "..."
            sis "{i}*Chu* Mm.. *Chuu*{/i}"
            sis "Mm..."
            show bg undercardboardstars_93
            sis "If-"
            sis "If you're awake..."
            sis "Or even if you're not..."
            sis "Know that I love you."
            show bg undercardboardstars_94
            $ renpy.pause()
    $ sister_path = 11.5

    scene black
    with fade
    $ renpy.pause()

    jump lbl_overselpt_in_basement
