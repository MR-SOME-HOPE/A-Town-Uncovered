## What are you Watching? ##
label lbl_what_are_you_watching:
    default momdrama_good = 0
    default momdrama_touch = 0
    if winc == 0:
        jump lbl_what_are_you_watching_winc0

    scene bg momdrama_1
    with fade
    pov "Hey, mom, what are you watching?"
    show bg momdrama_2
    mum "I'm just watching my dramas."
    show bg momdrama_3
    pov "The Korean stuff?"
    show bg momdrama_4
    mum "The one and only one for me."
    show bg momdrama_3
    pov "You're not usually up this late."
    show bg momdrama_5
    mum "I don't know. I just don't feel as sleepy as I used to be before."
    show bg momdrama_6
    $ renpy.pause ()
    show bg momdrama_7
    mum "You and [sister] are now young adults, not kids anymore."
    show bg momdrama_8
    mum "Well, you know, you'll both still be my babies forever but..."
    show bg momdrama_9
    pov "But what?"
    show bg momdrama_8
    mum "You two are growing up so fast and... and... I'm scared to lose my babies."

    menu:
        "[sister] and I will have to leave our nest eventually.":
            show bg momdrama_9
            pov "Mom, you know that [sister] and I will have to leave our nest eventually."
        "[sister] and I will always be there for you.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg momdrama_10
            pov "Mom, you know that [sister] and I will always be there for you."
        "That's just part of life.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_9
            pov "Mom, you know that's just part of life."
    show bg momdrama_11
    mum "It was only yesterday that I was pushing you both on the swing in your nappies.."
    mum "And... and... remember when you threw up all over my chest after breast feeding you?"
    show bg momdrama_12
    pov "Mom... that's a little too much."
    show bg momdrama_11
    mum "I'm sorry, [povname]. These dramas are bringing out my motherly emotions."
    show bg momdrama_12
    pov "Hehe, it's alright, Mom. I understand."
    show bg momdrama_7
    mum "Why does SeungHyun have to leave NaHyun?"
    show bg momdrama_13
    pov "Huh..?"
    show bg momdrama_14
    mum "He left her without saying goodbye."

    menu:
        "There there.":
            show bg momdrama_15
            pov "There there.."
        "I have no idea what you're on about.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_13
            pov "I have no idea what you're on about."
            show bg momdrama_17
            mum "The drama, [povname]. You're a smart, young man. Context clues please."
            show bg momdrama_18
            pov "Right, sorry."
        "That's unbelievable!":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg momdrama_19
            pov "What? That's unbelievable! How could he do that to her? "
            show bg momdrama_20
            mum "I know right, unfaithful jerk!"
        "I should get to bed.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_15
            pov "Hey, it's getting late, I should get to bed."
            show bg momdrama_8
            mum "Already..? I know as a mother I should be telling you to go to bed but can't you stay with me a little longer?"

            menu:
                "Did you want to talk?":
                    show bg momdrama_9
                    pov "Did you want to talk to me about something?"
                    show bg momdrama_8
                    mum "No, not really."
                "Only because I love you.":
                    if mum_points <= 8:
                        $ mum_points += 2
                        $ renpy.notify("Your relationship with Mom has increased by 2")
                    else:
                        $ mum_points = 10
                    show bg momdrama_10
                    pov "Alright, only because I love you."
                    show bg momdrama_21
                    mum "Naww, you're so adorable. You just made my whole week. I love you too."
                "I've had a long day.":
                    if mum_points >= 1:
                        $ mum_points -= 1
                        $ renpy.notify("Your relationship with Mom has decreased")
                    else:
                        $ mum_points = 0
                    show bg momdrama_22
                    pov "Sorry, but it's really getting late. I've had a long day."
                    show bg momdrama_23
                    mum "Fine. Be that way. Goodnight, [povname]."
                    show bg momdrama_24
                    pov "Goodnight, Mom."

                    jump lbl_what_are_you_watching_end
    show bg momdrama_25
    $ renpy.pause ()
    show bg momdrama_26
    mum "Hey, [povname]. Could you..."
    show bg momdrama_27
    pov "Hm? Could I what?"
    show bg momdrama_26
    mum "Could you hold your mother while she embarrassingly cries for her drama?"

    menu:
        "It's a little weird but sure.":
            show bg momdrama_12
            pov "It's a little weird but sure."
        "Of course.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg momdrama_10
            pov "Of course, Mom."
        "I'd rather not.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_9
            pov "I'd rather not, I'm not all that comfortable with the idea."
            show bg momdrama_8
            mum "Oh really? But I'm your mother? It hurts that you feel that way about a little intimacy."
            show bg momdrama_22
            pov "Sorry..."
            show bg momdrama_28
            mum "It's getting late, [povname]. I think you should get to sleep."
            show bg momdrama_29
            pov "You sure you don't want me to stay a little longer."
            show bg momdrama_28
            mum "No, it's late. You're young and need the energy for tomorrow."
            mum "Goodnight, [povname]."
            show bg momdrama_29
            pov "Goodnight, Mom."

            jump lbl_what_are_you_watching_end
    show bg momdrama_30
    $ renpy.pause ()
    show bg momdrama_31
    mum "You're so warm, [povname]."
    show bg momdrama_32
    pov "It's because I'm warm blooded."
    show bg momdrama_30
    mum "Hehe..."
    show bg momdrama_33
    mum "I can't believe you're graduating this year."
    show bg momdrama_34
    pov "Yeah, it's going to one hell of a stressful year."
    show bg momdrama_35
    mum "Remember to study hard and work hard, alright?"
    show bg momdrama_36
    pov "I know, Mom."
    show bg momdrama_35
    mum "Have you decided what you want to do after graduating? Any career caught your fancy?"
    show bg momdrama_37
    pov "Honestly, I have no idea yet. It's still early into the year."
    show bg momdrama_38
    mum "And yet I miss you already."
    show bg momdrama_39
    $ renpy.pause(1,hard=True)
    show bg momdrama_40
    $ renpy.pause(1,hard=True)
    show bg momdrama_39
    $ renpy.pause(1,hard=True)
    show bg momdrama_40
    $ renpy.pause(1,hard=True)
    show bg momdrama_39
    $ renpy.pause(1,hard=True)
    show bg momdrama_40
    $ renpy.pause(1,hard=True)
    show bg momdrama_41
    $ renpy.pause()

    menu:
        "What are you doing?":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_42
            pov "Mom? What are you doing?"
            show bg momdrama_43
            mum "What? I'm just stroking your leg, why? What's wrong with that?"
            show bg momdrama_42
            pov "It's a little weird."
            show bg momdrama_44
            mum "Are you serious, [povname]? I can't believe you're actually implying that I'm doing it sexually."
            show bg momdrama_45
            pov "What?! No.."
            show bg momdrama_46
            mum "Can't I just stroke your leg because I want to? What different is it from stroking your hair?"
            show bg momdrama_47
            pov "I didn't mean it that wa-"
            show bg momdrama_46
            mum "If a little mother-son intimacy is too much for you then don't sit so close to me."
            show bg momdrama_48
            mum "As a matter of fact, it IS getting late. You should get to bed."
            show bg momdrama_49
            $ renpy.pause()
            show bg momdrama_50
            pov "Fine. Sorry. Goodnight."

            jump lbl_what_are_you_watching_end
        "Stay silent":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg momdrama_40
            $ renpy.pause()
            show bg momdrama_51
            mum "Your dad doesn't do this for me anymore."
            show bg momdrama_52
            mum "Y'know, cuddle up with me and just spend time together."
            show bg momdrama_53
            pov "He's a very busy person. Very hardworking, don't you admire that?"
            show bg momdrama_54
            pov "Because of him, you don't have to worry about working yourself."
            show bg momdrama_55
            mum "I sure do miss going out and having my own life though."
            show bg momdrama_56
            pov "Why not get a job? [sister] and I don't need you stay home and babysit us anymore. We can help around the house and pull our weight."
            show bg momdrama_57
            mum "Your dad doesn't allow it. He's old fashioned and has that 1950s mentality."
            show bg momdrama_37
            pov "He doesn't own you, you're not his prisoner."
            show bg momdrama_58
            mum "I know that, but you know how intimidating and controlling he is."
            show bg momdrama_34
            pov "Yeah. We can't always get what we want."
            show bg momdrama_35
            mum "But don't you worry about a thing, okay? Your dad and I still love each other. I love him as much as I love you, and you know how much I love you, right?"
            show bg momdrama_37
            pov "I do, Mom. I won't forget it. You'll make sure of that."
            show bg momdrama_31
            mum "Haha, you can bet my body on that."

            menu:
                "Move her hand towards your crotch":
                    jump lbl_what_are_you_watching_5
                "I should get to bed.":
                    show bg momdrama_59
                    pov "I should really get to bed though. Thanks for the talk."
                    show bg momdrama_60
                    mum "No, thank you for cuddling up with me. I want us to do it more often. There's only so many days left before you decide to move out."
                    show bg momdrama_59
                    pov "I love you, Mom."
                    show bg momdrama_60
                    mum "I love you too. Sweet dreams."
                    $ momdrama_good = 1

                    jump lbl_what_are_you_watching_end
        "Move her hand towards your crotch":
            jump lbl_what_are_you_watching_5

