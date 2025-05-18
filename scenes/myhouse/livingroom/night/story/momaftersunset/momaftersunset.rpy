## Mom Past Sunset ##
label lbl_mom_past_sunset:

    scene bg momaftersunset_1
    with fade
    $ renpy.pause()
    show black
    with fade
    "Later that night."

    scene bg momaftersunset_2
    with fade
    $ renpy.pause()
    show bg momaftersunset_3
    if winc == 0:
        mum "You think [dadname] has gone to bed by now?"
    else:
        mum "You think Dad has gone to bed by now?"
    mum "He usually sleeps early because he has to wake up early."
    show bg momaftersunset_4
    pov "I guess if that's the case, he's out like a rock."
    show bg momaftersunset_3
    mum "What about [sister]?"
    show bg momaftersunset_5
    pov "I don't know. I honestly don't know if she's in her room or out of the house."
    pov "Do you want me to quickly go check?"
    show bg momaftersunset_6
    mum "No, it's alright. It's not that important, don't leave me."
    show bg momaftersunset_9
    mum "..."
    show bg momaftersunset_7
    mum "Thank you for keeping me company, honey."
    mum "It's been a lonely time. I'm all by myself in the house most of the time."
    show bg momaftersunset_8
    pov "Why don't you go out much?"
    show bg momaftersunset_7
    mum "I mean I do, but I'm more of an indoor cat."
    show bg momaftersunset_9
    mum "..."
    if mum_points >= 7:
        jump lbl_mom_past_sunset_1
    elif mum_points <= 6:
        jump lbl_mom_past_sunset_2

label lbl_mom_past_sunset_1:
    show bg momaftersunset_10
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_11
    mum "You don't mind if I let these puppies out right? It's a little stuffy in here."
    show bg momaftersunset_12
    pov "..."
    show bg momaftersunset_13
    pov "N-n-no... n-not at all."
    show bg momaftersunset_14
    mum "Thanks, honey."
    show bg momaftersunset_15
    mum "Hehehe."
    if winc == 0:
        mum "There's no need to feel flustered, we've seen each other naked before."
        show bg momaftersunset_16
        pov "[missus]... don't remind me of how embarrassing that was."
    else:
        mum "There's no need to feel flustered, we've seen each other naked before. You've sucked on these very breasts."
        show bg momaftersunset_16
        pov "Mom... that was more than 10 years ago."
    show bg momaftersunset_14
    mum "Oh, don't be like that."
    show bg momaftersunset_17
    $ renpy.pause()
    mum "..."
    if skill_str > skill_sta:
        jump lbl_mom_past_sunset_1_1
    elif skill_sta > skill_str:
        jump lbl_mom_past_sunset_1_2
    elif mum_points >= 7 and skill_sta == skill_str:
        $ mompastsunset_randomgen = renpy.random.randint(1,2)
        if mompastsunset_randomgen == 1:
            jump lbl_mom_past_sunset_1_1
        else:
            jump lbl_mom_past_sunset_1_2

