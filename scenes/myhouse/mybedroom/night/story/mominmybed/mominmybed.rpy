## Mom in my Bed ##
label lbl_mom_in_my_bed:
    if winc == 0:
        jump lbl_mom_in_my_bed_winc0

    scene bg mybedroom_night_lightson
    with fade
    show pov embarrassed at left
    with dissolve
    show mum embarrassed at right
    with dissolve
    mum "..."
    pov "..."
    show mum embarrassed_talk at right
    mum "I guess I should thank you for... y'know.."
    mum "Being there like you said you would."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "You know you can stay here as long as you want, you don't need to face Dad ever again."
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "You're being a little overdramatic aren't you."
    show mum embarrassed_talk at right
    mum "To be fair, this is between you and your dad. I just unfortunately happen to be the reason it all started."
    show pov sad_talk at left
    show mum sad at right
    pov "It's not you, Mom. You have nothing to do with it."
    if savemomfromdad == 1:
        show pov angry_talk at left
        show mum embarrassed at right
        pov "Dad's just turned into a right out prick and deserved it."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "Let the grownups fight about it later, okay, baby? It's nothing you need to actively keep your eye on."
        mum "You've been working out haven't you? I honestly doubted my squishy little bo-, excuse me. Man."
    else:
        show pov angry_talk at left
        show mum embarrassed at right
        pov "Dad's just turned into an asshole and he.."
        show pov sad_talk at left
        show mum neutral at right
        pov "Well... I didn't really win but..."
        show pov sad at left
        show mum embarrassed_talk at right
        mum "You tried your best, baby. I'm not saying that to tease you."
        show pov embarrassed at left
        mum "I really mean it when I say that that was the bravest thing I've ever seen."
    show pov embarrassed at left
    show mum embarrassed at right
    pov "..."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "C'mon, we should get some sleep."
    show pov embarrassed_talk at left
    show mum confused at right
    pov "You can pick which side you wanna sle-"
    show pov shocked at left
    show mum smirk_talk at right
    mum "Are- are you gonna strip down?"
    show pov shocked_talk at left
    show mum smirk at right
    pov "W-what?"
    if momfallenasleep_sleepnaked == 1:
        show pov shocked at left
        show mum smirk_talk at right
        mum "You told me that you sleep naked."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Oh... um.."
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Why are you shy all of a sudden?"
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Well... I- I don't.. know.."
    else:
        show pov shocked at left
        show mum smirk_talk at right
        mum "I know you sleep naked, [povname]. I'm your mother."
        mum "I've walked in on you while you're sleeping."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "..."
        show pov shocked at left
        show mum smirk_talk at right
        mum "Not on purpose of course. I was just looking for something and well.. you're definitely not a little boy anymore."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Mom..."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "C'mon and give your mother a show. It'll really lift my mood."

    menu:
        "Get ready for the sexiest show." if skill_cha >= 5:
            if mum_points <= 7:
                $ mum_points += 3
            else:
                $ mum_points = 10
            $ renpy.notify("Your relationship with Mom has increased by 3")
            show pov smirk_talk at left
            show mum smirk at right
            pov "Well, get ready for the sexiest show of your life."
        "Okay...":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show pov embarrassed_talk at left
            show mum smirk at right
            pov "O-Okay..."
        "Can you have you eyes closed.":
            if mum_points <= 1:
                $ mum_points -= 1
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with Mom has decreased")
            show pov sad_talk at left
            show mum bored at right
            pov "I-it's embarrassing. Can I just undress with your eyes closed?"
            show pov shocked at left
            show mum confused_talk at right
            mum "Are you still a virgin...?"

            menu:
                "No!":
                    show pov sad_talk at left
                    show mum smirk at right
                    pov "No!"
                "Mom!":
                    show pov sad_talk at left
                    show mum smirk at right
                    pov "Mom..!"
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show pov sad at left
            show mum neutral_talk at right
            mum "I'm teasing, [povname]. You don't have to answer that."
            mum "You're so adorable when you're flustered."

            jump lbl_mom_in_my_bed_strip_2

