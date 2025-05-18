####################
## Desk Anal Fuck
label lbl_mom_bedroom_hscene_after_desk_anal:
    stop sex_sounds
    scene bg mombedroomhscene_desk_anal_1
    with dissolve
    mum "I'm all yours, [povname]..."
    if winc == 0:
        mum "Fuck me silly."
    else:
        mum "Fuck Mommy silly."

    jump lbl_mom_bedroom_hscene_after_desk_anal_0

label lbl_mom_bedroom_hscene_after_desk_anal_0:
    #$ mom_bedroom_hscene_desk_anal_counter = 0
    if hscene_xray == 0:
        jump lbl_mom_bedroom_hscene_after_desk_anal_1
    else:
        jump lbl_mom_bedroom_hscene_after_desk_anal_1_0

####################
## Desk Anal Fuck Stage 1
label lbl_mom_bedroom_hscene_after_desk_anal_1:
    scene img_mom_bedroom_hscene_after_desk_anal_stage_1
    #$ mom_bedroom_hscene_desk_anal_counter += 1
    #show bg mombedroomhscene_desk_anal_1
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_2
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_3
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_4
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_desk_anal_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_cum
    #elif skill_sta <= 14 and mom_bedroom_hscene_desk_anal_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_2
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_anal_counter == 10:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_2
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_1

image img_mom_bedroom_hscene_after_desk_anal_stage_1:
    "bg mombedroomhscene_desk_anal_1"
    pause 0.2
    "bg mombedroomhscene_desk_anal_2"
    pause 0.2
    "bg mombedroomhscene_desk_anal_3"
    pause 0.2
    "bg mombedroomhscene_desk_anal_4"
    pause 0.2
    "bg mombedroomhscene_desk_anal_5"
    pause 0.2
    repeat

####################
## Desk Anal Fuck Stage 1 XRAY
label lbl_mom_bedroom_hscene_after_desk_anal_1_0:
    scene img_mom_bedroom_hscene_after_desk_anal_stage_1_0
    #$ mom_bedroom_hscene_desk_anal_counter += 1
    #show bg mombedroomhscene_desk_anal_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_desk_anal_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_cum
    #elif skill_sta <= 14 and mom_bedroom_hscene_desk_anal_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_2_0
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_anal_counter == 10:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_2_0
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_1_0

image img_mom_bedroom_hscene_after_desk_anal_stage_1_0:
    "bg mombedroomhscene_desk_anal_1_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_2_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_3_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_4_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_5_0"
    pause 0.2
    repeat

####################
## Desk Anal Fuck Stage 2
label lbl_mom_bedroom_hscene_after_desk_anal_2:
    scene img_mom_bedroom_hscene_after_desk_anal_stage_2
    #$ mom_bedroom_hscene_desk_anal_counter += 1
    #show bg mombedroomhscene_desk_anal_1
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_3
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_4
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mom_bedroom_hscene_desk_anal_counter == 14:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_cum
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_anal_counter == 16:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_3
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_2

image img_mom_bedroom_hscene_after_desk_anal_stage_2:
    "bg mombedroomhscene_desk_anal_1"
    pause 0.2
    "bg mombedroomhscene_desk_anal_3"
    pause 0.2
    "bg mombedroomhscene_desk_anal_4"
    pause 0.2
    "bg mombedroomhscene_desk_anal_5"
    pause 0.2
    repeat

####################
## Desk Anal Fuck Stage 2 XRAY
label lbl_mom_bedroom_hscene_after_desk_anal_2_0:
    scene img_mom_bedroom_hscene_after_desk_anal_stage_2_0
    #$ mom_bedroom_hscene_desk_anal_counter += 1
    #show bg mombedroomhscene_desk_anal_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and mom_bedroom_hscene_desk_anal_counter == 14:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_cum
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_anal_counter == 16:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_3_0
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_2_0

image img_mom_bedroom_hscene_after_desk_anal_stage_2_0:
    "bg mombedroomhscene_desk_anal_1_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_3_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_4_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_5_0"
    pause 0.2
    repeat

####################
## Desk Anal Fuck Stage 3
label lbl_mom_bedroom_hscene_after_desk_anal_3:
    scene img_mom_bedroom_hscene_after_desk_anal_stage_3
    #$ mom_bedroom_hscene_desk_anal_counter += 1
    #show bg mombedroomhscene_desk_anal_1
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_4
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mom_bedroom_hscene_desk_anal_counter == 24:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_cum
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_3

