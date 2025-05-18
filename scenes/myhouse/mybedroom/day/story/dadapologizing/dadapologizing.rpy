## Dad Apologizing ##
label lbl_dad_apologizing:

    scene bg mybedroom_day
    "{i}*Knock knock knock*{/i}"
    show pov confused at left
    with dissolve
    pov "..."
    show pov confused_talk at left
    pov "Come in?"
    show pov bored at left
    show dad sad_talk at right
    with dissolve
    dad "Hey there..."

    menu:
        "Oh, it's you.":
            show pov bored_talk at left
            pov "Oh, it's you."
            pov "What do you want."
            show pov bored at left
            show dad sad_talk at right
            dad "I've come to apologize."
        "Hi, Dad." if winc == 1:
            show pov bored_talk at left
            pov "Hi, Dad."
            show pov confused_talk at left
            pov "You're here to apologize?"
            show pov bored at left
            show dad sad_talk at right
            dad "Yes."
        "Hi, [dadname]." if winc == 0:
            show pov bored_talk at left
            pov "Hi, [dadname]."
            show pov confused_talk at left
            pov "You're here to apologize?"
            show pov bored at left
            show dad sad_talk at right
            dad "Yes."
        "Get out.":
            show pov angry_talk at left
            pov "Get out."
            show pov angry at left
            show dad sad_talk at right
            dad "Wait- give me a second to apologize."
    show pov bored at left
    show dad sad at right
    dad "..."
    show pov bored at left
    show dad sad_talk at right
    if winc == 0:
        dad "I'm sorry I ruined you and your [sisrole]'s box fort."
    else:
        dad "I'm sorry I ruined you and [sister]'s box fort."
    dad "No excuses, I'm just an asshole. I'll admit it."
    dad "I've been an asshole ever since we moved here and I just... I'm so-so sorry, [povname]."
    dad "I really hope you can forgive me."
    show dad sad at right
    dad "..."
    show pov confused at left
    show dad sad_talk at right
    if winc == 0:
        dad "I just came from your [sisrole]'s room. I've begged for her forgiveness and now I'm begging for yours."
    else:
        dad "I just came from [sister]'s room. I've begged for her forgiveness and now I'm begging for yours."
    show pov confused_talk at left
    show dad sad at right
    pov "Did she accept your apology?"
    show pov shocked at left
    show dad sad_talk at right
    dad "Fortunately for me, she did."
    show pov bored at left
    show dad sad_talk at right
    if winc == 0:
        dad "Admittedly, it did take a while. Your [sisrole]'s the stubborn one between you two, aye?"
    else:
        dad "Admittedly, it did take a while. [sister]'s the stubborn one between you two, aye?"
    show dad sad at right
    pov "..."
    show pov angry_talk at left
    pov "I know she forgave you but I don't know if I should."
    pov "She was traumatized by your actions, I don't know if you're aware."
    pov "She ran away from home all because of you."
    show pov angry at left
    show dad sad_talk at right
    dad "I know, I know. And if I could go back in time, I would never-never-ever-ever do that."
    show pov bored at left
    show dad sad_talk at right
    dad "I've been such a gigantic dick around here recently. But that's not who I really am."
    dad "You know who I really am."
    show pov bored_talk at left
    show dad sad at right
    pov "I don't know if I really do anymore."
    show pov confused at left
    show dad sad_talk at right
    dad "{i}*Sigh*{/i} Of course you don't..."
    dad "So much has changed."
    if winc == 0:
        dad "The other me has done a terrible job at maintaining a happy household..."
    else:
        dad "The other me has done a terrible job at maintaining a happy family..."
    show dad sad at right
    pov "..."
    show pov confused_talk at left
    show dad neutral at right
    pov "The other you?"
    show pov bored at left
    show dad sad_talk at right
    dad "...The- uhm.. Y'know. The crappy part of me."
    if winc == 0:
        dad "The side that went rampant and destroyed this family."
    else:
        dad "The side that went rampant and destroyed this household."
    dad "I- don't blame you if you can't forgive me. I can't forgive him- me."
    show pov confused at left
    dad "I can't forgive mesel- myself."
    show pov confused at left
    show dad sad at right
    pov "..."
    show dad sad_talk at right
    if winc == 0:
        dad "But please, [povname]. I promise you, I will never ever intrude on you and your [sisrole]'s box fort ever again."
    else:
        dad "But please, [povname]. I promise you, I will never ever intrude on you and [sister]'s box fort ever again."
    dad "Or anything that you don't want me to."
    if bathwithmom_eyereveal == 1:
        show pov angry_talk at left
        show dad sad at right
        if winc == 0:
            pov "And [missus]'s black eye?"
        else:
            pov "And Mom's black eye?"
        show pov bored at left
        show dad sad_talk at right
        dad "She has a black eye?!"
        dad "Did he- I give her a black eye?"
        show pov bored_talk at left
        show dad sad at right
        pov "Um.. yeah? Are you losing your mind or something?"
        show pov confused at left
        show dad angry_talk at right
        dad "That fucking-"
        show pov bored at left
        show dad sad_talk at right
        dad "I mean- sorry. I- {i}*sigh*{/i}."
    show pov bored at left
    show dad sad_talk at right
    dad "I'm so fucking sorry for causing you guys any pain."
    dad "I didn't mean to. Just- stress and hatred has come over me somehow and I hate that I can't control it."
    dad "I- will find some help. Anger management. Anything."
    dad "Just please, accept me back."
    show pov bored_talk at left
    show dad sad at right
    pov "You seem really desperate."
    show pov bored at left
    show dad sad_talk at right
    dad "I'm metaphorically on my knees, [povname]."

    menu:
        "Fine.":
            if dad_points <= 8:
                $ dad_points += 2
            else:
                $ dad_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [dadname] has increased by 2")
            else:
                $ renpy.notify("Your relationship with Dad has increased by 2")
            show pov sad_talk at left
            show dad sad at right
            if winc == 0:
                pov "Fine, welcome back to the household."
            else:
                pov "Fine, welcome back to the family."
        "Only because the others forgave you.":
            if dad_points <= 9:
                $ dad_points += 1
            else:
                $ dad_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [dadname] has increased")
            else:
                $ renpy.notify("Your relationship with Dad has increased")
            show pov bored_talk at left
            show dad sad at right
            if winc == 0:
                pov "Fine, but only because [missus] and [sister] forgave you."
            else:
                pov "Fine, but only because Mom and [sister] forgave you."
        "I'm not forgiving you, but you can stay.":
            show pov angry_talk at left
            show dad sad at right
            pov "I'm not forgiving you, but you can stay."
    show pov bored at left
    show dad sad_talk at right
    dad "Thank you, [povname]. Thank you for letting me stay."
    if winc == 0:
        dad "My household means so much to me and I'm an idiot to take you all for granted."
        dad "I promise to behave and be the male role model that you deserve."
    else:
        dad "My family means so much to me and I'm an idiot to take you all for granted."
        dad "I promise to behave and be the father figure that you deserve."
    show pov confused at left
    dad "Especially now that you're transitioning into a real man."
    show pov bored at left
    dad "Thank you, [povname]."
    show pov bored_talk at left
    show dad sad at right
    pov "Yeah, yeah. Don't get sobby on me. I have my eye on you."
    pov "Now, can you leave my room, please?"
    show pov bored at left
    show dad sad_talk at right
    dad "Of course, thank you and I'm sorry."
    show pov confused at left
    hide dad sad_talk
    pov "{i}He's... very different. It's like a light switch has turned on and he's now good.{/i}"
    if bathwithmom_eyereveal == 1:
        if winc == 0:
            pov "{i}I can't believe he doesn't remember hurting [missus]... {/i}"
        else:
            pov "{i}I can't believe he doesn't remember hurting Mom... {/i}"
        show pov bored at left
        pov "{i}I think he's getting old and his brain is shutting down on him.{/i}"
    else:
        show pov bored at left
        pov "{i}Probably has some bi-polar traits. Although, he's been more assholey than nice as of recently.{/i}"
    $ sister_path = 38
    $ townmap_enabled = 1
    pause 0.2
    jump lbl_mybedroom_day_setup
