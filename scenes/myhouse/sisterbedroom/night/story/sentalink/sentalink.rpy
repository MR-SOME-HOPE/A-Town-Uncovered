## Sent a Link ##
label lbl_sent_a_link:

    scene bg sentalink_1
    with fade
    sis "Yes, [povname]? Do you need something?"
    show bg sentalink_2
    pov "I wanted to talk about something."
    show bg sentalink_3
    sis "And that is...? I'm busy."

    menu:
        "Ask about her live cam feed text":
            show bg sentalink_5
            pov "You sent me a text message to your live cam feed."
            show bg sentalink_6
            sis "‘My' cam feed?"
            show bg sentalink_7
            pov "Yes. As in a website that where you strip for cash."
            show bg sentalink_1
            sis "You seriously think that I'd do that?"
            show bg sentalink_2
            pov "Yeah, maybe."

            menu:
                "There's nothing wrong with it.":
                    if sister_points <= 9:
                        $ sister_points += 1
                        $ renpy.notify("Your relationship with [sister] has increased")
                    else:
                        $ sister_points = 10
                    pov "There's nothing wrong with it."
                    show bg sentalink_8
                    sis "That doesn't mean I'd do it."
                    show bg sentalink_9
                    pov "So it wasn't you?"
                    show bg sentalink_1
                    sis "You're sounding like a broken record."
                    show bg sentalink_9
                    pov "I just want a straight answer."
                    show bg sentalink_10
                    sis "And I just want to be left in peace."
                    show bg sentalink_9
                    pov "Don't be offended, but it sort of makes sense."
                    show bg sentalink_5
                    pov "You're old enough and certainly attractive enough."
                    show bg sentalink_6
                    sis "I'm not offended, but I still don't want to talk about it."
                    show bg sentalink_9
                    pov "Fine. Then what are you doing for work?"
                    show bg sentalink_10
                    sis "[povname], time for you to go."
                "Is that how you're making money?":
                    show bg sentalink_5
                    pov "Is that how you're making your rent money?"
                    show bg sentalink_8
                    sis "I'm not a cam girl."
                    show bg sentalink_9
                    pov "Then where are you working? You're practically gone all the time."
                    show bg sentalink_10
                    if winc == 0:
                        sis "I told you. I have to pay rent. I can't just sit around. [dadname] will make you pay rent if you don't go to college."
                    else:
                        sis "I told you. I have to pay rent. I can't just sit around. Dad will make you pay rent if you don't go to college."
                    show bg sentalink_3
                    sis "Not that that's going to be a problem."
                    if winc == 0:
                        sis "You'll continue on being the golden boy. I'll be the problem [povdadrole] with or without stripping in front of cameras."
                    else:
                        sis "You'll continue on being the golden boy. I'll be the problem child with or without stripping in front of cameras."
                    show bg sentalink_2
                    if winc == 0:
                        pov "You're not a problem [povdadrole]."
                    else:
                        pov "You're not a problem child."
                    show bg sentalink_1
                    sis "Compared to you I am."
                    show bg sentalink_4
                    pov "We're just different. There's nothing wrong with that."
                    show bg sentalink_3
                    if winc == 0:
                        sis "[dadname] thinks there is."
                    else:
                        sis "Dad thinks there is."
                    show bg sentalink_2
                    if winc == 0:
                        pov "[missus] knows better. And you and I both know her opinion is the one that really matters."
                    else:
                        pov "Mom knows better. And you and I both know her opinion is the one that really matters."
                    show bg sentalink_3
                    sis "Yeah..."
                    if winc == 0:
                        sis "Unfortunately, [dadname] is the leader of this clan we have going on."
                    else:
                        sis "Unfortunately, Dad is the leader of this clan we have going on."
                    show bg sentalink_4
                    pov "..."
                    show bg sentalink_5
                    if main_story >= 22:
                        if sister_points <= 8:
                            $ sister_points += 2
                            $ renpy.notify("Your relationship with [sister] has increased by 2")
                        else:
                            $ sister_points = 10
                        pov "Since I have a job I can help you out some."
                    else:
                        if sister_points <= 9:
                            $ sister_points += 1
                            $ renpy.notify("Your relationship with [sister] has increased")
                        else:
                            $ sister_points = 10
                        pov "I can help you out once I get a job."
                    show bg sentalink_11
                    sis "No, I'll be fine."
                    show bg sentalink_12
                    pov "You'll have to have some free time at some point. I could introduce you to my friends."
                    show bg sentalink_13
                    sis "Maybe."
                    show bg sentalink_12
                    pov "..."
                "That's really slutty.":
                    if sister_points >= 1:
                        $ sister_points -= 1
                    else:
                        $ sister_points = 0
                    $ renpy.notify("Your relationship with [sister] has decreased")
                    show bg sentalink_5
                    pov "That's really slutty, even for you."
                    show bg sentalink_8
                    sis "Good thing the link wasn't to anything I was doing."
                    show bg sentalink_5
                    pov "So who was it?"
                    show bg sentalink_6
                    sis "A friend of mine from back home. I was helping spread the word."
                    show bg sentalink_7
                    pov "Then why did she delete it?"
                    show bg sentalink_6
                    sis "She didn't want you to see her."
                    show bg sentalink_5
                    pov "You know I don't believe you, right?"
                    show bg sentalink_8
                    sis "And you know I don't care, right?"
                    show bg sentalink_9
                    pov "Then where are you working? You keep making it into this huge secret. It's gotta be something you're ashamed of."
                    show bg sentalink_8
                    sis "It's not your business."
                    show bg sentalink_9
                    pov "You're being so weird about it."
                    show bg sentalink_10
                    sis "Listen, I told you I was busy when you came barging in here. All you're doing is irritating me."
                    if winc == 0:
                        sis "If you don't get out now I'm going to make sure [missus] finds out that you're harassing me."
                    else:
                        sis "If you don't get out now I'm going to make sure Mom finds out that you're harassing me."
                    show bg sentalink_9
                    if winc == 0:
                        pov "Leave [missus] out of it."
                    else:
                        pov "Leave Mom out of it."
                    show bg sentalink_10
                    sis "Whatever."
                    show bg sentalink_14
                    pov "..."

            jump lbl_sent_a_link_2
        "Ask about a weird link she sent":
            show bg sentalink_6
            pov "You sent me a weird link..."
            show bg sentalink_15
            sis "Huh?"
            show bg sentalink_9
            pov "Are you going to play coy about it?"
            show bg sentalink_10
            sis "No, I'm going to ‘play' clueless about it because I have no idea what you're talking about."

            menu:
                "Nevermind.":
                    show bg sentalink_1
                    pov "Nevermind, you must've meant to send it to someone else."
                    show bg sentalink_3
                    sis "I still don't know what you're talking about, and I honestly don't care. I'm busy. I told you."
                    show bg sentalink_4
                    pov "You know... I'd sort of hoped that we might get closer again once we moved here."

                    jump lbl_sent_a_link_2
                "I guess I'll just go.":
                    show bg sentalink_7
                    pov "I guess I'll just go then."
                    show bg sentalink_16
                    sis "..."
                "I was wondering about your rent.":
                    jump lbl_sent_a_link_3
                "You're sure you can't remember?":
                    show bg sentalink_2
                    pov "You're sure you can't remember?"
                    show bg sentalink_1
                    sis "Are you calling me a liar?"
                    show bg sentalink_2
                    pov "You keep answering questions with questions."
                    show bg sentalink_1
                    sis "And you didn't answer mine."
                    show bg sentalink_3
                    if winc == 0:
                        sis "Go. Or I'll call [missus]... Or maybe [dadname] instead."
                    else:
                        sis "Go. Or I'll call Mom... Or maybe Dad instead."
                    show bg sentalink_4
                    pov "Fine. Goodnight to you too, [sister]."
            $ sister_path = 3

            jump lbl_myhallway_night_setup
        "I was wondering about your rent.":
            jump lbl_sent_a_link_3

