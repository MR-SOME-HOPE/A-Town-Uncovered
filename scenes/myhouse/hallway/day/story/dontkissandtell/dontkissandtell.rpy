## Don't Kiss and Tell ##
label lbl_dont_kiss_and_tell:

    scene bg myhallway_day
    with fade
    show pov confused at left
    with dissolve
    show sis angry_talk at right
    with dissolve
    sis "Hey, [povname]."
    sis "Did you tell anyone about the that night in the basement?"
    if areyouplayingdoctor_boxfort == 1:
        show pov confused_talk at left
        show sis angry at right
        if winc == 0:
            pov "I told [missus] we were building a box fort..?"
        else:
            pov "I told Mom we were building a box fort..?"
        show pov shocked at left
        show sis angry_talk at right
        sis "What?! No I'm not talking about that, you idiot."
        sis "And what the hell did you tell her that for?"
        show pov confused_talk at left
        show sis angry at right
        pov "You think I was going to lie? It's not something worth hiding from her."
        show pov bored_talk at left
        pov "She's going to find out eventually anyway."
        show pov confused at left
        show sis angry_talk at right
        sis "That's not even what I'm talking about."
        show pov confused_talk at left
        show sis angry at right
        pov "What are you talking about then?"
    else:
        show pov confused_talk at left
        show sis angry at right
        pov "No? Why would I?"
        show pov shocked at left
        show sis angry_talk at right
        sis "You better not tell anyone, I'll kill you if you do."
        show pov shocked_talk at left
        show sis angry at right
        pov "Whoa, don't need to be so aggressive, [sister]."
        show pov confused_talk at left
        pov "It's not something I want to be going around boasting about."
        show pov smirk_talk at left
        pov "‘Oh hey, guys! Guess what I did the other night?'"
        if winc == 0:
            pov "‘My [sisrole] and I built a box fort!'"
        else:
            pov "‘My sister and I built a box fort!'"
        show pov confused at left
        show sis bored_talk at right
        sis "Oh, you know what I mean."
    show pov confused_talk at left
    show sis angry at right
    pov "The conversations we had?"
    if undercardboardstars_cuddle == 1:
        show pov confused at left
        show sis bored_talk at right
        sis "Well, obviously that too, that's meant to be kept between us two."
        show sis sad_talk at right
        sis "I'm talking about-"
        show sis embarrassed_talk at right
        sis "Y'know..."
        show pov embarrassed at left
        sis "When we fell asleep."
        sis "We..."
        sis "I..."
        sis "Yeah..."
        show sis embarrassed at right
        sis "..."
        if undercardboardstars_silent == 1:
            show sis confused_talk at right
            sis "Were you asleep?"

            menu:
                "I fell asleep eventually.":
                    show pov embarrassed_talk at left
                    show sis confused at right
                    pov "Well... I fell asleep eventually."
                    show pov neutral at left
                    show sis confused_talk at right
                    sis "Eventually..?"
                    show sis embarrassed_talk at right
                    sis "Hmm.. alright. Just- making sure."
                "I was awake for a while.":
                    show pov embarrassed_talk at left
                    show sis shocked at right
                    pov "I was awake for a while."
                    show pov embarrassed at left
                    show sis embarrassed_talk at right
                    sis "Oh. Really?"
                    sis "Like how long is ‘a while'?"
                    show pov confused at left
                    sis "Actually, I prefer not to know..."
                "I slept soon after.":
                    show pov neutral_talk at left
                    show sis shocked at right
                    pov "I slept very soon after."
                    show pov neutral at left
                    show sis embarrassed_talk at right
                    sis "Oh, good. Building and talking must've tired us right out."
                    show pov confused at left
                    sis "Hehehe..."
            show pov confused_talk at left
            show sis angry at right
            pov "Why? Did you do something that I should know about?"
            show pov shocked at left
            show sis angry_talk at right
            sis "Oh... no. It's better if you didn't know."
        else:
            show pov embarrassed at left
            show sis embarrassed_talk at right
            sis "You know what I'm talking about..."
            show pov embarrassed_talk at left
            show sis embarrassed at right
            pov "Oh. Don't worry, it's between you and me. I promise."
            show pov smirk_talk at left
            pov "It would embarrass me as well if anyone else knew that you were making out with my nec-"
            show pov neutral at left
            show sis bored_talk at right
            sis "Alright, alright. You don't have to shine a spotlight on it."
            show sis embarrassed_talk at right
            sis "Let's just leave it at that."
    else:
        show pov neutral at left
        show sis embarrassed_talk at right
        sis "Uh yeah... all the topics we covered and things we revealed."
        show pov neutral at left
        sis "Let's keep that between us. No one else needs to know about it."
        show pov embarrassed_talk at left
        show sis embarrassed at right
        pov "No worries. I assumed that was already implied."
        show pov neutral at left
        show sis embarrassed_talk at right
        sis "Good, good. Thanks, [povname]."
    show pov confused at left
    show sis confused_talk at right
    sis "Anyway, just to burn it into your mind."
    sis "That fort, holds our secrets. Got it?"
    show sis bored_talk at right
    if winc == 0:
        sis "[povsisrole] contract; what comes out in the [sisrole] Fortress, stays in the [sisrole] Fortress."
    else:
        sis "Sibling contract; what comes out in the Twin Fortress, stays in the Twin Fortress."
    sis "Say exactly what I said to accept the contract."

    menu:
        "Whatever happens in the Fortress...":
            if sister_points >= 1:
                $ sister_points -= 1
                $ renpy.notify("Your relationship with [sister] has decreased")
            else:
                $ sister_points = 0
            show pov neutral_talk at left
            show sis angry at right
            pov "Whatever happens in the Fortress, stays in the Fortress."
            show pov smirk at left
            show sis angry_talk at right
            sis "You're just making it sound perverted."
            show pov embarrassed at left
            show sis angry_talk at right
            if winc == 0:
                sis "And it's [sisrole] Fortress, you pickle dick."
            else:
                sis "And it's Twin Fortress, you pickle dick."
            show sis bored_talk at right
            sis "Whatever, close enough."
        "Anything that is revealed in the Twin Fortress..." if winc == 1:
            show pov neutral_talk at left
            show sis bored at right
            pov "Anything that is revealed in the Twin Fortress, stays in the Twin Fortress."
            show pov embarrassed at left
            show sis bored_talk at right
            sis "Uh, whatever, close enough."
        "Anything that is revealed in the [sisrole] Fortress..." if winc == 0:
            show pov neutral_talk at left
            show sis bored at right
            pov "Anything that is revealed in the [sisrole] Fortress, stays in the [sisrole] Fortress."
            show pov embarrassed at left
            show sis bored_talk at right
            sis "Uh, whatever, close enough."
        "What comes out in the Twin Fortress..." if winc == 1:
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Your relationship with [sister] has increased")
            else:
                $ sister_points = 10
            show pov neutral_talk at left
            show sis neutral at right
            pov "What comes out in the Twin Fortress, stays in the Twin Fortress."
            show pov neutral at left
            show sis neutral_talk at right
            sis "Great, thanks."
        "What comes out in the Twin Fortress..." if winc == 0:
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Your relationship with [sister] has increased")
            else:
                $ sister_points = 10
            show pov neutral_talk at left
            show sis neutral at right
            pov "What comes out in the [sisrole] Fortress, stays in the [sisrole] Fortress."
            show pov neutral at left
            show sis neutral_talk at right
            sis "Great, thanks."
        "What if I don't accept?":
            show pov confused_talk at left
            show sis angry at right
            pov "What if I don't accept?"
            show pov embarrassed at left
            show sis angry_talk at right
            sis "Then I'm never going to trust you."
            show sis angry at right
            pov "..."
            show pov embarrassed_talk at left
            if winc == 0:
                pov "Fine, whatever comes out in the [sisrole] Fortress, stays in the [sisrole] Fortress."
            else:
                pov "Fine, whatever comes out in the Twin Fortress, stays in the Twin Fortress."
            show pov embarrassed at left
            show sis bored_talk at right
            sis "Good enough."
    show pov embarrassed at left
    show sis bored_talk at right
    if winc == 0:
        sis "I'll talk to you later, [povname]."
    else:
        sis "I'll talk to you later, bro."
    show pov embarrassed_talk at left
    show sis bored at right
    pov "Alright."
    hide sis bored
    show pov confused at left
    pov "..."
    pov "{i}The fortress, our fortress. Is a safe place to share secrets?{/i}"
    pov "{i}Hmm.. if that's the case. I'm sure I can get her to spill some secrets.{/i}"
    show pov embarrassed at left
    pov "{i}Of course for my own benefit...{/i}"
    pov "{i}No reason for me to tell anyone else.{/i}"
    show pov smirk at left
    pov "{i}Yeah... let's do that, [povname].{/i}"
    $ sister_path = 14

    jump lbl_myhallway_day_setup
