## Twin Fortress Rebuild ##
label lbl_twin_fortress_rebuild:

    scene bg twinfortressrebuild_1
    with fade
    $ renpy.pause(1.5,hard=True)
    show bg twinfortressrebuild_2
    with dissolve
    $ renpy.pause(1.5,hard=True)
    show bg twinfortressrebuild_3
    with dissolve
    $ renpy.pause(1.5,hard=True)
    show bg twinfortressrebuild_4
    with dissolve
    $ renpy.pause(1.5,hard=True)
    show bg twinfortressrebuild_5
    with dissolve
    $ renpy.pause(1.5,hard=True)
    show bg twinfortressrebuild_0
    with dissolve
    $ renpy.pause()

    scene bg mybasement_lightson2
    with fade
    show pov embarrassed at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "I'm so proud of you, honey."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "Heh, it's just a box fort. It's not like the work of Leonardo Davingee."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "It's not what you made but why you made it."
    if winc == 0:
        mum "Taking care of your [sisrole] like this."
        show mum smirk_talk at right
        mum "How many [povsisrole]s do you think would go this far for their [sisrole]?"
    else:
        mum "Taking care of your sister like this."
        show mum smirk_talk at right
        mum "How many brothers do you think would go this far for their sister?"
    show mum embarrassed_talk at right
    mum "It calms my heart knowing that the two of you have each others backs."
    show pov confused at left
    show mum confused_talk at right
    mum "Although..."
    if (mum_points >= 8 or mum_path >= 27) and siblingjailtime_hj == 0:
        if mum_points >= 1:
            $ mum_points -= 1
        else:
            $ mum_points = 0
        if winc == 0:
            $ renpy.notify("Your relationship with [missus] has decreased")
        else:
            $ renpy.notify("Your relationship with Mom has decreased")
        show pov shocked at left
        show mum sad_talk at right
        mum "I cannot help but to feel a little bit jealous, you know?"
        show pov confused_talk at left
        show mum sad at right
        pov "Jealous of what?"
        show pov confused at left
        show mum embarrassed_talk at right
        mum "Well..."
        show pov embarrassed at left
        show mum sad_talk at left
        mum "You've been focusing a lot on her lately."
        mum "Not to mention you also took the time to do this."
        show pov sad at left
        mum "Kinda makes a woman needy to see their lover focus on someone else?"
        show pov embarrassed_talk at left
        show mum embarrassed at right
        if winc == 0:
            pov "There is nothing you should worry about, I just want the household back together."
            pov "Things are hard enough as they are and we don't need for them to get any harder with [sister] refusing to even sleep under the same roof as [dadname]."
        else:
            pov "There is nothing you should worry about, I just want the family back together."
            pov "Things are hard enough as they are and we don't need for them to get any harder with [sister] refusing to even sleep under the same roof as Dad."
        show pov embarrassed at left
        show mum sad_talk at right
        mum "I know that's true."
        show pov sad at left
        mum "But..."
        mum "I can't help but feel a little insecure, that's all."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "I promise to make it up to you."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        if winc == 0:
            pov "I just want our household back together. that's all."
            mum "And that dedication to us is one of the many reasons why I love you."
            mum "You're really proving to us that you are the man you said you are."
            show pov bored at left
            mum "But you'll always be my [povmumrole]."
            show pov embarrassed_talk at left
            show mum smirk at right
            pov "I love you too, [missus]."
        else:
            pov "I just want our family back together. that's all."
            mum "And that dedication to us is one of the many reasons why I love you."
            mum "You're really proving to us that you are the man you said you are."
            show pov bored at left
            mum "But you'll always be my baby."
            show pov embarrassed_talk at left
            show mum smirk at right
            pov "I love you too, Mom."
        show pov neutral_talk at left
        show mum embarrassed at right
        pov "I would do anything for my favourite girls in the world."
    elif (mum_points <= 7 or mum_path <= 26) and siblingjailtime_hj == 1:
        if mum_points >= 1:
            $ mum_points -= 1
        else:
            $ mum_points = 0
        if winc == 0:
            $ renpy.notify("Your relationship with [missus] has decreased")
        else:
            $ renpy.notify("Your relationship with Mom has decreased")
        show pov confused at left
        show mum confused_talk at right
        mum "I'm still not sure if the intentions behind this are completely pure."
        show pov embarrassed_talk at left
        show mum confused at right
        pov "What do you mean by 'completely pure'."
        show pov embarrassed at left
        show mum bored_talk at right
        mum "W-Well.."
        show pov shocked at left
        show mum confused_talk at right
        mum "There is still the issue of what the two of you were doing at that jail cell."
        show pov sad at left
        if winc == 0:
            mum "We never got to discuss it with your [dadrole]'s rampage and... well..."
            show pov sad_talk at left
            show mum bored at right
            pov "[missus], don't hold it against her."
        else:
            mum "We never got to discuss it with your father's rampage and... well..."
            show pov sad_talk at left
            show mum bored at right
            pov "Mom, don't hold it against her."
        show pov embarrassed_talk at left
        pov "I was drunk and confused, not to mentioned aroused."
        show mum confused at right
        pov "What happened was the result of a really long line of mistakes made that night, but at least we looked after each other."
        show pov embarrassed at left
        show mum bored_talk at right
        mum "I don't know if I would call that 'looking after each other'."
        show pov sad at left
        mum "It isn't something I'm happy or comfortable to know about..."
    elif (mum_points >= 8 or mum_path >= 27) and siblingjailtime_hj == 1:
        if mum_points >= 2:
            $ mum_points -= 2
        else:
            $ mum_points = 0
        if winc == 0:
            $ renpy.notify("Your relationship with [missus] has decreased by 2")
        else:
            $ renpy.notify("Your relationship with Mom has decreased by 2")
        show pov shocked at left
        show mum bored_talk at right
        mum "I'm still upset about where I found her touching you back then."
        show pov embarrassed_talk at left
        show mum bored at right
        pov "W-What do you mean?"
        show pov shocked at left
        show mum angry_talk at right
        mum "Don't play dumb with me, [povname]."
        mum "I already decided not blame you since it was the first time you were drunk."
        show mum angry at right
        mum "..."
        show pov embarrassed at left
        show mum confused_talk at right
        mum "It {i}was{/i} the first time you got drunk, right?"
        show pov embarrassed_talk at left
        show mum confused at right
        pov "O-Of course! I'd never even tasted alcohol before in my life!"
        show mum bored at right
        pov "Hehe.. he.."
        show pov embarrassed at left
        mum "..."
        show mum bored_talk at right
        mum "We are coming back to that conversation later young man."
        show pov embarrassed_talk at left
        show mum angry at right
        pov "Have I mentioned how beautiful you look when you're mad?"
        show pov shocked at left
        show mum angry_talk at right
        mum "Keep talking and I'll be resembling a Greek goddess soon enough."
        show pov sad_talk at left
        show mum bored at right
        pov "Sorry..."
        show pov embarrassed_talk at left
        show mum bored at right
        pov "Let me make it up to you! How about another date night soon?"
        show pov smirk_talk at left
        pov "Just you and I."
        show pov embarrassed at left
        mum "Hmm.."
        show pov embarrassed at left
        show mum sad_talk at right
        mum "You know I can't say no to that. I'll only be doing myself a disservice."
        show pov smirk_talk at left
        show mum embarrassed at right
        pov "I'll take that as a 'yes' then."
        show pov smirk at left
        show mum sad_talk at right
        mum "{i}*Sigh*{/i} You're too adorable to let slip away."
    elif (mum_points <= 7 or mum_path <= 26) and siblingjailtime_hj == 0:
        show pov confused at left
        show mum embarrassed_talk at right
        mum "I'm still wondering if this isn't just an in the moment thing."
        show pov confused_talk at left
        show mum embarrassed at right
        pov "What do you mean by that?"
        show pov embarrassed at left
        show mum confused_talk at right
        mum "Well, I'm half expecting a heartwarming reunion for a few hours only for the two of you to be at each other's throats again next thing in the morning."
        show pov embarrassed_talk at left
        show mum bored at right
        pov "We aren't that bad."
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Honey, who do you think you're talking to?"
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Withdrawn."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "Look, I promise to behave for at least a few days, I just want things to go back to normal."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        if winc == 0:
            mum "And I thank you for trying, it's been hard sleeping peacefully knowing [sister] is refusing to come home."
        else:
            mum "And I thank you for trying, it's been hard sleeping peacefully knowing my child is refusing to come home."
    show pov confused_talk at left
    show mum confused at right
    if winc == 0:
        pov "Anyway, I just hope [dadname] doesn't come down here and destroy it again in another fit of rage."
        show pov confused at left
        show mum confused_talk at right
        mum "Don't worry about your [dadrole], I'll make sure to deal with him when the time comes."
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "Are you sure, [missus]?"
    else:
        pov "Anyway, I just hope Dad doesn't come down here and destroy it again in another fit of rage."
        show pov confused at left
        show mum confused_talk at right
        mum "Don't worry about your father, I'll make sure to deal with him when the time comes."
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "Are you sure, Mom?"
    show pov sad_talk at left
    show mum embarrassed at right
    pov "He has been acting so assholey lately and I don't want you to get caught on the crossfire."
    if bathwithmom_eyereveal == 1:
        show pov angry_talk at left
        pov "I mean... If he were to hurt you again I might just kill him."
        pov "Or at the very least beat him senseless."
        show pov angry at left
        show mum embarrassed_talk at right
        mum "I'm sure you will, hon."
        show pov embarrassed at left
        mum "But you have to trust me a little bit too, I know what I'm doing."
        show pov sad_talk at left
        show mum embarrassed at right
        pov "I just don't want to see you hurt again..."
        show pov sad at left
        show mum embarrassed_talk at right
        mum "I know, darling."
    show pov smirk at left
    show mum bored_talk at right
    mum "Don't worry, I'll make him see reason one way or another."
    show mum smirk_talk at right
    mum "If he has any more lip to give us about it then he can spend the whole week on the streets for all I care."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I'll be sure to be nearby just in case you need some help."
    if mum_points >= 6:
        show pov embarrassed at left
        show mum neutral_talk at right
        mum "That's why you're my big, strong baby bo- I mean man."
    else:
        show pov bored at left
        show mum neutral_talk at right
        mum "That's why you're my big, strong baby boy."
    show pov embarrassed at left
    show mum smirk at right
    pov "..."
    show pov confused_talk at left
    pov "You think she is going to like this? I tried to make it as closely as I remember the fort looking... but better?"
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "I'm sure that sentiment alone will be enough to make her love it, no matter what."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Now come on, help me with dinner, sweetie."
    show pov neutral_talk at left
    show mum neutral at right
    if winc == 0:
        pov "Right behind you, [missus]."
    else:
        pov "Right behind you, Mom."

    scene black
    with fade
    $ renpy.pause()
    "After dinner..."
    if mowed_lawn == 1:
        scene bg mydiningroom_night
        with fade
    else:
        scene bg mydiningroom_night_grassy
        with fade
    $ sister_path = 33
    $ gtime = 2

    jump lbl_mydiningroom_night_setup
