## MISSIONARY (MISH) ##
label lbl_effie_mish_revisit_1:
    if hscene_xray == 0:
        scene bg hscene_effie_mish_1
        with fade
        $ renpy.pause()
        show bg hscene_effie_mish_2
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3
        eff "Fuck that's deep."
        show bg hscene_effie_mish_4
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1
        $ renpy.pause ()
        show bg hscene_effie_mish_2
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3
        eff "Right there..."
        show bg hscene_effie_mish_4
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1
        $ renpy.pause()
        show bg hscene_effie_mish_2
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3
        eff "Don't stop.."
    else:
        scene bg hscene_effie_mish_1_0
        with fade
        $ renpy.pause()
        show bg hscene_effie_mish_2_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3_0
        eff "Fuck that's deep."
        show bg hscene_effie_mish_4_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1_0
        $ renpy.pause ()
        show bg hscene_effie_mish_2_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3_0
        eff "Right there..."
        show bg hscene_effie_mish_4_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1_0
        $ renpy.pause ()
        show bg hscene_effie_mish_2_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_4_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1_0
        eff "Don't stop.."

    jump lbl_effie_mish_revisit_continue

label lbl_effie_mish_revisit_continue:
## Set Mish Counter
    $ vrheadset_revisitcounter = 0

label lbl_effie_mish_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        if hscene_xray == 0:
            jump lbl_effie_mish_revisit_3
        else:
            jump lbl_effie_mish_revisit_3_0
    elif 60 <= vrheadset_revisitcounter <= 89:
        if hscene_xray == 0:
            jump lbl_effie_mish_revisit_4
        else:
            jump lbl_effie_mish_revisit_4_0
    elif vrheadset_revisitcounter >= 90:
        if hscene_xray == 0:
            show bg hscene_effie_mish_1
        else:
            show bg hscene_effie_mish_1_0
        call screen scr_effie_mish_revisit
    else:
        if hscene_xray == 0:
            jump lbl_effie_mish_revisit_2
        else:
            jump lbl_effie_mish_revisit_2_0


####################
## Mish Stage 1
label lbl_effie_mish_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg hscene_effie_mish_1
    $ renpy.pause(0.3,hard=True)
    show bg hscene_effie_mish_2
    $ renpy.pause(0.1,hard=True)
    show bg hscene_effie_mish_3
    $ renpy.pause(0.3,hard=True)
    show bg hscene_effie_mish_4
    $ renpy.pause(0.3,hard=True)
    show bg hscene_effie_mish_5
    $ renpy.pause(0.3,hard=True)
    show bg hscene_effie_mish_6
    $ renpy.pause(0.1,hard=True)
    jump lbl_effie_mish_revisit_counter

####################
## Mish Stage 1 XRAY
label lbl_effie_mish_revisit_2_0:
    $ vrheadset_revisitcounter += 1
    show bg hscene_effie_mish_1_0
    $ renpy.pause(0.3,hard=True)
    show bg hscene_effie_mish_2_0
    $ renpy.pause(0.1,hard=True)
    show bg hscene_effie_mish_3_0
    $ renpy.pause(0.3,hard=True)
    show bg hscene_effie_mish_4_0
    $ renpy.pause(0.3,hard=True)
    show bg hscene_effie_mish_5_0
    $ renpy.pause(0.3,hard=True)
    show bg hscene_effie_mish_6_0
    $ renpy.pause(0.1,hard=True)
    jump lbl_effie_mish_revisit_counter


####################
## Mish Stage 2
label lbl_effie_mish_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg hscene_effie_mish_7
    $ renpy.pause(0.2,hard=True)
    show bg hscene_effie_mish_8
    $ renpy.pause(0.1,hard=True)
    show bg hscene_effie_mish_9
    $ renpy.pause(0.2,hard=True)
    show bg hscene_effie_mish_10
    $ renpy.pause(0.2,hard=True)
    jump lbl_effie_mish_revisit_counter


####################
## Mish Stage 2 XRAY
label lbl_effie_mish_revisit_3_0:
    $ vrheadset_revisitcounter += 1
    show bg hscene_effie_mish_7_0
    $ renpy.pause(0.2,hard=True)
    show bg hscene_effie_mish_8_0
    $ renpy.pause(0.1,hard=True)
    show bg hscene_effie_mish_9_0
    $ renpy.pause(0.2,hard=True)
    show bg hscene_effie_mish_10_0
    $ renpy.pause(0.2,hard=True)
    jump lbl_effie_mish_revisit_counter


####################
## Mish Stage 3
label lbl_effie_mish_revisit_4:
    $ vrheadset_revisitcounter += 1
    show bg hscene_effie_mish_11
    $ renpy.pause(0.1,hard=True)
    show bg hscene_effie_mish_12
    $ renpy.pause(0.1,hard=True)
    show bg hscene_effie_mish_13
    $ renpy.pause(0.1,hard=True)
    jump lbl_effie_mish_revisit_counter


####################
## Mish Stage 3 XRAY
label lbl_effie_mish_revisit_4_0:
    $ vrheadset_revisitcounter += 1
    show bg hscene_effie_mish_11_0
    $ renpy.pause(0.1,hard=True)
    show bg hscene_effie_mish_12_0
    $ renpy.pause(0.1,hard=True)
    show bg hscene_effie_mish_13_0
    $ renpy.pause(0.1,hard=True)
    jump lbl_effie_mish_revisit_counter

####################

screen scr_effie_mish_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_mish_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_mish_revisit_cumchoice")

label lbl_effie_mish_revisit_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_effie_mish_revisit_cumin
            else:
                jump lbl_effie_mish_revisit_cumin_0
        "Cum on her":
            jump lbl_effie_mish_revisit_cumout

label lbl_effie_mish_revisit_cumin:
    show bg hscene_effie_mish_cumin_1
    $ renpy.pause (1.8,hard=True)
    show bg hscene_effie_mish_cumin_6
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_7
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_8
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_9
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_10
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_11
    $ renpy.pause ()
    jump lbl_effie_mish_revisit_end

label lbl_effie_mish_revisit_cumin_0:
    show bg hscene_effie_mish_cumin_1_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_2_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_3_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_4_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_5_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_6_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_7_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_8_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_9_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_10_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_11_0
    $ renpy.pause ()
    jump lbl_effie_mish_revisit_end

label lbl_effie_mish_revisit_cumout:
    show bg hscene_effie_mish_cumout_1
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_2
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_3
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_4
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_5
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_6
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_7
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_8
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_9
    $ renpy.pause ()
    jump lbl_effie_mish_revisit_end

label lbl_effie_mish_revisit_end:
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
