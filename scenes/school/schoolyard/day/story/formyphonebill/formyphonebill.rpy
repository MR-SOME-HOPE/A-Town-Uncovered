## For My Phone Bill ##
label lbl_for_my_phone_bill:
    default formyphonebill_owe = 0
    show pov confused at left
    with dissolve
    sis "[povname]!"
    show pov shocked at left
    show sis neutral_talk at right
    with dissolve
    sis "Helloooooo!"
    show pov confused_talk at left
    show sis neutral at right
    pov "[sister]? What are you doing here?"
    show pov shocked at left
    show sis smirk_talk at right
    sis "Enrolling."
    show pov shocked_talk at left
    show sis smirk at right
    pov "...What?"
    show pov bored at left
    show sis smirk_talk at right
    sis "Kidding. I'm so fucking glad to be done with studying."
    show pov smirk at left
    show sis confused_talk at right
    sis "Are you sure you don't want to quit and spread your wings?"
    show pov neutral_talk at left
    show sis bored at right
    pov "Yeah, I'm sure."
    show pov embarrassed at left
    show sis bored_talk at right
    sis "That might be smart. That whole bills thing..."
    show pov embarrassed_talk at left
    show sis bored at right
    pov "Adulting, huh?"
    show pov embarrassed at left
    show sis bored_talk at right
    sis "Adulting. Anyway..."
    show pov confused at left
    show sis neutral_talk at right
    sis "I need to ask a favor of you."
    show pov confused_talk at left
    show sis neutral at right
    pov "Oh, a favor? It's been a long time since you asked for one of those."
    show pov bored at left
    show sis smirk_talk at right
    sis "Come on, don't be a dick."
    show pov bored_talk at left
    show sis neutral at right
    pov "Alright. What is it?"
    show pov bored at left
    show sis neutral_talk at right
    sis "I need some cash. I get paid next week so I can pay you back then."
    show pov bored_talk at left
    show sis embarrassed at right
    pov "{i}*Sigh*{/i}"
    pov "How much?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "$50. It's for my phone bill."
    show pov confused_talk at left
    show sis embarrassed at right
    if winc == 0:
        pov "But our [dadrole]s pay for that..."
    else:
        pov "But our parents pay for that..."
    show pov embarrassed at left
    show sis confused_talk at right
    sis "Not me anymore."
    show pov sad_talk at left
    show sis confused at right
    pov "Harsh."
    show pov embarrassed at left
    show sis bored_talk at right
    sis "Yeah. You win some you lose some."
    show pov confused_talk at left
    show sis bored at right
    pov "That makes more sense. I was wondering why you wouldn't just text or call about needing cash."
    pov "But if your plan is expired..."
    show pov embarrassed at left
    show sis bored_talk at right
    sis "Yep. You guessed it. So...?"
    show pov smirk_talk at left
    show sis shocked at right
    pov "You should say please."
    show pov smirk at left
    show sis bored at right
    sis "..."
    pov "..."
    show sis embarrassed_talk at right
    sis "... [povname], would you please lend me some money?"

    menu:
        "I think you can do better.":
            if skill_cha >= 3:
                show pov smirk_talk at left
                show sis bored at right
                pov "I think you can do better."
                show pov smirk at left
                sis "..."
                show sis embarrassed_talk at right
                if winc == 0:
                    sis "[povname], my beautiful little [povsisrole]. Would you pretty please lend me some money?"
                else:
                    sis "[povname], my beautiful little brother. Would you pretty please lend me some money?"

                menu:
                    "I think you can do EVEN better.":
                        if skill_cha >= 3 and skill_luc >= 3:
                            show pov smirk_talk at left
                            show sis angry at right
                            pov "I think you can do EVEN better."
                            show pov smirk at left
                            show sis angry_talk at right
                            sis "I'm gonna kick you in the dick..!"
                            show sis bored_talk at right
                            sis "{i}*Inhale*{/i}"
                            show sis embarrassed_talk at right
                            if winc == 0:
                                sis "Would my wonderful, amazing, most caring [povsisrole] in the world do his not-as-cool, desparate [sisrole] a favour..."
                            else:
                                sis "Would my wonderful, amazing, most caring brother in the world do his not-as-cool, desperate sister a favour..."
                            show sis bored_talk at right
                            sis "{i}*Inhale*{/i}"
                            show sis embarrassed_talk at right
                            sis "And lend me $50 for my phone bill. Pretty please with two titty like cherries on top."

                            jump lbl_for_my_phone_bill_2
                        else:
                            show pov smirk_talk at left
                            show sis angry at right
                            pov "I think you can do EV-"
                            show pov embarrassed at left
                            show sis angry_talk at right
                            sis "Don't. Even. Fucking go there, [povname]."
                            sis "Can't you just... {i}*inhale*{/i}"
                            show sis sad_talk at right
                            sis "...please?"
                            show sis embarrassed_talk at right
                            sis "I already asked nicely."

                            jump lbl_for_my_phone_bill_2

                    "Alright, when can you pay me back?" if inventory.money >= 50:
                        jump lbl_for_my_phone_bill_3
                    "Here, don't worry about paying me back." if inventory.money >= 50:
                        jump lbl_for_my_phone_bill_4
                    "Sorry, I'm broke.":
                        jump lbl_for_my_phone_bill_5
            else:
                show pov smirk_talk at left
                show sis bored at right
                pov "I think you can do better."
                show pov smirk at left
                sis "..."
                show pov bored at left
                show sis bored_talk at right
                sis "Well, I think you should stop being an anus but I still put up with you."
                show pov embarrassed at left
                show sis neutral_talk at right
                if winc == 0:
                    sis "With love of course, little [povsisrole]."
                else:
                    sis "With love of course, little bro."

                jump lbl_for_my_phone_bill_2

        "Alright, when can you pay me back?" if inventory.money >= 50:
            jump lbl_for_my_phone_bill_3
        "Here, don't worry about paying me back." if inventory.money >= 50:
            jump lbl_for_my_phone_bill_4
        "Sorry, I'm broke.":
            jump lbl_for_my_phone_bill_5