label lbl_mom_past_sunset_1_1:
    show bg momaftersunset_40
    mum "[povname]. Can you... um... massage my.. chest?"
    show bg momaftersunset_41
    pov "Your- chest?"
    show bg momaftersunset_40
    mum "Well... more like my boobs.. haha..."

    menu:
        "It'll be my pleasure.":
            jump lbl_momaftersunset_massage
        "I don't think I should.":
            show bg momaftersunset_42
            pov "I don't think I should be doing that to you."
            show bg momaftersunset_32
            mum "Oh... well, sorry I asked."
            mum "I thought that you'd be more than happy to do so for me..."
            show bg momaftersunset_43
            mum "Aren't you attracted to me?"
            show bg momaftersunset_31
            pov "It's not that."
            show bg momaftersunset_44
            mum "Am I not attractive at all?"
            show bg momaftersunset_45
            pov "You are, Mom..."
            show bg momaftersunset_32
            mum "Y'know what. Don't.. don't worry about. Seriously. Let's just, cuddle, and enjoy the movie. I'm sorry for putting you on the spot like that."
            show bg momaftersunset_46
            pov "..."
            show bg momaftersunset_30
            mum "Really, [povname]. It was really quite stupid of me to ask such a forward thing. Don't worry, sweetie."
            show bg momaftersunset_29
            pov "I hope so."
            show bg momaftersunset_47
            $ renpy.pause()
            show bg momaftersunset_48
            if winc == 0:
                mum "We'll still have [mumrole]-[povmumrole] time tomorrow right?"
            else:
                mum "We'll still have mother-son time tomorrow right?"

            menu:
                "Of course.":
                    show bg momaftersunset_49
                    if winc == 0:
                        pov "Of course, [missus]. I wouldn't leave you."
                        show bg momaftersunset_50
                        mum "That's my [povmumrole]."
                    else:
                        pov "Of course, Mom. I wouldn't leave you."
                        show bg momaftersunset_50
                        mum "That's my boy."
                    $ mompastsunset_attend = 4

                    jump lbl_mom_past_sunset_end
                "I can't...":
                    show bg momaftersunset_37
                    pov "I can't..."
                    show bg momaftersunset_51
                    mum "Oh. Alright.. Fine. No worries."
                    $ mompastsunset_attend = 3

                    jump lbl_mom_past_sunset_end

label lbl_mom_past_sunset_1_2:
    show bg momaftersunset_40
    mum "[povname]. Do you... want to... um... suck... on my... breast...?"
    show bg momaftersunset_41
    pov "Suck...?"
    show bg momaftersunset_40
    mum "Well... umm.. yeah! Hehehe..."
    show bg momaftersunset_30
    mum "Oh my God... did I really just ask that?"
    show bg momaftersunset_61
    mum "Just forget I even suggested it..."

    menu:
        "I'd love to.":
            show bg momaftersunset_63
            if winc == 0:
                pov "I'd love to, [missus]."
            else:
                pov "I'd love to, Mom."
            show bg momaftersunset_64
            mum "Y-you want to?"
            show bg momaftersunset_65
            pov "Why wouldn't I?"
            show bg momaftersunset_suck_1
            mum "Come here then."

            jump lbl_momaftersunset_suck
        "I didn't think it was right either way.":
            show bg momaftersunset_62
            pov "Alright... I didn't think it was right for me to either way..."
            show bg momaftersunset_18
            mum "Yeah, no. I understand. I have no idea why that was in my head."
            show bg momaftersunset_30
            mum "I hope you don't look down on me..."
            show bg momaftersunset_52
            mum "I'm really sorry..."
            show bg momaftersunset_53
            if winc == 0:
                pov "It's okay, [missus]. Really."
                show bg momaftersunset_54
                mum "We'll still have [mumrole]-[povmumrole] time tomorrow right?"
            else:
                pov "It's okay, Mom. Really."
                show bg momaftersunset_54
                mum "We'll still have mother-son time tomorrow right?"

            menu:
                "Of course.":
                    if winc == 0:
                        show bg momaftersunset_49
                        pov "Of course, [missus]. I wouldn't leave you."
                        show bg momaftersunset_50
                        mum "That's my [povmumrole]."
                    else:
                        show bg momaftersunset_49
                        pov "Of course, Mom. I wouldn't leave you."
                        show bg momaftersunset_50
                        mum "That's my boy."
                    $ mompastsunset_attend = 4

                    jump lbl_mom_past_sunset_end
                "I can't...":
                    show bg momaftersunset_37
                    pov "I can't..."
                    show bg momaftersunset_51
                    mum "Oh. Alright.. Fine. No worries."
                    $ mompastsunset_attend = 3

                    jump lbl_mom_past_sunset_end

