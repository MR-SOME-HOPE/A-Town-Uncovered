## Mom Fallen Asleep ##
label lbl_mom_fallen_asleep:
    default momfallenasleep_confession = 0
    default momfallenasleep_kiss = 0
    default momfallenasleep_goodbye = 0
    default momfallenasleep_lovewithsister = 0
    default momfallenasleep_sleepnaked = 0
    if winc == 0:
        jump lbl_mom_fallen_asleep_winc0

    scene bg momfallenasleep_1
    with fade
    $ renpy.pause ()

    menu:
        "Mom?":
            pov "Mom?"

            jump lbl_mom_fallen_asleep_0
        "Lift up her dress":
            show bg momfallenasleep_peek_1
            call screen scr_momfallenasleep_peek_1
            screen scr_momfallenasleep_peek_1():
                add "bg momfallenasleep_peek_1"
                imagebutton auto "btn momfallenasleep_peek_dress_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_fallen_asleep_peek_1")

label lbl_mom_fallen_asleep_0:
    show bg momfallenasleep_1
    mum "Mmm... wha- hmm?"
    mum "Mom?"
    show bg momfallenasleep_3
    $ renpy.pause (0.7,hard=True)
    show bg momfallenasleep_4
    mum "Hmm? D-did I fall asleep?"
    show bg momfallenasleep_3
    pov "Yeah, you did."
    show bg momfallenasleep_4
    mum "For how long? What time is it?"
    show bg momfallenasleep_3
    pov "I don't know how long you've slept for but it's late."
    show bg momfallenasleep_4
    mum "Uhh.. I don't wanna leave this couch."
    show bg momfallenasleep_5
    $ renpy.pause (0.7,hard=True)
    show bg momfallenasleep_6
    mum "Come here and cuddle with me, it's cold."
    show bg momfallenasleep_5
    pov "Uhm.. okay?"

    jump lbl_mom_fallen_asleep_1

label lbl_mom_fallen_asleep_peek_1:

    if skill_luc >= 6:
        $ skill_luc -= 3
        $ renpy.notify("You used 3 Luck Points")
        show bg momfallenasleep_peek_2
        $ renpy.pause()
        pov "{i}Wow...{/i}"
        mum "Mmm.."
        pov "{i}Oh shit, she's waking up.{/i}"

        jump lbl_mom_fallen_asleep_0
    elif skill_luc < 6:
        show bg momfallenasleep_peek_3
        $ renpy.pause(1,hard=True)
        show bg momfallenasleep_peek_4
        $ renpy.pause(0.5,hard=True)
        show bg momfallenasleep_peek_5
        $ renpy.pause(0.5,hard=True)
        show bg momfallenasleep_peek_6
        $ renpy.pause(0.3,hard=True)
        show bg momfallenasleep_peek_7
        with hpunch
        $ renpy.pause(0.5,hard=True)
        show bg momfallenasleep_12
        mum "Oh my God! I'm so sorry! I thought someone was peeking under my dress."
        pov "No, Mom. It's just me. Jeez that hurt."
        mum "I'm so sorry."
        show bg momfallenasleep_13
        mum "Come into my arms, baby. I didn't mean to hurt you."
        show bg momfallenasleep_14
        pov "I-it's okay, Mom."
        show bg momfallenasleep_13
        mum "Come here, I know you want to."
        show bg momfallenasleep_14
        pov "Um.. okay."

        jump lbl_mom_fallen_asleep_1

