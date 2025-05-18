####################
## Missionary Anal Pre
label lbl_mom_bedroom_hscene_after_mishanal:
    show bg mombedroomhscene_mishanal_24
    if winc == 0:
        pov "Ready, [missus]?"
    else:
        pov "Ready, Mom?"
    show bg mombedroomhscene_mishanal_25
    mum "What are you talking about? You're already poking me with-"
    if hscene_xray == 0:
        show bg mombedroomhscene_mishanal_26
        with vpunch
    else:
        show bg mombedroomhscene_mishanal_26_0
        with vpunch
    mum "Ahh... fuck..."
    mum "[povname]?"
    if winc == 0:
        mum "Fuck your [mumrole]'s asshole.. fuck me with that big cock of yours."
    else:
        mum "Fuck your mommy's asshole.. fuck me with that big cock of yours."
    mum "No mercy, okay, baby?"

    jump lbl_mom_bedroom_hscene_after_mishanal_0

label lbl_mom_bedroom_hscene_after_mishanal_0:
    #$ mom_bedroom_hscene_mishanal_counter = 0
    if hscene_xray == 0:
        jump lbl_mom_bedroom_hscene_after_mishanal_1
    else:
        jump lbl_mom_bedroom_hscene_after_mishanal_1_0

####################
## Missionary Anal Stage 1
label lbl_mom_bedroom_hscene_after_mishanal_1:
    scene img_mom_bedroom_hscene_after_mishanal_stage_1
    #$ mom_bedroom_hscene_mishanal_counter += 1
    #show bg mombedroomhscene_mishanal_1
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_2
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_3
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_4
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_mishanal_counter == 4:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_cum
    #elif skill_sta <= 14 and mom_bedroom_hscene_mishanal_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_2
    #elif skill_sta <= 20 and mom_bedroom_hscene_mishanal_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_2
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_1

image img_mom_bedroom_hscene_after_mishanal_stage_1:
    "bg mombedroomhscene_mishanal_1"
    pause 0.2
    "bg mombedroomhscene_mishanal_2"
    pause 0.2
    "bg mombedroomhscene_mishanal_3"
    pause 0.2
    "bg mombedroomhscene_mishanal_4"
    pause 0.2
    "bg mombedroomhscene_mishanal_5"
    pause 0.2
    repeat

####################
## Missionary Anal Stage 1 XRAY
label lbl_mom_bedroom_hscene_after_mishanal_1_0:
    scene img_mom_bedroom_hscene_after_mishanal_stage_1_0
    #$ mom_bedroom_hscene_mishanal_counter += 1
    #show bg mombedroomhscene_mishanal_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_mishanal_counter == 4:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_cum
    #elif skill_sta <= 14 and mom_bedroom_hscene_mishanal_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_2_0
    #elif skill_sta <= 20 and mom_bedroom_hscene_mishanal_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_2_0
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_1_0

image img_mom_bedroom_hscene_after_mishanal_stage_1_0:
    "bg mombedroomhscene_mishanal_1_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_2_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_3_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_4_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_5_0"
    pause 0.2
    repeat

####################
## Missionary Anal Stage 2
label lbl_mom_bedroom_hscene_after_mishanal_2:
    scene img_mom_bedroom_hscene_after_mishanal_stage_2
    #$ mom_bedroom_hscene_mishanal_counter += 1
    #show bg mombedroomhscene_mishanal_6
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_7
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_8
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_9
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mom_bedroom_hscene_mishanal_counter == 14:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_cum
    #elif skill_sta <= 20 and mom_bedroom_hscene_mishanal_counter == 16:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_3
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_2

image img_mom_bedroom_hscene_after_mishanal_stage_2:
    "bg mombedroomhscene_mishanal_6"
    pause 0.2
    "bg mombedroomhscene_mishanal_7"
    pause 0.2
    "bg mombedroomhscene_mishanal_8"
    pause 0.2
    "bg mombedroomhscene_mishanal_9"
    pause 0.2
    repeat

####################
## Missionary Anal Stage 2 XRAY
label lbl_mom_bedroom_hscene_after_mishanal_2_0:
    scene img_mom_bedroom_hscene_after_mishanal_stage_2_0
    #$ mom_bedroom_hscene_mishanal_counter += 1
    #show bg mombedroomhscene_mishanal_6_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_7_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_8_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_9_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mom_bedroom_hscene_mishanal_counter == 14:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_cum
    #elif skill_sta <= 20 and mom_bedroom_hscene_mishanal_counter == 16:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_3_0
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_2_0

image img_mom_bedroom_hscene_after_mishanal_stage_2_0:
    "bg mombedroomhscene_mishanal_6_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_7_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_8_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_9_0"
    pause 0.2
    repeat

