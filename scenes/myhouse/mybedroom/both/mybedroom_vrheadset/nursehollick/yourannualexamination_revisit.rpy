## Your Annual Examination ##
label lbl_your_annual_examination_revisit_5:
    $ yourannualexamination_hj = 0

    scene bg yourannualexamination_12

    jump lbl_your_annual_examination_revisit_hj_1

label lbl_your_annual_examination_revisit_hj_1:
    show bg yourannualexamination_12
    $ renpy.pause(0.4,hard=True)
    show bg yourannualexamination_13
    $ renpy.pause(0.4,hard=True)
    $ yourannualexamination_hj += 1

    jump lbl_your_annual_examination_revisit_hj_counter

label lbl_your_annual_examination_revisit_hj_counter:
    if skill_sta <= 4 and yourannualexamination_hj == 5:
        jump lbl_your_annual_examination_revisit_hj_end
    elif skill_sta <= 8 and yourannualexamination_hj == 12:
        jump lbl_your_annual_examination_revisit_hj_end
    elif skill_sta <= 12 and yourannualexamination_hj == 20:
        jump lbl_your_annual_examination_revisit_hj_end
    elif skill_sta <= 16 and yourannualexamination_hj == 20:
        scene bg yourannualexamination_13
        call screen scr_hospitalroom_night_revisit
        screen scr_hospitalroom_night_revisit():
            imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_your_annual_examination_revisit_5")
            imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_your_annual_examination_revisit_hj_end")
    else:
        jump lbl_your_annual_examination_revisit_hj_1

label lbl_your_annual_examination_revisit_hj_end:
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

            jump lbl_your_annual_examination_revisit_end

        "I want more.":
            show bg yourannualexamination_16
            pov "I want more."
            show bg yourannualexamination_15
            nur "Hehe, you sure? Maybe next time, too much of one thing can't be too good for you."
            nur "Give me a second while I wash up and take down some notes."
            show bg yourannualexamination_16
            pov "Sure thing."

            jump lbl_your_annual_examination_revisit_end


label lbl_your_annual_examination_revisit_end:
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
