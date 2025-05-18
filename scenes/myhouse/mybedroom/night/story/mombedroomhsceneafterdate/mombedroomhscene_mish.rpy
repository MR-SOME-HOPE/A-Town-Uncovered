####################
## Missionary (Mish)
label lbl_mom_bedroom_hscene_after_mish:

    scene bg mombedroomhscene_mish_31
    with fade

label lbl_mom_bedroom_hscene_after_mish_choice:

    menu:
        "Pussy fuck":
            jump lbl_mom_bedroom_hscene_after_mish_pussy
        "Anal fuck":
            jump lbl_mom_bedroom_hscene_after_mishanal

####################
## Missionary Pussy Pre
label lbl_mom_bedroom_hscene_after_mish_pussy:
    show bg mombedroomhscene_mish_26
    if winc == 0:
        pov "Ready, [missus]?"
    else:
        pov "Ready, Mom?"
    play sex_sounds penetration_a_01 noloop
    show bg mombedroomhscene_mish_27
    mum "What are you talking about? You're already poking me with-"
    play sex_sounds vagina_insertion_b_02 noloop
    if hscene_xray == 0:
        show bg mombedroomhscene_mish_28
        with vpunch
    else:
        show bg mombedroomhscene_mish_28_0
        with vpunch
    play sex_sounds penetration_a_08 noloop

    mum "Ahh... fuck..."
    mum "[povname]?"
    if winc == 0:
        mum "Fuck your [mumrole]'s pussy.. fuck me with that big cock of yours."
    else:
        mum "Fuck your mommy's pussy.. fuck me with that big cock of yours."
    mum "No mercy, okay, baby?"

    jump lbl_mom_bedroom_hscene_after_mish_0

label lbl_mom_bedroom_hscene_after_mish_0:
    #$ mom_bedroom_hscene_mish_counter = 0
    if hscene_xray == 0:
        jump lbl_mom_bedroom_hscene_after_mish_1
    else:
        jump lbl_mom_bedroom_hscene_after_mish_1_0

####################
## Missionary Stage 1
label lbl_mom_bedroom_hscene_after_mish_1:
    #$ mom_bedroom_hscene_mish_counter += 1
    scene img_mom_bedroom_hscene_after_mish_stage_1
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_mish_1
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_2
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_3
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_4
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_5
    ##stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_mish_counter == 4:
    #    jump lbl_mom_bedroom_hscene_after_mish_cum
    #elif skill_sta <= 14 and mom_bedroom_hscene_mish_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_mish_2
    #elif skill_sta <= 20 and mom_bedroom_hscene_mish_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_mish_2
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mish_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_1

image img_mom_bedroom_hscene_after_mish_stage_1:
    "bg mombedroomhscene_mish_1"
    pause 0.2
    "bg mombedroomhscene_mish_2"
    pause 0.2
    "bg mombedroomhscene_mish_3"
    pause 0.2
    "bg mombedroomhscene_mish_4"
    pause 0.2
    "bg mombedroomhscene_mish_5"
    pause 0.2
    repeat

####################
## Missionary Stage 1 XRAY
label lbl_mom_bedroom_hscene_after_mish_1_0:
    #$ mom_bedroom_hscene_mish_counter += 1
    scene img_mom_bedroom_hscene_after_mish_stage_1_0
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_mish_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_5_0
    ##stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_mish_counter == 4:
    #    jump lbl_mom_bedroom_hscene_after_mish_cum
    #elif skill_sta <= 14 and mom_bedroom_hscene_mish_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_mish_2_0
    #elif skill_sta <= 20 and mom_bedroom_hscene_mish_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_mish_2_0
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mish_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_1_0

image img_mom_bedroom_hscene_after_mish_stage_1_0:
    "bg mombedroomhscene_mish_1_0"
    pause 0.2
    "bg mombedroomhscene_mish_2_0"
    pause 0.2
    "bg mombedroomhscene_mish_3_0"
    pause 0.2
    "bg mombedroomhscene_mish_4_0"
    pause 0.2
    "bg mombedroomhscene_mish_5_0"
    pause 0.2
    repeat


