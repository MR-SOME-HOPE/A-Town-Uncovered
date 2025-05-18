## Mina Standing Leg Up
label lbl_mina_standing_legup_revisit_0:
    #$ mina_standing_legup_counter = 0
    if hscene_xray == 0:
        jump lbl_mina_standing_legup_revisit_1
    else:
        jump lbl_mina_standing_legup_revisit_1_0

####################
## Stage 1
label lbl_mina_standing_legup_revisit_1:
    scene img_mina_standing_legup_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mina_standing_legup_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mina_standing_legup_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mina_standing_legup_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mina_standing_legup_revisit_1

image img_mina_standing_legup_stage_1:
    "bg minastandinglegup_1"
    pause 0.2
    "bg minastandinglegup_2"
    pause 0.2
    "bg minastandinglegup_3"
    pause 0.2
    "bg minastandinglegup_4"
    pause 0.2
    "bg minastandinglegup_2"
    pause 0.2
    repeat

image img_mina_standing_legup_stage_4:
    "bg minastandinglegup_1"
    pause 0.2
    "bg minastandinglegup_2"
    pause 0.2
    "bg minastandinglegup_3"
    pause 0.2
    "bg minastandinglegup_4"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_mina_standing_legup_revisit_1_0:
    scene img_mina_standing_legup_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mina_standing_legup_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mina_standing_legup_revisit_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mina_standing_legup_revisit_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mina_standing_legup_revisit_1_0

image img_mina_standing_legup_stage_1_0:
    "bg minastandinglegup_1_0"
    pause 0.2
    "bg minastandinglegup_2_0"
    pause 0.2
    "bg minastandinglegup_3_0"
    pause 0.2
    "bg minastandinglegup_4_0"
    pause 0.2
    "bg minastandinglegup_2_0"
    pause 0.2
    repeat

image img_mina_standing_legup_stage_4_0:
    "bg minastandinglegup_1_0"
    pause 0.2
    "bg minastandinglegup_2_0"
    pause 0.2
    "bg minastandinglegup_3_0"
    pause 0.2
    "bg minastandinglegup_4_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_mina_standing_legup_revisit_2:
    scene img_mina_standing_legup_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mina_standing_legup_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mina_standing_legup_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mina_standing_legup_revisit_2

image img_mina_standing_legup_stage_2:
    "bg minastandinglegup_5"
    pause 0.2
    "bg minastandinglegup_6"
    pause 0.1
    "bg minastandinglegup_8"
    pause 0.2
    "bg minastandinglegup_6"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_mina_standing_legup_revisit_2_0:
    scene img_mina_standing_legup_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mina_standing_legup_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mina_standing_legup_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mina_standing_legup_revisit_2_0

image img_mina_standing_legup_stage_2_0:
    "bg minastandinglegup_5_0"
    pause 0.2
    "bg minastandinglegup_6_0"
    pause 0.1
    "bg minastandinglegup_8_0"
    pause 0.2
    "bg minastandinglegup_6_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_mina_standing_legup_revisit_3:
    scene img_mina_standing_legup_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mina_standing_legup_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mina_standing_legup_revisit_3

image img_mina_standing_legup_stage_3:
    "bg minastandinglegup_9"
    pause 0.2
    "bg minastandinglegup_11"
    pause 0.1
    "bg minastandinglegup_10"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_mina_standing_legup_revisit_3_0:
    scene img_mina_standing_legup_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mina_standing_legup_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mina_standing_legup_revisit_3_0

image img_mina_standing_legup_stage_3_0:
    "bg minastandinglegup_9_0"
    pause 0.2
    "bg minastandinglegup_11_0"
    pause 0.1
    "bg minastandinglegup_10_0"
    pause 0.2
    repeat

####################
## Cum
label lbl_mina_standing_legup_revisit_cum:
    jump lbl_mina_standing_legup_revisit_cum_2

label lbl_mina_standing_legup_revisit_cum_2:
    #if hscene_xray == 0:
    #    scene bg minastandinglegup_1
    #else:
    #    scene bg minastandinglegup_1_0
    call screen scr_mina_standing_legup_revisit_cum_2

screen scr_mina_standing_legup_revisit_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mina_standing_legup_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mina_standing_legup_revisit_cumchoice")