label lbl_mom_past_sunset_2:
    show bg momaftersunset_10
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_11
    mum "Hey, [povname]. You don't mind if I just.. let my boobs out right? It's a little hot."
    show bg momaftersunset_12
    pov "..."
    show bg momaftersunset_13
    pov "N-no.... n-not at all."
    show bg momaftersunset_14
    mum "Thanks, sweetie."
    show bg momaftersunset_15
    mum "If you're not fine with a little nudity, I can cover up again. It's no big deal."
    show bg momaftersunset_16
    pov "It's alright."
    show bg momaftersunset_14
    if winc == 0:
        mum "We're adults, both mature enough. There's nothing to be ashamed about."
    else:
        mum "We're family, both mature enough. There's nothing to be ashamed about."
    show bg momaftersunset_17
    $ renpy.pause()
    show bg momaftersunset_18
    mum "I really appreciate you taking the time out of your night to be with me, [povname]."
    mum "You don't know how much this means to me."
    show bg momaftersunset_19
    pov "I love being with you, strangely enough."
    show bg momaftersunset_20
    mum "Strangely enough."
    show bg momaftersunset_21
    pov "You do have your boobs out."
    show bg momaftersunset_22
    mum "What me to put them back?"
    show bg momaftersunset_23
    pov "No!"
    show bg momaftersunset_24
    mum "Hahahaha! I've never seen you so opposing about something before."
    mum "That's the type of ‘no!' that you'd use when you see me get murdered or something."
    show bg momaftersunset_25
    mum "Hahahaha!"
    show bg momaftersunset_26
    pov "Stop teasing me, both verbally and physically."
    show bg momaftersunset_27
    mum "You like me don't you?"
    mum "You like-like me don't you?"
    show bg momaftersunset_28
    pov "..."
    show bg momaftersunset_14
    mum "I love you, honey. Don't hate me, hehehe."
    if winc == 0:
        mum "Why don't we do this everyday? You and I, mother and son. Movie night, starting before the sun sets. What do you say?"
    else:
        mum "Why don't we do this everyday? You and I, [mumrole] and [povmumrole]. Movie night, starting before the sun sets. What do you say?"

    menu:
        "That sounds great.":
            show bg momaftersunset_16
            if winc == 0:
                pov "That sound great, [missus]."
            else:
                pov "That sound great, Mom."
            show bg momaftersunset_14
            mum "I'm glad you think so."
            show bg momaftersunset_17
            $ renpy.pause()
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ renpy.notify("Your relationship with Mom has increased")
            $ mompastsunset_attend = 4

            jump lbl_mom_past_sunset_end
        "I don't think so.":
            show bg momaftersunset_29
            pov "Everyday? I don't think so."
            show bg momaftersunset_30
            mum "Why not? You have the whole day to do whatever you want!"
            mum "You work, you have university, you have a little bit of time to do other activities."
            mum "All I'm asking is for a little time with you."

            menu:
                "You convinced me.":
                    show bg momaftersunset_16
                    if winc == 0:
                        pov "Alright, [missus]. You convinced me."
                    else:
                        pov "Alright, Mom. You convinced me."
                    show bg momaftersunset_14
                    mum "Thank you, honey. You won't regret it."
                    show bg momaftersunset_17
                    $ renpy.pause()
                    $ mompastsunset_attend = 4

                    jump lbl_mom_past_sunset_end
                "I don't think that's possible.":
                    show bg momaftersunset_31
                    pov "Sorry, I really don't think that's possible."
                    show bg momaftersunset_32
                    mum "Alright then. Fine by me."
                    show bg momaftersunset_33
                    $ renpy.pause()
                    $ mompastsunset_attend = 3

                    jump lbl_mom_past_sunset_end

label lbl_mom_past_sunset_end:
    $ gtime = 3
    if mum_path == 6:
        $ mompastsunset_went = 1
    else:
        pass

    scene bg mybedroom_night
    with fade

    jump lbl_mybedroom_night_setup

