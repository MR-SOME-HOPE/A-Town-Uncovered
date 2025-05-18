## Seen Her Somewhere ##
label lbl_seen_her_somewhere:
    #default seenhersomewhere_trytoreveal = 0
    #default seenhersomewhere_givedetails = 0

    scene bg schoolyard_day
    show pov neutral at left
    show jac neutral_talk at right
    with fade
    jac "Hey, [povname]!"
    show pov neutral_talk at left
    show jac smirk at right
    pov "Oh, hey Jacob. What's up?"
    show pov confused at left
    show jac smirk_talk at right
    jac "Man, that girl is gorgeous. How'd you get such a cute girlfriend?"
    show pov confused_talk at left
    show jac smirk at right
    pov "Huh?"
    show pov confused at left
    show jac smirk_talk at right
    jac "You've only just moved here and you've already got a hottie. You've got to give me some tips, man."
    show pov embarrassed_talk at left
    show jac smirk at right
    pov "Listen, it's not--"
    show pov bored at left
    show jac smirk_talk at right
    jac "You've seen the guys I hang out with. They're all cool, but they have no idea how to get anywhere with the ladies."
    show pov confused_talk at left
    show jac smirk at right
    pov "Wait, you're--"
    show pov bored at left
    show jac shocked_talk at right
    jac "Desperate? Damn right."
    show jac smirk_talk at right
    jac "Seriously, though. Don't be offended but I want to get on my knees and bury my face in that girl's pussy."
    show jac smirk at right
    pov "..."
    show pov bored_talk at left
    show jac confused at right
    pov "Dude."
    show pov bored at left
    show jac smirk_talk at right
    jac "Alright, alright. I know. It's not cool to talk about another guy's girlfriend like that."

    menu:
        "She's not my girlfriend. She's my [sisrole]." if winc == 0:
            $ seenhersomewhere_telljacob = 1
            show pov embarrassed_talk at left
            show jac confused at right
            pov "No, no. She's not my-"
            show pov bored at left
            show jac confused_talk at right
            jac "I know I've seen her somewhere..."
            jac "Not from uni."
            jac "Where did you meet her..?"
            show jac confused at right
            pov "..."
            show pov confused at left
            show jac smirk_talk at right
            jac "Oh! Comic book store? I swear I've seen her there."
            show jac confused_talk at right
            jac "Did Hitomi fix you guys up?"
            show pov bored at left
            show jac smirk_talk at right
            jac "I wish she'd fixed me up with her. But, hey, I guess this means Hitomi is still free for me."

            menu:
                "I don't think she's interested.":
                    show pov bored_talk at left
                    show jac neutral at right
                    pov "I don't think she's interested..."
                "Good luck and godspeed.":
                    show pov embarrassed_talk at left
                    show jac neutral at right
                    pov "Good luck and godspeed, man."
            show pov bored at left
            show jac neutral_talk at right
            jac "Gonna go see Hitomi and try my best. Laters, bro!"
            show pov neutral_talk at left
            hide jac neutral_talk at right
            pov "Laa-aaand- he's gone."
        "She's not my girlfriend. She's my sister." if winc == 1:
            $ seenhersomewhere_telljacob = 1
            show pov embarrassed_talk at left
            show jac confused at right
            pov "No, no. She's not my-"
            show pov bored at left
            show jac confused_talk at right
            jac "I know I've seen her somewhere..."
            jac "Not from uni."
            jac "Where did you meet her..?"
            show jac confused at right
            pov "..."
            show pov confused at left
            show jac smirk_talk at right
            jac "Oh! Comic book store? I swear I've seen her there."
            show jac confused_talk at right
            jac "Did Hitomi fix you guys up?"
            show pov bored at left
            show jac smirk_talk at right
            jac "I wish she'd fixed me up with her. But, hey, I guess this means Hitomi is still free for me."

            menu:
                "I don't think she's interested.":
                    show pov bored_talk at left
                    show jac neutral at right
                    pov "I don't think she's interested..."
                "Good luck and godspeed.":
                    show pov embarrassed_talk at left
                    show jac neutral at right
                    pov "Good luck and godspeed, man."
            show pov bored at left
            show jac neutral_talk at right
            jac "Gonna go see Hitomi and try my best. Laters bro!"
            show pov neutral_talk at left
            hide jac neutral_talk at right
            pov "Laa-aaand- he's gone."
        "Yeah, right?":
            show pov embarrassed_talk at left
            show jac smirk at right
            pov "...Yeah, right?"
            pov "I can't deny that she's gorgeous."
            show pov embarrassed at left
            show jac smirk_talk at right
            jac "Good in the sack?"
            show pov confused_talk at left
            show jac smirk at right
            pov "Oh, yeah."
            show pov bored at left
            show jac smirk_talk at right
            jac "I bet she's a screamer."
            show pov bored_talk at left
            show jac smirk at right
            pov "...Um, yep."
            show pov bored at left
            show jac sad_talk at right
            jac "Damn. How did you get so lucky?"
            show pov confused at left
            show jac confused_talk at right
            jac "Wait, I think I've seen her... At the comic book store?"
            jac "Is she friends with Hitomi?"
            show pov confused_talk at left
            show jac confused at right
            pov "Um, not-"
            show pov bored at left
            show jac confused_talk at right
            jac "I bet Hitomi fixed you guys up. Ugh. She should do that for me."
            show jac smirk_talk at right
            jac "Although she's probably just waiting for me to get past that hard-to-get phase she's in."
            show pov bored_talk at left
            show jac smirk at right
            pov "Right. The phase."
            show pov confused at left
            show jac confused_talk at right
            jac "But seriously. I want to know all the details."

            menu:
                "A gentleman never tells.":
                    if jacob_points <= 9:
                        $ jacob_points += 1
                    else:
                        $ jacob_points = 10
                    $ renpy.notify("Your relationship with Jacob has increased")
                    show pov smirk_talk at left
                    show jac smirk at right
                    pov "A gentleman never tells."
                    show pov embarrassed at left
                    show jac smirk_talk at right
                    jac "Then I've got some corrupting to do."
                "We'll talk about it sometime.":
                    #$ seenhersomewhere_givedetails = 0
                    show pov embarrassed_talk at left
                    show jac smirk at right
                    pov "For sure. We'll talk about it sometime."
            show pov embarrassed at left
            show jac smirk_talk at right
            jac "I'm going to go find Hitomi. Maybe I can convince her to let me bury my face in her pussy."
            show jac confused_talk at right
            jac "If not that, maybe she has another sexy friend to fix me up with."
            show jac neutral at right
            pov "..."
            show pov embarrassed_talk at left
            show jac neutral at right
            pov "Good luck."
    $ sister_path = 4

    jump lbl_schoolyard_day_setup
