label lbl_caught_in_4k_bj:
    scene img_caught_in_4k_bj_stage_1
    with fade
    jump lbl_caught_in_4k_bj_1

label lbl_caught_in_4k_bj_0:
    jump lbl_caught_in_4k_bj_1

####################
## Stage 1
label lbl_caught_in_4k_bj_1:
    scene img_caught_in_4k_bj_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_bj_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_caught_in_4k_bj_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_bj_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_bj_1

image img_caught_in_4k_bj_stage_1:
    "bg caughtin4k_bj_1"
    pause 0.2
    "bg caughtin4k_bj_2"
    pause 0.2
    "bg caughtin4k_bj_3"
    pause 0.2
    "bg caughtin4k_bj_4"
    pause 0.2
    "bg caughtin4k_bj_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_caught_in_4k_bj_2:
    scene img_caught_in_4k_bj_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_caught_in_4k_bj_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_bj_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_bj_2

image img_caught_in_4k_bj_stage_2:
    "bg caughtin4k_bj_5"
    pause 0.2
    "bg caughtin4k_bj_7"
    pause 0.2
    "bg caughtin4k_bj_8"
    pause 0.2
    "bg caughtin4k_bj_6"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_caught_in_4k_bj_3:
    scene img_caught_in_4k_bj_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_bj_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_bj_3

image img_caught_in_4k_bj_stage_3:
    "bg caughtin4k_bj_9"
    pause 0.2
    "bg caughtin4k_bj_12"
    pause 0.2
    "bg caughtin4k_bj_10"
    pause 0.2
    repeat

####################
## Cum
label lbl_caught_in_4k_bj_menu:
    call screen scr_caught_in_4k_bj_menu

screen scr_caught_in_4k_bj_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_caught_in_4k_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_caught_in_4k_bj_cumchoice")

label lbl_caught_in_4k_bj_cumchoice:
    jump lbl_caught_in_4k_bj_cumin

####################
## Cum In
label lbl_caught_in_4k_bj_cumin:
    scene bg caughtin4k_bj_cum
    show white
    with dissolve
    $ renpy.pause(0.2,hard=True)
    hide white
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show white
    with dissolve
    $ renpy.pause(0.5,hard=True)
    hide white
    with dissolve
    $ renpy.pause(0.5,hard=True)
    show white
    with dissolve
    $ renpy.pause(0.8,hard=True)
    hide white
    with dissolve
    $ renpy.pause()

    scene black
    with fade
    $ renpy.pause()

    jump lbl_caught_in_4k_cunnilingus