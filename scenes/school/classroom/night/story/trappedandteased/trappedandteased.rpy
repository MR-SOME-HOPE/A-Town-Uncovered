## Trapped and Teased ##
label lbl_trapped_and_teased:

    menu:
        "Put your hand between her legs":
            if missallaway_points >= 4 and skill_cha >= 5 and skill_luc >= 5:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ skill_cha -= 5
                $ skill_luc -= 5
                $ renpy.notify("You used 5 Charisma Points\nYou used 5 Luck Points\nYour relationship with Miss Allaway has increased")
                show bg trappedwithallaway_45
                with hpunch
                $ renpy.pause()
                mis "[povname]! W-what are you doing?"
                show bg trappedwithallaway_46
                pov "I can take my hand off if you want me to."
                pov "No one's here, remember?"
                pov "And you said whatever happens here, stays here."
                show bg trappedwithallaway_47
                mis "I- we- I-"
                show bg trappedwithallaway_48
                pov "Don't you want me touching you? C'mon, Miss Allaway."
                pov "Share with me your deep deep thoughts."
                show bg trappedwithallaway_49
                pov "I want to see the real Allaway come out."
                pov "Let her out."

                jump lbl_trapped_and_teased_1
            else:
                show bg trappedwithallaway_45
                with hpunch
                $ renpy.pause()
                show bg trappedwithallaway_50
                mis "[povname]! Get your hands off of me!"
                show bg trappedwithallaway_51
                mis "That isn't what I meant!"
                mis "I can't believe you actually tried to do that!"
                show bg trappedwithallaway_52
                pov "I- I thought that us being all alone and that you said everything that happens-"
                show bg trappedwithallaway_53
                mis "That. Is no. What I meant!"
                mis "You really are a messed up, perverted kid."
                show bg trappedwithallaway_54
                mis "{i}*Sigh*{/i} I'm going to pretend you didn't do that but I want you to keep your distance from me for tonight."
                mis "I don't care if we both catch a cold. Don't touch me."

                jump lbl_trapped_and_teased_2
        "You wanna put your words into action?":
            show bg trappedwithallaway_44
            pov "You wanna put your words into action?"
            show bg trappedwithallaway_39
            mis "I'm scared to know what you mean by that."
            show bg trappedwithallaway_38
            pov "I'll only do it if you want me to. You don't have to do anything."
            show bg trappedwithallaway_31
            mis "Do what...?"
            show bg trappedwithallaway_44
            pov "All you have to do is sit back, relax, and let me give you a massage."
            show bg trappedwithallaway_28
            mis "What kind of massage?"
            show bg trappedwithallaway_24
            pov "Mhmm. You must be pretty tired and sore there from sitting down a lot."
            if missallaway_points >= 5:
                show bg trappedwithallaway_26
                mis "I feel like you're going to do a lot more than just that."
                show bg trappedwithallaway_44
                pov "It's going to feel good, is all I'm promising."
                show bg trappedwithallaway_43
                mis "..."
                show bg trappedwithallaway_44
                pov "It's just us, remember?"
                pov "If we're going to die tonight, would you regret not saying yes to my offer?"
                show bg trappedwithallaway_26
                mis "I- I don't know..."
                mis "My brain says that you're just a horny teenager who wants to take advantage of me..."
                show bg trappedwithallaway_39
                mis "But..."
                show bg trappedwithallaway_44
                pov "I'll take that ‘but' as a yes."
                show bg trappedwithallaway_45
                $ renpy.pause()

                jump lbl_trapped_and_teased_1
            else:
                show bg trappedwithallaway_25
                mis "I feel... fine, [povname]."
                mis "Again, stop pushing me. I don't want whatever you have in that perverted mind of yours."
                mis "You're going too far with even asking me that."
                show bg trappedwithallaway_16
                mis "I- I want you away from me. For tonight."
                show bg trappedwithallaway_17
                pov "I'm not going to rap-"
                show bg trappedwithallaway_51
                mis "Don't. Put that shit in my head. Just go to the other side of the room and leave me be."

                jump lbl_trapped_and_teased_2
        "Alright.":
            if missallaway_points <= 9:
                $ missallaway_points += 1
            else:
                $ missallaway_points = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased")
            show bg trappedwithallaway_11
            pov "Alright, Miss Allaway."
            pov "My lips are locked."
            show bg trappedwithallaway_12
            mis "Good, thank you."
            show bg trappedwithallaway_10
            mis "I've had enough talking for one night. We may be locked in here but we still need to get some sleep."
            show bg trappedwithallaway_8
            pov "You're right. Let's do that."
            show bg trappedwithallaway_18
            pov "I'll apologies in advance if I snore too loud or if I accidentally touch you in any wrong way while I sleep."
            pov "I'm pretty all over the place."
            show bg trappedwithallaway_20
            mis "That's okay, so am I."
            show bg trappedwithallaway_0
            mis "..."
            mis "...."
            mis "....."

            menu:
                "Goodnight.":
                    pov "Goodnight, Miss Allaway."
                    mis "Goodnight, [povname]."

                    jump lbl_trapped_and_teased_3
                "Stay Silent":
                    pov "..."
                    mis "..."
                    mis "Don't you wish people good night?"
                    pov "Goodnight, Miss."
                    mis "Heheh, you're really such a cutie."

                    jump lbl_trapped_and_teased_3

