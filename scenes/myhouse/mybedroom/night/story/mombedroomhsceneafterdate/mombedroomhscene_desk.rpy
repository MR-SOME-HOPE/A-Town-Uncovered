####################
## Desk Pussy Fuck
label lbl_mom_bedroom_hscene_after_desk_pussy:

    scene bg mombedroomhscene_desk_pussy_1
    with dissolve
    play sex_sounds penetration_c_03 noloop
    mum "I'm all yours, [povname]..."
    if winc == 0:
        mum "Fuck me silly."
    else:
        mum "Fuck mommy silly."

    jump lbl_mom_bedroom_hscene_after_desk_pussy_0

label lbl_mom_bedroom_hscene_after_desk_pussy_0:
    #$ mom_bedroom_hscene_desk_pussy_counter = 0
    if hscene_xray == 0:
        jump lbl_mom_bedroom_hscene_after_desk_pussy_1
    else:
        jump lbl_mom_bedroom_hscene_after_desk_pussy_1_0

####################
## Desk Pussy Fuck Stage 1
label lbl_mom_bedroom_hscene_after_desk_pussy_1:
    #$ mom_bedroom_hscene_desk_pussy_counter += 1
    scene img_mom_bedroom_hscene_after_desk_pussy_stage_1
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_desk_pussy_1
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_2
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_3
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_4
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_5
    #stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_desk_pussy_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_cum
    #elif skill_sta <= 14 and mom_bedroom_hscene_desk_pussy_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_2
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_pussy_counter == 10:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_2
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_1

image img_mom_bedroom_hscene_after_desk_pussy_stage_1:
    "bg mombedroomhscene_desk_pussy_1"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_2"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_3"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_4"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_5"
    pause 0.2
    repeat

####################
## Desk Pussy Fuck Stage 1 XRAY
label lbl_mom_bedroom_hscene_after_desk_pussy_1_0:
    #$ mom_bedroom_hscene_desk_pussy_counter += 1
    scene img_mom_bedroom_hscene_after_desk_pussy_stage_1_0
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_desk_pussy_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_5_0
    #stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_desk_pussy_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_cum
    #elif skill_sta <= 14 and mom_bedroom_hscene_desk_pussy_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_2_0
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_pussy_counter == 10:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_2_0
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_1_0

image img_mom_bedroom_hscene_after_desk_pussy_stage_1_0:
    "bg mombedroomhscene_desk_pussy_1_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_2_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_3_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_4_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_5_0"
    pause 0.2
    repeat

####################
## Desk Pussy Fuck Stage 2
label lbl_mom_bedroom_hscene_after_desk_pussy_2:
    #$ mom_bedroom_hscene_desk_pussy_counter += 1
    scene img_mom_bedroom_hscene_after_desk_pussy_stage_2
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_desk_pussy_1
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_3
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_4
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_5
    #stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mom_bedroom_hscene_desk_pussy_counter == 14:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_cum
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_pussy_counter == 16:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_3
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_2

image img_mom_bedroom_hscene_after_desk_pussy_stage_2:
    "bg mombedroomhscene_desk_pussy_1"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_3"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_4"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_5"
    pause 0.2
    repeat

####################
## Desk Pussy Fuck Stage 2 XRAY
label lbl_mom_bedroom_hscene_after_desk_pussy_2_0:
    #$ mom_bedroom_hscene_desk_pussy_counter += 1
    scene img_mom_bedroom_hscene_after_desk_pussy_stage_2_0
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_desk_pussy_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_5_0
    #stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mom_bedroom_hscene_desk_pussy_counter == 14:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_cum
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_pussy_counter == 16:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_3_0
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_2_0

image img_mom_bedroom_hscene_after_desk_pussy_stage_2_0:
    "bg mombedroomhscene_desk_pussy_1_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_3_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_4_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_5_0"
    pause 0.2
    repeat

####################
## Desk Pussy Fuck Stage 3
label lbl_mom_bedroom_hscene_after_desk_pussy_3:
    #$ mom_bedroom_hscene_desk_pussy_counter += 1
    scene img_mom_bedroom_hscene_after_desk_pussy_stage_3
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_desk_pussy_1
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_4
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_5
    #stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mom_bedroom_hscene_desk_pussy_counter == 24:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_cum
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_3

image img_mom_bedroom_hscene_after_desk_pussy_stage_3:
    "bg mombedroomhscene_desk_pussy_1"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_4"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_5"
    pause 0.2
    repeat

####################
## Desk Pussy Fuck Stage 3 XRAY
label lbl_mom_bedroom_hscene_after_desk_pussy_3_0:
    #$ mom_bedroom_hscene_desk_pussy_counter += 1
    scene img_mom_bedroom_hscene_after_desk_pussy_stage_3_0
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_desk_pussy_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_pussy_5_0
    #stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mom_bedroom_hscene_desk_pussy_counter == 24:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_cum
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_pussy_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_pussy_3_0

image img_mom_bedroom_hscene_after_desk_pussy_stage_3_0:
    "bg mombedroomhscene_desk_pussy_1_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_4_0"
    pause 0.2
    "bg mombedroomhscene_desk_pussy_5_0"
    pause 0.2
    repeat

