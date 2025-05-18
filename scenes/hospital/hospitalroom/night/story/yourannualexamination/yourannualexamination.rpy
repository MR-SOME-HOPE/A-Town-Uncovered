## Your Annual Examination ##
label lbl_your_annual_examination:
    show bg yourannualexamination_1
    nur "Alright, [povname]. On a scale of 1 to 10, ‘1' being no pain and ‘10' being extreme pain, how is your head feeling?"

    menu:
        "1.":
            show bg yourannualexamination_2

            jump lbl_your_annual_examination_2
        "Around 3 or 4.":
            if skill_sta >= 1:
                $ skill_sta -= 1
            else:
                $ skill_sta = 0
            $ renpy.notify("You lost a Stamina Point")
            show bg yourannualexamination_2

            jump lbl_your_annual_examination_2
        "Around 6 or 7.":
            if skill_sta >= 3:
                $ skill_sta -= 3
            else:
                $ skill_sta = 0
            $ renpy.notify("You lost 3 Stamina Points")
            $ edgingunhealthiness += 1
            show bg yourannualexamination_3

            jump lbl_your_annual_examination_2
        "10.":
            if skill_sta >= 5:
                $ skill_sta -= 5
            else:
                $ skill_sta = 0
            $ renpy.notify("You lost 5 Stamina Points")
            $ edgingunhealthiness += 1
            show bg yourannualexamination_3

            jump lbl_your_annual_examination_2

label lbl_your_annual_examination_2:
    nur "Mhmm..."
    show bg yourannualexamination_1
    nur "And does your head feel like it's swollen or pulsing really hard?"

    menu:
        "Not at all.":
            show bg yourannualexamination_2

            jump lbl_your_annual_examination_3
        "I feel it a little.":
            if skill_sta >= 2:
                $ skill_sta -= 2
            else:
                $ skill_sta = 0
            $ renpy.notify("You lost 2 Stamina Points")
            $ edgingunhealthiness += 1
            show bg yourannualexamination_3

            jump lbl_your_annual_examination_3
        "Definitely swollen.":
            if skill_sta >= 4:
                $ skill_sta -= 4
            else:
                $ skill_sta = 0
            $ renpy.notify("You lost 4 Stamina Points")
            $ edgingunhealthiness += 1
            show bg yourannualexamination_3

            jump lbl_your_annual_examination_3

label lbl_your_annual_examination_3:
    nur "Mhmm..."
    show bg yourannualexamination_1
    nur "Just as I expected, obviously. I am a nurse after all."
    show bg yourannualexamination_4
    nur "Last question."
    show bg yourannualexamination_1
    nur "How much sex are you having?"
    show bg yourannualexamination_2
    pov "What does this have to do with my head?"
    show bg yourannualexamination_4
    nur "How does it not? And be honest with me, I'm a nurse."

    menu:
        "Tons.":
            if skill_sta <= 7:
                $ skill_sta += 3
            else:
                $ skill_sta = 10
            $ renpy.notify("You gained 3 Stamina Points")

            jump lbl_your_annual_examination_4
        "A good amount.":
            if skill_sta <= 8:
                $ skill_sta += 2
            else:
                $ skill_sta = 10
            $ renpy.notify("You gained 2 Stamina Points")

            jump lbl_your_annual_examination_4
        "Barely enough.":
            if skill_sta <= 9:
                $ skill_sta += 1
            else:
                $ skill_sta = 10
            $ renpy.notify("You gained a Stamina Point")
            $ edgingunhealthiness += 1

            jump lbl_your_annual_examination_4
        "Not enough.":
            $ edgingunhealthiness += 1

            jump lbl_your_annual_examination_4