label lbl_mom_past_sunset_again_pre:
    if mum_points >= 7:
        show pov smirk_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral at right
        with dissolve
        pov "Want to hang out tonight? Have some fun, maybe?"
        show pov smirk at left
        show mum smirk_talk at right
    else:
        show pov embarrassed_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral at right
        with dissolve
        pov "Want to hang out tonight? Spend time together?"
        show pov neutral at left
        show mum neutral_talk at right
    mum "Oh, I'd love that. Go and put a movie on."

label lbl_mom_past_sunset_again:

    scene bg momaftersunset_1
    with fade
    $ renpy.pause()
    show black
    with fade
    "Later that night."

    scene bg momaftersunset_34
    with fade
    $ renpy.pause()
    if mum_points >= 7:
        jump lbl_mom_past_sunset_again_1
    elif mum_points <= 6:
        jump lbl_mom_past_sunset_again_2

label lbl_mom_past_sunset_again_1:
    if skill_str > skill_sta:
        jump lbl_mom_past_sunset_again_1_1
    elif skill_sta > skill_str:
        jump lbl_mom_past_sunset_again_1_2
    elif mum_points >= 7 and skill_sta == skill_str:
        $ mompastsunset_randomgen = renpy.random.randint(1,2)
        if mompastsunset_randomgen == 1:
            jump lbl_mom_past_sunset_again_1_1
        else:
            jump lbl_mom_past_sunset_again_1_2

label lbl_mom_past_sunset_again_1_1:
    show bg momaftersunset_35
    if winc == 0:
        mum "[povname]. Be a good boy and massage [missus]'s breasts for her."
    else:
        mum "[povname]. Be a good boy and massage Mommy's breasts for her."

    menu:
        "I'd love to.":
            show bg momaftersunset_55
            pov "I'd love to."
            $ momaftersunset_massage_count = 0

            jump lbl_momaftersunset_massage_1
        "Not tonight.":
            show bg momaftersunset_56
            if winc == 0:
                pov "Not tonight, [missus]. I'm a little tired."
            else:
                pov "Not tonight, Mom. I'm a little tired."
            show bg momaftersunset_57
            mum "Are you now? I am too y'know."
            show bg momaftersunset_58
            mum "You should take care of me like the good boy that you are."

            menu:
                "Alright.":
                    show bg momaftersunset_59
                    if winc == 0:
                        pov "Alright, [missus]."
                    else:
                        pov "Alright, Mom."
                    show bg momaftersunset_50
                    mum "That's my boy."
                    $ momaftersunset_massage_count = 0

                    jump lbl_momaftersunset_massage_1
                "Seriously, [missus]." if winc == 0:
                    show bg momaftersunset_37
                    pov "Seriously, [missus]. I don't feel like it tonight."
                    show bg momaftersunset_51
                    mum "Fine. Be that way."
                    show bg momaftersunset_38
                    mum "Y'know, not a lot [mumrole]s let their grown-up [povmumrole]s play with their tits like I do."
                    show bg momaftersunset_51
                    mum "It's your loss."
                    if mum_path == 6:
                        $ mompastsunset_attend = 3
                    else:
                        pass

                    jump lbl_mom_past_sunset_end
                "Seriously, Mom." if winc == 1:
                    show bg momaftersunset_37
                    pov "Seriously, Mom. I don't feel like it tonight."
                    show bg momaftersunset_51
                    mum "Fine. Be that way."
                    show bg momaftersunset_38
                    mum "Y'know, not a lot mothers let their grown-up sons play with their tits like I do."
                    show bg momaftersunset_51
                    mum "It's your loss."
                    if mum_path == 6:
                        $ mompastsunset_attend = 3
                    else:
                        pass

                    jump lbl_mom_past_sunset_end

