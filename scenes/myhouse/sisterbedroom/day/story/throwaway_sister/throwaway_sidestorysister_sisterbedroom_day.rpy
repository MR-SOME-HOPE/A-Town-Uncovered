## Throwaway Sister Bedroom Day Side Story ##
label lbl_sister_bedroom_daynight_sister_play:
    default sister_hscenerevisit = 0
    default povrps = 'Rock'
    default sisrps = 'Rock'
    default povrps_points = 0
    default sisrps_points = 0

    show pov smirk_talk at left
    with dissolve
    show sis neutral at right
    with dissolve
    pov "I'm bored, wanna play?"
    show pov smirk at left
    show sis smirk_talk at right
    sis "I'm down, what do you have in mind?"
    menu:
        "Boxfort BJ":
            show pov smirk_talk at left
            show sis smirk at right
            pov "Wanna head to the Twin Fortress? I could use some help with something."
            show pov smirk at left
            show sis smirk_talk at right
            sis "I am feeling a little hungry now that you mention it..."
            show pov smirk_talk at left
            show sis smirk at right
            pov "Then what are we waiting for?"
            $ sister_hscenerevisit = 1
            jump lbl_breakinginfortrebuild_bj_revisit
        "Boxfort 69":
            show pov smirk_talk at left
            show sis smirk at right
            pov "Wanna head to the Twin Fortress? I'll scratch your back if you scratch mine."
            show pov smirk at left
            show sis smirk_talk at right
            sis "I could use a little back scratch now that you mention it."
            show pov smirk_talk at left
            show sis smirk at right
            pov "Let's go scratch that itch then."
            $ sister_hscenerevisit = 1
            jump lbl_whos_the_better_sibling_revisit
        "Trip to the Nudist Beach":
            if gtime <= 1:
                show pov smirk_talk at left
                show sis smirk at right
                pov "Wanna take the car and head to the beach again?"
                if winc == 1:
                    show pov smirk at left
                    show sis confused_talk at right
                    sis "I'll have to ask mom tonight."
                else:
                    show pov smirk at left
                    show sis confused_talk at right
                    sis "I'll have to ask [missus] tonight."
                show sis smirk_talk at right
                sis "Remind me later tonight if you still wanna go."
                show pov smirk_talk at left
                show sis smirk at right
                pov "Sure thing."
            else:
                show pov smirk_talk at left
                show sis neutral at right
                pov "Wanna take the car and head to the beach again?"
                if winc == 1:
                    show pov smirk at left
                    show sis neutral_talk at right
                    sis "Yup! Mom's fine with us taking the car."
                else:
                    show pov smirk at left
                    show sis neutral_talk at right
                    sis "Yup! [missus] is fine with us taking the car."
                $ sister_hscenerevisit = 1
                jump lbl_stargazing_fun_repeat
        "Rock, paper scissors?":
            show pov neutral at left
            show sis smirk_talk at right
            sis "Psssh- fine."
            $ sisrps = renpy.random.choice(['Rock', 'Paper', 'Scissors'])
            menu:
                "Rock":
                    $ povrps = 'Rock'
                "Paper":
                    $ povrps = 'Paper'
                "Scissors":
                    $ povrps = 'Scissors'
            show pov neutral at left
            show sis neutral_talk at right
            sis "After 3-"
            show pov neutral_talk at left
            show sis neutral at right
            pov "1-"
            show pov smirk at left
            show sis smirk_talk at right
            sis "2-"
            show pov smirk_talk at left
            show sis smirk at right
            pov "3-"
            show pov smirk at left
            show sis shocked_talk at right
            sis "[sisrps]!"
            show pov shocked_talk at left
            show sis shocked at right
            pov "[povrps]!"
            if sisrps == 'Rock':
                if povrps == 'Paper':
                    show pov smirk at left
                    show sis bored_talk at right
                    sis "You win."
                    $ povrps_points += 1
                elif povrps == 'Scissors':
                    show pov bored at left
                    show sis smirk_talk at right
                    sis "I win."
                    $ sisrps_points += 1
                else:
                    sis "It's a draw."
            elif sisrps == 'Paper':
                if povrps == 'Scissors':
                    show pov smirk at left
                    show sis bored_talk at right
                    sis "You win."
                    $ povrps_points += 1
                elif povrps == 'Rock':
                    show pov bored at left
                    show sis smirk_talk at right
                    sis "I win."
                    $ sisrps_points += 1
                else:
                    show pov bored at left
                    show sis neutral_talk at right
                    sis "It's a draw."
            elif sisrps == 'Scissors':
                if povrps == 'Rock':
                    show pov smirk at left
                    show sis bored_talk at right
                    sis "You win."
                    $ povrps_points += 1
                elif povrps == 'Paper':
                    show pov bored at left
                    show sis smirk_talk at right
                    sis "I win."
                    $ sisrps_points += 1
                else:
                    show pov bored at left
                    show sis neutral_talk at right
                    sis "It's a draw."
            show pov neutral at left
            sis "[povrps_points] wins for you and [sisrps_points] wins for me."