label lbl_for_my_phone_bill_2:

    menu:
        "Alright, when can you pay me back?" if inventory.money >= 50:
            jump lbl_for_my_phone_bill_3
        "Here, don't worry about paying me back." if inventory.money >= 50:
            jump lbl_for_my_phone_bill_4
        "Sorry, I'm broke.":
            jump lbl_for_my_phone_bill_5

label lbl_for_my_phone_bill_3:
    if sister_points <= 9:
        $ sister_points += 1
        $ renpy.notify("Your relationship with [sister] has increased")
    else:
        $ sister_points = 10
    $ formyphonebill_owe = 1
    $ inventory.money -= 50
    $ renpy.pause(3,hard=True)
    $ renpy.notify("Current Balance: $[inventory.money]")
    $ renpy.pause(3,hard=True)
    show pov bored_talk at left
    show sis neutral at right
    pov "Alright. $50, for you. When can you pay me back?"
    show pov bored at left
    show sis neutral_talk at right
    sis "I get paid at the end of the week."
    show pov neutral at left
    sis "I'll make sure you get it." ## PAY MC BACK
    show pov neutral_talk at left
    show sis neutral at right
    pov "I trust you."
    show pov smirk at left
    show sis embarrassed_talk at right
    sis "Lately I've been feeling like there aren't a lot of trustworthy people in the world."
    show pov confused_talk at left
    show sis sad at right
    pov "Why's that?"
    show pov embarrassed at left
    show sis sad_talk at right
    if winc == 0:
        sis "Maybe it's [dadname]. Maybe..."
    else:
        sis "Maybe it's Dad. Maybe..."
    show pov sad_talk at left
    show sis embarrassed at right
    pov "Maybe?"
    show pov embarrassed at left
    show sis sad_talk at right
    sis "Everyone just wants something from everyone else."
    show sis embarrassed_talk at right
    sis "I know I give you a lot of shit - but thanks. I'm going to pay you back anyway. Thanks for having my back."
    show pov neutral_talk at left
    show sis embarrassed at right
    pov "Of course. You can always trust me, okay?"
    if sister_points >= 4:
        show pov neutral at left
        show sis embarrassed_talk at right
        sis "Thanks."
    else:
        show pov neutral at left
        show sis neutral_talk at right
        sis "I know."
        sis "I do."

    jump lbl_seen_her_somewhere

