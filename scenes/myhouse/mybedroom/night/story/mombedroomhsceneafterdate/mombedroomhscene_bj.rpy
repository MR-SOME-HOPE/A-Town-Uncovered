####################
## BJ
label lbl_mom_bedroom_hscene_after_bj:
    default mum_bedroomsex = 0

    scene bg mombedroomhscene_bj_24
    with fade
    mum "Hard already?"
    show bg mombedroomhscene_bj_25
    pov "It's been this way ever since we got home."
    show bg mombedroomhscene_bj_24
    mum "Couldn't wait, could you?"
    show bg mombedroomhscene_bj_26
    pov "To be honest with you..."
    play sex_sounds mouth_suck_10 noloop
    show bg mombedroomhscene_bj_1
    $ renpy.pause(1.0,hard=True)

    play sex_voices mouth_puff_04 noloop
    pov "{i}*Inhale*{/i} I was wondering if we would end up doing this."

    jump lbl_mom_bedroom_hscene_after_bj_0

label lbl_mom_bedroom_hscene_after_bj_0:

    jump lbl_mom_bedroom_hscene_after_bj_1

####################
## BJ Stage 1
label lbl_mom_bedroom_hscene_after_bj_1:

    scene img_mom_bedroom_hscene_after_bj_stage_1
    #queue sex_sounds [mouth_suck_01,mouth_suck_02,mouth_suck_03,mouth_suck_04,mouth_suck_05,mouth_suck_06,mouth_suck_07,mouth_suck_08,mouth_suck_09]

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_1

image img_mom_bedroom_hscene_after_bj_stage_1:
    "bg mombedroomhscene_bj_1"
    pause 0.3
    "bg mombedroomhscene_bj_2"
    pause 0.1
    "bg mombedroomhscene_bj_3"
    pause 0.1
    "bg mombedroomhscene_bj_4"
    pause 0.3
    "bg mombedroomhscene_bj_5"
    pause 0.3
    repeat

####################
## BJ Stage 2
label lbl_mom_bedroom_hscene_after_bj_2:

    scene img_mom_bedroom_hscene_after_bj_stage_2
    #queue sex_sounds [mouth_suck_01,mouth_suck_02,mouth_suck_03,mouth_suck_04,mouth_suck_05,mouth_suck_06,mouth_suck_07,mouth_suck_08,mouth_suck_09]

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_2

image img_mom_bedroom_hscene_after_bj_stage_2:
    "bg mombedroomhscene_bj_1"
    pause 0.3
    "bg mombedroomhscene_bj_3"
    pause 0.1
    "bg mombedroomhscene_bj_4"
    pause 0.2
    "bg mombedroomhscene_bj_5"
    pause 0.2
    repeat

####################
## BJ Stage 3
label lbl_mom_bedroom_hscene_after_bj_3:

    scene img_mom_bedroom_hscene_after_bj_stage_3
    #queue sex_sounds [mouth_suck_01,mouth_suck_02,mouth_suck_03,mouth_suck_04,mouth_suck_05,mouth_suck_06,mouth_suck_07,mouth_suck_08,mouth_suck_09]

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_bj_3

image img_mom_bedroom_hscene_after_bj_stage_3:
    "bg mombedroomhscene_bj_1"
    pause 0.2
    "bg mombedroomhscene_bj_3"
    pause 0.1
    "bg mombedroomhscene_bj_5"
    pause 0.2
    repeat

####################
## BJ Cum
label lbl_mom_bedroom_hscene_after_bj_cum:
    if mum_points <= 4:
        jump lbl_mom_bedroom_hscene_after_bj_cum_2
    else:
        jump lbl_mom_bedroom_hscene_after_bj_cum_3

label lbl_mom_bedroom_hscene_after_bj_cum_2:

    call screen scr_mom_bedroom_hscene_after_bj_cum_2

screen scr_mom_bedroom_hscene_after_bj_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_bj_cumchoice")

label lbl_mom_bedroom_hscene_after_bj_cum_3:

    call screen scr_mom_bedroom_hscene_after_bj_cum_3

screen scr_mom_bedroom_hscene_after_bj_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_bj_next")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_bj_cumchoice")

label lbl_mom_bedroom_hscene_after_bj_cumchoice:

    menu:
        "Cum inside mouth":
            jump lbl_mom_bedroom_hscene_after_bj_cumin
        "Cum outside on face":
            jump lbl_mom_bedroom_hscene_after_bj_cumout

####################
## BJ Cum in
label lbl_mom_bedroom_hscene_after_bj_cumin:
    queue sex_sounds [mouth_swallow_01,mouth_swallow_02,mouth_swallow_03,mouth_swallow_04]
    scene bg mombedroomhscene_bj_2
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_bj_3
    $ renpy.pause(1,hard=True)
    show bg mombedroomhscene_bj_6
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_7
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_8
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_9
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_10
    stop sex_sounds fadeout 1.0
    $ renpy.pause()
    queue sex_sounds [mouth_saliva_04,blowjob_a_07,mouth_swallow_05,mouth_swallow_06] noloop
    show bg mombedroomhscene_bj_11
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_12
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_13
    $ renpy.pause(1.0,hard=True)

    mum "Wow.. you nearly drowned me, honey."
    show bg mombedroomhscene_bj_14
    if winc == 0:
        pov "Sorry, [missus]. I can't help it."
    else:
        pov "Sorry, Mom. I can't help it."
    show bg mombedroomhscene_bj_13
    mum "Never be sorry, you're a godsend."

    jump lbl_mybedroom_night_sleep

####################
## BJ Cum Out
label lbl_mom_bedroom_hscene_after_bj_cumout:
    play sex_sounds penis_cum_06 noloop
    scene bg mombedroomhscene_bj_15
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_16
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_17
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_18
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_19
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_20
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_21
    $ renpy.pause()
    show bg mombedroomhscene_bj_22
    mum "Damnit, honey. I can't breath through my nose!"
    show bg mombedroomhscene_bj_23
    if winc == 0:
        pov "Sorry, [missus]. I can't help it."
    else:
        pov "Sorry, Mom. I can't help it."
    pov "You look great though."
    show bg mombedroomhscene_bj_22
    mum "Very funny, [povname]."

    jump lbl_mybedroom_night_sleep

####################
## BJ Next
label lbl_mom_bedroom_hscene_after_bj_next:
    stop sex_sounds
    scene bg mombedroomhscene_bj_1
    if winc == 0:
        pov "[missus]... hold on.."
    else:
        pov "Mom... hold on.."
    show bg mombedroomhscene_bj_26
    pov "Do... do you wanna..."
    show bg mombedroomhscene_bj_24
    mum "Fuck? Excuse the language but yeah, let's fuck."

    jump lbl_mom_bedroom_hscene_after_mish
