## MUTUAL MASTURBATION (EXIB - EXHIBITION) ##
label lbl_effie_exib_revisit_1:

    scene bg hsceneeffieexib_1
    with fade
    show bg hsceneeffieexib_1
    eff "No touching okay? You're only allowed to watch me play with myself."
    eff "Got it?"
    pov "Yeah."

label lbl_effie_exib_revisit_continue:
    $ vrheadset_revisitcounter = 0

    jump lbl_effie_exib_revisit_2

####################
## Exib Stage 1
label lbl_effie_exib_revisit_1_1:
    $ vrheadset_revisitcounter += 1
    show bg hsceneeffieexib_2
    $ renpy.pause(0.4,hard=True)
    show bg hsceneeffieexib_3
    $ renpy.pause(0.4,hard=True)
    jump lbl_effie_exib_revisit_counter


####################
## Exib Stage 2
label lbl_effie_exib_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg hsceneeffieexib_2
    $ renpy.pause(0.2,hard=True)
    show bg hsceneeffieexib_3
    $ renpy.pause(0.2,hard=True)
    jump lbl_effie_exib_revisit_counter


####################
## Exib Stage 3
label lbl_effie_exib_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg hsceneeffieexib_4
    $ renpy.pause(0.1,hard=True)
    show bg hsceneeffieexib_5
    jump lbl_effie_exib_revisit_counter

label lbl_effie_exib_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_effie_exib_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_effie_exib_revisit_3
    elif vrheadset_revisitcounter >= 90:
        show bg hsceneeffieexib_2
        call screen scr_effie_exib_revisit
    else:
        jump lbl_effie_exib_revisit_1_1

screen scr_effie_exib_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_exib_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_exib_revisit_cum")


####################
## Exib Cum
label lbl_effie_exib_revisit_cum:

    scene bg hsceneeffieexib_6
    show bg hsceneeffieexib_6
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_7
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_8
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_9
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_10
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_11
    $ renpy.pause ()
    eff "Fuck that's a lot of cum."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