label lbl_mom_in_my_bed_strip_1:

    scene black
    with fade

    scene bg strippingformom_1
    with fade
    $ renpy.pause()
    show bg strippingformom_2
    $ renpy.pause()
    show bg strippingformom_3
    $ renpy.pause()

    jump lbl_mom_in_my_bed_2

label lbl_mom_in_my_bed_strip_2:

    scene black
    with fade

    scene bg strippingformom_4
    with fade
    $ renpy.pause()
    show bg strippingformom_5
    $ renpy.pause()
    show bg strippingformom_6
    $ renpy.pause()

label lbl_mom_in_my_bed_2:

    scene black
    with fade

    scene bg mominmybed_1
    with fade
    $ renpy.pause()
    show bg mominmybed_2
    with dissolve
    #$ mominmybed_handjob = 0
    mum "Goodnight, [povname]..."
    show bg mominmybed_3
    pov "Goodnight.. Mom.."
    show bg mominmybed_4
    mum "Hmm? What's wrong?"
    show bg mominmybed_5
    pov "Hm? Nothing."
    show bg mominmybed_6
    mum "No, tell me. We can still talk if you want."
    show bg mominmybed_7
    mum "We can gossip and braid each other's hair."
    mum "Hehehe."
    show bg mominmybed_8
    pov "..."
    show bg mominmybed_9
    mum "Naww, c'mon, sweetie. I'm just trying to lighten the mood. I can feel you're a little... tense.."
    show bg mominmybed_10
    mum "That's it, isn't it?"
    show bg mominmybed_11
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_12
    mum "My baby's a little tense?"
    show bg mominmybed_13
    mum "Oh... wow... you have a lot of girth on this thing..."
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_16
    mum "Do me a favour and avoid making a mess tonight. Washing day isn't until next week."
    show bg mominmybed_17
    pov "...I- I'll try."

    jump lbl_mominmybed_1

label lbl_mominmybed_1:
    #$ mominmybed_handjob += 1
    #show bg mominmybed_18
    #$ renpy.pause(0.5, hard=True)
    #show bg mominmybed_19
    #$ renpy.pause(0.5, hard=True)

    #jump lbl_mominmybed_2
    scene img_mominmybed_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mominmybed_3
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mominmybed_3

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mominmybed_4

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mominmybed_1
image img_mominmybed_1:
    "bg mominmybed_18"
    pause 0.5
    "bg mominmybed_19"
    pause 0.5
    repeat

#label lbl_mominmybed_2:
    #if skill_sta <= 4 and mominmybed_handjob == 3:
    #    jump lbl_mominmybed_3
    #elif skill_sta <= 9 and mominmybed_handjob == 7:
    #    jump lbl_mominmybed_3
    #elif skill_sta <= 14 and mominmybed_handjob == 11:
    #    jump lbl_mominmybed_4
    #elif skill_sta <= 20 and mominmybed_handjob == 15:
    #    jump lbl_mominmybed_4
    #else:
    #    jump lbl_mominmybed_1

label lbl_mominmybed_3:
    show bg mominmybed_20
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_21
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_22
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_23
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_24
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_25
    $ renpy.pause()
    show bg mominmybed_26
    mum "You're an idiot."
    show bg mominmybed_27
    pov "Screw you, Mom... you're such a tease."
    show bg mominmybed_28
    mum "Hehehe."
    show bg mominmybed_29
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_28
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_29
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_28
    $ renpy.pause(0.5, hard=True)
    $ mum_path = 11
    if skill_sta >= 5:
        $ skill_sta -= 5
    else:
        $ skill_sta = 0
    $ renpy.notify("You used 5 Stamina Points")

    jump lbl_mybedroom_night_sleep

label lbl_mominmybed_4:
    $ mum_path = 11

    scene black
    with fade
    "Despite receiving a handjob, you managed to keep yourself from cumming."

    jump lbl_mybedroom_night_sleep