label lbl_mom_fallen_asleep_1:
    show bg momfallenasleep_7
    $ renpy.pause()
    show bg momfallenasleep_8
    pov "L-like this?"
    show bg momfallenasleep_7
    mum "Mhmm?"
    show bg momfallenasleep_8
    pov "But I'm too heavy."
    show bg momfallenasleep_9
    mum "I don't mind, I like feeling the weight."
    show bg momfallenasleep_10
    $ renpy.pause(2,hard=True)
    show bg momfallenasleep_11
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_10
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_11
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_15
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_16
    show img momfallenasleep_carpet_1
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_15
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_16
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_17
    mum "You sleepy?"

    menu:
        "Yeah...":
            show bg momfallenasleep_16
            pov "Yeah..."
            show bg momfallenasleep_17
            mum "Naww, had a big day today huh?"
            show bg momfallenasleep_16
            pov "Been busy busy busy. A lot of places to go and stuff to do around town."
            show bg momfallenasleep_17
            mum "At least you're keeping yourself occupied."
            show bg momfallenasleep_18
            mum "You can rest on my chest if you want."
        "A little.":
            show bg momfallenasleep_16
            pov "A little."
            show bg momfallenasleep_17
            mum "Well, why don't you just rest your head on my chest?"
            show bg momfallenasleep_18
            mum "Close your eyes because...."
            show bg momfallenasleep_19
            mum "{i}*Yawn*{/i}"
            show bg momfallenasleep_18
            mum "I'm exhausted."
        "Not really.":
            show bg momfallenasleep_16
            pov "Not really."
            show bg momfallenasleep_17
            mum "Haven't you done much today?"
            show bg momfallenasleep_16
            pov "Well, depends what you mean by that."
            show bg momfallenasleep_17
            mum "Heheh, it's okay. I'm just pretty tired myself."
            show bg momfallenasleep_18
            mum "You don't mind resting your head on my chest, do you?"

    menu:
        "That'll be nice.":
            show bg momfallenasleep_15
            pov "That'll be nice. I'll be able to feel your.. heartbeat."
        "Your boobs.":
            show bg momfallenasleep_20
            pov "Your boobs though..."
            show bg momfallenasleep_23
            mum "Oh, don't be like that, they're out of the way, I'm not wearing a bra."
            show bg momfallenasleep_22
            mum "Don't make me ask again."
    show bg momfallenasleep_24
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_24
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_26
    mum "Lullaby baby on Mommy's chest..."
    show bg momfallenasleep_27
    mum "When the sun sleeps, these moons on you'll rest..."
    show bg momfallenasleep_26
    mum "When the wind blows a cooling air-drift..."
    show bg momfallenasleep_27
    mum "Come now, my baby..."
    show bg momfallenasleep_28
    mum "My nipples are stiff."
    show bg momfallenasleep_29
    pov "..."
    show bg momfallenasleep_28
    mum "Remember when I sang that to you?"
    show bg momfallenasleep_15
    pov "You sang that to me? That's so... immature."
    show bg momfallenasleep_18
    mum "What? You loved it, and heck, you didn't understand what I was saying."
    show bg momfallenasleep_17
    mum "You just loved the sound of my voice."
    show bg momfallenasleep_16
    pov "I understand them now."
    show bg momfallenasleep_30
    mum "Everyone's got their own rendition."
    show bg momfallenasleep_31
    pov "Never would've imagined that was yours."
    show bg momfallenasleep_24
    mum "Hehehe.."
    show bg momfallenasleep_25
    mum "..."
    show bg momfallenasleep_26
    mum "How is everything going for you?"
    show bg momfallenasleep_31
    pov "Fine I guess."
    show bg momfallenasleep_30
    mum "Just fine?"
    show bg momfallenasleep_31
    pov "I mean yeah. Y'know, not complaining."
    show bg momfallenasleep_32
    mum "Hmm..."
    show bg momfallenasleep_33
    mum "Nothing at all to tell me?"
    show bg momfallenasleep_34
    pov "I can't really think of anything."
    show bg momfallenasleep_27
    mum "Alright, alright."
    show bg momfallenasleep_15
    pov "Why? Was there something you know that I don't?"
    show bg momfallenasleep_18
    mum "No, I was just making sure."
    show bg momfallenasleep_15
    pov "You sure?"
    show bg momfallenasleep_18
    mum "Sure I'm sure. Are you sure?"
    show bg momfallenasleep_15
    pov "I'm not sure."
    show bg momfallenasleep_18
    mum "Sure.."
    show bg momfallenasleep_35
    mum "{i}*Mwa*{/i}"
    show bg momfallenasleep_26
    mum "I guess I should thank you for fixing my laptop. It's working perfectly fine now."
    show bg momfallenasleep_36
    pov "Hey, no problem, it was my pleasure."
    show bg momfallenasleep_27
    mum "Where'd you learn to do that?"
    show bg momfallenasleep_31
    pov "Hmm? Fix computers?"
    show bg momfallenasleep_26
    mum "Yeah. At university possibly?"
    show bg momfallenasleep_37
    pov "The internet, Mom."
    show bg momfallenasleep_26
    mum "Ahh of course, how silly of me. The source of all knowledge and answers to the world."
    show bg momfallenasleep_27
    mum "Can the internet tell me why my son is the best son in the world?"
    show bg momfallenasleep_38
    pov "Mother, you're smothering me."
    show bg momfallenasleep_27
    mum "How can I not? Look at yourself, lying on me, resting in my arms."
    show bg momfallenasleep_39
    mum "I miss this feeling so much."
    show bg momfallenasleep_33
    mum "It only really lasts until you're 3. After that age, you constantly rolled around and couldn't stay on me."
    show bg momfallenasleep_36
    pov "What goes around comes around."
    show bg momfallenasleep_27
    mum "Luckily you did."
    show bg momfallenasleep_24
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_24
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_26
    mum "You like it when I play with your hair?"

    menu:
        "It's comforting.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg momfallenasleep_37
            pov "It's very comforting."
            show bg momfallenasleep_26
            mum "Is it putting you to sleep?"
            show bg momfallenasleep_37
            pov "Very much so.."
        "I like the back rubs.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg momfallenasleep_37
            pov "I like the back rubs better."
            show bg momfallenasleep_26
            mum "I know how you like them."
            show bg momfallenasleep_31
            pov "It's making me sleepy."
        "It's distracting.":
            show bg momfallenasleep_40
            pov "It's kind of distracting."
            show bg momfallenasleep_39
            mum "Do you want me to stop?"
            show bg momfallenasleep_40
            pov "Please."
            show bg momfallenasleep_33
            mum "Fine. Then will you do me a favour?"
            show bg momfallenasleep_20
            pov "Mmm? What is it?"
            show bg momfallenasleep_22
            mum "Go to bed."
            show bg momfallenasleep_20
            pov "What?!"
            show bg momfallenasleep_22
            mum "Obviously you don't appreciate your mother's love. You can go straight to bed if you feel that way."
            show bg momfallenasleep_20
            pov "..."
            pov "I guess goodnight then..."
            show bg momfallenasleep_22
            mum "Goodnight, [povname]."

            jump lbl_mom_fallen_asleep_end
    show bg momfallenasleep_26
    mum "Don't fall asleep on me. Okay?"
    show bg momfallenasleep_31
    pov "I'll try not to."
    show bg momfallenasleep_26
    mum "I still want to talk."
    show bg momfallenasleep_25
    pov "Mhmm..."
    show bg momfallenasleep_24
    mum "..."
    show bg momfallenasleep_27
    mum "Tell me a secret, [povname]."
    show bg momfallenasleep_38
    pov "A secret?"
    show bg momfallenasleep_30
    mum "Yeah, something that I don't know about you."
    show bg momfallenasleep_15
    pov "It wouldn't be a secret anymore now would it?"
    show bg momfallenasleep_18
    mum "It will be with me."

    menu:
        "I love you.":
            show bg momfallenasleep_15
            pov "I love you."
            show bg momfallenasleep_18
            mum "Is that your secret? That's not much of a secret."
            show bg momfallenasleep_17
            mum "But I love you too, [povname]."

            jump lbl_mom_fallen_asleep_5
        "I love you more than you think.":
            show bg momfallenasleep_15
            pov "I love you more than you think."
            show bg momfallenasleep_42
            mum "Really? Impossible. How much do you love me?"

            menu:
                "Like a lover.":
                    $ momfallenasleep_confession = 1
                    show bg momfallenasleep_43
                    pov "Like a lover."
                    show bg momfallenasleep_44
                    mum "Like.. a lover?"
                    mum "Like... love love."
                    mum "Like like... lover love."
                    show bg momfallenasleep_43
                    pov "...Yeah..."
                    show bg momfallenasleep_45
                    mum "Wow.. um. I don't know what to say..."
                    show bg momfallenasleep_46
                    pov "Tell me how much you love me."
                    if mum_points >= 6:
                        jump lbl_mom_fallen_asleep_4_1
                    elif 3 <= mum_points <= 5:
                        jump lbl_mom_fallen_asleep_4_2
                    elif mum_points <= 2:
                        if mum_points >= 1:
                            $ mum_points -= 1
                        else:
                            $ mum_points = 0
                        $ renpy.notify("Your relationship with Mom has decreased")
                        show bg momfallenasleep_47
                        mum "Um... I wasn't really expecting that."

                        jump lbl_mom_fallen_asleep_4_3
                "Like a lot.":
                    if mum_points <= 9:
                        $ mum_points += 1
                        $ renpy.notify("Your relationship with Mom has increased")
                    else:
                        $ mum_points = 10
                    show bg momfallenasleep_15
                    pov "Like a lot."
                    show bg momfallenasleep_18
                    mum "Like a lot lot?"
                    show bg momfallenasleep_15
                    pov "Yup, that much."
                    show bg momfallenasleep_18
                    mum "I love you a lot lot too."
                    show bg momfallenasleep_35
                    mum "{i}*Mwa*{/i}"

                    jump lbl_mom_fallen_asleep_5
        "I have sexual feelings for you.":
            $ momfallenasleep_confession = 1
            show bg momfallenasleep_43
            pov "I have sexual feelings for you."
            mum "..."
            show bg momfallenasleep_44
            mum "Wow... sorry. That caught me by surprise. I didn't expect you'd go there."
            mum "I- I'm speechless..."
            show bg momfallenasleep_46
            pov "Tell me you feel the same way. I know you do."
            if mum_points >= 6:
                jump lbl_mom_fallen_asleep_4_1
            elif 3 <= mum_points <= 5:
                jump lbl_mom_fallen_asleep_4_2
            elif mum_points <= 2:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased")

                jump lbl_mom_fallen_asleep_4_3
        "I'm in love with [sister].":
            if mum_points >= 2:
                $ mum_points -= 2
            else:
                $ mum_points = 0
            if sister_points <= 8:
                $ sister_points += 2
            else:
                $ sister_points = 10
            $ renpy.notify("Your relationship with Mom has decreased by 2")
            $ renpy.pause(3,hard=True)
            $ renpy.notify("Your relationship with [sister] has increased by 2")
            $ renpy.pause(3,hard=True)
            $ momfallenasleep_lovewithsister = 1
            show bg momfallenasleep_43
            pov "I'm in love with [sister]."
            show bg momfallenasleep_44
            mum "You... you what?"
            show bg momfallenasleep_43
            pov "I love her."
            show bg momfallenasleep_47
            mum "Like a sister right? You too are always fighting and annoying each other."
            show bg momfallenasleep_48
            pov "Yeah, but.. y'know. She is my twin sister after all."
            show bg momfallenasleep_47
            mum "I don't know where you're going with this."
            show bg momfallenasleep_43
            pov "Like... I love her more than a sister."
            show bg momfallenasleep_49
            mum "Don't tell me... you've had sex with her."
            show bg momfallenasleep_46
            pov "You wanted a secret. I'm trusting you with this, Mom."
            pov "I know it's wrong but please understand..."
            show bg momfallenasleep_49
            mum "I don't understand why, I mean I understand but how?"
            mum "Why would you tell me this?"
            show bg momfallenasleep_46
            pov "We're your children. Who else can I talk to about this?"
            show bg momfallenasleep_49
            mum "I didn't think you'd be so open to me about this."
            show bg momfallenasleep_46
            pov "No one else would get it."
            show bg momfallenasleep_49
            mum "You're dropping a lot on me right now."
            mum "Can- can you get off me and go to bed. I'm a little confused at the moment."
            show bg momfallenasleep_50
            mum "G-goodnight, [povname]..."
            show bg momfallenasleep_51
            pov "Goodnight, Mom. Sorry but I need to let it ou-"
            show bg momfallenasleep_50
            mum "Goodnight, [povname]."

            jump lbl_mom_fallen_asleep_end
        "I sleep naked.":
            $ momfallenasleep_sleepnaked = 1
            show bg momfallenasleep_15
            pov "I sleep naked."
            show bg momfallenasleep_42
            mum "That's a very mild secret."
            show bg momfallenasleep_15
            pov "Well, it's a secret never the less."
            show bg momfallenasleep_18
            mum "Actually it's not. I already know you sleep naked."
            show bg momfallenasleep_15
            pov "..."
            show bg momfallenasleep_16
            pov "You what now?"
            show bg momfallenasleep_17
            mum "I've been in your room while you sleep, sometimes when you roll around, the bedsheet slips off from over you."
            show bg momfallenasleep_16
            pov "Why were you in my room when I was sleeping."
            show bg momfallenasleep_17
            mum "I wasn't like watching you or anything. I was probably looking for something in your room and happen to see you naked."
            show bg momfallenasleep_16
            pov "That's embarrassing."
            show bg momfallenasleep_17
            mum "Then don't sleep naked if you're so embarrassed about it."
            show bg momfallenasleep_42
            mum "From seeing your body, there's nothing to be embarrassed about."
            show bg momfallenasleep_52
            pov "Stop, Mom."
            show bg momfallenasleep_53
            mum "Hehehe."

            jump lbl_mom_fallen_asleep_5