####################
## Missionary Anal Stage 3
label lbl_mom_bedroom_hscene_after_mishanal_3:
    scene img_mom_bedroom_hscene_after_mishanal_stage_3
    #$ mom_bedroom_hscene_mishanal_counter += 1
    #show bg mombedroomhscene_mishanal_10
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_11
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_12
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mom_bedroom_hscene_mishanal_counter == 24:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_cum
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_3

image img_mom_bedroom_hscene_after_mishanal_stage_3:
    "bg mombedroomhscene_mishanal_10"
    pause 0.2
    "bg mombedroomhscene_mishanal_11"
    pause 0.2
    "bg mombedroomhscene_mishanal_12"
    pause 0.2
    repeat

####################
## Missionary Anal Stage 3 XRAY
label lbl_mom_bedroom_hscene_after_mishanal_3_0:
    scene img_mom_bedroom_hscene_after_mishanal_stage_3_0
    #$ mom_bedroom_hscene_mishanal_counter += 1
    #show bg mombedroomhscene_mishanal_10_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_11_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_mishanal_12_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mom_bedroom_hscene_mishanal_counter == 24:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_cum
    #else:
    #    jump lbl_mom_bedroom_hscene_after_mishanal_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_mishanal_3_0

image img_mom_bedroom_hscene_after_mishanal_stage_3_0:
    "bg mombedroomhscene_mishanal_10_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_11_0"
    pause 0.2
    "bg mombedroomhscene_mishanal_12_0"
    pause 0.2
    repeat

####################
## Missionary Anal Cum
label lbl_mom_bedroom_hscene_after_mishanal_cum:
    if mum_points <= 6:
        jump lbl_mom_bedroom_hscene_after_mishanal_cum_2
    else:
        jump lbl_mom_bedroom_hscene_after_mishanal_cum_3

label lbl_mom_bedroom_hscene_after_mishanal_cum_2:
    #if hscene_xray == 0:
    #    scene bg mombedroomhscene_mishanal_13
    #else:
    #    scene bg mombedroomhscene_mishanal_13_0
    call screen scr_mom_bedroom_hscene_after_mishanal_cum_2

screen scr_mom_bedroom_hscene_after_mishanal_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_mishanal_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_mishanal_cumchoice")

label lbl_mom_bedroom_hscene_after_mishanal_cum_3:
    #if hscene_xray == 0:
    #    scene bg mombedroomhscene_mishanal_13
    #else:
    #    scene bg mombedroomhscene_mishanal_13_0
    call screen scr_mom_bedroom_hscene_after_mishanal_cum_3

screen scr_mom_bedroom_hscene_after_mishanal_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_scenechoice_mishanal")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_mishanal_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_mishanal_cumchoice")

label lbl_mom_bedroom_hscene_after_mishanal_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_mom_bedroom_hscene_after_mishanal_cumin
            else:
                jump lbl_mom_bedroom_hscene_after_mishanal_cumin_0
        "Cum on her":
            jump lbl_mom_bedroom_hscene_after_mish_cumout

####################
## Missionary Anal Cum In
label lbl_mom_bedroom_hscene_after_mishanal_cumin:
    stop sex_sounds#TODO
    scene bg mombedroomhscene_mishanal_13
    $ renpy.pause(1.5,hard=True)
    show bg mombedroomhscene_mishanal_19
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_20
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_21
    $ renpy.pause()
    show bg mombedroomhscene_mishanal_22
    mum "{i}*Pants*{/i}"
    mum "You filled me up... so much..."
    if winc == 0:
        pov "Sorry, [missus]. I couldn't stop myself."
    else:
        pov "Sorry, Mom. I couldn't stop myself."
    show bg mombedroomhscene_mishanal_23
    mum "At... least it wasn't in my vagina..."

    jump lbl_mybedroom_night_sleep

####################
## Missionary Anal Cum In XRAY
label lbl_mom_bedroom_hscene_after_mishanal_cumin_0:
    stop sex_sounds#TODO
    scene bg mombedroomhscene_mishanal_13_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_14_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_15_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_16_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_17_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_18_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_19_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_20_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mishanal_21_0
    $ renpy.pause()
    show bg mombedroomhscene_mishanal_22_0
    mum "You filled me up... so much..."
    if winc == 0:
        pov "Sorry, [missus]. I couldn't stop myself."
    else:
        pov "Sorry, Mom. I couldn't stop myself."
    show bg mombedroomhscene_mishanal_23_0
    mum "At... least it wasn't in my vagina..."

    jump lbl_mybedroom_night_sleep

####################
## Missionary Anal Next
label lbl_mom_bedroom_hscene_after_mishanal_next:
    stop sex_sounds
    scene bg mombedroomhscene_mishanal_28
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_mish_31
    $ renpy.pause(0.3,hard=True)
    if winc == 0:
        pov "Let's move to the desk, [missus]."
    else:
        pov "Let's move to the desk, Mom."

    jump lbl_mom_bedroom_hscene_after_desk
