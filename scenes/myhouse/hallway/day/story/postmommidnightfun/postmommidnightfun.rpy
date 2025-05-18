## Post Mom Midnight Fun ##
label lbl_post_mom_midnight_fun:

    scene bg myhallway_day
    with fade
    show pov smirk at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Good morning, honey. How was your sleep?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was..."

    menu:
        "Good.":
            pov "Good. Had a... strange... but nice dream."
            show pov neutral at left
            show mum neutral_talk at right
            mum "Naww, that's great to hear."
            show mum confused_talk at right
            mum "I had a little hard time sleeping last night but y'know-"
            show pov smirk at left
            show mum neutral_talk at right
            mum "After a midnight snack, I was out like a rock."
            show pov smirk_talk at left
            show mum neutral at right
            pov "Midnight snack, aye?"
            show pov embarrassed at left
            show mum neutral_talk at right
            mum "Yeah, nothing too big."
            show mum neutral at right
            pov "..."
            if mum_points >= 9:
                show pov neutral at left
                show mum smirk_talk at right
                mum "I'm totally messing with you, honey. You're the biggest I've ever had."
                show pov smirk at left
                mum "Definitely the thickest."
                show pov smirk_talk at left
                show mum smirk at right
                pov "I guess it- wasn't a dream then."
            else:
                jump lbl_post_mom_midnight_fun_fail
        "Amazing.":
            show pov smirk_talk at left
            pov "It was. Amazing."
            show pov smirk at left
            show mum neutral_talk at right
            mum "Really? Gosh, you're a lucky one, aren't you?"
            show pov confused at left
            show mum bored_talk at right
            mum "All the sleeps I ever get is just ‘good'. Never mindblowing."
            show pov smirk_talk at left
            show mum neutral at right
            pov "Oh, it definitely was mind-'blowing'."
            show pov smirk_talk at left
            show mum bored at right
            pov "Ehh?! Am I right?"
            show pov embarrassed at left
            show mum confused at right
            mum "..."
            show mum confused_talk at right
            mum "Do you have a fever or something, honey?"
            show pov embarrassed_talk at left
            show mum neutral at right
            pov "I'm alright, Mom."
            if mum_points >= 10:
                show pov neutral at left
                show mum smirk_talk at right
                mum "I'm totally messing with you, honey. Last night was definitely amazing."
                show pov smirk at left
                show mum confused_talk at right
                mum "You really shot out a big load."
                show pov smirk_talk at left
                show mum embarrassed at right
                pov "A big load to show you how much I love you."
                show pov smirk at left
                show mum embarrassed_talk at right
                mum "That's the sweetest thing anyone has ever said to me."
                show pov bored at left
                show mum neutral_talk at right
                mum "Not really."
            else:
                jump lbl_post_mom_midnight_fun_fail
        "So hot.":
            show pov smirk_talk at left
            show mum confused at right
            pov "So hot."
            pov "Last night, was soo hot, Mom."
            show pov confused at left
            show mum confused_talk at right
            mum "Really? I thought it was pretty cool, a gentle breeze coming from outside."
            show pov embarrassed_talk at left
            show mum confused at right
            pov "I meant-"
            show pov bored_talk at left
            pov "Uh nevermind."
            show pov embarrassed at left
            show mum smirk_talk at right
            mum "Maybe you shouldn't sleep with the blankets over you, honey."
            show pov embarrassed_talk at left
            show mum neutral at right
            pov "Ah."
            if mum_points >= 10:
                show pov neutral at left
                show mum smirk_talk at right
                mum "I'm totally messing with you, honey. I know what you meant."
                show pov embarrassed at left
                show mum smirk_talk at right
                mum "Besides, when I came in the room, you were already out in the open for me."
                show pov embarrassed_talk at left
                show mum smirk at right
                pov "That wasn't planned."
                show pov smirk at left
                show mum smirk_talk at right
                mum "Which was even better."
            else:
                jump lbl_post_mom_midnight_fun_fail
    show pov smirk at left
    show mum embarrassed_talk at right
    mum "Anyway, I just wanted to give you a little treat as thank you for what you did to and for me."
    show mum smirk_talk at right
    mum "I would like to feel your lips on my lips again sometime."
    show pov smirk_talk at left
    show mum smirk at right
    if winc == 0:
        pov "Anytime, [missus]. I'll be more than happy to treat you right."
        show pov neutral at left
        show mum neutral_talk at right
        mum "I love you."
        show pov neutral_talk at left
        show mum neutral at right
        pov "I love you too, [missus]."
    else:
        pov "Anytime, Mom. I'll be more than happy to treat you right."
        show pov neutral at left
        show mum neutral_talk at right
        mum "I love you."
        show pov neutral_talk at left
        show mum neutral at right
        pov "I love you too, Mom."
        
    $ townmap_enabled = 1
    $ mum_path = 25

    jump lbl_myhallway_day_setup

label lbl_post_mom_midnight_fun_fail:
    show pov neutral at left
    show mum neutral_talk at right
    mum "Anyways, take care today, alright?"
    show pov neutral at left
    show mum neutral_talk at right
    mum "Don't stay up too late."
    show pov neutral_talk at left
    show mum neutral at right
    pov "I-I won't."
    show pov neutral at left
    show mum neutral_talk at right
    mum "You feeling okay?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "Nev-ver better."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Uh-huh..."

    $ townmap_enabled = 1
    $ mum_path = 25

    jump lbl_myhallway_day_setup