label lbl_mom_fallen_asleep_4_1:
    if mum_points <= 9:
        $ mum_points += 1
    else:
        $ mum_points = 10
    $ renpy.notify("Your relationship with Mom has increased")
    show bg momfallenasleep_45
    mum "Don't tell anyone else but... I feel the same way about you..."
    show bg momfallenasleep_54
    pov "Really?"
    show bg momfallenasleep_22
    mum "Don't. Tell. Anyone."
    mum "This is between us-"
    show bg momfallenasleep_20
    pov "I know, Mom. I'm not stupid."
    show bg momfallenasleep_26
    mum "Good..."

    jump lbl_mom_fallen_asleep_5

label lbl_mom_fallen_asleep_4_2:
    show bg momfallenasleep_47
    mum "Well... [povname]. I've said it a million times before, I don't know if you keep forgetting."
    mum "But I am your mother."
    show bg momfallenasleep_20
    pov "So no?"
    show bg momfallenasleep_21
    mum "..."
    show bg momfallenasleep_45
    mum "This is for your ears only. But I have thought about you... Y'know... in that way."
    show bg momfallenasleep_54
    pov "In what way?"
    show bg momfallenasleep_49
    mum "Y'know. Don't make me say it..."
    show bg momfallenasleep_45
    mum "It's normal, right? Everyone has thought about that about their family members at least once before, right?"
    show bg momfallenasleep_54
    pov "I'm sure either consciously or unconsciously."
    show bg momfallenasleep_45
    mum "Well, that's my secret to you."

    jump lbl_mom_fallen_asleep_5

label lbl_mom_fallen_asleep_4_3:
    show bg momfallenasleep_22
    mum "[povname], I'm going to be serious with you for just a second."
    mum "I'm your biological mother, you're my biological son. It is wrong to have sexual relations with each other, got it?"
    show bg momfallenasleep_20
    pov "I- I'm sorry. It's just feelings."
    show bg momfallenasleep_22
    mum "I'm not going to tell you what to feel and what not to feel but remember that okay, dear?"
    show bg momfallenasleep_20
    pov "I will. Sorry..."

    jump lbl_mom_fallen_asleep_5

label lbl_mom_fallen_asleep_5:
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_32
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_56
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_55
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_58
    mum "[povname]? Is it a curse or a blessing that I'm your mother?"
    show bg momfallenasleep_59
    pov "Why would it be a curse?"
    show bg momfallenasleep_62
    mum "I guess, to put it simply. I could've been destined to be your soul mate by being born later."
    show bg momfallenasleep_61
    mum "But instead, I've been destined to mother you."
    show bg momfallenasleep_64
    pov "Are you regretting giving birth to me or something."
    show bg momfallenasleep_61
    mum "Oh no, far, far from that. Just thinking hypothetically and questioning too deeply about what the universe has in store for us."
    show bg momfallenasleep_62
    mum "You get the most thought provoking stuff late at night."

    menu:
        "It's a blessing.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg momfallenasleep_36
            pov "I think it's a blessing."
            show bg momfallenasleep_37
            pov "I mean, I couldn't have asked for a better mom. I couldn't even think of having someone more, umm, ‘qualified'."
            show bg momfallenasleep_26
            mum "Heheh, ‘qualified'."
            show bg momfallenasleep_27
            mum "I'm doing a good job, aren't I?"
            show bg momfallenasleep_36
            pov "Yeah, you are."
            if mum_points >= 4:
                show bg momfallenasleep_28
                mum "Reward me then."
                show bg momfallenasleep_15
                pov "How so?"
                show bg momfallenasleep_23
                mum "Kiss me."

                jump lbl_mom_fallen_asleep_6
            elif mum_points <= 3:
                show bg momfallenasleep_27
                mum "At least I'm on the right track."
                show bg momfallenasleep_36
                pov "Yup, you've successfully raised me and [sister] to adulthood without any trouble."
                show bg momfallenasleep_27
                mum "What an accomplishment."
                show bg momfallenasleep_36
                pov "I'm thankful for it."
                show bg momfallenasleep_15
                pov "Thank you, Mom."
                show bg momfallenasleep_45
                mum "Stop making me blush."
                show bg momfallenasleep_54
                mum "..."
                show bg momfallenasleep_45
                mum "C'mon. It's pretty late already. I wish I could stay down here all night but your Dad might blow the roof off this place."
                show bg momfallenasleep_36
                pov "Can't argue with that."
                show bg momfallenasleep_27
                mum "Thanks for cuddling with me, [povname]."
                show bg momfallenasleep_36
                pov "Let's do it again sometime soon."
                show bg momfallenasleep_27
                mum "Goodnight, my baby. I love you."
                show bg momfallenasleep_15
                pov "I love you too."
                $ momfallenasleep_goodbye = 1

                jump lbl_mom_fallen_asleep_end
        "It's a curse.":
            show bg momfallenasleep_59
            pov "I think it's a curse."
            if mum_points >= 5 and momfallenasleep_confession == 1:
                if mum_points <= 8:
                    $ mum_points += 2
                    $ renpy.notify("Your relationship with Mom has increased by 2")
                else:
                    $ mum_points = 10
                pov "I want to be with you so bad and yet, it's not all that easy and simple."
                show bg momfallenasleep_58
                mum "I understand. If only we live in a society that accepts this."
                show bg momfallenasleep_55
                pov "..."
                show bg momfallenasleep_63
                pov "What's stopping us?"
                show bg momfallenasleep_62
                mum "I am."
                show bg momfallenasleep_48
                pov "Why are you?"
                show bg momfallenasleep_49
                mum "I don't know..."
                show bg momfallenasleep_51
                pov "There's no one here but us."
                show bg momfallenasleep_46
                pov "We're in a new town, new life, new start."
                show bg momfallenasleep_49
                mum "Kiss me, [povname]."

                jump lbl_mom_fallen_asleep_6_1
            elif mum_points >= 5 and momfallenasleep_confession == 0:
                if mum_points <= 9:
                    $ mum_points += 1
                else:
                    $ mum_points = 10
                $ renpy.notify("Your relationship with Mom has increased")
                pov "You're really fun to talk to, and I can totally see you being my best friend, or even more."
                show bg momfallenasleep_65
                mum "Even more, huh?"
                show bg momfallenasleep_15
                pov "I- I didn't mean to say that.."
                show bg momfallenasleep_18
                mum "Hehe, it's alright. I'm flattered. Accidents happen, I know what you mean."
                show bg momfallenasleep_17
                mum "Whoever you end up with in life, she's going to be one lucky girl."
                show bg momfallenasleep_16
                pov "You think so?"
                show bg momfallenasleep_17
                mum "I know so."
                show bg momfallenasleep_16
                mum "..."
                show bg momfallenasleep_17
                mum "[povname]?"
                show bg momfallenasleep_16
                pov "Mmm?"
                show bg momfallenasleep_17
                mum "Won't you give me a kiss?"

                jump lbl_mom_fallen_asleep_6
            elif mum_points <= 4:
                show bg momfallenasleep_59
                pov "I think it's a curse..."

                menu:
                    "When we talk, I forget that you're my mom.":
                        show bg momfallenasleep_60
                        pov "When we talk like this, I forget you're my mom."
                        show bg momfallenasleep_59
                        pov "And yet the very thought is still in the back of my mind."
                        show bg momfallenasleep_58
                        mum "That's not an issue right? I hope it's not preventing you from being yourself with me."
                        show bg momfallenasleep_59
                        pov "Not at all."
                        show bg momfallenasleep_62
                        mum "Oh, good. Cause it almost sounded like it's a curse that the fact that I'm your mother is there haunting you."
                        show bg momfallenasleep_20
                        pov "I didn't mean it like that."
                        show bg momfallenasleep_18
                        mum "It's alright. It just sort of sounded like that."
                        show bg momfallenasleep_55
                        mum "..."
                        show bg momfallenasleep_62
                        mum "Umm... I think it's time to head to bed."
                        show bg momfallenasleep_20
                        pov "You don't want to cuddle a little longer?"
                        show bg momfallenasleep_22
                        mum "I wish, [povname]. But your Dad is expecting me."
                        show bg momfallenasleep_16
                        pov "Alright then. I love you, Mom."
                        show bg momfallenasleep_17
                        mum "I love you too."
                        $ momfallenasleep_goodbye = 1

                        jump lbl_mom_fallen_asleep_end
                    "I'd prefer you just to be a friend.":
                        if mum_points >= 1:
                            $ mum_points -= 1
                        else:
                            $ mum_points = 0
                        $ renpy.notify("Your relationship with Mom has decreased")
                        show bg momfallenasleep_59
                        pov "I'd prefer you just to be a friend rather than a mom."
                        pov "I guess we were both born at the wrong time. The butterfly effect."
                        show bg momfallenasleep_57
                        mum "So you don't really like me being your mother?"
                        show bg momfallenasleep_63
                        pov "I mean-"
                        show bg momfallenasleep_49
                        mum "Is that it? Alright, I get it."
                        show bg momfallenasleep_46
                        pov "Wha-?"
                        show bg momfallenasleep_49
                        mum "You've made it clear to me that I'm not doing a good job parenting you. What? Am I embarrassing to be around?"
                        show bg momfallenasleep_46
                        pov "No, it's not what I mean."
                        show bg momfallenasleep_47
                        mum "Yeah, save it, [povname]. I'm not in the mood anymore."
                        show bg momfallenasleep_20
                        pov "..."
                        show bg momfallenasleep_22
                        mum "Go to bed."
                        show bg momfallenasleep_20
                        pov "I didn-"
                        show bg momfallenasleep_22
                        mum "Goodnight, [povname]."
                        show bg momfallenasleep_20
                        pov "...Goodnight."

                        jump lbl_mom_fallen_asleep_end