label lbl_what_are_you_watching_5:
    if mum_points <= 2:
        if mum_points >= 1:
            $ mum_points -= 1
        else:
            $ mum_points = 0
        $ renpy.notify("Your relationship with Mom has decreased")
        show bg momdrama_61
        $ renpy.pause()
        show bg momdrama_62
        mum "[povname]! What are you doing? That's quite inappropriate of you. I'm your mother!"
        show bg momdrama_48
        mum "Alright... I'm uncomfortable now. I'm going to bid you goodnight and pretend that that didn't just happen."
        mum "Goodnight, [povname]."
        show bg momdrama_50
        pov "Sorry, I shouldn't hav-"
        show bg momdrama_63
        $ renpy.pause()
        show bg momdrama_50
        pov "Goodnight, Mom. I love you."
        $ momdrama_touch = 1

        jump lbl_what_are_you_watching_end
    elif mum_points >=3:
        show bg momdrama_61
        $ renpy.pause
        show bg momdrama_64
        mum "[povname]?! What are yo- oh.."
        show bg momdrama_65
        mum "Wow. You've definitely grown a lot..."
        show bg momdrama_66
        $ renpy.pause()
        show bg momdrama_67
        $ renpy.pause()
        show bg momdrama_66
        $ renpy.pause()
        show bg momdrama_67
        $ renpy.pause()
        show bg momdrama_68
        mum "The last I saw your... penis- was when you were 7 years old."

        menu:
            "I remember our bath times.":
                show bg momdrama_69
                pov "I remember those times when I had bath times with you."
                show bg momdrama_70
                mum "I remember those too. I remember that time you had an erection in front of me and you kept slapping it left and right. Hahaha!"
                show bg momdrama_71
                pov "Mom..."
                show bg momdrama_72
                mum "I guess no one taught you how to masturbate at that age."
                show bg momdrama_67
                $ renpy.pause ()
                show bg momdrama_72
                mum "You poked your sister and I in the face with it. How naughty you were back then."
                show bg momdrama_73
                mum "And look how naughty you are right now."

                jump lbl_what_are_you_watching_wank_0
            "This isn't even how big it can get.":
                show bg momdrama_69
                pov "This isn't even how big it can actually get."
                show bg momdrama_70
                mum "Oooh, you're a grower?"
                show bg momdrama_73
                mum "Would you like to show your mother how much you can grow?"
                show bg momdrama_74
                pov "If you keep stroking it, you'll see it in no time."

                jump lbl_what_are_you_watching_wank_0
            "Stay silent":
                show bg momdrama_67
                $ renpy.pause()
                show bg momdrama_73
                mum "Hehe, too shy to say anything? I'm your mother. You have nothing to be shy about towards me."
                show bg momdrama_75
                mum "Here, why don't you show me how big you can get, I need to know these things."

                jump lbl_what_are_you_watching_wank_0