####################
## Missionary Stage 2
label lbl_mom_bedroom_hscene_after_mish_2:
    #$ mom_bedroom_hscene_mish_counter += 1
    scene img_mom_bedroom_hscene_after_mish_stage_2
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_mish_6
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_7
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_8
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_9
    ##stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mom_bedroom_hscene_mish_counter == 14:
    #    jump lbl_mom_bedroom_hscene_after_mish_cum
    #elif skill_sta <= 20 and mom_bedroom_hscene_mish_counter == 16:
    #    jump lbl_mom_bedroom_hscene_after_mish_3
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mish_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_2

image img_mom_bedroom_hscene_after_mish_stage_2:
    "bg mombedroomhscene_mish_6"
    pause 0.2
    "bg mombedroomhscene_mish_7"
    pause 0.2
    "bg mombedroomhscene_mish_8"
    pause 0.2
    "bg mombedroomhscene_mish_9"
    pause 0.2
    repeat

####################
## Missionary Stage 2 XRAY
label lbl_mom_bedroom_hscene_after_mish_2_0:
    #$ mom_bedroom_hscene_mish_counter += 1
    scene img_mom_bedroom_hscene_after_mish_stage_2_0
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_mish_6_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_7_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_8_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_9_0
    ##stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mom_bedroom_hscene_mish_counter == 14:
    #    jump lbl_mom_bedroom_hscene_after_mish_cum
    #elif skill_sta <= 20 and mom_bedroom_hscene_mish_counter == 16:
    #    jump lbl_mom_bedroom_hscene_after_mish_3_0
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mish_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_2_0

image img_mom_bedroom_hscene_after_mish_stage_2_0:
    "bg mombedroomhscene_mish_6_0"
    pause 0.2
    "bg mombedroomhscene_mish_7_0"
    pause 0.2
    "bg mombedroomhscene_mish_8_0"
    pause 0.2
    "bg mombedroomhscene_mish_9_0"
    pause 0.2
    repeat

####################
## Missionary Stage 3
label lbl_mom_bedroom_hscene_after_mish_3:
    #$ mom_bedroom_hscene_mish_counter += 1
    scene img_mom_bedroom_hscene_after_mish_stage_3
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_mish_10
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_11
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_12
    ##stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mom_bedroom_hscene_mish_counter == 24:
    #    jump lbl_mom_bedroom_hscene_after_mish_cum
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mish_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_3

image img_mom_bedroom_hscene_after_mish_stage_3:
    "bg mombedroomhscene_mish_10"
    pause 0.2
    "bg mombedroomhscene_mish_11"
    pause 0.2
    "bg mombedroomhscene_mish_12"
    pause 0.2
    repeat

####################
## Missionary Stage 3 XRAY
label lbl_mom_bedroom_hscene_after_mish_3_0:
    #$ mom_bedroom_hscene_mish_counter += 1
    scene img_mom_bedroom_hscene_after_mish_stage_3_0
    queue sex_sounds [vagina_queff_03,vagina_queff_04, penetration_b_05,penetration_c_03,penetration_a_07,vagina_touch_04,body_slap_soft_06]
    #show bg mombedroomhscene_mish_10_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_11_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mish_12_0
    ##stop sex_sounds fadeout 1.0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mom_bedroom_hscene_mish_counter == 24:
    #    jump lbl_mom_bedroom_hscene_after_mish_cum
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mish_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mish_3_0

image img_mom_bedroom_hscene_after_mish_stage_3_0:
    "bg mombedroomhscene_mish_10_0"
    pause 0.2
    "bg mombedroomhscene_mish_11_0"
    pause 0.2
    "bg mombedroomhscene_mish_12_0"
    pause 0.2
    repeat

####################
## Missionary Cum
label lbl_mom_bedroom_hscene_after_mish_cum:
    if mum_points <= 6 or sister_points <= 6:
        jump lbl_mom_bedroom_hscene_after_mish_cum_2
    else:
        jump lbl_mom_bedroom_hscene_after_mish_cum_3