label lbl_mom_fallen_asleep_6:

    scene bg momfallenasleep_66
    $ renpy.pause(2,hard=True)
    show bg momfallenasleep_67
    $ renpy.pause(0.8,hard=True)
    show bg momfallenasleep_68
    $ renpy.pause(1.5,hard=True)
    show bg momfallenasleep_67
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_66
    $ renpy.pause(2,hard=True)

    jump lbl_mom_fallen_asleep_6_1

label lbl_mom_fallen_asleep_6_1:
    $ momfallenasleep_kiss = 1

    scene bg momfallenasleep_69
    with vpunch
    $ renpy.pause(1.2,hard=True)
    show bg momfallenasleep_70
    $ renpy.pause(1.2,hard=True)
    show bg momfallenasleep_71
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_72
    $ renpy.pause(0.5,hard=True)
    show bg momfallenasleep_73
    $ renpy.pause(2,hard=True)
    show bg momfallenasleep_74
    $ renpy.pause()
    show bg momfallenasleep_75
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg momfallenasleep_76
    $ renpy.pause(0.8,hard=True)
    show bg momfallenasleep_77
    $ renpy.pause(1.5,hard=True)
    show bg momfallenasleep_78
    mum "Tell me I'm drunk..."
    show bg momfallenasleep_79
    pov "Did you drink?"
    show bg momfallenasleep_80
    mum "No..."
    show bg momfallenasleep_79
    pov "Then why-?"
    show bg momfallenasleep_80
    mum "Tell me I'm drunk... so I can somewhat comprehend what we just did..."
    show bg momfallenasleep_81
    pov "..."

    menu:
        "You're drunk.":
            show bg momfallenasleep_82
            pov "Mom, you're drunk."
            show bg momfallenasleep_83
            mum "Yeah... yeah you're right..."
            mum "I probably forgot that I even drank..."
            mum "We- we should get to bed."
            mum "In our own beds, I mean."
            show bg momfallenasleep_84
            pov "Hehe, sure, Mom."
            show bg momfallenasleep_83
            mum "Thank you for tonight. I love you."
            show bg momfallenasleep_84
            pov "I love you too, Mom."
            show bg momfallenasleep_67
            $ renpy.pause(1,hard=True)
            show bg momfallenasleep_75
            $ renpy.pause()
        "You're drunk with love.":
            show bg momfallenasleep_82
            pov "Mom, you're drunk... with love."
            show bg momfallenasleep_83
            mum "Oh, why do you have to be so cheesy, [povname]."
            show bg momfallenasleep_84
            pov "Well, it's true."
            show bg momfallenasleep_83
            mum "Heh.. I know I love you, baby."
            mum "I can't help myself."
            mum "We should get to bed."
            show bg momfallenasleep_84
            pov "Yeah, it's pretty damn late."
            pov "I love you too, by the way."
            show bg momfallenasleep_83
            mum "You just made my night."
            show bg momfallenasleep_67
            $ renpy.pause(1,hard=True)
            show bg momfallenasleep_75
            $ renpy.pause()
        "You're not drunk.":
            show bg momfallenasleep_79
            pov "Mom, you're not drunk, you know what you did, and you know you liked it."
            show bg momfallenasleep_85
            mum "..."
            show bg momfallenasleep_86
            mum "Screw you, [povname]."
            mum "This is your fault. I can't help what I just did."
            mum "Please tell me I'm drunk talking right now."

            menu:
                "You are.":
                    show bg momfallenasleep_84
                    pov "I'm just kidding, you are."
                    show bg momfallenasleep_83
                    mum "Oh, thank goodness."
                    mum "I guess my drunk-ass should get to bed, huh?"
                    show bg momfallenasleep_84
                    pov "I think so."
                    show bg momfallenasleep_83
                    mum "Goodnight, [povname]. Thank you for tonight."
                    show bg momfallenasleep_84
                    pov "I love you, Mom."
                    show bg momfallenasleep_83
                    mum "I love you too, baby."
                    show bg momfallenasleep_67
                    $ renpy.pause(1,hard=True)
                    show bg momfallenasleep_75
                    $ renpy.pause()
                "Completely sober.":
                    show bg momfallenasleep_84
                    pov "Nope. Completely sober."
                    show bg momfallenasleep_86
                    mum "You enjoy this, don't you?"
                    mum "You know this is wrong and yet you like it."
                    show bg momfallenasleep_84
                    pov "Blaming me now?"
                    show bg momfallenasleep_86
                    mum "Yes, you kissed first."
                    show bg momfallenasleep_84
                    pov "You asked me to."
                    show bg momfallenasleep_87
                    mum "Hmm? I can't hear you."
                    show bg momfallenasleep_88
                    mum "{i}*Yawn*{/i} Oh man, we should get to bed."
                    show bg momfallenasleep_89
                    pov "Heheh, I love you, Mom."
                    show bg momfallenasleep_90
                    mum "Love you too, sweetie."
                    show bg momfallenasleep_67
                    $ renpy.pause(1,hard=True)
                    show bg momfallenasleep_75
                    $ renpy.pause()

label lbl_mom_fallen_asleep_end:
    $ mum_path = 5
    $ gtime = 3

    scene bg mybedroom_night
    with fade

    jump lbl_mybedroom_night_setup

