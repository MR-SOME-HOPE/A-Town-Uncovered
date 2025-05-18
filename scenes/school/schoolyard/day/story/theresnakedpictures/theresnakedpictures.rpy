## There's Naked Pictures ##
label lbl_theres_naked_pictures:

    scene bg schoolyarddoor_day
    with fade
    show pov sad at left
    with dissolve
    show eff embarrassed at Position(xpos=1300)
    with dissolve
    show jac confused at right
    with dissolve
    pov "{i}*Inhale*{/i}"
    pov "..."
    show pov sad_talk at left
    pov "{i}*Exhale*{/i}"
    show pov sad at left
    show eff embarrassed_talk at Position(xpos=1300)
    show jac confused at right
    eff "Nervous?"
    show eff embarrassed at Position(xpos=1300)
    show jac confused_talk at right
    jac "Can you blame the guy? His pictures are everywhere!"
    show pov shocked_talk at left
    show eff shocked at Position(xpos=1300)
    show jac shocked at right
    pov "Wait- What?!"
    pov "There are pictures?!"
    show pov shocked at left
    show jac embarrassed_talk at right
    jac "Just a few."
    show jac confused_talk at right
    jac "I think it was one of the “-egans”. One of them found you unconscious and called the police after taking some pictures of you."
    show pov shocked_talk at left
    show eff embarrassed at Position(xpos=1300)
    show jac embarrassed at right
    pov "Oh, you've got to be shitting my tits..."
    show pov shocked at left
    show eff embarrassed_talk at Position(xpos=1300)
    eff "Don't feel to bad."
    show pov bored at left
    show jac smirk at right
    eff "She took ‘em at angles that makes your dick look bigger."
    show jac neutral at right
    eff "I'd say she did you quite the favour."
    if sexwitheffie_bj >= 1:
        show pov embarrassed at left
        show jac confused at right
        eff "I mean, it's not like you needed any help with making it look big."
        show eff shocked at Position(xpos=1300)
        show jac confused_talk at right
        jac "Wai- what?"
        show pov smirk at left
        show eff embarrassed_talk at Position(xpos=1300)
        show jac confused at right
        eff "Hm? *mumbles* Fckfacesayswha-?"
        show eff smirk at Position(xpos=1300)
        show jac confused_talk at right
        jac "What?"
        show pov confused at left
        show eff neutral_talk at Position(xpos=1300)
        show jac bored at right
        eff "Nyehehe, cracks me up every time."
    show pov confused_talk at left
    show eff embarrassed at Position(xpos=1300)
    show jac embarrassed at right
    pov "Hold the phone, did one of them actually take the pictures?"
    show pov bored at left
    show eff embarrassed at Position(xpos=1300)
    show jac smirk_talk at right
    jac "Yeah, dude. Say whatever you want about the trio but they take very good pictures of other guys' junks."
    show pov confused_talk at left
    show jac neutral at right
    pov "That's sort of comforting..."
    pov "I guess..."
    show pov sad at left
    show eff embarrassed_talk at Position(xpos=1300)
    show jac embarrassed at right
    eff "Let's just get this over with, you'll have to face ‘em eventually."
    show eff embarrassed at Position(xpos=1300)
    show jac embarrassed_talk at right
    jac "Yeah dude, just like a band-aid, don't think to much about it and try to get it done quick."
    show pov sad_talk at left
    show jac embarrassed at right
    pov "Yeah... I suppose you're right."
    show pov sad at left
    pov "{i}*Inhale*{/i}"
    pov "..."
    show pov sad_talk at left
    pov "{i}*Exhale*{/i}"

    scene bg theresnakedpictures_1
    with fade
    $ renpy.pause()
    pov "{i}I can feel their eyes staring at me. God, this is awkward... I can hear them whispering too...{/i}"
    $ main_story = 43

    jump lbl_schoolhallway1_day_setup
