## Healed Eye ##
label lbl_healed_eye:
    default healedeye_tellsister = 0

    scene bg myhallway_day
    with fade
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right
    with dissolve
    if winc == 0:
        pov "Oh, hey, [missus]."
    else:
        pov "Oh, hey, Mom."
    pov "It's really great to see you out and about now."
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "It does feel nice not having to trap myself in my room."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Your eye healed pretty quickly."
    show pov smirk at left
    show mum embarrassed_talk at right
    mum "Oh, well, it's still a little dark but I've applied some makeup so it isn't that obvious."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Just until it completely heals of course."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    if winc == 0:
        mum "I don't want your [sisrole] getting worried about me."
    else:
        mum "I don't want your sister getting worried about me."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "As long as you're feeling alright now."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "I am, honey. Thanks for your concern."
    show pov embarrassed_talk at left
    show mum confused at right
    if winc == 0:
        pov "Hey, [missus]?"
    else:
        pov "Hey, Mom?"
    show pov embarrassed at left
    mum "Mhmm?"

    menu:
        "I love you.":
            show pov neutral_talk at left
            show mum embarrassed at right
            pov "I love you."
            show pov neutral at left
            show mum smirk_talk at right
            mum "Naww, I love you too, [povname] baby."
        "You look great." if skill_cha >= 2:
            $ skill_cha -= 2
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("You used 2 Charisma Points\nYour relationship with [missus] has increased")
            else:
                $ renpy.notify("You used 2 Charisma Points\nYour relationship with Mom has increased")
            show pov smirk_talk at left
            show mum embarrassed at right
            pov "You look great."
            show pov smirk at left
            show mum embarrassed_talk at right
            mum "You think so?"
            show pov smirk_talk at left
            show mum embarrassed at right
            if winc == 0:
                pov "Of course, [missus]. You're such a gorgeous, beautiful, dare I say, sexy woman."
            else:
                pov "Of course, Mom. You're such a gorgeous, beautiful, dare I say, sexy woman."
            show pov neutral at left
            show mum embarrassed_talk at right
            if winc == 0:
                mum "Oh, stop it. You're too much. You're just saying that because I'm your [mumrole]."
            else:
                mum "Oh, stop it. You're too much. You're just saying that because I'm your mother."
            show pov shocked_talk at left
            show mum smirk at right
            pov "It's true."
            show pov neutral at left
            show mum embarrassed_talk at right
            mum "Well, thank you, baby. You just made my day."
        "I'll kill Dad if he hurts you again." if skill_str >= 15 and winc == 1:
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            $ renpy.notify("Your relationship with Mom has increased")
            show pov bored_talk at left
            show mum shocked at right
            pov "I'll kill Dad if he hurts you again."
            show pov bored at left
            show mum embarrassed_talk at right
            mum "Oh, honey. As much as I appreciate how protective you are over me."
            mum "We talked about this. Don't get too worked up over it."
            show pov angry at left
            show mum sad_talk at right
            mum "Things just got too heated between us and well..."
            show pov bored at left
            show mum embarrassed_talk at right
            mum "Just, let's... just drop it."
            show pov sad_talk at left
            show mum embarrassed at right
            pov "..."
            show pov embarrassed_talk at left
            pov "Alright, Mom. If you really want me to."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Thank you, [povname]."
        "I'll kill [dadname] if he hurts you again." if skill_str >= 15 and winc == 0:
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            $ renpy.notify("Your relationship with [missus] has increased")
            show pov bored_talk at left
            show mum shocked at right
            pov "I'll kill [dadname] if he hurts you again."
            show pov bored at left
            show mum embarrassed_talk at right
            mum "Oh, honey. As much as I appreciate how protective you are over me."
            mum "We talked about this. Don't get too worked up over it."
            show pov angry at left
            show mum sad_talk at right
            mum "Things just got too heated between us and well..."
            show pov bored at left
            show mum embarrassed_talk at right
            mum "Just, let's... just drop it."
            show pov sad_talk at left
            show mum embarrassed at right
            pov "..."
            show pov embarrassed_talk at left
            pov "Alright, [missus]. If you really want me to."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Thank you, [povname]."
        "I think you should tell [sister] about it.":
            if mum_points >= 1:
                $ mum_points -= 1
            else:
                $ mum_points = 0
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Your relationship with [sister] has increased")
            else:
                $ sister_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ renpy.notify("Your relationship with Mom has decreased")
            $ renpy.pause(3,hard=True)
            show pov confused_talk at left
            show mum confused at right
            pov "I think you should tell [sister] about what happened."
            show pov confused at left
            show mum confused_talk at right
            mum "Oh, I really don't think that's a good idea."
            show pov angry_talk at left
            show mum shocked at right
            if winc == 0:
                pov "We're a household, she's on our side. She deserves to know. No secrets between-"
            else:
                pov "We're a family, she's on our side. She deserves to know. No secrets between fam-"
            show pov angry at left
            show mum angry_talk at right
            mum "What if I do tell her?"
            mum "What then?"
            show pov angry at left
            show mum bored_talk at right
            mum "..."
            show pov bored at left
            show mum sad_talk at right
            mum "Nothing but more worry and tension between us will come of it."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "It's best if we keep it between us. Can you do that for me?"
            show pov sad_talk at left
            show mum embarrassed at right
            pov "..."

            menu:
                "Fine.":
                    show pov embarrassed_talk at left
                    show mum embarrassed at right
                    pov "Fine. If you say so."
                    show pov embarrassed at left
                    show mum embarrassed_talk at right
                    mum "Thank you. And that'll be the end of it."
                    show pov embarrassed_talk at left
                    show mum neutral at right
                    pov "Alright, I won't bring it up again."
                "No.":
                    $ healedeye_tellsister = 1
                    show pov angry_talk at left
                    show mum bored at right
                    pov "No, that's not right."
                    show pov sad_talk at left
                    pov "She'll find out one way or another and where'll be the trust when she finds out that we kept it from her?"
                    show pov sad at left
                    show mum sad at right
                    mum "..."
                    show mum sad_talk at right
                    mum "I guess I can't stop you, can I? I just want things to settle down, not burn stronger."
                    show mum sad at right
                    pov "..."
    $ mum_path = 17.5
    $ townmap_enabled = 1

    jump lbl_myhallway_day_setup
