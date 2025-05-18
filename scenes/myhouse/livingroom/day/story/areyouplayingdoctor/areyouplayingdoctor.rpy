## Are you Playing Doctor ##
label lbl_are_you_playing_doctor:
    default areyouplayingdoctor_boxfort = 0
    if winc == 0:
        jump lbl_are_you_playing_doctor_winc0
    $ townmap_enabled = 1

    scene bg mylivingroom_day
    with fade
    show pov embarrassed at left
    with dissolve
    show mum confused_talk at right
    with dissolve
    mum "Where were you two?"
    mum "I called you down for breakfast ages ago."
    mum "Were you two in the basement?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "Haha.. yeah."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "...Why?"
    show pov shocked at left
    if mum_path >= 6:
        show mum sad_talk at right
    else:
        show mum smirk_talk at right
    mum "You two weren't playing doctor were you?"

    menu:
        "Mooom..!":
            show pov sad_talk at left
            show mum smirk at right
            pov "Mooom!"
            show pov bored at left
            show mum smirk_talk at right
            mum "What? I'm just teasing you."
            mum "It's not like you two are actually playing doctor."
        "What? No!":
            show pov angry_talk at left
            show mum confused at right
            pov "What? No!"
            show pov angry at left
            show mum confused_talk at right
            mum "Okay, okay. You don't have to get so defensive."
            show pov bored at left
            show mum smirk_talk at right
            mum "Someone must've woken up on the wrong side of the basement."
        "We were building a box fort.":
            $ areyouplayingdoctor_boxfort = 1
            show pov embarrassed_talk at left
            show mum confused at right
            pov "We fell asleep building a box fort."
            show pov embarrassed at left
            show mum smirk_talk at right
            mum "You built a boxfort? Downstairs. I might have to go and have a look at that later."
            show pov bored_talk at left
            show mum confused at right
            pov "Yeah, we were exhausted."
            show pov shocked at left
            show mum confused_talk at right
            mum "From.. the boxfort building, right?"
            show pov bored_talk at left
            show mum smirk at right
            pov "Of course, Mom."
            show pov bored at left
            show mum smirk_talk at right
            mum "Just clarifying. It's not like you two built a cardboard hospital or anything..."
    show pov angry at left
    show mum confused_talk at right
    mum "You do know what playing doctor means right?"
    show pov confused_talk at left
    show mum confused at right
    pov "God, Mom. What's up with your mind this morning."
    show pov bored_talk at left
    pov "Of course I know what that means."
    show pov shocked at left
    show mum embarrassed_talk at right
    mum "I'm just checking. The last time your father and I caught you two playing was-"
    show pov sad_talk at left
    show mum smirk at right
    pov "We were like 7 or something."
    show pov shocked at left
    show mum confused_talk at right
    mum "You were giving [sister] CPR."
    show mum smirk_talk at right
    mum "To her chest, if I recalled correctly."
    mum "You were supposed to pump her chest with your hands, and blow into her mouth, not her nip-"
    show pov bored_talk at left
    pov "I'm... gonna go before you embarrass me anymore."
    show pov bored at left
    show mum neutral_talk at right
    mum "Hahaha, c'mon. From a parent's point of view, that was hilarious."
    show mum embarrassed_talk at right
    mum "Hahaha, y-you were so small, and- and clueless, and- and..."
    show pov bored_talk at left
    show mum neutral at right
    pov "I'm not listening!"
    show pov bored at left
    show mum neutral_talk at right
    mum "Hehehe, anyway, get ready for university, honey. You're running late, like your sister."
    $ sister_path = 13

    jump lbl_mylivingroom_day_setup

### NO WINC ###
label lbl_are_you_playing_doctor_winc0:
    $ townmap_enabled = 1

    scene bg mylivingroom_day
    with fade
    show pov embarrassed at left
    with dissolve
    show mum confused_talk at right
    with dissolve
    mum "Where were you two?"
    mum "I called you down for breakfast ages ago."
    mum "Were you two in the basement?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "Haha.. yeah."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "...Why?"
    show pov shocked at left
    if mum_path >= 6:
        show mum sad_talk at right
    else:
        show mum smirk_talk at right
    mum "You two weren't playing doctor were you?"

    menu:
        "[missus]..!":
            show pov sad_talk at left
            show mum smirk at right
            pov "[missus]!"
            show pov bored at left
            show mum smirk_talk at right
            mum "What? I'm just teasing you."
            mum "It's not like you two are actually playing doctor."
        "What? No!":
            show pov angry_talk at left
            show mum confused at right
            pov "What? No!"
            show pov angry at left
            show mum confused_talk at right
            mum "Okay, okay. You don't have to get so defensive."
            show pov bored at left
            show mum smirk_talk at right
            mum "Someone must've woken up on the wrong side of the basement."
        "We were building a box fort.":
            $ areyouplayingdoctor_boxfort = 1
            show pov embarrassed_talk at left
            show mum confused at right
            pov "We fell asleep building a box fort."
            show pov embarrassed at left
            show mum smirk_talk at right
            mum "You built a boxfort? Downstairs. I might have to go and have a look at that later."
            show pov bored_talk at left
            show mum confused at right
            pov "Yeah, we were exhausted."
            show pov shocked at left
            show mum confused_talk at right
            mum "From.. the boxfort building, right?"
            show pov bored_talk at left
            show mum smirk at right
            pov "Of course, [missus]."
            show pov bored at left
            show mum smirk_talk at right
            mum "Just clarifying. It's not like you two built a cardboard hospital or anything..."
    show pov angry at left
    show mum confused_talk at right
    mum "You do know what playing doctor means right?"
    show pov confused_talk at left
    show mum confused at right
    pov "God, [missus]. What's up with your mind this morning."
    show pov bored_talk at left
    pov "Of course I know what that means."
    show pov shocked at left
    show mum embarrassed_talk at right
    mum "I'm just checking. The last time your [povdadrole] and I caught you two playing was-"
    show pov sad_talk at left
    show mum smirk at right
    pov "We were like 7 or something."
    show pov shocked at left
    show mum confused_talk at right
    mum "You were giving [sister] CPR."
    show mum smirk_talk at right
    mum "To her chest, if I recalled correctly."
    mum "You were supposed to pump her chest with your hands, and blow into her mouth, not her nip-"
    show pov bored_talk at left
    pov "I'm... gonna go before you embarrass me anymore."
    show pov bored at left
    show mum neutral_talk at right
    mum "Hahaha, c'mon. From a [povmumrole]'s point of view, that was hilarious."
    show mum embarrassed_talk at right
    mum "Hahaha, y-you were so small, and- and clueless, and- and..."
    show pov bored_talk at left
    show mum neutral at right
    pov "I'm not listening!"
    show pov bored at left
    show mum neutral_talk at right
    mum "Hehehe, anyway, get ready for university, honey. You're running late, like your [povsisrole]."
    $ sister_path = 13

    jump lbl_mylivingroom_day_setup