label lbl_trapped_and_teased_1:
    show bg trappedwithallaway_55
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_55
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_55
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.8,hard=True)
    mis "Mm... your hand is warm..."
    show bg trappedwithallaway_55
    mis "Has- has it always been this warm..?"
    show bg trappedwithallaway_56
    pov "You like it don't you?"
    show bg trappedwithallaway_55
    mis "Mmm.."
    show bg trappedwithallaway_56
    pov "I want to hear you say it."
    show bg trappedwithallaway_55
    mis "I- I shouldn't..."
    show bg trappedwithallaway_56
    pov "Ah- that's not it."
    show bg trappedwithallaway_55
    mis "I- I like it, [povname]... it feels nice."
    show bg trappedwithallaway_56
    mis "Ahh... yeeahh.. Oh... yeah..."
    show bg trappedwithallaway_55
    mis "That's the spot, [povname]..."
    show bg trappedwithallaway_56
    $ trappedandteased_counter = 0

    jump lbl_trapped_and_teased_1_1

####################
## Stage 1
label lbl_trapped_and_teased_1_1:
    scene img_trapped_and_teased_1_stage_1
    #$ trappedandteased_counter += 1
    #show bg trappedwithallaway_55
    #$ renpy.pause(0.4,hard=True)
    #show bg trappedwithallaway_56
    #$ renpy.pause(0.4,hard=True)
    #if skill_sta <= 7 and trappedandteased_counter == 8:
    #    jump lbl_trapped_and_teased_1_4
    #elif skill_sta <= 14 and trappedandteased_counter == 12:
    #    jump lbl_trapped_and_teased_1_2
    #elif skill_sta <= 20 and trappedandteased_counter == 16:
    #    jump lbl_trapped_and_teased_1_2
    #else:
    #    jump lbl_trapped_and_teased_1_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_trapped_and_teased_1_4
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_trapped_and_teased_1_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_trapped_and_teased_1_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_trapped_and_teased_1_1

image img_trapped_and_teased_1_stage_1:
    "bg trappedwithallaway_55"
    pause 0.4
    "bg trappedwithallaway_56"
    pause 0.4
    repeat

####################
## Stage 2
label lbl_trapped_and_teased_1_2:
    scene img_trapped_and_teased_1_stage_2
    #$ trappedandteased_counter += 1
    #show bg trappedwithallaway_55
    #$ renpy.pause(0.2,hard=True)
    #show bg trappedwithallaway_56
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and trappedandteased_counter == 28:
    #    jump lbl_trapped_and_teased_1_4
    #elif skill_sta <= 20 and trappedandteased_counter == 32:
    #    jump lbl_trapped_and_teased_1_3
    #else:
    #    jump lbl_trapped_and_teased_1_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_trapped_and_teased_1_4

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_trapped_and_teased_1_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_trapped_and_teased_1_2