label lbl_what_are_you_watching_wank_0:
    #$ what_are_you_watching_wank_counter = 0
    jump lbl_what_are_you_watching_wank_1

####################
## Wank Stage 1
label lbl_what_are_you_watching_wank_1:
    scene img_what_are_you_watching_wank_stage_1
    #$ what_are_you_watching_wank_counter += 1
    #show bg momdrama_76
    #$ renpy.pause(0.5,hard=True)
    #show bg momdrama_77
    #$ renpy.pause(0.5,hard=True)
    #if skill_sta <= 7 and what_are_you_watching_wank_counter == 6:
    #    jump lbl_what_are_you_watching_7
    #elif skill_sta <= 14 and what_are_you_watching_wank_counter == 8:
    #    jump lbl_what_are_you_watching_wank_2
    #elif skill_sta <= 20 and what_are_you_watching_wank_counter == 10:
    #    jump lbl_what_are_you_watching_wank_2
    #else:
    #    jump lbl_what_are_you_watching_wank_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_what_are_you_watching_7
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_what_are_you_watching_wank_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_what_are_you_watching_wank_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_what_are_you_watching_wank_1

image img_what_are_you_watching_wank_stage_1:
    "bg momdrama_76"
    pause 0.5
    "bg momdrama_77"
    pause 0.5
    repeat