### NO WINC ###
label lbl_mom_fallen_asleep_winc0:

    scene bg momfallenasleep_1
    with fade
    $ renpy.pause ()

    menu:
        "[missus]?":
            pov "[missus]?"

            jump lbl_mom_fallen_asleep_0_winc0
        "Lift up her dress":
            show bg momfallenasleep_peek_1
            call screen scr_momfallenasleep_peek_1_winc0
            screen scr_momfallenasleep_peek_1_winc0():
                add "bg momfallenasleep_peek_1"
                imagebutton auto "btn momfallenasleep_peek_dress_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_fallen_asleep_peek_1_winc0")

label lbl_mom_fallen_asleep_0_winc0:
    show bg momfallenasleep_1
    mum "Mmm... wha- hmm?"
    mum "[missus]?"
    show bg momfallenasleep_3
    $ renpy.pause (0.7,hard=True)
    show bg momfallenasleep_4
    mum "Hmm? D-did I fall asleep?"
    show bg momfallenasleep_3
    pov "Yeah, you did."
    show bg momfallenasleep_4
    mum "For how long? What time is it?"
    show bg momfallenasleep_3
    pov "I don't know how long you've slept for but it's late."
    show bg momfallenasleep_4
    mum "Uhh.. I don't wanna leave this couch."
    show bg momfallenasleep_5
    $ renpy.pause (0.7,hard=True)
    show bg momfallenasleep_6
    mum "Come here and cuddle with me, it's cold."
    show bg momfallenasleep_5
    pov "Uhm.. okay?"

    jump lbl_mom_fallen_asleep_1_winc0

label lbl_mom_fallen_asleep_peek_1_winc0:
    if skill_luc >= 6:
        $ skill_luc -= 3
        $ renpy.notify("You used 3 Luck Points")


        show bg momfallenasleep_peek_2
        $ renpy.pause()
        pov "{i}Wow...{/i}"
        mum "Mmm.."
        pov "{i}Oh shit, she's waking up.{/i}"

        jump lbl_mom_fallen_asleep_0_winc0
    elif skill_luc < 6:
        show bg momfallenasleep_peek_3
        $ renpy.pause(1,hard=True)
        show bg momfallenasleep_peek_4
        $ renpy.pause(0.5,hard=True)
        show bg momfallenasleep_peek_5
        $ renpy.pause(0.5,hard=True)
        show bg momfallenasleep_peek_6
        $ renpy.pause(0.3,hard=True)
        show bg momfallenasleep_peek_7
        with hpunch
        $ renpy.pause(0.5,hard=True)
        show bg momfallenasleep_12
        mum "Oh my God! I'm so sorry! I thought someone was peeking under my dress."
        pov "No, [missus]. It's just me. Jeez that hurt."
        mum "I'm so sorry."
        show bg momfallenasleep_13
        mum "Come into my arms, baby. I didn't mean to hurt you."
        show bg momfallenasleep_14
        pov "I-it's okay, [missus]."
        show bg momfallenasleep_13
        mum "Come here, I know you want to."
        show bg momfallenasleep_14
        pov "Um.. okay."

        jump lbl_mom_fallen_asleep_1_winc0

