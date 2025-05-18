label lbl_caught_in_4k_spooning:
    scene img_caught_in_4k_spooning_stage_1
    with fade
    jump lbl_caught_in_4k_spooning_1

label lbl_caught_in_4k_spooning_0:
    jump lbl_caught_in_4k_spooning_1

####################
## Stage 1
label lbl_caught_in_4k_spooning_1:
    scene img_caught_in_4k_spooning_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_spooning_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_caught_in_4k_spooning_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_spooning_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_spooning_1

image img_caught_in_4k_spooning_stage_1:
    "bg caughtin4k_spooning_1"
    pause 0.2
    "bg caughtin4k_spooning_2"
    pause 0.2
    "bg caughtin4k_spooning_3"
    pause 0.2
    "bg caughtin4k_spooning_4"
    pause 0.2
    "bg caughtin4k_spooning_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_caught_in_4k_spooning_2:
    scene img_caught_in_4k_spooning_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_caught_in_4k_spooning_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_spooning_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_spooning_2

image img_caught_in_4k_spooning_stage_2:
    "bg caughtin4k_spooning_1"
    pause 0.2
    "bg caughtin4k_spooning_3"
    pause 0.2
    "bg caughtin4k_spooning_4"
    pause 0.2
    "bg caughtin4k_spooning_2"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_caught_in_4k_spooning_3:
    scene img_caught_in_4k_spooning_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_caught_in_4k_spooning_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_caught_in_4k_spooning_3

image img_caught_in_4k_spooning_stage_3:
    "bg caughtin4k_spooning_1"
    pause 0.2
    "bg caughtin4k_spooning_4"
    pause 0.2
    "bg caughtin4k_spooning_2"
    pause 0.2
    repeat

####################
## Cum
label lbl_caught_in_4k_spooning_menu:
    call screen scr_caught_in_4k_spooning_menu

screen scr_caught_in_4k_spooning_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_caught_in_4k_spooning_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_caught_in_4k_spooning_cumchoice")

label lbl_caught_in_4k_spooning_cumchoice:
    jump lbl_caught_in_4k_spooning_cumin

####################
## Cum In
label lbl_caught_in_4k_spooning_cumin:
    scene bg caughtin4k_spooning_cum
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

    $ hitomi_path = 24

    scene black
    with fade
    $ renpy.pause()
    "..."

    jump lbl_confession_over_a_recording