### NO WINC ###
label lbl_mom_in_my_bed_winc0:

    scene bg mybedroom_night_lightson
    with fade
    show pov embarrassed at left
    with dissolve
    show mum embarrassed at right
    with dissolve
    mum "..."
    pov "..."
    show mum embarrassed_talk at right
    mum "I guess I should thank you for... y'know.."
    mum "Being there like you said you would."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "You know you can stay here as long as you want, you don't need to face [dadname] ever again."
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "You're being a little overdramatic aren't you."
    show mum embarrassed_talk at right
    mum "To be fair, this is between you and your [dadrole]. I just unfortunately happen to be the reason it all started."
    show pov sad_talk at left
    show mum sad at right
    pov "It's not you, [missus]. You have nothing to do with it."
    if savemomfromdad == 1:
        show pov angry_talk at left
        show mum embarrassed at right
        pov "[dadname]'s just turned into a right out prick and deserved it."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "Let the grownups fight about it later, okay, baby? It's nothing you need to actively keep your eye on."
        mum "You've been working out haven't you? I honestly doubted my squishy little bo-, excuse me. Man."
    else:
        show pov angry_talk at left
        show mum embarrassed at right
        pov "[dadname]'s just turned into an asshole and he.."
        show pov sad_talk at left
        show mum neutral at right
        pov "Well... I didn't really win but..."
        show pov sad at left
        show mum embarrassed_talk at right
        mum "You tried your best, baby. I'm not saying that to tease you."
        show pov embarrassed at left
        mum "I really mean it when I say that that was the bravest thing I've ever seen."
    show pov embarrassed at left
    show mum embarrassed at right
    pov "..."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "C'mon, we should get some sleep."
    show pov embarrassed_talk at left
    show mum confused at right
    pov "You can pick which side you wanna sle-"
    show pov shocked at left
    show mum smirk_talk at right
    mum "Are- are you gonna strip down?"
    show pov shocked_talk at left
    show mum smirk at right
    pov "W-what?"
    if momfallenasleep_sleepnaked == 1:
        show pov shocked at left
        show mum smirk_talk at right
        mum "You told me that you sleep naked."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Oh... um.."
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Why are you shy all of a sudden?"
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "Well... I- I don't.. know.."
    else:
        show pov shocked at left
        show mum smirk_talk at right
        mum "I know you sleep naked, [povname]. I'm your [mumrole]."
        mum "I've walked in on you while you're sleeping."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "..."
        show pov shocked at left
        show mum smirk_talk at right
        mum "Not on purpose of course. I was just looking for something and well.. you're definitely not a little boy anymore."
        show pov embarrassed_talk at left
        show mum smirk at right
        pov "[missus]..."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "C'mon and give your [mumrole] a show. It'll really lift my mood."

    menu:
        "Get ready for the sexiest show." if skill_cha >= 5:
            if mum_points <= 7:
                $ mum_points += 3
            else:
                $ mum_points = 10
            $ renpy.notify("Your relationship with [missus] has increased by 3")
            show pov smirk_talk at left
            show mum smirk at right
            pov "Well, get ready for the sexiest show of your life."
        "Okay...":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show pov embarrassed_talk at left
            show mum smirk at right
            pov "O-Okay..."
        "Can you have you eyes closed.":
            if mum_points <= 1:
                $ mum_points -= 1
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with [missus] has decreased")
            show pov sad_talk at left
            show mum bored at right
            pov "I-it's embarrassing. Can I just undress with your eyes closed?"
            show pov shocked at left
            show mum confused_talk at right
            mum "Are you still a virgin...?"

            menu:
                "No!":
                    show pov sad_talk at left
                    show mum smirk at right
                    pov "No!"
                "[missus]!":
                    show pov sad_talk at left
                    show mum smirk at right
                    pov "[missus]..!"
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show pov sad at left
            show mum neutral_talk at right
            mum "I'm teasing, [povname]. You don't have to answer that."
            mum "You're so adorable when you're flustered."

            jump lbl_mom_in_my_bed_strip_2_winc0

