label lbl_caught_in_4k_cunnilingus:
    scene img_caught_in_4k_cunnilingus_stage_1
    with fade

    jump lbl_caught_in_4k_cunnilingus_1

label lbl_caught_in_4k_cunnilingus_0:
    jump lbl_caught_in_4k_cunnilingus_1

####################
## Stage 1
label lbl_caught_in_4k_cunnilingus_1:
    scene img_caught_in_4k_cunnilingus_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_cunnilingus_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_caught_in_4k_cunnilingus_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_cunnilingus_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_cunnilingus_1

image img_caught_in_4k_cunnilingus_stage_1:
    "bg caughtin4k_cunnilingus_1"
    pause 0.2
    "bg caughtin4k_cunnilingus_2"
    pause 0.2
    "bg caughtin4k_cunnilingus_3"
    pause 0.2
    "bg caughtin4k_cunnilingus_4"
    pause 0.2
    "bg caughtin4k_cunnilingus_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_caught_in_4k_cunnilingus_2:
    scene img_caught_in_4k_cunnilingus_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_caught_in_4k_cunnilingus_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_cunnilingus_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_cunnilingus_2

image img_caught_in_4k_cunnilingus_stage_2:
    "bg caughtin4k_cunnilingus_1"
    pause 0.2
    "bg caughtin4k_cunnilingus_3"
    pause 0.2
    "bg caughtin4k_cunnilingus_4"
    pause 0.2
    "bg caughtin4k_cunnilingus_2"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_caught_in_4k_cunnilingus_3:
    scene img_caught_in_4k_cunnilingus_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_cunnilingus_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_cunnilingus_3

image img_caught_in_4k_cunnilingus_stage_3:
    "bg caughtin4k_cunnilingus_1"
    pause 0.2
    "bg caughtin4k_cunnilingus_4"
    pause 0.2
    "bg caughtin4k_cunnilingus_2"
    pause 0.2
    repeat

####################
## Cum
label lbl_caught_in_4k_cunnilingus_menu:
    call screen scr_caught_in_4k_cunnilingus_menu

screen scr_caught_in_4k_cunnilingus_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_caught_in_4k_cunnilingus_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_caught_in_4k_cunnilingus_cumchoice")

label lbl_caught_in_4k_cunnilingus_cumchoice:
    jump lbl_caught_in_4k_cunnilingus_cumin

####################
## Cum In
label lbl_caught_in_4k_cunnilingus_cumin:
    scene bg caughtin4k_cunnilingus_cum
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

    jump lbl_caught_in_4k_spooning