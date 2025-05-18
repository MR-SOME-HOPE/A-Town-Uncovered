## Family Dinner ##
label lbl_family_dinner:

    scene bg familydinner_1
    with fade
    #"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    $ hardpause(1.5)
    show bg familydinner_2
    sis "Mmmm!"
    show bg familydinner_3
    sis "Dhiss- iss- shoo- gjoooood!"
    show bg familydinner_4
    mum "Please don't talk with your mouth full, [sister]."
    show bg familydinner_5
    sis "Hssorry-"
    show bg familydinner_6
    if winc == 1:
        pov "Jesus, Mom! Tell her she eats like a pig."
    else:
        pov "Jesus, [missus]! Tell her she eats like a pig."
    show bg familydinner_7
    mum "You eat like a pig, honey. Chew with your mouth shut."
    show bg familydinner_8
    sis "Hs-"
    show bg familydinner_9
    mum "..."
    show bg familydinner_10
    sis "..."
    show bg familydinner_11
    mum "So, [povname]. How's university going these days? Have you looked into any colleges?"
    show bg familydinner_12
    pov "Not at the moment. Just thinking about it stresses me out."
    show bg familydinner_13
    mum "Don't leave it to the last second, this is your future we're talking about."
    show bg familydinner_14
    pov "Yeah, yeah."
    show bg familydinner_15
    mum "[sister]'s got plans for her education."
    show bg familydinner_16
    mum "Of course, ignoring the whole dropping out thing."
    show bg familydinner_17
    sis "Do you really have to bring that up?"
    sis "I know that was not the brightest play but at least I'm doing things on my terms."
    show bg familydinner_18
    mum "Oh, yes, baby-girl. I'm really proud of you, don't think I'm not."
    show bg familydinner_19
    mum "I'm proud of both of you."

    menu:
        "We're proud of you too, Mom." if winc == 1:
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg familydinner_20
            pov "We're proud of you too, Mom."
            pov "For being the best mom ever."
            show bg familydinner_21
            sis "Yeah, I'm really glad that out of all the moms in the world, you're the one I have."
            show bg familydinner_22
            mum "Oh, you two. Stop it. You're gonna make me cry."
        "We're proud of you too, [missus]." if winc == 0:
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg familydinner_20
            pov "We're proud of you too, [missus]."
            pov "For being the best [mumrole] ever."
            show bg familydinner_21
            sis "Yeah, I'm really glad that out of all the [mumrole] in the world, you're the one I have."
            show bg familydinner_22
            mum "Oh, you two. Stop it. You're gonna make me cry."
        "I'm super proud of [sister].":
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Your relationship with [sister] has increased")
            else:
                $ sister_points = 10
            show bg familydinner_23
            pov "I'm super proud of [sister]."
            pov "She's been through a lot recently but now, she's strong-willed, passionate, and-"
            show bg familydinner_24
            if winc == 1:
                pov "Just a really awesome twin sister that I cannot imagine living without."
            else:
                pov "Just a really awesome [sisrole] that I cannot imagine living without."
            show bg familydinner_25
            sis "Are we having Italian tonight? Because that was really cheesy, [povname]. Hehehe~"
            if siblingjailtime_hj == 1:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                if winc == 1:
                    $ renpy.notify("Your relationship with Mom has decreased")
                else:
                    $ renpy.notify("Your relationship with [missus] has decreased")
                show bg familydinner_26
                mum "You two have really gotten close, huh?"
                show bg familydinner_27
                mum "As much as I'm happy to hear this, I-"
                show bg familydinner_28
                mum "Y'know what? The past is the past, there's no point bringing it up."
                show bg familydinner_29
                mum "You two know what's right and wrong..."
                show bg familydinner_30
                mum "What happened in that jail cell stays in the jail cell."
            else:
                show bg familydinner_19
                mum "That's really sweet of you to say, [povname]."
                if winc == 1:
                    mum "I'm so happy to see my babies get along so well. A mother's dream come true."
                else:
                    mum "I'm so happy to see my [povmumrole]s get along so well. A [mumrole]'s dream come true."
        "Thanks, Mom." if winc == 1:
            show bg familydinner_20
            pov "Thanks, Mom."
            show bg familydinner_21
            sis "We love you, Mom."
            show bg familydinner_31
            mum "I love you both, so-so much."
            show bg familydinner_12
            pov "And I love tonight's dinner!"
            show bg familydinner_22
            mum "One of your favourites."
        "Thanks, [missus]." if winc == 0:
            show bg familydinner_20
            pov "Thanks, [missus]."
            show bg familydinner_21
            sis "We love you, [missus]."
            show bg familydinner_31
            mum "I love you both, so-so much."
            show bg familydinner_12
            pov "And I love tonight's dinner!"
            show bg familydinner_22
            mum "One of your favourites."
    show bg familydinner_32
    sis "..."
    show bg familydinner_33
    if winc == 1:
        sis "Are you and- dad- gonna..."
        show bg familydinner_34
        mum "Your father and I have talked."
    else:
        sis "Are you and- [dadname]- gonna..."
        show bg familydinner_34
        mum "Your [dadrole] and I have talked."
    mum "And he has agreed to leave your fort alone as long as you're either working and paying board, or you're studying."
    show bg familydinner_35
    mum "That goes for the both of you."
    show bg familydinner_36
    pov "So you're not gonna..."
    show bg familydinner_34
    if winc == 1:
        mum "My kids shouldn't really be asking that sort of thing."
    else:
        mum "My [povmumrole]s shouldn't really be asking that sort of thing."

    mum "We are not getting a divorce, we're going to try harder, that's all."
    show bg familydinner_37
    if winc == 1:
        mum "We're both going to try to be better parents and a better couple."
        show bg familydinner_38
        sis "You're perfect, Mom. It's him that needs to get his shit together."
    else:
        mum "We're both going to try to be better [povmumrole]s and a better couple."
        show bg familydinner_38
        sis "You're perfect, [missus]. It's him that needs to get his shit together."
    show bg familydinner_39
    mum "Ahem- language. Not at the table."
    show bg familydinner_40
    sis "Sorry..."
    show bg familydinner_41
    menu:
        "Wouldn't it be better to divorce him?":
            show bg familydinner_42
            pov "Wouldn't it be better to divorce his ass?"
            show bg familydinner_43
            mum "Hey! What did I say about language?"
            show bg familydinner_42
            pov "I'm sorry, but I'm just saying that you don't have to stay together just for us."
            show bg familydinner_44
            pov "If you ask for our opinions-"
            show bg familydinner_45
            mum "That's enough from you, [povname]."
            mum "You're young and ignorant. You don't know what years of marriage means."
            show bg familydinner_46
            if winc == 1:
                mum "Just because your father is having a rough time in this new town, does not mean that he's going to be like this forever."
            else:
                mum "Just because your [dadrole] is having a rough time in this new town, does not mean that he's going to be like this forever."
            mum "I know him, I know how he really is."
            show bg familydinner_47
            mum "He just needs more love and support, he needs a family to be behind him."
        "I won't have to deal with him.":
            show bg familydinner_42
            pov "I won't have to deal with him for much longer anyways."
            show bg familydinner_43
            mum "What does that mean?"
            show bg familydinner_48
            pov "As in I'm going to be moving to college soon-"
            show bg familydinner_49
            mum "So you {i}are{/i} going to college."
            show bg familydinner_50
            pov "I mean, that's the general plan."
            show bg familydinner_47
            mum "{i}*Sigh*{/i} Listen, the both of you."
            if winc == 1:
                mum "Your dad, you know how he normally is."
            else:
                mum "Your [dadrole], you know how he normally is."
            show bg familydinner_43
            mum "It's just been so hard for him ever since we moved here. I hope you understand how much he's struggling with everything."
            show bg familydinner_47
            mum "And he's struggling and stressing all for us. So at least be thankful for that."
        "I'm worried about you.":
            show bg familydinner_51
            pov "I'm worried about you."
            show bg familydinner_52
            mum "Why are you worried about me?"
            if undercardboardstars_sisterknowsabouteye == 1:
                show bg familydinner_53
                sis "It's because he might hurt you again!"
                show bg familydinner_34
                mum "..."
                mum "{i}*Sigh*{/i}"
                mum "Listen, you two don't have to worry about it at all."
                show bg familydinner_35
                mum "I'm not saying that it was alright for him to do that."
                show bg familydinner_34
                mum "[povname]. I'm telling you right now, it is never okay to hit a woman."
                mum "Things were just in the heat of the moment and I can't say that I'd been the most supportive and understanding at the time."
                show bg familydinner_39
                mum "{i}*Sigh*{/i} I'm okay. Just- eat your food."
            else:
                show bg familydinner_53
                sis "It's because he might hurt you again!"
                show bg familydinner_34
                mum "..."
                mum "H-He won't hurt me, [sister]."
                mum "If he touches me..."
                show bg familydinner_35
                mum "Y'know what, we shouldn't be talking about this."
                mum "Let's just continue eating and change the subject."
                show bg familydinner_39
                mum "Don't worry about Mommy. Okay, [sister]?"
                if winc == 1:
                    mum "Mommy loves the both of you."
                else:
                    mum "I love the both of you."
    show bg familydinner_32
    mum "..."
    show bg familydinner_1
    mum "So, [sister]. Are you still going to work at that store?"
    show bg familydinner_2
    mum "Um... [povname]... knows right?"
    show bg familydinner_21
    if winc == 1:
        sis "Yes, Mom. He knows, don't worry. We've talked plenty about it."
    else:
        sis "Yes, [missus]. He knows, don't worry. We've talked plenty about it."
    show bg familydinner_19
    mum "Oh well, I'm free to talk freely about it then."
    show bg familydinner_21
    sis "And to answer your first question; yes, I'm still going to be working at the store."
    sis "I may as well, I'll need the money for the online college."
    show bg familydinner_30
    mum "Oh, good. That- that's good to hear."
    show bg familydinner_23
    pov "‘Good to hear'."
    show bg familydinner_13
    mum "Hmm?"
    show bg familydinner_12
    if winc == 1:
        pov "Oh, it's just a little funny that your daughter is continuing to work as a sex toy tester and that's good news to you."
    else:
        pov "Oh, it's just a little funny that your [povmumrole] is continuing to work as a sex toy tester and that's good news to you."
    show bg familydinner_54
    sis "Y'know, just because you all know what I do, doesn't make it less embarrassing when you say it out loud like that."
    show bg familydinner_55
    mum "It's an honest-paying blue-collar job."
    mum "You could be doing something worst, like drug dealing."
    if missallaway_path >= 23:
        show bg familydinner_56
        pov "Haha... yeah. Drug dealing. Funny example."
        show bg familydinner_57
        sis "Why do you sound so guilty."
        show bg familydinner_58
        pov "Hahaha.. It's part of the comedy. To sound like I've actually done that..."
        pov "Which I haven't!"
        show bg familydinner_59
        pov "I-I'm still doing the bit... hahaha!"
        pov "Funnies!"
        show bg familydinner_60
        sis "..."
        show bg familydinner_61
        mum "Kids these days and their internet mee-mees."
        show bg familydinner_62
        sis "Oof."
    else:
        show bg familydinner_63
        pov "You should be one of those people who dives into shit and cleans the sewers. Have you seen that video on MeTube?"
        pov "‘Worst job in the world'."
        show bg familydinner_64
        sis "That is fucking disgusting."
        show bg familydinner_65
        mum "Excuse me, both of you. I'm eating here!"
        show bg familydinner_66
        pov "Sorry."
        show bg familydinner_67
        sis "Sorry."
    show bg familydinner_55
    mum "And you, [povname]?"
    show bg familydinner_12
    pov "Yup, still working as Icecream'py."
    show bg familydinner_6
    pov "Where the cream is better and your mouth gets wetter."
    show bg familydinner_68
    mum "Is- is that the slogan?"
    show bg familydinner_69
    pov "Yeah?"
    show bg familydinner_70
    sis "Really?"
    show bg familydinner_71
    pov "Yeah..."
    show bg familydinner_72
    mum "Huh-"
    show bg familydinner_73
    if winc == 1:
        mum "Anyway, better I clean up, I just wanted to tell you both that your father will be coming back home on Monday."
    else:
        mum "Anyway, better I clean up, I just wanted to tell you both that your [dadrole] will be coming back home on Monday."
    mum "We figured that it's better that he comes back on a day where he's not home all day."
    show bg familydinner_74
    sis "He's still dead to me."
    show bg familydinner_75
    mum "I told him that if he doesn't apologize sincerely enough to you, that he'll be out for another week until he's accepted back."
    show bg familydinner_76
    sis "That sounds fair."
    show bg familydinner_77
    pov "Show no mercy?"
    show bg familydinner_78
    sis "Show no mercy."
    show bg familydinner_32
    if winc == 1:
        mum "Children. Please."
    else:
        mum "[povmumrole]s. Please."
    mum "It's like you both have forgotten how loving he was before we moved."
    show bg familydinner_39
    mum "I know things have been rough for not just him but all of us, but together, we'll make it through each day."
    show bg familydinner_35
    mum "Family comes first, right?"

    menu:
        "Even if that includes douche-dad." if winc == 1:
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg familydinner_79
            pov "Family comes first, even if it that includes douche-dad."
            show bg familydinner_26
            mum "Thank you, [povname]."
            mum "[sister]? What do you say?"
            sis "..."
            show bg familydinner_57
            sis "As long as [povname] is with me, I'll feel safe."
        "Even if that includes douche-[dadrole]." if winc == 0:
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg familydinner_79
            pov "Family comes first, even if it that includes douche-[dadrole]."
            show bg familydinner_26
            mum "Thank you, [povname]."
            mum "[sister]? What do you say?"
            sis "..."
            show bg familydinner_57
            sis "As long as [povname] is with me, I'll feel safe."
        "Some more than others.":
            show bg familydinner_79
            pov "Some more than others."
            show bg familydinner_52
            mum "..."
            if winc == 1:
                mum "Family is family. If you say that about dad, you can say that about anyone."
                show bg familydinner_60
                mum "Including me, or your sister."
            else:
                mum "Family is family. If you say that about [dadrole], you can say that about anyone."
                show bg familydinner_60
                mum "Including me, or [sister]."
            show bg familydinner_77
            pov "I didn't mean you guys."
            show bg familydinner_52
            mum "Just- try? Okay? [sister]?"
            show bg familydinner_8
            sis "Yeah... I'll try too."
        "Not really.":
            show bg familydinner_80
            pov "Not really."
            if mum_points >= 1:
                $ mum_points -= 1
            else:
                $ mum_points = 0
            if sister_points >= 1:
                $ sister_points -= 1
            else:
                $ sister_points = 0
            if winc == 1:
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ renpy.notify("Your relationship with [missus] has decreased")
            $ renpy.pause(1,hard=False)
            $ renpy.notify("Your relationship with [sister] has decreased")
            show bg familydinner_81
            mum "[povname]!"
            mum "I can't believe you don't think family comes first!"
            show bg familydinner_82
            if winc == 1:
                sis "You don't think Mom and I are important to you?"
            else:
                sis "You don't think [missus] and I are important to you?"
            show bg familydinner_83
            pov "You are!"
            show bg familydinner_84
            mum "That's-"
            show bg familydinner_82
            sis "I'm disappointed in you, [povname]. I thought we had an agreement on family."
            show bg familydinner_72
            mum "At least [sister] has her head in the right place."
    show bg familydinner_32
    mum "Hm."
    show bg familydinner_41
    mum "Well, I think I'm done. [sister], it's your turn to do the dishes."
    show bg familydinner_67
    sis "Ugh, I hate doing dishes when you cook this. It's so saucy."
    show bg familydinner_20
    if winc == 1:
        pov "Thanks for dinner, Mom."
    else:
        pov "Thanks for dinner, [missus]."
    show bg familydinner_21
    sis "Mhmm, thank-a-you."
    show bg familydinner_19
    mum "Welcome."
    $ sister_path = 37
    $ gtime = 3

    scene black
    with fade
    $ renpy.pause()

    scene bg mybedroom_night
    with fade

    jump lbl_mybedroom_night_setup