label lbl_your_annual_examination_4:
    show bg yourannualexamination_4
    nur "Alright, that's all the questions I have for today."
    if edgingunhealthiness <= 2:
        show bg yourannualexamination_5
        nur "Ooh, actually, could you do me a solid and release your semen into this here beaker for me."
        show bg yourannualexamination_6
        pov "You want me to cum, inside a beaker?"
        show bg yourannualexamination_5
        nur "Standard procedure. It's just for me to make sure you're healthy."
        show bg yourannualexamination_6
        pov "Well, alright then..."
        show bg yourannualexamination_7
        nur "The bathroom is right there."
        scene black
        with fade
        "A few short seconds later..."
        scene bg hospitalroom_night_lightson_closed
        with fade
        show povn embarrassed at left
        with dissolve
        show nursw smirk_talk at right
        with dissolve
        nur "Wow, new record?"
        show povn confused_talk at left
        show nursw smirk at right
        pov "Huh? What?"
        show povn confused at left
        show nursw neutral_talk at right
        nur "Nothing, let me see that beaker."
        scene black
        with fade
        "Another few seconds later..."

        jump lbl_your_annual_examination_end
    else:
        show bg yourannualexamination_8
        nur "Just sit back and let me do my job."

        menu:
            "Alright.":
                show bg yourannualexamination_9
                pov "Alright."

                jump lbl_your_annual_examination_5
            "I can do it myself.":
                show bg yourannualexamination_9
                pov "Actually, I can do it myself."
                show bg yourannualexamination_8
                nur "You sure? You're not embarrassed about your erect penis are you? I'm a nurse. I've seen them curve in all directions."
                show bg yourannualexamination_9
                pov "No, no. It's not that, I just prefer to do it myself."
                show bg yourannualexamination_11
                nur "Well, could you do me a favour then? Could you use the bathroom and ejaculate inside this beaker? I'm not really in the cleaning mood at this time of night."
                show bg yourannualexamination_10
                pov "You want me to cum, inside a beaker?"
                show bg yourannualexamination_11
                nur "Standard procedure. It's just for me to make sure you're healthy."
                show bg yourannualexamination_10
                pov "Well, alright then..."
                scene black
                with fade
                "A few short seconds later..."
                scene bg hospitalroom_night_lightson_closed
                with fade
                show povn embarrassed at left
                with dissolve
                show nursw smirk_talk at right
                with dissolve
                nur "Wow, new record?"
                show povn confused_talk at left
                show nursw smirk at right
                pov "Huh? What?"
                show povn confused at left
                show nursw neutral_talk at right
                nur "Nothing, let me see that beaker."
                scene black
                with fade
                "Another few seconds later..."

                jump lbl_your_annual_examination_end

label lbl_your_annual_examination_5:
    $ yourannualexamination_hj = 0

    scene bg yourannualexamination_12

    jump lbl_your_annual_examination_hj_1

label lbl_your_annual_examination_hj_1:
    show bg yourannualexamination_12
    $ renpy.pause(0.4,hard=True)
    show bg yourannualexamination_13
    $ renpy.pause(0.4,hard=True)
    $ yourannualexamination_hj += 1

    jump lbl_your_annual_examination_hj_counter

label lbl_your_annual_examination_hj_counter:
    if skill_sta <= 4 and yourannualexamination_hj == 5:
        jump lbl_your_annual_examination_hj_end
    elif skill_sta <= 8 and yourannualexamination_hj == 12:
        jump lbl_your_annual_examination_hj_end
    elif skill_sta <= 12 and yourannualexamination_hj == 20:
        jump lbl_your_annual_examination_hj_end
    elif skill_sta <= 16 and yourannualexamination_hj == 20:
        scene bg yourannualexamination_13
        call screen scr_hospitalroom_night
        screen scr_hospitalroom_night():
            imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_your_annual_examination_5")
            imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_your_annual_examination_hj_end")
    else:
        jump lbl_your_annual_examination_hj_1

label lbl_your_annual_examination_hj_end:
    show bg yourannualexamination_14
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_1
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_2
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_3
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_4
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_5
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_6
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_7
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_8
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_9
    $ renpy.pause(0.2,hard=True)
    show bg yourannualexamination_14_10
    $ renpy.pause()
    show bg yourannualexamination_15
    nur "Wow, holy crap that is a lot of semen."
    nur "Jeez, it must've been really tense keeping all that in there."
    nur "How do you feel?"

    menu:
        "Relieved.":
            show bg yourannualexamination_16
            pov "I feel so relieved."
            show bg yourannualexamination_15
            nur "Hehe, that's good. Like a good ol' crack in the back, that's what my mom always used to say."
            nur "Give me a second while I wash up and take down some notes."
            show bg yourannualexamination_16
            pov "Sure thing."
            scene black
            with fade
            "Shortly after..."

            jump lbl_your_annual_examination_end
        "I want more.":
            show bg yourannualexamination_16
            pov "I want more."
            show bg yourannualexamination_15
            nur "Hehe, you sure? Maybe next time, too much of one thing can't be too good for you."
            nur "Give me a second while I wash up and take down some notes."
            show bg yourannualexamination_16
            pov "Sure thing."
            scene black
            with fade
            "Shortly after..."

            jump lbl_your_annual_examination_end

label lbl_your_annual_examination_end:
    $ main_story = 27

    jump lbl_hospitalroom_night_setup_1
