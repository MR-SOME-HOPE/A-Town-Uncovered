## The Awkward Ride Home ##
label lbl_the_awkward_ride_home:
    default theawkwarddrivehome_truth = 0

    scene black
    with fade
    "On the way home..."

    scene bg awkwardridehome_1
    with fade
    pov ".."
    mum "..."
    show bg awkwardridehome_2
    pov "...."
    mum "....."
    show bg awkwardridehome_3
    menu:
        "So...":
            show bg awkwardridehome_4
            pov "So..."
            show bg awkwardridehome_5
            mum "Do you have ANY idea of what you just put me through?"
            mum "I stayed up all night waiting for you to come home!"
            show bg awkwardridehome_6
            mum "Do you know how anxious I felt every time I saw someone pass down the street?"
            mum "I called everyone I know! I looked for you in every building!"
            show bg awkwardridehome_7
            mum "Do you even care?"
            show bg awkwardridehome_8
            pov "Of course I do, what are you talking about?"
            show bg awkwardridehome_10
            mum "Well, that's not what you're showing me right now!"
            mum "... I-I just... I don't know what's going on with you anymore!"
            show bg awkwardridehome_7
            if winc == 1:
                mum "Please... [povname] I'm begging you here! I'm your mother, I deserve to know things, don't I?"
            else:
                mum "Please... [povname] I'm begging you here! I'm your [mumrole], I deserve to know things, don't I?"
            mum "Just. Give me a reason, anything! Tell me what has you acting like this!"
            show bg awkwardridehome_5
            mum "Tell. Me. The truth!"
        "Turn on some music":
            #"You reach over to turn on the radio."
            show bg awkwardridehome_9
            $ hardpause(1.5)
            show bg awkwardridehome_5
            mum "...Seriously?"
            mum "Don't you even dare touch the dashboard, [povname]. This isn't something you can just drown away with music."
            show bg awkwardridehome_11
            pov "I-I'm just trying to lighten the mood."
            show bg awkwardridehome_5
            mum "You wouldn't need to lighten the mood had you not disappeared yesterday!"
            mum "Where the fuck have you been?!"
            show bg awkwardridehome_10
            mum "I have been worried sick all day and when the police showed up I- I-"
            mum "..."
            show bg awkwardridehome_5
            mum "I- thought you were hurt or injured or even dead!"
            show bg awkwardridehome_6
            mum "They arrested you for being naked in public in a town with a fucking nudist beach?!"
            show bg awkwardridehome_12
            pov "I-I can explain!"
            show bg awkwardridehome_6
            mum "You better!"
            mum "I-Is it something at university?! Did you get tricked?! Talk to me [povname]!"
            show bg awkwardridehome_11
            pov "I'm tryin-"
            show bg awkwardridehome_6
            mum "I don't know what else to do if you don't tell me what's wrong!"
            show bg awkwardridehome_12
            pov "I'm trying to expla-"
            show bg awkwardridehome_10
            mum "Do you not trust me, [povname]? Have I done something to make you hate me? Have I not proven to you that you can tell me anything?"
            mum "You must think I'm a terrible parent if this is what I deserve."
            show bg awkwardridehome_7
            mum "What am I doing wrong, [povname]?!"
            mum "What do I need to do for you to be honest with me?!"
        "You're looking beautiful today.":
            show bg awkwardridehome_17
            if winc == 0:
                pov "You're looking beautiful today, [missus]."
            else:
                pov "You're looking beautiful today, Mom."
            show bg awkwardridehome_6
            mum "Flattery is going to get you nowhere this time, [povname], I'm way too pissed at you..."
            show bg awkwardridehome_1
            pov "..."
            show bg awkwardridehome_2
            mum "..."
            show bg awkwardridehome_3
            mum "...."
            if mum_path >= 24 and mum_path >= 7:
                show bg awkwardridehome_7
                mum "Am I not enough for you?"
                show bg awkwardridehome_8
                pov "W-what? What are you asking?"
                show bg awkwardridehome_10
                mum "Am I not enough of a thrill for you? Do you see me as just your backup cumrag or something?"
                show bg awkwardridehome_5
                mum "Do you now need to go around town naked for you to feel anything, is that what this is?"
                show bg awkwardridehome_15
                pov "Did you seriously just say that?"
                pov "Of course not! How can you even ask that?!"
                show bg awkwardridehome_16
                mum "Well, I don't see any other explanation and you sure as hell aren't explaining yourself either!"
            show bg awkwardridehome_10
            mum "I can't believe you, [povname]!"
            mum "While I'm dying of worry back home, hoping to have you back in my arms safe and sound, they find you passed out naked at the lake!"
            show bg awkwardridehome_16
            mum "Now that you finally come back to me you have the audacity to try and flirt with me as if nothing had happened?!"
            mum "What was it? Alcohol? Cocaine? Uh- Marijuana?!"
            show bg awkwardridehome_15
            pov "You got it all wrong! It's not like that at all!"
            show bg awkwardridehome_16
            mum "Then how is it like, [povname]?! If you value what we have and want me to ever look at you the same way, you're going to be a man and tell me truth!"
            mum "And if you lie to me, I doubt I'll be able to forgive you so easily."
            show bg awkwardridehome_5
            mum "I'm giving you this. One. Last. Chance."
            show bg awkwardridehome_6
            mum "Where. The. Fuck. Were you yesterday?!"
    show bg awkwardridehome_8
    pov "I-It's not something that's easy to explain... To be honest, I'm not even sure where to begin..."
    show bg awkwardridehome_10
    mum "Well, I'm asking you to try."
    show bg awkwardridehome_18
    menu:
        "Tell her about the sex world":
            if skill_cha >= 16:
                $ skill_luc -= 10
                $ renpy.notify("You used 10 Charisma Points")
            else:
                if mum_points >= 2:
                    $ mum_points -= 2
                else:
                    $ mum_points = 0
                if winc == 0:
                    $ renpy.notify("Your relationship with [missus] has decreased by 2")
                else:
                    $ renpy.notify("Your relationship with Mom has decreased by 2")
            $ theawkwarddrivehome_truth = 1
            show bg awkwardridehome_12
            pov "Alright... Alright, I'll tell you the complete truth but..."
            show bg awkwardridehome_19
            pov "But you might not believe it... I myself am having trouble doing so..."
            show bg awkwardridehome_20
            mum "No matter what it is, [povname]. I want to know..."
            scene black
            with fade
            "A confusing explanation later..."
            scene bg awkwardridehome_21
            with fade
            #"[missus] looks clearly surprised."
            $ renpy.pause(1.5,hard=True)
            show bg awkwardridehome_22
            pov "That's all I remember... I'm still debating if I didn't hallucinate the whole thing..."
            show bg awkwardridehome_21
            mum "..."
            show bg awkwardridehome_23
            mum "That... That's quite the story...."
            show bg awkwardridehome_24
            pov "I don't blame you for not believing me."
            show bg awkwardridehome_23
            mum "It's way too detailed for you to have came up with it just now, maybe a fever dream?"
            show bg awkwardridehome_25
            mum "Maybe you were drugged?"
            show bg awkwardridehome_23
            mum "It's not a comforting thought, I can't say that I believe it..."
            mum "But at least I know that you were out of your mind."
            show bg awkwardridehome_25
            mum "No sane person is crazy enough to come up with that detailed explanation."
            mum "And I mean, you really went in with the detail."
            show bg awkwardridehome_22
            pov "It all seemed so real... I'm still not sure if it was just a dream."
            show bg awkwardridehome_25
            mum "Honey, it had to be. It's ridiculous!"
            show bg awkwardridehome_5
            mum "I don't want you drinking anything from an open container from now on, stick to closed water bottles and drinking at home."
            show bg awkwardridehome_6
            mum "Just a text of where you are from time to time wouldn't kill you and it sure as hell wouldn't kill me!"
            show bg awkwardridehome_2
            pov "..."
            scene bg myhousefront_day
            with fade
            #"The car pulls up in front of the house."
            show bg awkwardridehome_37
            $ renpy.pause(0.4,hard=True)
            show bg awkwardridehome_38
            $ renpy.pause(0.4,hard=True)
            show bg awkwardridehome_39
            $ renpy.pause(0.8,hard=True)
            $ main_story = 39
        "Avoid the question":
            if skill_luc >= 16:
                $ skill_luc -= 10
                $ renpy.notify("You used 10 Luck Points")
            else:
                if mum_points >= 2:
                    $ mum_points -= 2
                else:
                    $ mum_points = 0
                if winc == 0:
                    $ renpy.notify("Your relationship with [missus] has decreased by 2")
                else:
                    $ renpy.notify("Your relationship with Mom has decreased by 2")
            show bg awkwardridehome_19
            if winc == 0:
                pov "I-I'm sorry, [missus], I honestly don't remember..."
            else:
                pov "I-I'm sorry, Mom, I honestly don't remember..."
            pov "Everything was really just a blur."
            show bg awkwardridehome_9
            mum "..."
            show bg awkwardridehome_6
            mum "I want you straight home every afternoon after class."
            mum "I know you're working now, so I'll be expecting a text message when you leave university, when you arrive at work and vice versa."
            show bg awkwardridehome_16
            mum "You're forbidden from staying out too late and If you EVER do something like this again, I'll consider your father's more severe punishment ideas."
            if indecentarrest_shutup == 1:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                if winc == 0:
                    $ renpy.notify("Your relationship with [missus] has decreased")
                else:
                    $ renpy.notify("Your relationship with Mom has decreased")
                show bg awkwardridehome_6
                mum "He is already pissed at your behavior and what you did yesterday only served to anger him even more."
                show bg awkwardridehome_16
                mum "You have no right to speak to your father that way."
                mum "Much less when you're standing naked in a jail cell after he was kind enough to agree on bringing you clothes!"
                show bg awkwardridehome_10
                mum "You're aware how unstable your father has been lately and you go ahead and piss him off even more?! I thought he was going to explode when he came back home!"
            show bg awkwardridehome_2
            pov "..."
            scene bg myhousefront_day
            with fade
            #"The car pulls up in front of the house."
            show bg awkwardridehome_37
            $ renpy.pause(0.4,hard=True)
            show bg awkwardridehome_38
            $ renpy.pause(0.4,hard=True)
            show bg awkwardridehome_39
            $ renpy.pause(0.8,hard=True)

            $ main_story = 39

        "Hide the sex world from her":
            if skill_int >= 10 and skill_cha >= 10:
                $ skill_int -= 5
                $ skill_cha -= 5
                $ renpy.notify("You used 5 Charisma Points\nYou used 5 Intelligence Points")
                show bg awkwardridehome_2
                pov "..."
                show bg awkwardridehome_22
                pov "It's all a blur to be honest..."
                pov "All I remember was being invited somewhere with some of the guys at university and having a few drinks..."
                show bg awkwardridehome_24
                pov "It's all a giant blur after that..."
                pov "I can't even remember the faces of the guys I was with."
                if winc == 0:
                    pov "I'm sorry, [missus].. I was just trying to make friends here..."
                else:
                    pov "I'm sorry, Mom.. I was just trying to make friends here..."
                show bg awkwardridehome_8
                pov "This new place and all... I-It has been a bit hard to adapt to..."
                show bg awkwardridehome_26
                mum "...Thank you for being sincere with me..."
                mum "T-That's all I wanted..."
                show bg awkwardridehome_27
                $ renpy.pause(1.5,hard=True)
                #"[missus] smiles a little, keeping her nerves calm."
                show bg awkwardridehome_28
                mum "I know this whole change is something hard to adapt to, sweetheart..."
                mum "And I thank you for trying to make the most of it! Don't get me wrong."
                show bg awkwardridehome_29
                mum "Knowing you're willing to give this place a shot and are trying to reach out to other people fills me with relief."
                mum "But you still can't let your guard down completely like that."
                show bg awkwardridehome_30
                mum "There are bad people even in small towns like this... Next time you could wake up in a bathtub full of ice and missing a kidney!"
                show bg awkwardridehome_31
                if winc == 0:
                    pov "You're watching too many dramas again, [missus]."
                else:
                    pov "You're watching too many dramas again, Mom."
                show bg awkwardridehome_10
                mum "Well, the possibility still scares me, [povname]!"
                show bg awkwardridehome_28
                mum "...I know you aren't a bad kid and that you wouldn't disappear like this without a reason."
                show bg awkwardridehome_29
                mum "Will you promise me to be careful from now on? I don't want you hanging with bad company."
                show bg awkwardridehome_24
                if winc == 0:
                    pov "I will, [missus], of course..."
                else:
                    pov "I will, [missus], of course..."
                show bg awkwardridehome_29
                mum "Thank you, honey... Thank you for trusting me..."
                show bg awkwardridehome_36
                pov "..."
                show bg awkwardridehome_33
                pov "Yeah..."
                show bg awkwardridehome_35
                if winc == 0:
                    pov "No problem, [missus]."
                else:
                    pov "No problem, Mom."
                show bg awkwardridehome_28
                mum "Just... Call me or text me every time you move somewhere else... Just until I'm calm enough, okay?"
                show bg awkwardridehome_29
                mum "Can you do that for me?"
                show bg awkwardridehome_32
                pov "..."
                show bg awkwardridehome_33
                pov "Of course... I promise..."
                if mum_points >= 8 and mum_path >= 30:
                    show bg awkwardridehome_20
                    mum "And... I didn't think I would need to remind you of this..."
                    show bg awkwardridehome_30
                    mum "But do remember you have me... ALL of me."
                    mum "I chose this on my own and I'm more than ready to give myself fully to you anytime you want."
                    show bg awkwardridehome_34
                    mum "We both decided this as consenting adults, don't you forget that."
                    show bg awkwardridehome_19
                    if winc == 0:
                        pov "I won't forget it, [missus]. Don't you worry about that."
                    else:
                        pov "I won't forget it, Mom. Don't you worry about that."
                    show bg awkwardridehome_10
                    mum "I was so scared, [povname]."
                    mum "The idea of you disappearing."
                    show bg awkwardridehome_30
                    mum "Of you leaving me alone after everything we have been through lately."
                    show bg awkwardridehome_10
                    mum "It broke my heart... I... I-I thought you didn't want me anymore."
                    show bg awkwardridehome_24
                    if winc == 0:
                        pov "Why would you even think that, [missus]? You're all I want."
                    else:
                        pov "Why would you even think that, Mom? You're all I want."
                    show bg awkwardridehome_28
                    mum "I know... You have proven that enough but..."
                    mum "But..."
                    show bg awkwardridehome_26
                    mum "It still hurt, [povname]. It still scared me."
                    show bg awkwardridehome_13
                    pov "..."
                    mum "..."
                    show bg awkwardridehome_28
                    mum "I love you."
                    show bg awkwardridehome_34
                    mum "I love you so damn much, [povname]."
                    show bg awkwardridehome_35
                    if winc == 0:
                        pov "I love you too, [missus]."
                    else:
                        pov "I love you too, Mom."
                scene bg myhousefront_day
                with fade
                #"The car pulls up in front of the house."
                show bg awkwardridehome_37
                $ renpy.pause(0.4,hard=True)
                show bg awkwardridehome_38
                $ renpy.pause(0.4,hard=True)
                show bg awkwardridehome_39
                $ renpy.pause(0.8,hard=True)

                $ main_story = 39

            else:
                if mum_points <= 6:
                    if mum_points >= 3:
                        $ mum_points -= 3
                    else:
                        $ mum_points = 0
                    if winc == 0:
                        $ renpy.notify("Your relationship with [missus] has decreased by 3")
                    else:
                        $ renpy.notify("Your relationship with Mom has decreased by 3")
                else:
                    $ mum_points -= 4
                    if winc == 0:
                        $ renpy.notify("Your relationship with [missus] has decreased by 4")
                    else:
                        $ renpy.notify("Your relationship with Mom has decreased by 4")
                show bg awkwardridehome_2
                pov "..."
                show bg awkwardridehome_22
                pov "I-I..."
                pov "I fell asleep in the park and someone must've taken my clothes..."
                show bg awkwardridehome_2
                mum "..."
                show bg awkwardridehome_3
                mum "...."
                mum "....."
                #"[missus] starts to shed a tear."
                scene bg myhousefront_day
                with fade
                show bg awkwardridehome_37
                $ renpy.pause(0.4,hard=True)
                #"The car pulls up in front of the house. She doesn't get out, she just sits there crying."
                show bg awkwardridehome_38
                pov "..."
                mum "{i}*Sniff*{/i}"
                if winc == 0:
                    pov "[missus], I-"
                else:
                    pov "Mom, I-"
                mum "Just get out, [povname]."
                mum "Please..."
                mum "..."
                mum "I need to uhm- get some.. milk..."
                menu:
                    "Get out":
                        show bg awkwardridehome_39
                        $ renpy.pause(0.8,hard=True)
                        show bg awkwardridehome_40
                        $ renpy.pause(0.4,hard=True)
                        show bg awkwardridehome_41
                        $ renpy.pause(1.2,hard=True)
                        #"You get out and she drives off."
                    "Stay":
                        pov "I-"
                        mum "I said get out!"
                        show bg awkwardridehome_39
                        $ renpy.pause(0.8,hard=True)
                        show bg awkwardridehome_40
                        $ renpy.pause(0.4,hard=True)
                        show bg awkwardridehome_41
                        $ renpy.pause(1.2,hard=True)
                        #"She closes her eyes and tears pour down her cheeks."
                        #"You get out and she drives off."

                $ main_story = 40

    if main_story == 39:
        jump lbl_never_again
    else:
        jump lbl_myhousefront_day_setup