####################
## Desk Pussy Fuck Cum
label lbl_mom_bedroom_hscene_after_desk_pussy_cum:
    if mum_points <= 8:
        jump lbl_mom_bedroom_hscene_after_desk_pussy_cum_2
    else:
        jump lbl_mom_bedroom_hscene_after_desk_pussy_cum_3

label lbl_mom_bedroom_hscene_after_desk_pussy_cum_2:
    #if hscene_xray == 0:
    #    scene bg mombedroomhscene_desk_pussy_1
    #else:
    #    scene bg mombedroomhscene_desk_pussy_1_0
    call screen scr_mom_bedroom_hscene_after_desk_pussy_cum

screen scr_mom_bedroom_hscene_after_desk_pussy_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_pussy_cumchoice")

label lbl_mom_bedroom_hscene_after_desk_pussy_cum_3:
    #if hscene_xray == 0:
    #    scene bg mombedroomhscene_desk_pussy_1
    #else:
    #    scene bg mombedroomhscene_desk_pussy_1_0
    call screen scr_mom_bedroom_hscene_after_desk_pussy_cum_2

screen scr_mom_bedroom_hscene_after_desk_pussy_cum_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_scenechoice_desk_pussy")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_pussy_cumchoice")

label lbl_mom_bedroom_hscene_after_desk_pussy_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_mom_bedroom_hscene_after_desk_pussy_cumin
            else:
                jump lbl_mom_bedroom_hscene_after_desk_pussy_cumin_0
        "Cum on her":
            scene bg mombedroomhscene_desk_pussy_17
            $ renpy.pause(0.3,hard=True)

            jump lbl_mom_bedroom_hscene_after_desk_cumout

####################
## Desk Pussy Fuck Cum In
label lbl_mom_bedroom_hscene_after_desk_pussy_cumin:
    queue sex_sounds [vagina_squirt_short_02,vagina_squirt_short_05,vagina_squirt_long_03,vagina_squirt_long_04] noloop
    scene bg mombedroomhscene_desk_pussy_6
    $ renpy.pause(1.5,hard=True)
    show bg mombedroomhscene_desk_pussy_13
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_14
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_15
    stop sex_sounds fadeout 1.0
    $ renpy.pause()
    show bg mombedroomhscene_desk_pussy_16
    play sex_sounds mouth_puff_02 noloop
    mum "{i}*Pants*{/i}"
    play sex_sounds vagina_squirt_short_06 noloop
    mum "Why... why did you cum inside me..?"
    if winc == 0:
        pov "Sorry, [missus]. I couldn't stop myself."
    else:
        pov "Sorry, mom. I couldn't stop myself."
    mum "You're... lucky that... I'm on... the pill."

    jump lbl_mybedroom_night_sleep

####################
## Desk Pussy Fuck Cum In XRAY
label lbl_mom_bedroom_hscene_after_desk_pussy_cumin_0:
    queue sex_sounds [vagina_squirt_short_02,vagina_squirt_short_05,vagina_squirt_long_03,vagina_squirt_long_04] noloop
    scene bg mombedroomhscene_desk_pussy_6_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_7_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_8_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_9_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_10_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_11_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_12_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_13_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_14_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_pussy_15_0
    stop sex_sounds fadeout 1.0
    $ renpy.pause()
    show bg mombedroomhscene_desk_pussy_16_0
    play sex_sounds mouth_puff_02 noloop
    mum "{i}*Pants*{/i}"
    play sex_sounds vagina_squirt_short_06 noloop
    mum "Why... why did you cum inside me..?"
    if winc == 0:
        pov "Sorry, [missus]. I couldn't stop myself."
    else:
        pov "Sorry, mom. I couldn't stop myself."
    mum "You're... lucky that... I'm on... the pill."

    jump lbl_mybedroom_night_sleep

####################
## Desk Pussy Fuck Cum Out
label lbl_mom_bedroom_hscene_after_desk_cumout:
    queue sex_sounds [penis_cum_06,penis_cum_03,body_collide_naked_08] noloop
    scene bg mombedroomhscene_desk_cumout_1
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_2
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_3
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_4
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_5
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_6
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_7
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_8
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_9
    #stop sex_sounds fadeout 1.0
    $ renpy.pause()
    show bg mombedroomhscene_desk_cumout_10
    play sex_sounds mouth_puff_02 noloop
    mum "{i}*Pants*{/i} Thanks for making a gigantic, pain-in-the-ass mess."
    mum "How- How am I suppose to get to the bathroom without staining the carpet?"
    if winc == 0:
        pov "Your back looks amazing, [missus]."
    else:
        pov "Your back looks amazing, mom."
    mum "It's not like you painted the Mona Lisa on there."

    jump lbl_mybedroom_night_setup

####################
## Desk Pussy Fuck Next
label lbl_mom_bedroom_hscene_after_desk_pussy_next:
    stop sex_sounds
    show bg mombedroomhscene_desk_pussy_17
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_1
    $ renpy.pause(0.3,hard=True)
    if winc == 0:
        pov "Let's move to the bed, [missus]."
    else:
        pov "Let's move to the bed, mom."

    jump lbl_mom_bedroom_hscene_after_mish