label lbl_mom_past_sunset_again_1_2:
    show bg momaftersunset_35
    if winc == 0:
        mum "[povname]. Be a good boy and come suck on [missus]'s breasts."
    else:
        mum "[povname]. Be a good boy and come suck on Mommy's breasts."

    menu:
        "It'll be my pleasure.":
            show bg momaftersunset_60
            if winc == 0:
                pov "It'll be my pleasure."
            else:
                pov "It'll be my pleasure, 'Mommy'."
            scene bg momaftersunset_suck_1
            $ renpy.pause()
            scene bg momaftersunset_suck_2
            with fade
            $ momaftersunset_suck_count = 0

            jump lbl_momaftersunset_suck_1
        "Not tonight.":
            show bg momaftersunset_56
            pov "Not tonight, Mom. I'm a little tired."
            show bg momaftersunset_57
            mum "Are you now? C'mon and suck them."
            show bg momaftersunset_58
            mum "They'll give you energy again, a Mommy's guarantee."

            menu:
                "Alright.":
                    show bg momaftersunset_59
                    if winc == 0:
                        pov "Alright, [missus]."
                    else:
                        pov "Alright, Mom."
                    show bg momaftersunset_50
                    mum "That's my boy."
                    scene bg momaftersunset_suck_1_1
                    $ renpy.pause()
                    scene bg momaftersunset_suck_2
                    with fade
                    $ momaftersunset_suck_count = 0

                    jump lbl_momaftersunset_suck_1
                "Seriously, [missus]." if winc == 0:
                    show bg momaftersunset_37
                    pov "Seriously, [missus]. I don't feel like it tonight."
                    show bg momaftersunset_51
                    mum "Fine. Be that way."
                    show bg momaftersunset_38
                    mum "Y'know, not a lot [mumrole]s let their grown-up [povmumrole]s suck on their tits like I do."
                    show bg momaftersunset_51
                    mum "It's your loss."
                    if mum_path == 6:
                        $ mompastsunset_attend = 3
                    else:
                        pass

                    jump lbl_mom_past_sunset_end
                "Seriously, Mom." if winc == 1:
                    show bg momaftersunset_37
                    pov "Seriously, Mom. I don't feel like it tonight."
                    show bg momaftersunset_51
                    mum "Fine. Be that way."
                    show bg momaftersunset_38
                    mum "Y'know, not a lot mothers let their grown-up sons suck on their tits like I do."
                    show bg momaftersunset_51
                    mum "It's your loss."
                    if mum_path == 6:
                        $ mompastsunset_attend = 3
                    else:
                        pass

                    jump lbl_mom_past_sunset_end

label lbl_mom_past_sunset_again_2:
    show bg momaftersunset_35
    mum "Hey, [povname]? You're going to be spending time with me tomorrow again, right?"

    menu:
        "Yeah, of course.":
            show bg momaftersunset_36
            if winc == 0:
                pov "Of course, [missus]. I wouldn't miss a night with you."
            else:
                pov "Of course, Mom. I wouldn't miss a night with you."
            show bg momaftersunset_35
            mum "Good boy."
            show bg momaftersunset_34
            $ renpy.pause()
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ renpy.notify("Your relationship with Mom has increased")

            jump lbl_mom_past_sunset_end
        "Again? I don't think so.":
            show bg momaftersunset_37
            if winc == 0:
                pov "Again? I don't think so, [missus]. I've got other things to do."
                show bg momaftersunset_38
                mum "Am I not important enough to spend a few hours with everyday?"
                mum "What happened to us?"
            else:
                pov "Again? I don't think so, Mom. I've got other things to do."
                show bg momaftersunset_38
                mum "Am I not important enough to spend a few hours with everyday?"
                mum "What happened to family?"
            show bg momaftersunset_39
            $ renpy.pause()
            if mum_path == 6:
                $ mompastsunset_attend = 3
            else:
                pass

            jump lbl_mom_past_sunset_end