####################
## Wank Stage 2
label lbl_what_are_you_watching_wank_2:
    scene img_what_are_you_watching_wank_stage_2
    #$ what_are_you_watching_wank_counter += 1
    #show bg momdrama_76
    #$ renpy.pause(0.3,hard=True)
    #show bg momdrama_77
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 14 and what_are_you_watching_wank_counter == 16:
    #    jump lbl_what_are_you_watching_7
    #elif skill_sta <= 20 and what_are_you_watching_wank_counter == 18:
    #    jump lbl_what_are_you_watching_wank_3
    #else:
    #    jump lbl_what_are_you_watching_wank_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_what_are_you_watching_7

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_what_are_you_watching_wank_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_what_are_you_watching_wank_2

image img_what_are_you_watching_wank_stage_2:
    "bg momdrama_76"
    pause 0.3
    "bg momdrama_77"
    pause 0.3
    repeat

####################
## Wank Stage 3
label lbl_what_are_you_watching_wank_3:
    scene img_what_are_you_watching_wank_stage_3
    #$ what_are_you_watching_wank_counter += 1
    #show bg momdrama_78
    #$ renpy.pause(0.2,hard=True)
    #show bg momdrama_79
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and what_are_you_watching_wank_counter == 40:
    #    jump lbl_what_are_you_watching_7
    #else:
    #    jump lbl_what_are_you_watching_wank_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_what_are_you_watching_7

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_what_are_you_watching_wank_3

image img_what_are_you_watching_wank_stage_3:
    "bg momdrama_78"
    pause 0.2
    "bg momdrama_79"
    pause 0.2
    repeat
####################
label lbl_what_are_you_watching_7:
    scene bg momdrama_80
    $ renpy.pause(0.5,hard=True)
    show bg momdrama_80
    with vpunch
    dad "Honey, why aren't you in bed?"
    show bg momdrama_81
    mum "O-Oh! I was just watching my drama with [povname]. I'll be up in a bit."
    show bg momdrama_82
    dad "Alright, I need to ‘talk' to you about something."
    dad "Something big came up."
    show bg momdrama_81
    mum "Oh, um sure."
    mum "I guess it's bed time, [povname]. Thanks for staying the night with me."
    mum "I love you."
    show bg momdrama_83
    pov "I love you too, Mom."
    show bg momdrama_84
    $ renpy.pause()
    dad "Get to bed, [povname]."
    dad "Now."
    $ momdrama_good = 1
    $ momdrama_touch = 1

label lbl_what_are_you_watching_end:
    $ mum_path = 1
    $ gtime = 3

    scene black
    with fade

    scene bg mybedroom_night
    with fade
    $ renpy.pause()

    jump lbl_mybedroom_night_setup

