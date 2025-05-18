## A Predictable Realization
label lbl_a_predictable_realization_handjob_revisit:
    $ apredictablerealization_handjob = 1

    scene bg apredictablerealization_handjob_1
    with fade

label lbl_a_predictable_realization_handjob_revisit_0:
    jump lbl_a_predictable_realization_handjob_revisit_1


label lbl_a_predictable_realization_handjob_revisit_1:
    scene img_a_predictable_realization_handjob_revisit_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_1

image img_a_predictable_realization_handjob_revisit_1:
    "bg apredictablerealization_handjob_1"
    pause 0.3
    "bg apredictablerealization_handjob_2"
    pause 0.1
    "bg apredictablerealization_handjob_3"
    pause 0.1
    "bg apredictablerealization_handjob_4"
    pause 0.2
    "bg apredictablerealization_handjob_2"
    pause 0.2
    repeat

label lbl_a_predictable_realization_handjob_revisit_2:
    scene img_a_predictable_realization_handjob_revisit_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_2

image img_a_predictable_realization_handjob_revisit_2:
    "bg apredictablerealization_handjob_1"
    pause 0.3
    "bg apredictablerealization_handjob_2"
    pause 0.1
    "bg apredictablerealization_handjob_4"
    pause 0.2
    "bg apredictablerealization_handjob_2"
    pause 0.2
    repeat

label lbl_a_predictable_realization_handjob_revisit_3:
    scene img_a_predictable_realization_handjob_revisit_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_a_predictable_realization_handjob_revisit_3

image img_a_predictable_realization_handjob_revisit_3:
    "bg apredictablerealization_handjob_1"
    pause 0.2
    "bg apredictablerealization_handjob_4"
    pause 0.1
    "bg apredictablerealization_handjob_2"
    pause 0.2
    repeat

label lbl_a_predictable_realization_handjob_revisit_cum:
    call screen scr_a_predictable_realization_handjob_revisit_cum

screen scr_a_predictable_realization_handjob_revisit_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_a_predictable_realization_handjob_revisit_0")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_a_predictable_realization_handjob_revisit_cumming")
    else:
        pass

label lbl_a_predictable_realization_handjob_revisit_cumming:
    scene bg apredictablerealization_handjob_5_1
    $ renpy.pause(0.4,hard=True)
    show bg apredictablerealization_handjob_5_2
    $ renpy.pause(0.4,hard=True)
    show bg apredictablerealization_handjob_5_3
    $ renpy.pause(0.4,hard=True)
    show bg apredictablerealization_handjob_5_4
    $ renpy.pause(0.4,hard=True)
    show bg apredictablerealization_handjob_5_5
    $ renpy.pause()

    pov "H-holy shit."

    eff "God you still let out like a firehose."
    eff "If I do this often enough I might try becoming a firewoman!"

    pov "Dude, that was risky as hell…"

    eff "And exactly what I needed to get out of zombie worker mode!"
    eff "Besides, are you really going to complain when you are the one who got to unwind~?"

    pov "N-No…"

    eff "Good boy!"
    eff "Think of it like an expansion to our usual fooling around, but next time let’s do it at my place."
    eff "I’d rather get my turn when we are in private since I don’t plan on being anything but loud and I doubt we can get away with that here~"

    pov "I’ll… be sure to remember that."

    eff "You better!"
    eff "Alright, now that I had my fun, I really need to get back for my shift."
    eff "Don’t be a stranger and let me know when we can mess around again!"

    pov "S-Sure thing, Effie…"

    eff "See you around, Stud~"

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection