## Fort Rebuild Reveal ##
label lbl_fort_rebuild_reveal:
    $ townmap_enabled = 1

    scene black
    with fade
    sis "I'm telling you, Effie, I really don't think I'm ready for coming back here."
    eff "Just trust me a little bit, ok? And don't even peek."
    sis "I can't see anything through this blindfold. Is it really that big a deal that I'm blindfolded?"
    eff "[povname] has worked on something for you that I think you're going to like."
    eff "Besides, when have I ever wronged you?"
    sis "Well, alright..."
    if winc == 1:
        sis "Is my douchebag Dad around? Because if he is, we're leaving this very instant."
        sis "I'm definitely not ready to see that fuck-face again and I doubt he will be happy to see me either."
        mum "Hey! Language, missy. Don't worry about your father."
        mum "I made sure he stays as far away from this house as possible today."
        sis "Thanks, Mom..."
        sis "I'm sorry I have to make you do this in the first place."
        mum "Nonsense, honey."
        mum "He deserves it this time."
        sis "So, can somebody tell what this is all about?"
        eff "I told you already, your brother made something for you."
        sis "Alright, but if he got me a bouncy castle shouldn't it be outside?"
        eff "It's not a bouncy castle!"
        mum "You know I don't let you kids around bouncy castles anymore!"
        sis "Is it a clown then? Those are fun."
        eff "God, you guys really are siblings."
    else:
        sis "Is my douchebag [dadrole] around? Because if he is, we're leaving this very instant."
        sis "I'm definitely not ready to see that fuck-face again and I doubt he will be happy to see me either."
        mum "Hey! Language, missy. Don't worry about your [dadrole]."
        mum "I made sure he stays as far away from this house as possible today."
        sis "Thanks, [missus]..."
        sis "I'm sorry I have to make you do this in the first place."
        mum "Nonsense, honey."
        mum "He deserves it this time."
        sis "So, can somebody tell what this is all about?"
        eff "I told you already, your [povsisrole] made something for you."
        sis "Alright, but if he got me a bouncy castle shouldn't it be outside?"
        eff "It's not a bouncy castle!"
        mum "You know I don't let you kids around bouncy castles anymore!"
        sis "Is it a clown then? Those are fun."
        eff "God, you guys really are [povsisrole]s."
    eff "Stop trying to guess, watch your step, here comes the stairs."
    sis "[povname]?"
    sis "Dude, what is it?"
    sis "Unless you got an oiled up and naked Chris Hemmingsworth down here, I would really rather go back to bed."
    mum "Ditto..."
    pov "It isn't any of those options but I do hope you still like it."
    pov "Take a look!"
    scene bg fortrebuildreveal_1
    with dissolve
    $ renpy.pause(0.4,hard=True)
    show bg fortrebuildreveal_2
    $ renpy.pause(0.4,hard=True)
    show bg fortrebuildreveal_3
    $ renpy.pause(0.4,hard=True)
    show bg fortrebuildreveal_4
    $ renpy.pause(0.4,hard=True)
    show bg fortrebuildreveal_5
    $ renpy.pause(0.4,hard=True)
    show bg fortrebuildreveal_6
    $ renpy.pause(1.5,hard=True)
    show bg fortrebuildreveal_7
    $ renpy.pause()
    show bg fortrebuildreveal_9
    sis "Y-you..."
    sis "Our fort?"
    show bg fortrebuildreveal_10


    menu:
        "I wanted you back home.":
            show bg fortrebuildreveal_11
            pov "I wanted you back home."
        "I can be nice too.":
            show bg fortrebuildreveal_11
            pov "I can be nice too."
        "I am the greatest.":
            show bg fortrebuildreveal_12
            pov "I am the greatest, aren't I?"

    #"She looks at him with tears"

    scene bg fortrebuildreveal_13
    with hpunch
    sis "Thank you! Thank you, thank you, thank you!"
    sis "{i}*Sniff*{/i}"
    sis "Thank you, [povname]... {i}*Sniff*{/i}"
    sis "Oh, fuck.. here comes the ugly sobbin-"
    #"She goes in for the hug"
    sis "{i}*Sniff*{/i} Uhuhuhuuuu-"
    #show bg fortrebuildreveal_14
    eff "We should give you guys some time alone, I gotta get home anyway."
    #show bg fortrebuildreveal_15
    eff "And hey, [sister]. You're always welcome in my home anytime."
    eff "If anything's wrong, I'm always here for you."
    sis "{i}*Sniff*{/i}"
    #"It dissolves into her hugging Effie."
    scene bg fortrebuildreveal_17
    with hpunch
    sis "{i}*Sniff*{/i} Thank you, Effie..."
    sis "Thank you everything..."
    show bg fortrebuildreveal_16
    sis "I- I'm so thankful.. and sorry."
    show bg fortrebuildreveal_18
    eff "Oh, bab- [sister]. Don't apologise one bit. I'm just happy to see you full of joy again."
    show bg fortrebuildreveal_19
    eff "Tah tah for now, boo- bestie."
    scene bg fortrebuildreveal_20
    with fade
    mum "May I drive you home, Effie?"
    show bg fortrebuildreveal_21
    eff "Oh, no. That's okay. It's only a short walk-"
    show bg fortrebuildreveal_22
    mum "Oh, please, I insist. I need to head out anyway."
    show bg fortrebuildreveal_23
    eff "Alright, thank you very much."
    #"They leave and it goes back to the line-up shot with just the siblings now."
    scene bg fortrebuildreveal_24
    with fade
    sis "..."
    show bg fortrebuildreveal_25
    sis "B-But..."
    sis "What about..."
    show bg fortrebuildreveal_26
    if winc == 1:
        pov "Mom and I have the whole business with Dad taken care of."
    else:
        pov "[missus] and I have the whole business with [dadname] taken care of."
    show bg fortrebuildreveal_27
    pov "He isn't about to destroy this fort, not if I have a say about it or if he has any wishes of sleeping on this house ever again."
    show bg fortrebuildreveal_28
    sis "I- I still don't get it..."
    show bg fortrebuildreveal_29
    sis "Why?"
    sis "Why do all of this- for me?"
    show bg fortrebuildreveal_30
    menu:
        "Be understanding":
            scene bg fortrebuildreveal_31
            with fade
            pov "Because I know-"
            pov "I know what this means to you-"
            show bg fortrebuildreveal_32
            pov "to us."
            pov "This box fort, formally known as Twin Fortress, and what it represents."
            show bg fortrebuildreveal_33
            pov "I know it's importance and I think I now understand why we actually made it in the first place."
            #"you gently take a hold of her cheek"
            show bg fortrebuildreveal_37
            pov "Life sucks."
            pov "The older you get, the more it sucks."
            show bg fortrebuildreveal_38
            pov "Dreams get shattered..."
            pov "Things change..."
            show bg fortrebuildreveal_39
            pov "And as much as we wish we could forever be six year olds making dumb faces at each other-"
            pov "And argue about who gets first ride on the swings."
            show bg fortrebuildreveal_38
            pov "We will have to grow older."
            show bg fortrebuildreveal_40
            pov "..."
            pov "But.."
            show bg fortrebuildreveal_41
            pov "That doesn't mean we can't have fun the same way we used to do."
            pov "Right?"
            show bg fortrebuildreveal_42
            pov "We're adults now, we can live our lives the way we want."
            pov "That's the point of a Twin Fortress, isn't it?"
            show bg fortrebuildreveal_39
            pov "To keep the bad stuff out and the good things in?"
            show bg fortrebuildreveal_43
            sis "Mhmm..."
            show bg fortrebuildreveal_42
            pov "Well, I'm not going to let anyone take that away from you."
            show bg fortrebuildreveal_38
            pov "Not dad, not anyone."
            show bg fortrebuildreveal_39
            pov "This is our place."
            pov "Our home away from home..."
            show bg fortrebuildreveal_42
            pov "At home..."
            pov "And I want you to know..."
            show bg fortrebuildreveal_37
            pov "To pretty much tattoo it in that thick skull of yours."
            pov "That no matter where we end up or how fucked up things get..."
            show bg fortrebuildreveal_42
            pov "There is always going to be a cardboard fort with the names [povname] and [sister]."
            show bg fortrebuildreveal_41
            pov "Plastic stars and all."
        "Be romantic":
            scene bg fortrebuildreveal_34
            with fade
            pov "Why do you think, [sister]."
            if winc == 1:
                pov "If you asked me a year ago, I would probably say that Mom made me do it."
            else:
                pov "If you asked me a year ago, I would probably say that [missus] made me do it."
            show bg fortrebuildreveal_35
            pov "Maybe I would have said that I did it because your crying was annoying."
            show bg fortrebuildreveal_34
            pov "Or even that the mess annoyed the hell out of me."
            show bg fortrebuildreveal_36
            pov "But not now."
            #"you gently take a hold of her cheek"
            show bg fortrebuildreveal_37
            pov "None of them would be true now."
            pov "..."
            show bg fortrebuildreveal_39
            pov "We have been getting so much closer lately."
            pov "For the first time in my life since we were kids..."
            show bg fortrebuildreveal_41
            pov "I actually feel like I know you."
            pov "The real you..."
            show bg fortrebuildreveal_39
            pov "The you who isn't afraid of being vulnerable."
            pov "The you I can wholeheartedly trust."
            show bg fortrebuildreveal_42
            pov "The you I have grown to adore ever since we moved here."
            pov "..."
            show bg fortrebuildreveal_39
            pov "The one and only person I've been missing to death."
            show bg fortrebuildreveal_38
            if winc == 1:
                pov "When I saw how devastated you were when Dad destroyed our fort."
            else:
                pov "When I saw how devastated you were when [dadname] destroyed our fort."
            pov "How scared you were..."
            show bg fortrebuildreveal_37
            pov "It killed me knowing I couldn't take that pain away."
            pov "That I failed to protect you-"
            show bg fortrebuildreveal_38
            pov "I let him trample all over your-"
            show bg fortrebuildreveal_39
            pov "Our safe haven."
            show bg fortrebuildreveal_38
            pov "I failed as a man in every sense of the word."
            pov "..."
            show bg fortrebuildreveal_39
            pov "That isn't a mistake I intend to let happen again."
            show bg fortrebuildreveal_37
            pov "So know this."
            pov "No matter what happens and what stands in our way."
            show bg fortrebuildreveal_39
            pov "We are in this together."
            show bg fortrebuildreveal_42
            pov "And I plan on protecting you and our safe haven from anything and everything."
            show bg fortrebuildreveal_39
            pov "I'm not losing you again."
            show bg fortrebuildreveal_41
            pov "And if you still need to ask why I'm doing this..."
            show bg fortrebuildreveal_42
            pov "It should be more than obvious that I'm doing it because I lov-"
        "Be playful":
            scene bg fortrebuildreveal_35
            with fade
            pov "Dum-dum, are you really asking that?"
            if winc == 1:
                pov "Come on, sis, you're supposed to be the smart one of the duo!"
            else:
                pov "Come on, [sister], you're supposed to be the smart one of the duo!"
            show bg fortrebuildreveal_34
            pov "Geez, I suppose I'm now, the brains, the looks and the brawn then."
            show bg fortrebuildreveal_35
            pov "Looks like you're left with being the potty mouth."
            #"you gently take a hold of her cheek"
            show bg fortrebuildreveal_37
            pov "Hmmm..."
            show bg fortrebuildreveal_40
            pov "Why do you think I did it?"
            show bg fortrebuildreveal_41
            pov "Hell, do I really need a reason to begin with?"
            show bg fortrebuildreveal_42
            pov "It's me and you against the world!"
            show bg fortrebuildreveal_43
            pov "That's the vow we made when we were little kids and renown when we built the fort for the first time."
            show bg fortrebuildreveal_41
            pov "Unlike years ago, we're not actually fighting a globe with eyes."
            show bg fortrebuildreveal_42
            pov "That saying really confused us but we heard it in a movie and therefore, it was cool."
            show bg fortrebuildreveal_44
            sis "{i}*Chuckles*{/i}"
            show bg fortrebuildreveal_38
            pov "I miss that laugh of yours."
            show bg fortrebuildreveal_39
            if winc == 1:
                pov "Mom described it as the cure to all sadness."
            else:
                pov "[missus] described it as the cure to all sadness."
            pov "But you know what they say, the goofier the laugh, the funnier it is."
            show bg fortrebuildreveal_41
            pov "Actually no one says that, I just made that up."
            pov "Pretty good, huh?"
            show bg fortrebuildreveal_39
            pov "Y'know. Even on our hundredth birthday, I would climb into a box fort and just lay there with you."
            show bg fortrebuildreveal_41
            pov "Even if it does kill our backs."
            show bg fortrebuildreveal_39
            pov "It may as well be our coffin."
            show bg fortrebuildreveal_42
            pov "That isn't something I'm going to let anyone take away from us."
            show bg fortrebuildreveal_40
            pov "You're the Robin to my Batman, although with a nicer rack."
            show bg fortrebuildreveal_45
            sis "W-"
            show bg fortrebuildreveal_37
            pov "So!"
            show bg fortrebuildreveal_41
            pov "{i}*Clears throat*{/i}"
            show bg fortrebuildreveal_42
            pov "Have you figured it out why I did all of this or do you need me to spell it out for yo-"

    #"[sister] rushes in and wraps her arms around you again."
    #"The two stay locked together for a few moments."
    #"[sister] rushes in and kisses your lips, wrapping her arms around your neck."
    #"The two stay locked together for a few moments before she breaks the kiss and lays her head on your shoulder."
    scene bg fortrebuildreveal_46
    with hpunch
    sis "..."
    sis "Thank you, [povname]."
    if winc == 1:
        sis "You really are the best brother in the world."
    else:
        sis "You really are the best [sisrole] in the world."
    sis "And I would fight anyone who objects to the death."
    #"You chuckle and hug her harder"
    pov "Don't mention it."
    pov "Taking care of you is part of the job."
    pov "A part I have come to enjoy a lot recently."
    show bg fortrebuildreveal_13
    sis "You are..."
    sis "You're just the best..."
    pov "Took you long enough to realise, didn't it?"
    #"She continues to cry."
    pov "Come on."
    pov "We should at least enter the fort, don't you think?"

    jump lbl_breaking_in_fort_rebuild