### NO WINC ###
label lbl_what_are_you_watching_winc0:

    scene bg momdrama_1
    with fade
    pov "Hey, [missus], what are you watching?"
    show bg momdrama_2
    mum "I'm just watching my dramas."
    show bg momdrama_3
    pov "The Korean stuff?"
    show bg momdrama_4
    mum "The one and only one for me."
    show bg momdrama_3
    pov "You're not usually up this late."
    show bg momdrama_5
    mum "I don't know. I just don't feel as sleepy as I used to be before."
    show bg momdrama_6
    $ renpy.pause ()
    show bg momdrama_7
    mum "You and your [sisrole] are now young adults, not kids anymore."
    show bg momdrama_8
    mum "Well, you know, you'll both still be my [povmumrole]s forever but..."
    show bg momdrama_9
    pov "But what?"
    show bg momdrama_8
    mum "You two are growing up so fast and... and... I'm scared to lose my [povmumrole]s."

    menu:
        "[sister] and I will have to leave our nest eventually.":
            show bg momdrama_9
            pov "[missus], you know that [sister] and I will have to leave our nest eventually."
        "[sister] and I will always be there for you.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg momdrama_10
            pov "[missus], you know that [sister] and I will always be there for you."
        "That's just part of life.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_9
            pov "[missus], you know that's just part of life."
    show bg momdrama_11
    mum "It was only yesterday that I was pushing you both on the swing in your nappies.."
    mum "And... and... remember when you threw up all over my chest?"
    show bg momdrama_12
    pov "[missus]... that's a little too much."
    show bg momdrama_11
    mum "I'm sorry, [povname]. These dramas are bringing out my womanly emotions."
    show bg momdrama_12
    pov "Hehe, it's alright, [missus]. I understand."
    show bg momdrama_7
    mum "Why does SeungHyun have to leave NaHyun?"
    show bg momdrama_13
    pov "Huh..?"
    show bg momdrama_14
    mum "He left her without saying goodbye."

    menu:
        "There there.":
            show bg momdrama_15
            pov "There there.."
        "I have no idea what you're on about.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_13
            pov "I have no idea what you're on about."
            show bg momdrama_17
            mum "The drama, [povname]. You're a smart, young man. Context clues please."
            show bg momdrama_18
            pov "Right, sorry."
        "That's unbelievable!":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg momdrama_19
            pov "What? That's unbelievable! How could he do that to her? "
            show bg momdrama_20
            mum "I know right, unfaithful jerk!"
        "I should get to bed.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_15
            pov "Hey, it's getting late, I should get to bed."
            show bg momdrama_8
            mum "Already..? I know as a [mumrole] I should be telling you to go to bed but can't you stay with me a little longer?"

            menu:
                "Did you want to talk?":
                    show bg momdrama_9
                    pov "Did you want to talk to me about something?"
                    show bg momdrama_8
                    mum "No, not really."
                "Only because I love you.":
                    if mum_points <= 8:
                        $ mum_points += 2
                    else:
                        $ mum_points = 10
                    $ renpy.notify("Your relationship with [missus] has increased")
                    show bg momdrama_10
                    pov "Alright, only because I love you."
                    show bg momdrama_21
                    mum "Naww, you're so adorable. You just made my whole week. I love you too."
                "I've had a long day.":
                    if mum_points >= 1:
                        $ mum_points -= 1
                        $ renpy.notify("Your relationship with [missus] has decreased")
                    else:
                        $ mum_points = 0
                    show bg momdrama_22
                    pov "Sorry, but it's really getting late. I've had a long day."
                    show bg momdrama_23
                    mum "Fine. Be that way. Goodnight, [povname]."
                    show bg momdrama_24
                    pov "Goodnight, [missus]."

                    jump lbl_what_are_you_watching_end_winc0
    show bg momdrama_25
    $ renpy.pause ()
    show bg momdrama_26
    mum "Hey, [povname]. Could you..."
    show bg momdrama_27
    pov "Hm? Could I what?"
    show bg momdrama_26
    mum "Could you hold your [mumrole] while she embarrassingly cries for her drama?"

    menu:
        "It's a little weird but sure.":
            show bg momdrama_12
            pov "It's a little weird but sure."
        "Of course.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg momdrama_10
            pov "Of course, [missus]."
        "I'd rather not.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_9
            pov "I'd rather not, I'm not all that comfortable with the idea."
            show bg momdrama_8
            mum "Oh, really? But I'm your [mumrole]? It hurts that you feel that way about a little intimacy."
            show bg momdrama_22
            pov "Sorry..."
            show bg momdrama_28
            mum "It's getting late, [povname]. I think you should get to sleep."
            show bg momdrama_29
            pov "You sure you don't want me to stay a little longer."
            show bg momdrama_28
            mum "No, it's late. You're young and need the energy for tomorrow."
            mum "Goodnight, [povname]."
            show bg momdrama_29
            pov "Goodnight, [missus]."

            jump lbl_what_are_you_watching_end_winc0
    show bg momdrama_30
    $ renpy.pause ()
    show bg momdrama_31
    mum "You're so warm, [povname]."
    show bg momdrama_32
    pov "It's because I'm warm blooded."
    show bg momdrama_30
    mum "Hehe..."
    show bg momdrama_33
    mum "I can't believe you're graduating this year."
    show bg momdrama_34
    pov "Yeah, it's going to one hell of a stressful year."
    show bg momdrama_35
    mum "Remember to study hard and work hard, alright?"
    show bg momdrama_36
    pov "I know, [missus]."
    show bg momdrama_35
    mum "Have you decided what you want to do after graduating? Any career caught your fancy?"
    show bg momdrama_37
    pov "Honestly, I have no idea yet. It's still early into the year."
    show bg momdrama_38
    mum "And yet I miss you already."
    show bg momdrama_39
    $ renpy.pause(1,hard=True)
    show bg momdrama_40
    $ renpy.pause(1,hard=True)
    show bg momdrama_39
    $ renpy.pause(1,hard=True)
    show bg momdrama_40
    $ renpy.pause(1,hard=True)
    show bg momdrama_39
    $ renpy.pause(1,hard=True)
    show bg momdrama_40
    $ renpy.pause(1,hard=True)
    show bg momdrama_41
    $ renpy.pause()

    menu:
        "What are you doing?":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
            show bg momdrama_42
            pov "[missus]? What are you doing?"
            show bg momdrama_43
            mum "What? I'm just stroking your leg, why? What's wrong with that?"
            show bg momdrama_42
            pov "It's a little weird."
            show bg momdrama_44
            mum "Are you serious, [povname]? I can't believe you're actually implying that I'm doing it sexually."
            show bg momdrama_45
            pov "What?! No.."
            show bg momdrama_46
            mum "Can't I just stroke your leg because I want to? What different is it from stroking your hair?"
            show bg momdrama_47
            pov "I didn't mean it that wa-"
            show bg momdrama_46
            mum "If a little [mumrole]-[povmumrole] intimacy is too much for you then don't sit so close to me."
            show bg momdrama_48
            mum "As a matter of fact, it IS getting late. You should get to bed."
            show bg momdrama_49
            $ renpy.pause()
            show bg momdrama_50
            pov "Fine. Sorry. Goodnight."

            jump lbl_what_are_you_watching_end_winc0
        "Stay silent":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg momdrama_40
            $ renpy.pause()
            show bg momdrama_51
            mum "Your [dadrole] doesn't do this for me anymore."
            show bg momdrama_52
            mum "Y'know, cuddle up with me and just spend time together."
            show bg momdrama_53
            pov "He's a very busy person. Very hardworking, don't you admire that?"
            show bg momdrama_54
            pov "Because of him, you don't have to worry about working yourself."
            show bg momdrama_55
            mum "I sure do miss going out and having my own life though."
            show bg momdrama_56
            pov "Why not get a job? [sister] and I don't need you stay home and babysit us anymore. We can help around the house and pull our weight."
            show bg momdrama_57
            mum "Your [dadrole] doesn't allow it. He's old fashioned and has that 1950s mentality."
            show bg momdrama_37
            pov "He doesn't own you, you're not his prisoner."
            show bg momdrama_58
            mum "I know that, but you know how intimidating and controlling he is."
            show bg momdrama_34
            pov "Yeah. We can't always get what we want."
            show bg momdrama_35
            mum "But don't you worry about a thing, okay? Your [dadrole] and I still love each other. I love him as much as I love you, and you know how much I love you, right?"
            show bg momdrama_37
            pov "I do, [missus]. I won't forget it. You'll make sure of that."
            show bg momdrama_31
            mum "Haha, you can bet my body on that."

            menu:
                "Move her hand towards your crotch":
                    jump lbl_what_are_you_watching_5_winc0
                "I should get to bed.":
                    show bg momdrama_59
                    pov "I should really get to bed though. Thanks for the talk."
                    show bg momdrama_60
                    mum "No, thank you for cuddling up with me. I want us to do it more often. There's only so many days left before you decide to move out."
                    show bg momdrama_59
                    pov "I love you, [missus]."
                    show bg momdrama_60
                    mum "I love you too. Sweet dreams."
                    $ momdrama_good = 1

                    jump lbl_what_are_you_watching_end_winc0
        "Move her hand towards your crotch":
            jump lbl_what_are_you_watching_5_winc0

