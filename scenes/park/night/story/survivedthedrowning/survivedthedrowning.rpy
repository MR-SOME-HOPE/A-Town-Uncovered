## Survived the Drowning ##
label lbl_survived_the_drowning:
    default violetteboobjobpark = 0

    scene black
    show bg survivedthedrowning_1_1
    with fade
    $ renpy.pause(1,hard=True)
    show black
    with fade
    $ renpy.pause(1,hard=True)
    show bg survivedthedrowning_1_3
    with fade
    vio "Oh, thank God, you're alive."
    show bg survivedthedrowning_1_4
    pov "{i}*Cough cough*{/i}"
    show bg survivedthedrowning_1_3
    vio "Take it easy, [povname]. You just swallowed a lot of nasty pond water."
    show bg survivedthedrowning_1_4
    pov "W-where am I?"
    show bg survivedthedrowning_1_5
    vio "You're in the middle of the park is where you are."
    vio "You must've gotten too close to the water, slipped on the mud, hit your head on the concrete path and rolled into the water."
    show bg survivedthedrowning_1_6
    pov "Seriously?"
    show bg survivedthedrowning_1_5
    vio "I mean, I wasn't here to see it but it must've been one hell of a funny sight."
    show bg survivedthedrowning_1_7
    pov "Fuck off."
    show bg survivedthedrowning_1_8
    vio "Fuck me, fuck you. I just saved your life and mind you, I'm off duty."

    scene bg park_night
    with fade
    show pov sad at left
    with dissolve
    show vioc bored at right
    with dissolve
    pov "..."
    show pov sad_talk at left
    show vioc confused at right
    pov "Where is she?"
    show pov sad at left
    show vioc confused_talk at right
    vio "Who?"
    show pov confused_talk at left
    show vioc confused at right
    pov "That girl?"
    show pov confused at left
    show vioc confused_talk at right
    vio "Um, you gotta be a little bit more specific than that, [povname]. I was the only one around here."
    show pov confused_talk at left
    show vioc confused at right
    pov "It couldn't have been you though."
    show pov bored at left
    show vioc smirk_talk at right
    vio "I don't know what you're talking about but I'm a little offended. What if it was me?!"
    show pov sad_talk at left
    show vioc confused at right
    pov "I saw this girl walk on water and then go under."
    show pov bored at left
    show vioc neutral_talk at right
    vio "Uh-huh... and yesterday I saw a pink flying elephant singing 'Ode to Joy' in Japanese."
    show pov sad_talk at left
    show vioc smirk at right
    pov "I know I sound crazy..."
    show pov bored at left
    show vioc neutral_talk at right
    vio "Well good, at least you're aware. Though I would still advise you to take a trip to the hospital."
    show pov confused_talk at left
    show vioc bored at right
    pov "What? I'm fine."
    show pov angry at left
    show vioc bored_talk at right
    vio "I wouldn't count on it. You must've hit your head harder than I thought from what utter bullshit that's been coming out of your mouth."
    show pov angry at left
    show vioc smirk at right
    pov "..."
    show pov bored_talk at left
    show vioc smirk at right
    pov "I'm going home and I'm going to rest my head on my pillow, maybe I'm just really tired and delusional."
    show pov confused at left
    show vioc smirk_talk at right
    vio "[povname]."
    show pov bored at left
    vio "C'mon, I'll give you a boob job right here, right now."

    menu:
        "You've convinced me.":
            $ violetteboobjobpark = 1
            show pov smirk_talk at left
            show vioc smirk at right
            pov "You've convinced me."

            jump lbl_survived_the_drowning_boobjob
        "I don't think that's a good idea.":
            show pov bored_talk at left
            show vioc smirk at right
            pov "I don't think that's a good idea right now."
            show pov bored at left
            show vioc smirk_talk at right
            vio "See, you are delusional! I guess it's straight to the hospital for you then."
            show pov bored_talk at left
            show vioc smirk at right
            pov "Is this really necessary?"
            show pov bored at left
            show vioc neutral_talk at right
            vio "It's just to make sure there's no internal damage."
            show pov angry_talk at left
            show vioc smirk at right
            pov "But I didn't hit my head."
            show pov angry at left
            show vioc smirk_talk at right
            vio "Uh-huh. You're a stubborn one, aren't you? Let's go."
            if skill_cha >= 2:
                $ skill_cha -= 2
            else:
                $ skill_cha = 0
            $ renpy.notify("You lost 2 Charisma Points")
            $ main_story = 25

            jump lbl_hospitalroom_night_setup_1

label lbl_survived_the_drowning_boobjob:
    scene bg survivedthedrowning_2_1
    with fade

    jump lbl_survived_the_drowning_boobjob_0