label lbl_mina_standing_legup_revisit_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_mina_standing_legup_revisit_cumin
            else:
                jump lbl_mina_standing_legup_revisit_cumin_0
        "Cum on her":
            jump lbl_mina_standing_legup_revisit_cumout

####################
## Cum In
label lbl_mina_standing_legup_revisit_cumin:
    pov "{i}*Groans*{/i} Fuck-"
    pov "I'm cumming-"
    pov "Take it all..."
    scene bg minastandinglegup_6
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_7
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_8
    $ renpy.pause(1.5,hard=True)
    show bg minastandinglegup_14_1
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_14_2
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_14_3
    $ renpy.pause(0.3,hard=True)
    show bg minastandinglegup_14_4
    $ renpy.pause(0.8,hard=True)
    mina "Ahh- goddamn, [povname]."
    mina "{i}*Moans*{/i}"
    mina "You fat cock son-of-a-bitch."
    mina "{i}*Pants* *Gulp*{/i}"
    mina "Even dumping it all inside me, it's still overflowing."
    pov "I wanna make sure I give you my all, officer."
    mina "I can feel that."
    mina "Well, quick, go grab-"
    mina "Uhh- grab those papers to catch your cum."
    mina "Don't you dare leave any evidence in this room."
    scene black
    with fade
    if mina_points < 10:
        $ mina_points += 1
        $ renpy.notify("Your relationship with Officer Mina has increased")
    $ renpy.pause()
    "After cleaning up..."
    "And disposing all the evidence..."
    scene bg policestationinside_daynight
    with fade

    if gtime <= 1:
        jump lbl_policestationinside_day
    else:
        jump lbl_policestationinside_night

####################
## Cum In XRAY
label lbl_mina_standing_legup_revisit_cumin_0:
    pov "{i}*Groans*{/i} Fuck-"
    pov "I'm cumming-"
    pov "Take it all..."
    scene bg minastandinglegup_6_0
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_7_0
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_8_0
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_13_1
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_13_2
    $ renpy.pause(0.2,hard=True)
    show bg minastandinglegup_13_3
    $ renpy.pause(0.3,hard=True)
    show bg minastandinglegup_13_4
    $ renpy.pause(0.3,hard=True)
    show bg minastandinglegup_13_5
    $ renpy.pause(0.3,hard=True)
    show bg minastandinglegup_13_6
    $ renpy.pause(0.3,hard=True)
    show bg minastandinglegup_13_7
    $ renpy.pause(0.3,hard=True)
    show bg minastandinglegup_13_8
    $ renpy.pause(0.3,hard=True)
    show bg minastandinglegup_13_9
    $ renpy.pause(0.3,hard=True)
    show bg minastandinglegup_13_10
    $ renpy.pause(0.8,hard=True)
    mina "Ahh- goddamn, [povname]."
    mina "{i}*Moans*{/i}"
    mina "You fat cock son-of-a-bitch."
    mina "{i}*Pants* *Gulp*{/i}"
    mina "Even dumping it all inside me, it's still overflowing."
    pov "I wanna make sure I give you my all, officer."
    mina "I can feel that."
    mina "Well, quick, go grab-"
    mina "Uhh- grab those papers to catch your cum."
    mina "Don't you dare leave any evidence in this room."
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Missionary Cum Out
label lbl_mina_standing_legup_revisit_cumout:
    pov "I- I'm about to cum-"
    if hscene_xray == 0:
        scene img_mina_standing_legup_stage_4

    else:
        scene img_mina_standing_legup_stage_4_0

    pov "I'm gonna cum all over you!"
    if hscene_xray == 0:
        show bg minastandinglegup_15
    else:
        show bg minastandinglegup_15_0
    mina "Don't you fucking dare cum outside of me!"
    mina "You're not gonna leave any evidence that we were here, you hear?"
    if hscene_xray == 0:
        hide bg minastandinglegup_15
    else:
        hide bg minastandinglegup_15_0
    pov "Shit-"

    if hscene_xray == 0:
        jump lbl_mina_standing_legup_revisit_cumin
    else:
        jump lbl_mina_standing_legup_revisit_cumin_0