label lbl_for_my_phone_bill_4:
    if sister_points <= 8:
        $ sister_points += 2
        $ renpy.notify("Your relationship with [sister] has increased by 2")#\nCurrent Balance: $[inventory.money]
    else:
        $ sister_points = 10

    $ inventory.money -= 50
    $ renpy.pause(3,hard=True)
    $ renpy.notify("Current Balance: $[inventory.money]")
    $ renpy.pause(3,hard=True)
    show pov neutral_talk at left
    show sis embarrassed at right
    pov "Here's $50. Don't worry about paying me back."
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "Really?"
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "Yeah. You're the one loaded up with bills."
    show pov smirk_talk at left
    pov "I'd hate to see you regress just when you're starting out adulting."
    show pov smirk at left
    show sis smirk_talk at right
    sis "Ha, ha. Very funny."
    show pov smirk_talk at left
    show sis neutral at right
    pov "Now will you tell me where you work?"
    show pov bored at left
    show sis neutral_talk at right
    sis "Nope!"
    show pov bored_talk at left
    show sis neutral at right
    pov "Damn, I should have asked that first."
    show pov neutral at left
    show sis neutral_talk at right
    sis "Yes. But it's too late. Love you, [povname]."

    jump lbl_seen_her_somewhere

label lbl_for_my_phone_bill_5:
    show pov sad_talk at left
    show sis bored at right
    pov "Sorry, but I'm pretty broke."
    show pov embarrassed_talk at left
    if winc == 0:
        pov "Why don't you try asking [missus]?"
    else:
        pov "Why don't you try asking Mom?"
    show pov embarrassed at left
    show sis bored_talk at right
    sis "Oh. Fine."
    sis "I didn't want to have to ask more of her, but I can't just go on without a cellphone."

    menu:
        "Just kidding! Here." if inventory.money >= 50:
            show pov smirk_talk at left
            show sis bored at right
            pov "Just kidding! Here."
            $ inventory.money -= 50
            if skill_cha >= 2 and sister_points >= 3:
                if sister_points <= 9:
                    $ sister_points += 1
                    $ renpy.notify("Your relationship with [sister] has increased")
                else:
                    $ sister_points = 10
                $ formyphonebill_owe = 1
                $ renpy.pause(3,hard=True)
                $ renpy.notify("Current Balance: $[inventory.money]")
                show pov neutral at left
                show sis neutral_talk at right
                sis "You fuckin' asshole, haha!"
                sis "Thank you desu!"
                sis "I'll pay you back when I can."
                show sis smirk_talk at right
                sis "See ya, little me."
                show pov neutral_talk at left
            else:
                $ formyphonebill_owe = 1
                $ renpy.notify("Current Balance: $[inventory.money]")
                show pov embarrassed at left
                show sis bored_talk at right
                sis "Thanks. I guess."
                show pov embarrassed at left
                show sis embarrassed_talk at right
                sis "Anyway, I'll pay you back soon."
                sis "See ya, [povname]."
                show pov embarrassed_talk at left
            show sis neutral at right
            pov "Alright. Take care of yourself."
        "She'll understand.":
            if sister_points >= 1:
                $ sister_points -= 1
                $ renpy.notify("Your relationship with [sister] has decreased")
            else:
                $ sister_points = 0
            show pov embarrassed_talk at left
            show sis sad at right
            pov "She'll understand."
            show pov sad at left
            show sis sad_talk at right
            sis "That doesn't mean that she doesn't need the strain."
            show pov sad at left
            show sis confused_talk at right
            sis "Sometimes I think you just want to put everything on her."
            sis "I know that you've always been close, but..."
            show pov confused_talk at left
            show sis bored at right
            pov "But?"
            show pov bored at left
            show sis bored_talk at right
            sis "You're going to have to leave the nest one day and survive without her."
            show pov bored_talk at left
            show sis bored at right
            pov "How does this have anything to do with what we're talking about?"
            show pov angry_talk at left
            pov "You're still living at home and needing help to pay {i}your{/i} bills."
            show pov bored at left
            show sis bored_talk at right
            sis "My point is that you better be ready to take care of yourself one day."
            show sis confused_talk at right
            if winc == 0:
                sis "[dadname] might be 'nice' now, but he'll pull the rug out from under you too if you're not careful."
            else:
                sis "Dad might be 'nice' now, but he'll pull the rug out from under you too if you're not careful."
            show pov bored_talk at left
            show sis bored at right
            pov "...Whatever."
            show pov bored at left
            hide sis bored
            $ renpy.pause()

    jump lbl_seen_her_somewhere