image img_mom_bedroom_hscene_after_desk_anal_stage_3:
    "bg mombedroomhscene_desk_anal_1"
    pause 0.2
    "bg mombedroomhscene_desk_anal_4"
    pause 0.2
    "bg mombedroomhscene_desk_anal_5"
    pause 0.2
    repeat

####################
## Desk Anal Fuck Stage 3 XRAY
label lbl_mom_bedroom_hscene_after_desk_anal_3_0:
    scene img_mom_bedroom_hscene_after_desk_anal_stage_3_0
    #$ mom_bedroom_hscene_desk_anal_counter += 1
    #show bg mombedroomhscene_desk_anal_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg mombedroomhscene_desk_anal_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and mom_bedroom_hscene_desk_anal_counter == 24:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_cum
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_anal_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_anal_3_0

image img_mom_bedroom_hscene_after_desk_anal_stage_3_0:
    "bg mombedroomhscene_desk_anal_1_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_4_0"
    pause 0.2
    "bg mombedroomhscene_desk_anal_5_0"
    pause 0.2
    repeat

####################
## Desk Anal Fuck Cum
label lbl_mom_bedroom_hscene_after_desk_anal_cum:
    if mum_points <= 8:
        jump lbl_mom_bedroom_hscene_after_desk_anal_cum_2
    else:
        jump lbl_mom_bedroom_hscene_after_desk_anal_cum_3

label lbl_mom_bedroom_hscene_after_desk_anal_cum_2:
    #if hscene_xray == 0:
    #    scene bg mombedroomhscene_desk_anal_1
    #else:
    #    scene bg mombedroomhscene_desk_anal_1_0
    call screen scr_mom_bedroom_hscene_after_desk_anal_cum

screen scr_mom_bedroom_hscene_after_desk_anal_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_anal_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_anal_cumchoice")

label lbl_mom_bedroom_hscene_after_desk_anal_cum_3:
    #if hscene_xray == 0:
    #    scene bg mombedroomhscene_desk_anal_1
    #else:
    #    scene bg mombedroomhscene_desk_anal_1_0
    call screen scr_mom_bedroom_hscene_after_desk_anal_cum_2

screen scr_mom_bedroom_hscene_after_desk_anal_cum_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_scenechoice_desk_anal")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_anal_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_anal_cumchoice")

label lbl_mom_bedroom_hscene_after_desk_anal_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_mom_bedroom_hscene_after_desk_anal_cumin
            else:
                jump lbl_mom_bedroom_hscene_after_desk_anal_cumin_0
        "Cum on her":
            scene bg mombedroomhscene_desk_anal_16
            $ renpy.pause(0.3,hard=True)

            jump lbl_mom_bedroom_hscene_after_desk_cumout

####################
## Desk Anal Fuck Cum In
label lbl_mom_bedroom_hscene_after_desk_anal_cumin:
    scene bg mombedroomhscene_desk_anal_6
    $ renpy.pause(1.5,hard=True)
    show bg mombedroomhscene_desk_anal_12
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_13
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_14
    $ renpy.pause()
    show bg mombedroomhscene_desk_anal_15
    mum "{i}*Pants*{/i}"
    mum "You filled me up... so much..."
    if winc == 0:
        pov "Sorry, [missus]. I couldn't stop myself."
    else:
        pov "Sorry, mom. I couldn't stop myself."
    mum "At... least it wasn't in my vagina..."

    jump lbl_mybedroom_night_sleep

####################
## Desk Anal Fuck Cum In XRAY
label lbl_mom_bedroom_hscene_after_desk_anal_cumin_0:
    scene bg mombedroomhscene_desk_anal_6_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_7_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_8_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_9_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_10_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_11_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_12_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_13_0
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_anal_14_0
    $ renpy.pause()
    show bg mombedroomhscene_desk_anal_15_0
    mum "{i}*Pants*{/i}"
    mum "You filled me up... so much..."
    if winc == 0:
        pov "Sorry, [missus]. I couldn't stop myself."
    else:
        pov "Sorry, mom. I couldn't stop myself."
    mum "At... least it wasn't in my vagina..."

    jump lbl_mybedroom_night_sleep

####################
## Desk Anal Fuck Next
label lbl_mom_bedroom_hscene_after_desk_anal_next:
    scene bg mombedroomhscene_desk_anal_16
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_cumout_1
    $ renpy.pause(0.3,hard=True)
    if winc == 0:
        pov "Let's move to the bed, [missus]."
    else:
        pov "Let's move to the bed, mom."

    jump lbl_mom_bedroom_hscene_after_mish