image img_trapped_and_teased_1_stage_2:
    "bg trappedwithallaway_55"
    pause 0.2
    "bg trappedwithallaway_56"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_trapped_and_teased_1_3:
    scene img_trapped_and_teased_1_stage_3
    #$ trappedandteased_counter += 1
    #show bg trappedwithallaway_55
    #$ renpy.pause(0.1,hard=True)
    #show bg trappedwithallaway_56
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and trappedandteased_counter == 48:
    #    jump lbl_trapped_and_teased_1_4
    #else:
    #    jump lbl_trapped_and_teased_1_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_trapped_and_teased_1_4

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_trapped_and_teased_1_3

image img_trapped_and_teased_1_stage_3:
    "bg trappedwithallaway_55"
    pause 0.1
    "bg trappedwithallaway_56"
    pause 0.1
    repeat

####################
## Cum or Not
label lbl_trapped_and_teased_1_4:
    if skill_str >= 12:
        $ skill_str -= 6
        $ renpy.notify("You used 6 Strength Points")
        scene bg trappedwithallaway_57
        with vpunch
        mis "Oh- fucckk!"
        show bg trappedwithallaway_58
        mis "Oh, fuck..."
        show bg trappedwithallaway_59
        mis "Fuck fuckity fuck!"
        show bg trappedwithallaway_60
        $ renpy.pause(0.5,hard=True)
        show bg trappedwithallaway_61
        $ renpy.pause(0.5,hard=True)
        show bg trappedwithallaway_62
        $ renpy.pause(0.5,hard=True)
        show bg trappedwithallaway_63
        $ renpy.pause(0.5,hard=True)
        mis "Oh God, that felt so good."
        show bg trappedwithallaway_62
        mis "I fucking needed that."
        mis "Shit... what a fucking mess."
        mis "..."
        mis "Excuse my French, [povname]."
        pov "Hahaha, you can speak all the French you want. I find it so hot and unlike you."
        mis "..."
        mis "C'mon. Let's get some sleep. We may be stuck in the classroom but we still need to get some shut eye."
        pov "Right. Good idea. I guess next time you can return the favour."
        mis "Ha. Good one, [povname]. In your dreams. As if this will ever happen again."
        mis "I hope..."

        jump lbl_trapped_and_teased_3
    else:
        scene bg trappedwithallaway_55
        mis "Okay.. okay.. Stop."
        show bg trappedwithallaway_56
        mis "Sorry, [povname]. I don't feel like I'm close at all..."
        mis "Sorry, it's not your fault."
        show bg trappedwithallaway_55
        mis "Maybe partially your fault for not doing it well enough."
        mis "Was that out loud or in my head?"
        pov "Out loud."
        mis "Oh..."
        mis "This is awkward on so many levels..."
        pov "Maybe you could teach me then, teacher."
        mis "Funny thing you said there, [povname]."
        mis "But as much as I want to make a mess in front of my own student."
        mis "..."
        mis "I'm not thinking clearly."
        mis "Uh- let's just forget what happened okay?"
        pov "But-"
        mis "[povname]! Please?"
        pov "{i}*Sigh*{/i}"
        pov "Fine."
        mis "Let's get some sleep and hopefully it won't be too long a night."

        jump lbl_trapped_and_teased_3

label lbl_trapped_and_teased_2:

    scene black
    with fade
    show bg trappedwithallaway_02
    with fade
    $ renpy.pause()

    jump lbl_morning_freedom

label lbl_trapped_and_teased_3:

    scene black
    with fade
    "Hours later..."
    show bg trappedwithallaway_03
    with fade
    $ renpy.pause()

    jump lbl_morning_freedom