label lbl_what_are_you_watching_5_winc0:
    if mum_points <= 2:
        if mum_points >= 1:
            $ mum_points -= 1
        else:
            $ mum_points = 0
        $ renpy.notify("Your relationship with [missus] has decreased")
        show bg momdrama_61
        $ renpy.pause()
        show bg momdrama_62
        mum "[povname]! What are you doing? That's quite inappropriate of you. I'm your [mumrole]!"
        show bg momdrama_48
        mum "Alright... I'm uncomfortable now. I'm going to bid you goodnight and pretend that that didn't just happen."
        mum "Goodnight, [povname]."
        show bg momdrama_50
        pov "Sorry, I shouldn't hav-"
        show bg momdrama_63
        $ renpy.pause()
        show bg momdrama_50
        pov "Goodnight, [missus]. I love you."
        $ momdrama_touch = 1

        jump lbl_what_are_you_watching_end_winc0
    elif mum_points >=3:
        show bg momdrama_61
        $ renpy.pause
        show bg momdrama_64
        mum "[povname]?! What are yo- oh.."
        show bg momdrama_65
        mum "Wow. You've definitely grown a lot..."
        show bg momdrama_66
        $ renpy.pause()
        show bg momdrama_67
        $ renpy.pause()
        show bg momdrama_66
        $ renpy.pause()
        show bg momdrama_67
        $ renpy.pause()
        show bg momdrama_68
        mum "The last I saw your... penis- was when you pooped your diaper."

        menu:
            "I remember our bath times.":
                show bg momdrama_69
                pov "I remember those times when I had bath times with you."
                show bg momdrama_70
                mum "I remember those too. I remember that time you had an erection in front of me and you kept slapping it left and right. Hahaha!"
                show bg momdrama_71
                pov "Mom..."
                show bg momdrama_72
                mum "I guess no one taught you how to masturbate at that age."
                show bg momdrama_67
                $ renpy.pause ()
                show bg momdrama_72
                mum "You poked your me and your [sisrole] in the face with it. How naughty you were back then."
                show bg momdrama_73
                mum "And look how naughty you are right now."

                jump lbl_what_are_you_watching_wank_0_winc0
            "This isn't even how big it can get.":
                show bg momdrama_69
                pov "This isn't even how big it can actually get."
                show bg momdrama_70
                mum "Oooh, you're a grower?"
                show bg momdrama_73
                mum "Would you like to show your [mumrole] how much you can grow?"
                show bg momdrama_74
                pov "If you keep stroking it, you'll see it in no time."

                jump lbl_what_are_you_watching_wank_0_winc0
            "Stay silent":
                show bg momdrama_67
                $ renpy.pause()
                show bg momdrama_73
                mum "Hehe, too shy to say anything? I'm your [mumrole]. You have nothing to be shy about towards me."
                show bg momdrama_75
                mum "Here, why don't you show me how big you can get, I need to know these things."

                jump lbl_what_are_you_watching_wank_0_winc0