## Sister Play End
label lbl_sister_bedroom_daynight_sister_play_end:
    if gtime <= 1:
        jump lbl_sisterbedroom_day_setup
    else:
        jump lbl_sisterbedroom_night_setup

## Sister Movie Date
label lbl_sisterbedroom_daynight_sister_moviedate:
    show pov neutral_talk at left
    with dissolve
    if gtime <= 1:
        hide btn sisterbedroom_day_sister_idle
    else:
        hide btn sisterbedroom_night_sister_idle
    show sis confused at right
    with dissolve
    pov "Yo, [sister]. Wanna go catch a movie tonight?"
    show pov confused at left
    show sis confused_talk at right
    sis "At the cinema? Hmmmm- what's the catch?"
    show pov confused_talk at left
    show sis confused at right
    pov "No catch, I felt like watching something and figured you might as well."
    show pov smirk_talk at left
    show sis bored at right
    pov "It doesn't look like you have anything going on at the moment."
    show pov smirk at left
    show sis bored_talk at right
    sis "Shut up, you don't know that..."
    show sis bored at right
    sis "..."
    show sis bored_talk at right
    sis "Fine- I'm free. But not because I wasn't before!"
    sis "I just didn't feel like doing the other stuff tonight-"
    show pov smirk_talk at left
    show sis angry at right
    pov "Alright, we'll head out after dinner."

    scene black
    with fade
    $ renpy.pause(1.5)
    "At the cinema..."
    stop music fadeout 2.0
    $ moviedate = 2
    $ gtime = 2

    jump lbl_cinema_night_setup

## MC x Sister Eating Effie
label lbl_mcxsister_eating_effie_pre:
    default mcxsistereatingeffie_firsttimedone = 0

    if mcxsistereatingeffie_firsttimedone == 0:
        $ mcxsistereatingeffie_firsttimedone = 1
        show pov neutral_talk at left
        show sis confused at right
        with dissolve
        pov "Hey, I was thinking, we should give Effie a visit and thank her for taking care of you when you needed a place to stay."
        show pov neutral at left
        show sis neutral_talk at right
        sis "I could always visit Effie, she's the best. I'm lucky she was around for me."
        show sis embarrassed_talk at right
        sis "I could never thank her enough, so I'm in."
        show sis confused_talk at right
        sis "Do you have a gift idea?"
        show pov smirk_talk at left
        show sis confused at right
        pov "She's always saying how much she finds us both attractive."
        show pov neutral at left
        show sis smirk_talk at right
        if winc == 1:
            sis "Oh yeah, well. If you're up for it, bro-bro. We could eat her out together?"
        else:
            sis "Oh yeah, well. If you're up for it, [povname]. We could eat her out together?"
        show pov neutral_talk at left
        show sis smirk at right
        pov "I'm down, I'm sure she'd absolutely love it."
        show pov neutral at left
        show sis neutral_talk at right
        sis "Alright, that's the plan. Let's head there together."

        jump lbl_mcxsister_eating_effie_pre2

    else:
        show pov neutral_talk at left
        show sis confused at right
        with dissolve
        pov "Hey, you wanna go visit Effie again for breakfast?"
        show pov neutral at left
        show sis confused_talk at right
        sis "You think she'd appreciate us coming over?"
        show pov neutral_talk at left
        show sis smirk at right
        pov "You heard her last time, she's always happy to welcome us over."

        jump lbl_mcxsister_eating_effie_pre2