label lbl_mom_bedroom_hscene_after_mish_cum_2:
    #if hscene_xray == 0:
    #    scene bg mombedroomhscene_mish_13
    #else:
    #    scene bg mombedroomhscene_mish_13_0
    call screen scr_mom_bedroom_hscene_after_mish_cum_2

screen scr_mom_bedroom_hscene_after_mish_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_mish_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_mish_cumchoice")

label lbl_mom_bedroom_hscene_after_mish_cum_3:
    #if hscene_xray == 0:
    #    scene bg mombedroomhscene_mish_13
    #else:
    #    scene bg mombedroomhscene_mish_13_0
    call screen scr_mom_bedroom_hscene_after_mish_cum_3

screen scr_mom_bedroom_hscene_after_mish_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_scenechoice_mish")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_mish_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_mish_cumchoice")

label lbl_mom_bedroom_hscene_after_mish_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_mom_bedroom_hscene_after_mish_cumin
            else:
                jump lbl_mom_bedroom_hscene_after_mish_cumin_0
        "Cum on her":
            jump lbl_mom_bedroom_hscene_after_mish_cumout

####################
## Missionary Cum In
label lbl_mom_bedroom_hscene_after_mish_cumin:
    queue sex_sounds [vagina_squirt_short_02,vagina_squirt_short_05,vagina_squirt_long_03,vagina_squirt_long_04] noloop
    scene bg mombedroomhscene_mish_13
    $ renpy.pause(1.5,hard=True)
    show bg mombedroomhscene_mish_20
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_21
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_22
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_23
    stop sex_sounds fadeout 1.0
    $ renpy.pause()
    play sex_sounds vagina_squirt_short_06 noloop
    show bg mombedroomhscene_mish_24
    mum "Why... why did you cum inside me..?"
    if winc == 0:
        pov "Sorry, [missus]. I couldn't stop myself."
    else:
        pov "Sorry, Mom. I couldn't stop myself."
    show bg mombedroomhscene_mish_25
    mum "You're... lucky that... I'm on... the pill."

    jump lbl_mybedroom_night_sleep

####################
## Missionary Cum In XRAY
label lbl_mom_bedroom_hscene_after_mish_cumin_0:
    queue sex_sounds [vagina_squirt_short_02,vagina_squirt_short_05,vagina_squirt_long_03,vagina_squirt_long_04] noloop
    scene bg mombedroomhscene_mish_13_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_14_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_15_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_16_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_17_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_18_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_19_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_20_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_21_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_22_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_23_0
    stop sex_sounds fadeout 1.0
    $ renpy.pause()
    play sex_sounds vagina_squirt_short_06 noloop
    show bg mombedroomhscene_mish_24_0
    mum "Why... why did you cum inside me..?"
    if winc == 0:
        pov "Sorry, [missus]. I couldn't stop myself."
    else:
        pov "Sorry, Mom. I couldn't stop myself."
    show bg mombedroomhscene_mish_25_0
    mum "You're... lucky that... I'm on... the pill."

    jump lbl_mybedroom_night_sleep

####################
## Missionary Cum Out
label lbl_mom_bedroom_hscene_after_mish_cumout:
    queue sex_sounds [penis_cum_06,penis_cum_03,body_collide_naked_08] noloop
    scene bg mombedroomhscene_mish_30
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_31
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_32
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_33
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_34
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_35
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_36
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_37
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_38
    #stop sex_sounds fadeout 1.0
    $ renpy.pause()
    show bg mombedroomhscene_mish_39
    mum "Thanks for making a gigantic, pain-in-the-ass mess for me to wash."
    show bg mombedroomhscene_mish_40
    mum "But it was so worth it..."

    jump lbl_mybedroom_night_sleep

####################
## Missionary Next
label lbl_mom_bedroom_hscene_after_mish_next:
    stop sex_sounds
    show bg mombedroomhscene_mish_30
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_31
    $ renpy.pause(0.3,hard=True)
    if winc == 0:
        pov "Let's move to the desk, [missus]."
    else:
        pov "Let's move to the desk, Mom."

    jump lbl_mom_bedroom_hscene_after_desk