label lbl_mom_fallen_asleep_1_winc0:
    show bg momfallenasleep_7
    $ renpy.pause()
    show bg momfallenasleep_8
    pov "L-like this?"
    show bg momfallenasleep_7
    mum "Mhmm?"
    show bg momfallenasleep_8
    pov "But I'm too heavy."
    show bg momfallenasleep_9
    mum "I don't mind, I like feeling the weight."
    show bg momfallenasleep_10
    $ renpy.pause(2,hard=True)
    show bg momfallenasleep_11
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_10
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_11
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_15
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_16
    show img momfallenasleep_carpet_1
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_15
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_16
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_17
    mum "You sleepy?"

    menu:
        "Yeah...":
            show bg momfallenasleep_16
            pov "Yeah..."
            show bg momfallenasleep_17
            mum "Naww, had a big day today huh?"
            show bg momfallenasleep_16
            pov "Been busy busy busy. A lot of places to go and stuff to do around town."
            show bg momfallenasleep_17
            mum "At least you're keeping yourself occupied."
            show bg momfallenasleep_18
            mum "You can rest on my chest if you want."
        "A little.":
            show bg momfallenasleep_16
            pov "A little."
            show bg momfallenasleep_17
            mum "Well, why don't you just rest your head on my chest?"
            show bg momfallenasleep_18
            mum "Close your eyes because...."
            show bg momfallenasleep_19
            mum "{i}*Yawn*{/i}"
            show bg momfallenasleep_18
            mum "I'm exhausted."
        "Not really.":
            show bg momfallenasleep_16
            pov "Not really."
            show bg momfallenasleep_17
            mum "Haven't you done much today?"
            show bg momfallenasleep_16
            pov "Well, depends what you mean by that."
            show bg momfallenasleep_17
            mum "Heheh, it's okay. I'm just pretty tired myself."
            show bg momfallenasleep_18
            mum "You don't mind resting your head on my chest, do you?"

    menu:
        "That'll be nice.":
            show bg momfallenasleep_15
            pov "That'll be nice. I'll be able to feel your.. heartbeat."
        "Your boobs.":
            show bg momfallenasleep_20
            pov "Your boobs though..."
            show bg momfallenasleep_23
            mum "Oh, don't be like that, they're out of the way, I'm not wearing a bra."
            show bg momfallenasleep_22
            mum "Don't make me ask again."
    show bg momfallenasleep_24
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_24
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_26
    mum "Lullaby baby on [missus]'s chest..."
    show bg momfallenasleep_27
    mum "When the sun sleeps, these moons on you'll rest..."
    show bg momfallenasleep_26
    mum "When the wind blows a cooling air-drift..."
    show bg momfallenasleep_27
    mum "Come now, my baby..."
    show bg momfallenasleep_28
    mum "My nipples are stiff."
    show bg momfallenasleep_29
    pov "..."
    show bg momfallenasleep_28
    mum "Remember when I sang that to you?"
    show bg momfallenasleep_15
    pov "You sang that to me? That's so... immature."
    show bg momfallenasleep_18
    mum "What? You loved it, and heck, you didn't understand what I was saying."
    show bg momfallenasleep_17
    mum "You just loved the sound of my voice."
    show bg momfallenasleep_16
    pov "I understand them now."
    show bg momfallenasleep_30
    mum "Everyone's got their own rendition."
    show bg momfallenasleep_31
    pov "Never would've imagined that was yours."
    show bg momfallenasleep_24
    mum "Hehehe.."
    show bg momfallenasleep_25
    mum "..."
    show bg momfallenasleep_26
    mum "How is everything going for you?"
    show bg momfallenasleep_31
    pov "Fine I guess."
    show bg momfallenasleep_30
    mum "Just fine?"
    show bg momfallenasleep_31
    pov "I mean yeah. Y'know, not complaining."
    show bg momfallenasleep_32
    mum "Hmm..."
    show bg momfallenasleep_33
    mum "Nothing at all to tell me?"
    show bg momfallenasleep_34
    pov "I can't really think of anything."
    show bg momfallenasleep_27
    mum "Alright, alright."
    show bg momfallenasleep_15
    pov "Why? Was there something you know that I don't?"
    show bg momfallenasleep_18
    mum "No, I was just making sure."
    show bg momfallenasleep_15
    pov "You sure?"
    show bg momfallenasleep_18
    mum "Sure I'm sure. Are you sure?"
    show bg momfallenasleep_15
    pov "I'm not sure."
    show bg momfallenasleep_18
    mum "Sure.."
    show bg momfallenasleep_35
    mum "{i}*Mwa*{/i}"
    show bg momfallenasleep_26
    mum "I guess I should thank you for fixing my laptop. It's working perfectly fine now."
    show bg momfallenasleep_36
    pov "Hey, no problem, it was my pleasure."
    show bg momfallenasleep_27
    mum "Where'd you learn to do that?"
    show bg momfallenasleep_31
    pov "Hmm? Fix computers?"
    show bg momfallenasleep_26
    mum "Yeah. At university possibly?"
    show bg momfallenasleep_37
    pov "The internet, [missus]."
    show bg momfallenasleep_26
    mum "Ahh of course, how silly of me. The source of all knowledge and answers to the world."
    show bg momfallenasleep_27
    mum "Can the internet tell me why my [povmumrole] is the best [povmumrole] in the world?"
    show bg momfallenasleep_38
    pov "[mumrole], you're smothering me."
    show bg momfallenasleep_27
    mum "How can I not? Look at yourself, lying on me, resting in my arms."
    show bg momfallenasleep_39
    mum "I miss this feeling so much."
    show bg momfallenasleep_33
    mum "It only really lasts until you're 3. After that age, you constantly rolled around and couldn't stay on me."
    show bg momfallenasleep_36
    pov "What goes around comes around."
    show bg momfallenasleep_27
    mum "Luckily you did."
    show bg momfallenasleep_24
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_24
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_26
    mum "You like it when I play with your hair?"

    menu:
        "It's comforting.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg momfallenasleep_37
            pov "It's very comforting."
            show bg momfallenasleep_26
            mum "Is it putting you to sleep?"
            show bg momfallenasleep_37
            pov "Very much so.."
        "I like the back rubs.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg momfallenasleep_37
            pov "I like the back rubs better."
            show bg momfallenasleep_26
            mum "I know how you like them."
            show bg momfallenasleep_31
            pov "It's making me sleepy."
        "It's distracting.":
            show bg momfallenasleep_40
            pov "It's kind of distracting."
            show bg momfallenasleep_39
            mum "Do you want me to stop?"
            show bg momfallenasleep_40
            pov "Please."
            show bg momfallenasleep_33
            mum "Fine. Then will you do me a favour?"
            show bg momfallenasleep_20
            pov "Mmm? What is it?"
            show bg momfallenasleep_22
            mum "Go to bed."
            show bg momfallenasleep_20
            pov "What?!"
            show bg momfallenasleep_22
            mum "Obviously you don't appreciate your [mumrole]'s love. You can go straight to bed if you feel that way."
            show bg momfallenasleep_20
            pov "..."
            pov "I guess goodnight then..."
            show bg momfallenasleep_22
            mum "Goodnight, [povname]."

            jump lbl_mom_fallen_asleep_end_winc0
    show bg momfallenasleep_26
    mum "Don't fall asleep on me. Okay?"
    show bg momfallenasleep_31
    pov "I'll try not to."
    show bg momfallenasleep_26
    mum "I still want to talk."
    show bg momfallenasleep_25
    pov "Mhmm..."
    show bg momfallenasleep_24
    mum "..."
    show bg momfallenasleep_27
    mum "Tell me a secret, [povname]."
    show bg momfallenasleep_38
    pov "A secret?"
    show bg momfallenasleep_30
    mum "Yeah, something that I don't know about you."
    show bg momfallenasleep_15
    pov "It wouldn't be a secret anymore now would it?"
    show bg momfallenasleep_18
    mum "It will be with me."

    menu:
        "I love you.":
            show bg momfallenasleep_15
            pov "I love you."
            show bg momfallenasleep_18
            mum "Is that your secret? That's not much of a secret."
            show bg momfallenasleep_17
            mum "But I love you too, [povname]."

            jump lbl_mom_fallen_asleep_5_winc0
        "I love you more than you think.":
            show bg momfallenasleep_15
            pov "I love you more than you think."
            show bg momfallenasleep_42
            mum "Really? Impossible. How much do you love me?"

            menu:
                "Like a lover.":
                    $ momfallenasleep_confession = 1
                    show bg momfallenasleep_43
                    pov "Like a lover."
                    show bg momfallenasleep_44
                    mum "Like.. a lover?"
                    mum "Like... love love."
                    mum "Like like... lover love."
                    show bg momfallenasleep_43
                    pov "...Yeah..."
                    show bg momfallenasleep_45
                    mum "Wow.. um. I don't know what to say..."
                    show bg momfallenasleep_46
                    pov "Tell me how much you love me."
                    if mum_points >= 6:
                        jump lbl_mom_fallen_asleep_4_1_winc0
                    elif 3 <= mum_points <= 5:
                        jump lbl_mom_fallen_asleep_4_2_winc0
                    elif mum_points <= 2:
                        if mum_points >= 1:
                            $ mum_points -= 1
                        else:
                            $ mum_points = 0
                        $ renpy.notify("Your relationship with [missus] has decreased")
                        show bg momfallenasleep_47
                        mum "Um... I wasn't really expecting that."

                        jump lbl_mom_fallen_asleep_4_3_winc0
                "Like a lot.":
                    if mum_points <= 9:
                        $ mum_points += 1
                        $ renpy.notify("Your relationship with [missus] has increased")
                    else:
                        $ mum_points = 10
                    show bg momfallenasleep_15
                    pov "Like a lot."
                    show bg momfallenasleep_18
                    mum "Like a lot lot?"
                    show bg momfallenasleep_15
                    pov "Yup, that much."
                    show bg momfallenasleep_18
                    mum "I love you a lot lot too."
                    show bg momfallenasleep_35
                    mum "{i}*Mwa*{/i}"

                    jump lbl_mom_fallen_asleep_5_winc0
        "I have sexual feelings for you.":
            $ momfallenasleep_confession = 1
            show bg momfallenasleep_43
            pov "I have sexual feelings for you."
            mum "..."
            show bg momfallenasleep_44
            mum "Wow... sorry. That caught me by surprise. I didn't expect you'd go there."
            mum "I- I'm speechless..."
            show bg momfallenasleep_46
            pov "Tell me you feel the same way. I know you do."
            if mum_points >= 6:
                jump lbl_mom_fallen_asleep_4_1_winc0
            elif 3 <= mum_points <= 5:
                jump lbl_mom_fallen_asleep_4_2_winc0
            elif mum_points <= 2:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased")

                jump lbl_mom_fallen_asleep_4_3_winc0
        "I'm in love with [sister].":
            if mum_points >= 2:
                $ mum_points -= 2
            else:
                $ mum_points = 0
            if sister_points <= 8:
                $ sister_points += 2
            else:
                $ sister_points = 10
            $ renpy.notify("Your relationship with [missus] has decreased by 2")
            $ renpy.pause(3,hard=True)
            $ renpy.notify("Your relationship with [sister] has increased by 2")
            $ renpy.pause(3,hard=True)
            $ momfallenasleep_lovewithsister = 1
            show bg momfallenasleep_43
            pov "I'm in love with [sister]."
            show bg momfallenasleep_44
            mum "You... you what?"
            show bg momfallenasleep_43
            pov "I love her."
            show bg momfallenasleep_47
            mum "Like a [povsisrole] right? You too are always fighting and annoying each other."
            show bg momfallenasleep_48
            pov "Yeah, but.. y'know. She is my [sisrole] after all."
            show bg momfallenasleep_47
            mum "I don't know where you're going with this."
            show bg momfallenasleep_43
            pov "Like... I love her more than a [sisrole]."
            show bg momfallenasleep_49
            mum "Don't tell me... you've had sex with her."
            show bg momfallenasleep_46
            pov "You wanted a secret. I'm trusting you with this, [missus]."
            pov "I know it's wrong but please understand..."
            show bg momfallenasleep_49
            mum "I don't understand why, I mean I understand but how?"
            mum "Why would you tell me this?"
            show bg momfallenasleep_46
            pov "We're your [povdadrole]. Who else can I talk to about this?"
            show bg momfallenasleep_49
            mum "I didn't think you'd be so open to me about this."
            show bg momfallenasleep_46
            pov "No one else would get it."
            show bg momfallenasleep_49
            mum "You're dropping a lot on me right now."
            mum "Can- can you get off me and go to bed. I'm a little confused at the moment."
            show bg momfallenasleep_50
            mum "G-goodnight, [povname]..."
            show bg momfallenasleep_51
            pov "Goodnight, [missus]. Sorry but I need to let it ou-"
            show bg momfallenasleep_50
            mum "Goodnight, [povname]."

            jump lbl_mom_fallen_asleep_end_winc0
        "I sleep naked.":
            $ momfallenasleep_sleepnaked = 1
            show bg momfallenasleep_15
            pov "I sleep naked."
            show bg momfallenasleep_42
            mum "That's a very mild secret."
            show bg momfallenasleep_15
            pov "Well, it's a secret never the less."
            show bg momfallenasleep_18
            mum "Actually it's not. I already know you sleep naked."
            show bg momfallenasleep_15
            pov "..."
            show bg momfallenasleep_16
            pov "You what now?"
            show bg momfallenasleep_17
            mum "I've been in your room while you sleep, sometimes when you roll around, the bedsheet slips off from over you."
            show bg momfallenasleep_16
            pov "Why were you in my room when I was sleeping."
            show bg momfallenasleep_17
            mum "I wasn't like watching you or anything. I was probably looking for something in your room and happen to see you naked."
            show bg momfallenasleep_16
            pov "That's embarrassing."
            show bg momfallenasleep_17
            mum "Then don't sleep naked if you're so embarrassed about it."
            show bg momfallenasleep_42
            mum "From seeing your body, there's nothing to be embarrassed about."
            show bg momfallenasleep_52
            pov "Stop, [missus]."
            show bg momfallenasleep_53
            mum "Hehehe."

            jump lbl_mom_fallen_asleep_5_winc0