label lbl_survived_the_drowning_boobjob_0:
    $ violetteboobjobparkcounter = 0

    jump lbl_survived_the_drowning_boobjob_1

label lbl_survived_the_drowning_boobjob_1:
    show bg survivedthedrowning_2_1
    $ renpy.pause(0.4,hard=True)
    show bg survivedthedrowning_2_2
    $ renpy.pause(0.4,hard=True)
    show bg survivedthedrowning_2_3
    $ renpy.pause(0.4,hard=True)
    show bg survivedthedrowning_2_2
    $ renpy.pause(0.4,hard=True)
    $ violetteboobjobparkcounter += 1

    if skill_sta <= 7 and violetteboobjobparkcounter == 10:
        jump lbl_survived_the_drowning_boobjob_menu
    elif skill_sta <= 14 and violetteboobjobparkcounter == 12:
        jump lbl_survived_the_drowning_boobjob_2
    elif skill_sta <= 20 and violetteboobjobparkcounter == 14:
        jump lbl_survived_the_drowning_boobjob_2
    else:
        jump lbl_survived_the_drowning_boobjob_1

label lbl_survived_the_drowning_boobjob_2:
    show bg survivedthedrowning_2_4
    $ renpy.pause(0.3,hard=True)
    show bg survivedthedrowning_2_5
    $ renpy.pause(0.2,hard=True)
    show bg survivedthedrowning_2_6
    $ renpy.pause(0.2,hard=True)
    show bg survivedthedrowning_2_5
    $ renpy.pause(0.2,hard=True)
    $ violetteboobjobparkcounter += 1

    if skill_sta <= 14 and violetteboobjobparkcounter == 28:
        jump lbl_survived_the_drowning_boobjob_menu
    elif skill_sta <= 20 and violetteboobjobparkcounter == 32:
        jump lbl_survived_the_drowning_boobjob_3
    else:
        jump lbl_survived_the_drowning_boobjob_2

label lbl_survived_the_drowning_boobjob_3:
    show bg survivedthedrowning_2_7
    $ renpy.pause(0.2,hard=True)
    show bg survivedthedrowning_2_8
    $ renpy.pause(0.2,hard=True)
    show bg survivedthedrowning_2_9
    $ renpy.pause(0.2,hard=True)
    $ violetteboobjobparkcounter += 1

    if skill_sta <= 20 and violetteboobjobparkcounter == 46:
        jump lbl_survived_the_drowning_boobjob_menu
    else:
        jump lbl_survived_the_drowning_boobjob_3

label lbl_survived_the_drowning_boobjob_menu:
    scene bg survivedthedrowning_2_4
    call screen scr_survived_the_drowning_boobjob

screen scr_survived_the_drowning_boobjob():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_survived_the_drowning_boobjob_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_survived_the_drowning_boobjob_end")

label lbl_survived_the_drowning_boobjob_end:
    if skill_sta <= 7:
        show bg survivedthedrowning_2_1
        $ renpy.pause(0.4,hard=True)
        show bg survivedthedrowning_2_2
        $ renpy.pause(0.4,hard=True)
        show bg survivedthedrowning_2_3
        $ renpy.pause(0.4,hard=True)
    elif skill_sta <= 14:
        show bg survivedthedrowning_2_4
        $ renpy.pause(0.3,hard=True)
        show bg survivedthedrowning_2_5
        $ renpy.pause(0.2,hard=True)
        show bg survivedthedrowning_2_6
        $ renpy.pause(0.2,hard=True)
    elif skill_sta <= 20:
        show bg survivedthedrowning_2_7
        $ renpy.pause(0.2,hard=True)
        show bg survivedthedrowning_2_8
        $ renpy.pause(0.2,hard=True)
        show bg survivedthedrowning_2_9
        $ renpy.pause(0.2,hard=True)
    pov "I'm cumming-"
    show bg survivedthedrowning_2_5
    $ renpy.pause(0.5,hard=True)
    show bg survivedthedrowning_2_4
    $ renpy.pause(0.5,hard=True)
    show bg survivedthedrowning_2_10
    vio "Alright, That's enough of that, let's go."
    show bg survivedthedrowning_2_11
    pov "W-What!? I didn't get to finish."
    show bg survivedthedrowning_2_12
    vio "Oh, poor you, I let you fuck my tits and you can't cum."
    show bg survivedthedrowning_2_13
    vio "Let's go, my little bitch."
    if skill_sta >= 2:
        $ skill_sta -= 2
    else:
        $ skill_sta = 0
    $ renpy.notify("You used 2 Stamina Points")

    scene black
    with fade
    "At the hospital..."

    $ main_story = 25

    jump lbl_hospitalroom_night_setup_1