label lbl_what_are_you_watching_wank_0_winc0:
    #$ what_are_you_watching_wank_counter = 0
    jump lbl_what_are_you_watching_wank_1_winc0

####################
## Wank Stage 1
label lbl_what_are_you_watching_wank_1_winc0:
    scene img_what_are_you_watching_wank_stage_1
    #$ what_are_you_watching_wank_counter += 1
    #show bg momdrama_76
    #$ renpy.pause(0.5,hard=True)
    #show bg momdrama_77
    #$ renpy.pause(0.5,hard=True)
    #if skill_sta <= 7 and what_are_you_watching_wank_counter == 6:
    #    jump lbl_what_are_you_watching_7_winc0
    #elif skill_sta <= 14 and what_are_you_watching_wank_counter == 8:
    #    jump lbl_what_are_you_watching_wank_2_winc0
    #elif skill_sta <= 20 and what_are_you_watching_wank_counter == 10:
    #    jump lbl_what_are_you_watching_wank_2_winc0
    #else:
    #    jump lbl_what_are_you_watching_wank_1_winc0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_what_are_you_watching_7_winc0
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_what_are_you_watching_wank_2_winc0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_what_are_you_watching_wank_2_winc0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_what_are_you_watching_wank_1_winc0


####################
## Wank Stage 2
label lbl_what_are_you_watching_wank_2_winc0:
    scene img_what_are_you_watching_wank_stage_2
    #$ what_are_you_watching_wank_counter += 1
    #show bg momdrama_76
    #$ renpy.pause(0.3,hard=True)
    #show bg momdrama_77
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 14 and what_are_you_watching_wank_counter == 16:
    #    jump lbl_what_are_you_watching_7_winc0
    #elif skill_sta <= 20 and what_are_you_watching_wank_counter == 18:
    #    jump lbl_what_are_you_watching_wank_3_winc0
    #else:
    #    jump lbl_what_are_you_watching_wank_2_winc0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_what_are_you_watching_7_winc0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_what_are_you_watching_wank_3_winc0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_what_are_you_watching_wank_2_winc0