label lbl_mom_fallen_asleep_4_1_winc0:
    if mum_points <= 9:
        $ mum_points += 1
    else:
        $ mum_points = 10
    $ renpy.notify("Your relationship with [missus] has increased")
    show bg momfallenasleep_45
    mum "Don't tell anyone else but... I feel the same way about you..."
    show bg momfallenasleep_54
    pov "Really?"
    show bg momfallenasleep_22
    mum "Don't. Tell. Anyone."
    mum "This is between us-"
    show bg momfallenasleep_20
    pov "I know, [missus]. I'm not stupid."
    show bg momfallenasleep_26
    mum "Good..."

    jump lbl_mom_fallen_asleep_5_winc0

label lbl_mom_fallen_asleep_4_2_winc0:
    show bg momfallenasleep_47
    mum "Well... [povname]. I've said it a million times before, I don't know if you keep forgetting."
    mum "But I am your [mumrole]."
    show bg momfallenasleep_20
    pov "So no?"
    show bg momfallenasleep_21
    mum "..."
    show bg momfallenasleep_45
    mum "This is for your ears only. But I have thought about you... Y'know... in that way."
    show bg momfallenasleep_54
    pov "In what way?"
    show bg momfallenasleep_49
    mum "Y'know. Don't make me say it..."
    show bg momfallenasleep_45
    mum "It's normal, right? Everyone has thought about that about their [mumrole] at least once before, right?"
    show bg momfallenasleep_54
    pov "I'm sure either consciously or unconsciously."
    show bg momfallenasleep_45
    mum "Well, that's my secret to you."

    jump lbl_mom_fallen_asleep_5_winc0

label lbl_mom_fallen_asleep_4_3_winc0:
    show bg momfallenasleep_22
    mum "[povname], I'm going to be serious with you for just a second."
    mum "I'm your [mumrole], you're my [povmumrole]. It is wrong to have sexual relations with each other, got it?"
    show bg momfallenasleep_20
    pov "I- I'm sorry. It's just feelings."
    show bg momfallenasleep_22
    mum "I'm not going to tell you what to feel and what not to feel but remember that okay, dear?"
    show bg momfallenasleep_20
    pov "I will. Sorry..."

    jump lbl_mom_fallen_asleep_5_winc0

label lbl_mom_fallen_asleep_5_winc0:
    show bg momfallenasleep_25
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_32
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_56
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_55
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_58
    mum "[povname]? Is it a curse or a blessing that I'm your [mumrole]?"
    show bg momfallenasleep_59
    pov "Why would it be a curse?"
    show bg momfallenasleep_62
    mum "I guess, to put it simply. I could've been destined to be your soul mate by being born later."
    show bg momfallenasleep_61
    mum "But instead, I've been destined to [mumrole] you."
    show bg momfallenasleep_64
    pov "Are you regretting everything or something."
    show bg momfallenasleep_61
    mum "Oh no, far, far from that. Just thinking hypothetically and questioning too deeply about what the universe has in store for us."
    show bg momfallenasleep_62
    mum "You get the most thought provoking stuff late at night."

    menu:
        "It's a blessing.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg momfallenasleep_36
            pov "I think it's a blessing."
            show bg momfallenasleep_37
            pov "I mean, I couldn't have asked for a better [mumrole]. I couldn't even think of having someone more, umm, ‘qualified'."
            show bg momfallenasleep_26
            mum "Heheh, ‘qualified'."
            show bg momfallenasleep_27
            mum "I'm doing a good job, aren't I?"
            show bg momfallenasleep_36
            pov "Yeah, you are."
            if mum_points >= 4:
                show bg momfallenasleep_28
                mum "Reward me then."
                show bg momfallenasleep_15
                pov "How so?"
                show bg momfallenasleep_23
                mum "Kiss me."

                jump lbl_mom_fallen_asleep_6_winc0
            elif mum_points <= 3:
                show bg momfallenasleep_27
                mum "At least I'm on the right track."
                show bg momfallenasleep_36
                pov "Yup, you've successfully raised me and [sister] to adulthood without any trouble."
                show bg momfallenasleep_27
                mum "What an accomplishment."
                show bg momfallenasleep_36
                pov "I'm thankful for it."
                show bg momfallenasleep_15
                pov "Thank you, [missus]."
                show bg momfallenasleep_45
                mum "Stop making me blush."
                show bg momfallenasleep_54
                mum "..."
                show bg momfallenasleep_45
                mum "C'mon. It's pretty late already. I wish I could stay down here all night but your [dadrole] might blow the roof off this place."
                show bg momfallenasleep_36
                pov "Can't argue with that."
                show bg momfallenasleep_27
                mum "Thanks for cuddling with me, [povname]."
                show bg momfallenasleep_36
                pov "Let's do it again sometime soon."
                show bg momfallenasleep_27
                mum "Goodnight, my baby. I love you."
                show bg momfallenasleep_15
                pov "I love you too."
                $ momfallenasleep_goodbye = 1

                jump lbl_mom_fallen_asleep_end_winc0
        "It's a curse.":
            show bg momfallenasleep_59
            pov "I think it's a curse."
            if mum_points >= 5 and momfallenasleep_confession == 1:
                if mum_points <= 8:
                    $ mum_points += 2
                else:
                    $ mum_points = 10
                $ renpy.notify("Your relationship with [missus] has increased by 2")
                pov "I want to be with you so bad and yet, it's not all that easy and simple."
                show bg momfallenasleep_58
                mum "I understand. If only we live in a society that accepts this."
                show bg momfallenasleep_55
                pov "..."
                show bg momfallenasleep_63
                pov "What's stopping us?"
                show bg momfallenasleep_62
                mum "I am."
                show bg momfallenasleep_48
                pov "Why are you?"
                show bg momfallenasleep_49
                mum "I don't know..."
                show bg momfallenasleep_51
                pov "There's no one here but us."
                show bg momfallenasleep_46
                pov "We're in a new town, new life, new start."
                show bg momfallenasleep_49
                mum "Kiss me, [povname]."

                jump lbl_mom_fallen_asleep_6_1_winc0
            elif mum_points >= 5 and momfallenasleep_confession == 0:
                if mum_points <= 9:
                    $ mum_points += 1
                else:
                    $ mum_points = 10
                $ renpy.notify("Your relationship with [missus] has increased")
                pov "You're really fun to talk to, and I can totally see you being my best friend, or even more."
                show bg momfallenasleep_65
                mum "Even more, huh?"
                show bg momfallenasleep_15
                pov "I- I didn't mean to say that.."
                show bg momfallenasleep_18
                mum "Hehe, it's alright. I'm flattered. Accidents happen, I know what you mean."
                show bg momfallenasleep_17
                mum "Whoever you end up with in life, she's going to be one lucky girl."
                show bg momfallenasleep_16
                pov "You think so?"
                show bg momfallenasleep_17
                mum "I know so."
                show bg momfallenasleep_16
                mum "..."
                show bg momfallenasleep_17
                mum "[povname]?"
                show bg momfallenasleep_16
                pov "Mmm?"
                show bg momfallenasleep_17
                mum "Won't you give me a kiss?"

                jump lbl_mom_fallen_asleep_6_winc0
            elif mum_points <= 4:
                show bg momfallenasleep_59
                pov "I think it's a curse..."

                menu:
                    "When we talk, I forget that you're my [mumrole].":
                        show bg momfallenasleep_60
                        pov "When we talk like this, I forget you're my [mumrole]."
                        show bg momfallenasleep_59
                        pov "And yet the very thought is still in the back of my mind."
                        show bg momfallenasleep_58
                        mum "That's not an issue right? I hope it's not preventing you from being yourself with me."
                        show bg momfallenasleep_59
                        pov "Not at all."
                        show bg momfallenasleep_62
                        mum "Oh, good. Cause it almost sounded like it's a curse that the fact that I'm your [mumrole] is there haunting you."
                        show bg momfallenasleep_20
                        pov "I didn't mean it like that."
                        show bg momfallenasleep_18
                        mum "It's alright. It just sort of sounded like that."
                        show bg momfallenasleep_55
                        mum "..."
                        show bg momfallenasleep_62
                        mum "Umm... I think it's time to head to bed."
                        show bg momfallenasleep_20
                        pov "You don't want to cuddle a little longer?"
                        show bg momfallenasleep_22
                        mum "I wish, [povname]. But your [dadrole] is expecting me."
                        show bg momfallenasleep_16
                        pov "Alright then. I love you, [mumrole]."
                        show bg momfallenasleep_17
                        mum "I love you too."
                        $ momfallenasleep_goodbye = 1

                        jump lbl_mom_fallen_asleep_end_winc0
                    "I'd prefer you just to be a friend.":
                        if mum_points >= 1:
                            $ mum_points -= 1
                        else:
                            $ mum_points = 0
                        $ renpy.notify("Your relationship with [missus] has decreased")
                        show bg momfallenasleep_59
                        pov "I'd prefer you just to be a friend rather than a [mumrole]."
                        pov "I guess we were both born at the wrong time. The butterfly effect."
                        show bg momfallenasleep_57
                        mum "So you don't really like me being your [mumrole]?"
                        show bg momfallenasleep_63
                        pov "I mean-"
                        show bg momfallenasleep_49
                        mum "Is that it? Alright, I get it."
                        show bg momfallenasleep_46
                        pov "Wha-?"
                        show bg momfallenasleep_49
                        mum "You've made it clear to me that I'm not doing a good job being around you. What? Am I embarrassing to be around?"
                        show bg momfallenasleep_46
                        pov "No, it's not what I mean."
                        show bg momfallenasleep_47
                        mum "Yeah, save it, [povname]. I'm not in the mood anymore."
                        show bg momfallenasleep_20
                        pov "..."
                        show bg momfallenasleep_22
                        mum "Go to bed."
                        show bg momfallenasleep_20
                        pov "I didn-"
                        show bg momfallenasleep_22
                        mum "Goodnight, [povname]."
                        show bg momfallenasleep_20
                        pov "...Goodnight."

                        jump lbl_mom_fallen_asleep_end_winc0

