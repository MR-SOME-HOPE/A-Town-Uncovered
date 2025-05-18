## Just a Friend ##
label lbl_just_a_friend:

    scene bg myhallway_day
    with fade
    show pov confused at left
    with dissolve
    show sis confused_talk at right
    with dissolve
    sis "Hey, [povname]. So, about that sleepover you and Mom were discussing..."
    show pov confused_talk at left
    show sis confused at right
    pov "...Huh?"
    show pov confused at left
    show sis confused_talk at right
    sis "Was it really just a ‘friend'?"
    show pov confused_talk at left
    show sis confused at right
    pov "What are you talking abo-"
    show pov shocked_talk at left
    pov "Oh, that."
    show pov confused at left
    show sis confused_talk at right
    sis "Yes, that..."
    show pov confused at left
    sis "Did you hook up with her or not?"

    menu:
        "Of course.":
            show pov smirk_talk at left
            show sis neutral at right
            pov "Of course we did."
            pov "You think I would leave without getting some?"
            show pov neutral at left
            show sis neutral_talk at right
            sis "Whoa, props to you bro."
            show pov neutral at left
            show sis confused_talk at right
            sis "I need to get laid myself."
            show pov confused at left
            show sis neutral_talk at right
            sis "So when can I meet her?"

            menu:
                "Why do you want to meet her?":
                    show pov confused_talk at left
                    show sis neutral at right
                    pov "Why do you even want to meet her, it didn't mean anything."
                    show pov bored at left
                    show sis smirk_talk at right
                    if winc == 0:
                        sis "Just in case your amateur little ass gets her pregnant, I want to know who my [povsisrole]'s child's mother is."
                    else:
                        sis "Just in case your amateur little ass gets her pregnant, I want to know who my brother's child's mother is."
                    show pov bored_talk at left
                    show sis smirk at right
                    pov "I won't get her pregnant."
                    show pov bored at left
                    show sis smirk_talk at right
                    sis "Do you have condoms?"
                    show sis smirk at right
                    pov "..."
                    show pov bored_talk at left
                    pov "I.. {i}did{/i} have condoms..."
                "Someday.":
                    show pov confused_talk at left
                    show sis neutral at right
                    pov "Someday, maybe. It's not like I'm going to plan a dinner party."
                    show pov confused at left
                    show sis neutral_talk at right
                    sis "If we ever see her in public, just point her out and I'll punch her in the boob."
                    show pov confused_talk at left
                    show sis smirk at right
                    pov "What? Why would you even do that?"
                    show pov confused at left
                    show sis bored_talk at right
                    sis "Because she's using you for your body."
                    show pov bored at left
                    show sis bored_talk at right
                    sis "Don't let people use you, bro. You're too... clingy. You want things you can't have all to yourself."
                    show pov bored_talk at left
                    show sis neutral at right
                    pov "Thanks..."
                "Never.":
                    show pov neutral_talk at left
                    show sis confused at right
                    pov "Never. Ever ever ever."
                    show pov bored at left
                    show sis smirk_talk at right
                    sis "Why? Is it because you fucked a 3?"
                    show pov bored_talk at left
                    show sis smirk at right
                    pov "Shut up, she's not a 3. I'm not that desperate."
                    show pov smirk at left
                    show sis neutral_talk at right
                    sis "Oh, sorry, a 4."
                    show pov smirk_talk at left
                    show sis smirk at right
                    pov "Be nice."
                    show pov embarrassed at left
                    show sis neutral_talk at right
                    if winc == 0:
                        sis "My [povsisrole] deserves an 11."
                    else:
                        sis "My little brother deserves an 11."
                    show pov bored at left
                    show sis smirk_talk at right
                    sis "I'll make sure of that, they'll need to get past my approval."
        "Almost.":
            show pov embarrassed_talk at left
            show sis confused at right
            pov "Almost."
            show pov embarrassed at left
            show sis confused_talk at right
            sis "Almost?"
            show pov sad at left
            show sis bored_talk at right
            sis "Don't tell me you freaked out at the moment of truth."
            show pov sad_talk at left
            show sis bored at right
            pov "It wasn't like that."
            show pov sad at left
            show sis confused_talk at right
            sis "So, how was it?"
            show pov sad_talk at left
            show sis smirk at right
            pov "...Her dad came home."
            show pov bored at left
            show sis smirk_talk at right
            sis "And your lady love couldn't trust herself to hold back her moans?"
            show pov bored_talk at left
            show sis smirk at right
            pov "She's not my ‘lady love.'"
            show pov bored at left
            show sis smirk_talk at right
            sis "Do you think she just wants you for your body or your charming personality?"

            menu:
                "Both, I hope.":
                    show pov confused_talk at left
                    show sis smirk at right
                    pov "Both, I hope."
                    show pov embarrassed at left
                    show sis smirk_talk at right
                    sis "Aw, don't let her break your heart."
                    show pov embarrassed_talk at left
                    show sis neutral at right
                    pov "It won't be the only muscle that'll hurt."
                "Definitely my body.":
                    show pov confused_talk at left
                    show sis smirk at right
                    pov "Last night she was definitely more focused on my body."
                    show pov neutral at left
                    show sis smirk_talk at right
                    sis "Ha, I bet she was."
                    show pov smirk_talk at left
                    show sis bored at right
                    pov "How can anyone say no to this sex icon."
        "No way.":
            show pov confused_talk at left
            show sis confused at right
            pov "No way."
            show pov confused at left
            show sis bored_talk at right
            sis "I don't believe you."
            show pov bored_talk at left
            show sis confused at right
            pov "You can believe what you want."
            show pov bored at left
            show sis confused_talk at right
            sis "You were alone with a girl and you didn't do {i}anything?{/i}"

            menu:
                "Maybe something.":
                    show pov embarrassed_talk at left
                    show sis smirk at right
                    pov "Maybe something."
                    show pov smirk at left
                    show sis smirk_talk at right
                    sis "Cryptic, aren't you?"
                "Yes, exactly.":
                    show pov bored_talk at left
                    show sis bored at right
                    pov "Yes, exactly. Are you calling me a liar?"
                    show pov bored at left
                    show sis smirk_talk at right
                    sis "Maybe. If not a liar than I'm saying you need to work on your game."
        "Kind of.":
            show pov embarrassed_talk at left
            show sis confused at right
            pov "Kind of."
            show pov bored at left
            show sis bored_talk at right
            sis "That sounds like a let down."
            show sis confused_talk at right
            sis "Maybe even literally?"
            show pov confused_talk at left
            show sis neutral at right
            pov "...That was not the problem. Trust me."
            show pov sad at left
            show sis confused_talk at right
            sis "What was?"
            show pov sad_talk at left
            show sis smirk at right
            pov "Her dad coming home."
            show pov sad at left
            show sis smirk_talk at right
            sis "Ouch."
            show pov sad_talk at left
            show sis neutral at right
            if winc == 0:
                pov "Just imagine if [dadname] came home and found someone in your room. I didn't want that to happen to me."
            else:
                pov "Just imagine if Dad came home and found someone in your room. I didn't want that to happen to me."
            show pov embarrassed at left
            show sis neutral_talk at right
            sis "Yeah, I see what you mean."
            show pov embarrassed_talk at left
            show sis neutral at right
            pov "Yeah... But it's not a problem."
            show pov bored at left
            show sis smirk_talk at right
            sis "Just don't make Mom wash more of those socks, okay? Showers are your friend."
            show pov sad_talk at left
            show sis smirk at right
            pov "...[sister]?"
            show pov bored_talk at left
            pov "Shut up."
    show pov confused at left
    show sis confused at right
    sis "..."
    sis "Hmmm..."
    show pov confused_talk at left
    pov "What?"
    show pov confused at left
    show sis confused_talk at right
    if winc == 0:
        sis "It's funny. We're [sisrole]s, but obviously not identical."
    else:
        sis "It's funny. We're twins, but obviously not identical."
    show sis smirk_talk at right
    sis "I wonder what it would be like to know you look the same naked as another person."
    show pov confused_talk at left
    show sis smirk at right
    pov "Why are you even thinking about that?"
    show pov confused at left
    show sis angry_talk at right
    sis "Because you know what I look like naked and I don't know what you look like."
    show pov embarrassed_talk at left
    show sis smirk at right
    pov "Wait, what are you saying?"
    show pov embarrassed at left
    show sis smirk_talk at right
    sis "Just that you're going to have to pay up some day..."
    show pov embarrassed_talk at left
    show sis smirk at right
    pov "Pay up?"
    show pov shocked at left
    show sis smirk_talk at right
    sis "It's only fair for me to get a good look too, right? Kidding, kidding... Don't look so freaked out."

    menu:
        "Uhh...":
            show pov embarrassed_talk at left
            show sis smirk at right
            pov "Uhh..."
            show pov embarrassed at left
            show sis neutral_talk at right
            sis "I said I was kidding! Anyway, I've got to go."
            show pov confused_talk at left
            show sis bored at right
            pov "You're always leaving."
            show pov confused at left
            show sis bored_talk at right
            sis "Not all of us have the pleasure of getting to just live here. Some of us have to pay rent."
            show pov shocked_talk at left
            show sis bored at right
            pov "You have to pay rent?"
        "That's fair.":
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Your relationship with [sister] has increased")
            else:
                $ sister_points = 10
            show pov smirk_talk at left
            show sis shocked at right
            pov "I guess that's only fair."
            show pov smirk at left
            show sis confused_talk at right
            sis "Not running away in fear?"
            show pov smirk_talk at left
            show sis smirk at right
            pov "You don't scare me."
            show pov embarrassed at left
            show sis smirk_talk at right
            sis "I don't know... I might strike you with voyeurism at any time."
            sis "Keep your eyes peeled... I might be watching you from right around the corner."
            show sis smirk at right
            pov "..."
            show pov confused at left
            show sis bored_talk at right
            sis "Anyway, I'll leave you to trying to come up with ways to defend yourself from me. I've got to head to work."
            show pov confused_talk at left
            show sis bored at right
            pov "Again? You're always at work."
            show pov bored at left
            show sis bored_talk at right
            sis "Some of us have bills to pay."
            show pov confused_talk at left
            show sis bored at right
            if winc == 0:
                pov "Oh yeah, sure. Let me guess, [missus] and [dadname] are making you pay rent?"
            else:
                pov "Oh yeah, sure. Let me guess, Mom and Dad are making you pay rent?"
            show pov confused at left
            show sis bored_talk at right
            if winc == 0:
                sis "[dadname] is."
            else:
                sis "Dad is."
            show pov sad_talk at left
            show sis bored at right
            pov "Seriously?"
        "Not gonna happen.":
            if sister_points >= 1:
                $ sister_points -= 1
                $ renpy.notify("Your relationship with [sister] has decreased")
            else:
                $ sister_points = 0
            show pov bored_talk at left
            show sis sad at right
            pov "Not gonna happen."
            show pov confused at left
            show sis bored_talk at right
            sis "Always with the double standards..."
            sis "Good luck with your eager little girlfriend. I'm heading to work."
            show pov confused_talk at left
            show sis bored at right
            pov "Do you ever {i}not{/i} work?"
            show pov confused at left
            show sis bored_talk at right
            sis "Maybe I'll stop working once I don't have bills to pay."
            show pov confused_talk at left
            show sis bored at right
            pov "It's not like you're having to pay rent or anything."
            show pov confused at left
            show sis bored at right
            sis "..."
            show pov shocked_talk at left
            pov "You're paying rent? Why?"
    show pov sad at left
    show sis bored_talk at right
    sis "I really don't feel like talking about it."
    show pov embarrassed at left
    show sis embarrassed_talk at right
    sis "I'll just see ya later."
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "... Alright. See ya."
    $ sister_path = 1
    $ townmap_enabled = 1
    jump lbl_myhallway_day_setup