####################
## Wank Stage 3
label lbl_what_are_you_watching_wank_3_winc0:
    scene img_what_are_you_watching_wank_stage_3
    #$ what_are_you_watching_wank_counter += 1
    #show bg momdrama_78
    #$ renpy.pause(0.2,hard=True)
    #show bg momdrama_79
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and what_are_you_watching_wank_counter == 40:
    #    jump lbl_what_are_you_watching_7_winc0
    #else:
    #    jump lbl_what_are_you_watching_wank_3_winc0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_what_are_you_watching_7_winc0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_what_are_you_watching_wank_3_winc0

####################
label lbl_what_are_you_watching_7_winc0:
    scene bg momdrama_80
    $ renpy.pause(0.5,hard=True)
    show bg momdrama_80
    with vpunch
    dad "Honey, why aren't you in bed?"
    show bg momdrama_81
    mum "O-Oh! I was just watching my drama with [povname]. I'll be up in a bit."
    show bg momdrama_82
    dad "Alright, I need to ‘talk' to you about something."
    dad "Something big came up."
    show bg momdrama_81
    mum "Oh, um sure."
    mum "I guess it's bed time, [povname]. Thanks for staying the night with me."
    mum "I love you."
    show bg momdrama_83
    pov "I love you too, [missus]."
    show bg momdrama_84
    $ renpy.pause()
    dad "Get to bed, [povname]."
    dad "Now."
    $ momdrama_good = 1
    $ momdrama_touch = 1

label lbl_what_are_you_watching_end_winc0:
    $ mum_path = 1
    $ gtime = 3

    scene black
    with fade

    scene bg mybedroom_night
    with fade
    $ renpy.pause()

    jump lbl_mybedroom_night_setup
