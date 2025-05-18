## BJ
label lbl_effie_bj_revisit_1:
    scene bg hsceneeffiebj_1
    with fade
    show bg hsceneeffiebj_1
    $ renpy.pause ()
    show bg hsceneeffiebj_2
    $ renpy.pause ()
    show bg hsceneeffiebj_3
    eff "Can I put this in my mouth? I love feeling it grow hard in my throat."
    show bg hsceneeffiebj_2
    pov "Go ahead."
    show bg hsceneeffiebj_4
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_4_1
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_5
    $ renpy.pause (1.5,hard=True)
    show bg hsceneeffiebj_5_1
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_5_2
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_6_1
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffiebj_6
    $ renpy.pause ()
    jump lbl_effie_bj_revisit_continue

label lbl_effie_bj_revisit_continue:
    $ vrheadset_revisitcounter = 0

label lbl_effie_bj_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_effie_bj_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_effie_bj_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_effie_bj_revisit
    else:
        jump lbl_effie_bj_revisit_1_1


####################
## BJ Stage 1
label lbl_effie_bj_revisit_1_1:
    $ vrheadset_revisitcounter += 1
    show bg hsceneeffiebj_10
    $ renpy.pause(0.3,hard=True)
    show bg hsceneeffiebj_10_1
    $ renpy.pause(0.1,hard=True)
    show bg hsceneeffiebj_11
    $ renpy.pause(0.1,hard=True)
    show bg hsceneeffiebj_11_1
    $ renpy.pause(0.3,hard=True)
    show bg hsceneeffiebj_10_1
    $ renpy.pause(0.3,hard=True)
    jump lbl_effie_bj_revisit_counter

####################
## BJ Stage 2
label lbl_effie_bj_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg hsceneeffiebj_10
    $ renpy.pause(0.3,hard=True)
    show bg hsceneeffiebj_11
    $ renpy.pause(0.1,hard=True)
    show bg hsceneeffiebj_11_1
    $ renpy.pause(0.2,hard=True)
    show bg hsceneeffiebj_10_1
    $ renpy.pause(0.2,hard=True)
    jump lbl_effie_bj_revisit_counter


####################
## BJ Stage 3
label lbl_effie_bj_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg hsceneeffiebj_10
    $ renpy.pause(0.2,hard=True)
    show bg hsceneeffiebj_11
    $ renpy.pause(0.1,hard=True)
    show bg hsceneeffiebj_10_1
    $ renpy.pause(0.2,hard=True)
    jump lbl_effie_bj_revisit_counter


screen scr_effie_bj_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_bj_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_bj_revisit_cum")

####################
## BJ Cum
label lbl_effie_bj_revisit_cum:
    show bg hsceneeffiebj_11
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_1
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_2
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_3
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_4
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_5
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_6
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_7
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_13
    $ renpy.pause (1,hard=True)
    show bg hsceneeffiebj_14
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_15
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_16
    $ renpy.pause ()
    show bg hsceneeffiebj_20
    eff "I haven't had a dick like that in a long time."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    
    jump lbl_vrheadset_character_selection