label lbl_mom_in_my_bed_strip_1_winc0:

    scene black
    with fade

    scene bg strippingformom_1
    with fade
    $ renpy.pause()
    show bg strippingformom_2
    $ renpy.pause()
    show bg strippingformom_3
    $ renpy.pause()

    jump lbl_mom_in_my_bed_2_winc0

label lbl_mom_in_my_bed_strip_2_winc0:

    scene black
    with fade

    scene bg strippingformom_4
    with fade
    $ renpy.pause()
    show bg strippingformom_5
    $ renpy.pause()
    show bg strippingformom_6
    $ renpy.pause()

label lbl_mom_in_my_bed_2_winc0:

    scene black
    with fade

    scene bg mominmybed_1
    with fade
    $ renpy.pause()
    show bg mominmybed_2
    with dissolve
    #$ mominmybed_handjob = 0
    mum "Goodnight, [povname]..."
    show bg mominmybed_3
    pov "Goodnight.. [missus].."
    show bg mominmybed_4
    mum "Hmm? What's wrong?"
    show bg mominmybed_5
    pov "Hm? Nothing."
    show bg mominmybed_6
    mum "No, tell me. We can still talk if you want."
    show bg mominmybed_7
    mum "We can gossip and braid each other's hair."
    mum "Hehehe."
    show bg mominmybed_8
    pov "..."
    show bg mominmybed_9
    mum "Naww, c'mon, sweetie. I'm just trying to lighten the mood. I can feel you're a little... tense.."
    show bg mominmybed_10
    mum "That's it, isn't it?"
    show bg mominmybed_11
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_12
    mum "My baby's a little tense?"
    show bg mominmybed_13
    mum "Oh... wow... you have a lot of girth on this thing..."
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_16
    mum "Do me a favour and avoid making a mess tonight. Washing day isn't until next week."
    show bg mominmybed_17
    pov "...I- I'll try."

    jump lbl_mominmybed_1_winc0

label lbl_mominmybed_1_winc0:
    #$ mominmybed_handjob += 1
    #show bg mominmybed_18
    #$ renpy.pause(0.5, hard=True)
    #show bg mominmybed_19
    #$ renpy.pause(0.5, hard=True)

    #jump lbl_mominmybed_2_winc0
    scene img_mominmybed_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mominmybed_3_winc0
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mominmybed_3_winc0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mominmybed_4_winc0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mominmybed_1_winc0


#label lbl_mominmybed_2_winc0:
    #if skill_sta <= 4 and mominmybed_handjob == 3:
    #    jump lbl_mominmybed_3_winc0
    #elif skill_sta <= 9 and mominmybed_handjob == 7:
    #    jump lbl_mominmybed_3_winc0
    #elif skill_sta <= 14 and mominmybed_handjob == 11:
    #    jump lbl_mominmybed_4_winc0
    #elif skill_sta <= 20 and mominmybed_handjob == 15:
    #    jump lbl_mominmybed_4_winc0
    #else:
    #    jump lbl_mominmybed_1_winc0

label lbl_mominmybed_3_winc0:
    show bg mominmybed_20
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_21
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_22
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_23
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_24
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_25
    $ renpy.pause()
    show bg mominmybed_26
    mum "You're an idiot."
    show bg mominmybed_27
    pov "Screw you, [missus]... you're such a tease."
    show bg mominmybed_28
    mum "Hehehe."
    show bg mominmybed_29
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_28
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_29
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_28
    $ renpy.pause(0.5, hard=True)
    $ mum_path = 11

    jump lbl_mybedroom_night_sleep

label lbl_mominmybed_4_winc0:
    $ mum_path = 11

    scene black
    with fade
    "Despite receiving a handjob, you managed to keep yourself from cumming."

    jump lbl_mybedroom_night_sleep