label lbl_sent_a_link_2:
    show bg sentalink_16
    pov "Do you remember that we used to be best friends?"
    pov "We were young, sure. But we did everything together."
    show bg sentalink_17
    sis "..."
    show bg sentalink_18
    if winc == 0:
        sis "You were always clinging to me or [missus], saying you were going to marry one of us."
    else:
        sis "You were always clinging to me or Mom, saying you were going to marry one of us."

    menu:
        "I was going to marry [missus]." if winc == 0:
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
        "I was going to marry Mom." if winc == 1:
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ renpy.notify("Your relationship with Mom has increased")
            show bg sentalink_19
            if winc == 0:
                pov "I think I said I was going to marry Mom."
            else:
                pov "I think I said I was going to marry Mom."
            show bg sentalink_20
            sis "Sounds like you. Anyway, you're not going to endear yourself to me by sticking around."
            show bg sentalink_1
            sis "Shoo, bitch."
        "I was going to marry you.":
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Your relationship with [sister] has increased")
            else:
                $ sister_points = 10
            show bg sentalink_19
            pov "I think I said I was going to marry you."
            show bg sentalink_18
            if winc == 0:
                sis "[dadname] cleared that up for us when he saw us kissing."
            else:
                sis "Dad cleared that up for us when he saw us kissing."
            sis "We were only six. But I think it freaked him out."
            show bg sentalink_15
            pov "But we stayed close even after that. So how did we get here?"
            show bg sentalink_11
            sis "I told you--I'm busy. And I'm tired. I don't want some bullshit heart to heart right now."
            show bg sentalink_12
            sis "..."
            show bg sentalink_13
            sis "I'll talk to you later."
    $ sister_path = 3

    jump lbl_myhallway_night_setup

