## Back to Safety ##
label lbl_back_to_safety:
    default backtosafety_angel = 0

    scene black
    with fade
    $ renpy.pause()
    show bg backtosafety_1
    with fade
    $ renpy.pause(2,hard=True)

    scene black
    with fade
    show bg backtosafety_1
    with fade
    pov "Uhhh... Wha- where am I?..."
    show bg backtosafety_2
    with fade
    $ renpy.pause(3,hard=True)

    scene black
    show bg backtosafety_3
    with fade

    menu:
        "Uh... hi?":
            pov "Uh... hi?"
            show bg backtosafety_4
            mina "Do you know how many dumb teenagers have I seen passed out on the ground?"
            mina "It's not a good way to start my morning."
            mina "Much less when they are naked."
            mina "C'mon, get up. You're under arrest."
        "Good morning?":
            pov "Good morning?"
            show bg backtosafety_4
            mina "Good Morning yourself! You're under arrest."
        "Are you an angel?":
            $ backtosafety_angel = 1
            pov "Are you an angel sent from heaven to save me?"
            show bg backtosafety_4
            mina "Save your compliments for someone who cares, get your butt up off the ground!"
            mina "You're under arrest."
    show bg backtosafety_5
    pov "W-Wait, What?! Arrest me?! L-Listen to me, I was almost killed last night, you have to help me!"

    scene bg backtosafety_6
    with hpunch
    mina "Yeah, Yeah, Yeah."
    show bg backtosafety_7
    mina "Look buddy, I don't know what you're on but regardless of it, you can't just go around without clothes."
    mina "Keep it in your own home or at the nudist beach."
    mina "I can't believe I'm actually arresting someone for public indecency in a town with a nudist beach."
    show bg backtosafety_6
    mina "Now move it!"
    show bg backtosafety_8
    pov "W-Wait up! Let me explain!"
    show bg backtosafety_9
    mina "I don't want to hear it and you better not start struggling!"
    mina "You better not give me a reason to mace or tase that pretty face of yours, because I won't hesitate!"
    show bg backtosafety_10
    mina "HQ, I have the park exhibisionist in custody, bringing him for questioning, over."
    show bg backtosafety_11
    radio "Copy that, officer. Awaiting arrival and transport of suspect - over."
    $ main_story = 37
    $ gtime = 0
    if day <= 5:
        $ day += 1
    else:
        $ day = 0
    call lbl_next_date

    jump lbl_indecent_arrest