label lbl_mom_fallen_asleep_6_winc0:

    scene bg momfallenasleep_66
    $ renpy.pause(2,hard=True)
    show bg momfallenasleep_67
    $ renpy.pause(0.8,hard=True)
    show bg momfallenasleep_68
    $ renpy.pause(1.5,hard=True)
    show bg momfallenasleep_67
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_66
    $ renpy.pause(2,hard=True)

    jump lbl_mom_fallen_asleep_6_1_winc0

label lbl_mom_fallen_asleep_6_1_winc0:
    $ momfallenasleep_kiss = 1

    scene bg momfallenasleep_69
    with vpunch
    $ renpy.pause(1.2,hard=True)
    show bg momfallenasleep_70
    $ renpy.pause(1.2,hard=True)
    show bg momfallenasleep_71
    $ renpy.pause(1,hard=True)
    show bg momfallenasleep_72
    $ renpy.pause(0.5,hard=True)
    show bg momfallenasleep_73
    $ renpy.pause(2,hard=True)
    show bg momfallenasleep_74
    $ renpy.pause()
    show bg momfallenasleep_75
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg momfallenasleep_76
    $ renpy.pause(0.8,hard=True)
    show bg momfallenasleep_77
    $ renpy.pause(1.5,hard=True)
    show bg momfallenasleep_78
    mum "Tell me I'm drunk..."
    show bg momfallenasleep_79
    pov "Did you drink?"
    show bg momfallenasleep_80
    mum "No..."
    show bg momfallenasleep_79
    pov "Then why-?"
    show bg momfallenasleep_80
    mum "Tell me I'm drunk... so I can somewhat comprehend what we just did..."
    show bg momfallenasleep_81
    pov "..."

    menu:
        "You're drunk.":
            show bg momfallenasleep_82
            pov "[missus], you're drunk."
            show bg momfallenasleep_83
            mum "Yeah... yeah you're right..."
            mum "I probably forgot that I even drank..."
            mum "We- we should get to bed."
            mum "In our own beds, I mean."
            show bg momfallenasleep_84
            pov "Hehe, sure, [missus]."
            show bg momfallenasleep_83
            mum "Thank you for tonight. I love you."
            show bg momfallenasleep_84
            pov "I love you too, [missus]."
            show bg momfallenasleep_67
            $ renpy.pause(1,hard=True)
            show bg momfallenasleep_75
            $ renpy.pause()
        "You're drunk with love.":
            show bg momfallenasleep_82
            pov "Mom, you're drunk... with love."
            show bg momfallenasleep_83
            mum "Oh, why do you have to be so cheesy, [povname]."
            show bg momfallenasleep_84
            pov "Well, it's true."
            show bg momfallenasleep_83
            mum "Heh.. I know I love you, baby."
            mum "I can't help myself."
            mum "We should get to bed."
            show bg momfallenasleep_84
            pov "Yeah, it's pretty damn late."
            pov "I love you too, by the way."
            show bg momfallenasleep_83
            mum "You just made my night."
            show bg momfallenasleep_67
            $ renpy.pause(1,hard=True)
            show bg momfallenasleep_75
            $ renpy.pause()
        "You're not drunk.":
            show bg momfallenasleep_79
            pov "Mom, you're not drunk, you know what you did, and you know you liked it."
            show bg momfallenasleep_85
            mum "..."
            show bg momfallenasleep_86
            mum "Screw you, [povname]."
            mum "This is your fault. I can't help what I just did."
            mum "Please tell me I'm drunk talking right now."

            menu:
                "You are.":
                    show bg momfallenasleep_84
                    pov "I'm just kidding, you are."
                    show bg momfallenasleep_83
                    mum "Oh, thank goodness."
                    mum "I guess my drunk-ass should get to bed, huh?"
                    show bg momfallenasleep_84
                    pov "I think so."
                    show bg momfallenasleep_83
                    mum "Goodnight, [povname]. Thank you for tonight."
                    show bg momfallenasleep_84
                    pov "I love you, [missus]."
                    show bg momfallenasleep_83
                    mum "I love you too, baby."
                    show bg momfallenasleep_67
                    $ renpy.pause(1,hard=True)
                    show bg momfallenasleep_75
                    $ renpy.pause()
                "Completely sober.":
                    show bg momfallenasleep_84
                    pov "Nope. Completely sober."
                    show bg momfallenasleep_86
                    mum "You enjoy this, don't you?"
                    mum "You know this is wrong and yet you like it."
                    show bg momfallenasleep_84
                    pov "Blaming me now?"
                    show bg momfallenasleep_86
                    mum "Yes, you kissed first."
                    show bg momfallenasleep_84
                    pov "You asked me to."
                    show bg momfallenasleep_87
                    mum "Hmm? I can't hear you."
                    show bg momfallenasleep_88
                    mum "{i}*Yawn*{/i} Oh, man, we should get to bed."
                    show bg momfallenasleep_89
                    pov "Heheh, I love you, [missus]."
                    show bg momfallenasleep_90
                    mum "Love you too, sweetie."
                    show bg momfallenasleep_67
                    $ renpy.pause(1,hard=True)
                    show bg momfallenasleep_75
                    $ renpy.pause()

label lbl_mom_fallen_asleep_end_winc0:
    $ mum_path = 5
    $ gtime = 3

    scene bg mybedroom_night
    with fade

    jump lbl_mybedroom_night_setup