label lbl_sent_a_link_3:
    show bg sentalink_5
    if winc == 0:
        pov "I was wondering about your rent. Our [dadrole]s are really making you pay?"
    else:
        pov "I was wondering about your rent. Our parents are really making you pay?"
    sis "..."
    show bg sentalink_1
    sis "...Yeah."
    show bg sentalink_3
    if winc == 0:
        sis "It's [dadname]. [missus] told him not to even ask for it. She says that if they're not charging you rent that they shouldn't charge me."
    else:
        sis "It's Dad. Mom told him not to even ask for it. She says that if they're not charging you rent that they shouldn't charge me."
    show bg sentalink_4
    if winc == 0:
        pov "So why does [dadname] think you should?"
    else:
        pov "So why does Dad think you should?"
    show bg sentalink_3
    sis "He's still angry I didn't go to uni."
    show bg sentalink_4
    pov "Ahh. Do you regret it at all?"
    show bg sentalink_6
    sis "No. I was done. Further studies just isn't for me."
    show bg sentalink_22
    pov "I understand that."
    show bg sentalink_15
    sis "Do you? You're always the golden boy; always getting fantastic scores."
    show bg sentalink_11
    sis "I know you're not going to have a problem getting whatever career you want."
    show bg sentalink_21
    if winc == 0:
        pov "Look, we might be [sisrole]s but that doesn't mean we don't have different paths to take."
        pov "[dadname] is stupid if he thinks we have to do the same thing."
    else:
        pov "Look, we might be twins but that doesn't mean we don't have different paths to take."
        pov "Dad is stupid if he thinks we have to do the same thing."
    pov "Don't worry about him, okay?"
    show bg sentalink_12
    sis "..."
    show bg sentalink_13
    sis "Of course not."
    show bg sentalink_12
    pov "Good."
    show bg sentalink_1
    sis "But I have work tomorrow. You should go."
    show bg sentalink_22
    pov "Alright. Sweet dreams."
    $ sister_path = 3

    jump lbl_myhallway_night_setup
