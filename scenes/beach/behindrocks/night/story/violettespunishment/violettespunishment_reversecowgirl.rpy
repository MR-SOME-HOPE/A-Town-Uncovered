## Violettes Punishment Reverse Cowgirl
label lbl_violettes_punishment_reversecowgirl:
    $ violettespunishment_reversecowgirl = 1

    scene bg violettespunishment_reversecowgirl_1
    with fade

label lbl_violettes_punishment_reversecowgirl_1:
    scene img_violettes_punishment_reversecowgirl_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_1

image img_violettes_punishment_reversecowgirl_1:
    "bg violettespunishment_reversecowgirl_1"
    pause 0.3
    "bg violettespunishment_reversecowgirl_2"
    pause 0.1
    "bg violettespunishment_reversecowgirl_3"
    pause 0.1
    "bg violettespunishment_reversecowgirl_4"
    pause 0.2
    "bg violettespunishment_reversecowgirl_5"
    pause 0.2
    repeat

label lbl_violettes_punishment_reversecowgirl_2:
    scene img_violettes_punishment_reversecowgirl_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_2

image img_violettes_punishment_reversecowgirl_2:
    "bg violettespunishment_reversecowgirl_1"
    pause 0.3
    "bg violettespunishment_reversecowgirl_3"
    pause 0.1
    "bg violettespunishment_reversecowgirl_4"
    pause 0.2
    "bg violettespunishment_reversecowgirl_5"
    pause 0.2
    repeat

label lbl_violettes_punishment_reversecowgirl_3:
    scene img_violettes_punishment_reversecowgirl_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_reversecowgirl_3

image img_violettes_punishment_reversecowgirl_3:
    "bg violettespunishment_reversecowgirl_1"
    pause 0.2
    "bg violettespunishment_reversecowgirl_4"
    pause 0.1
    "bg violettespunishment_reversecowgirl_5"
    pause 0.2
    repeat

label lbl_violettes_punishment_reversecowgirl_cum:
    call screen scr_violettes_punishment_reversecowgirl_cum

screen scr_violettes_punishment_reversecowgirl_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violettes_punishment_reversecowgirl_1")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violettes_punishment_reversecowgirl_cumming")
    else:
        pass

label lbl_violettes_punishment_reversecowgirl_cumming:
    scene bg violettespunishment_reversecowgirl_16_0
    $ renpy.pause(1,hard=True)
    show bg violettespunishment_reversecowgirl_16_1
    $ renpy.pause(0.4,hard=True)
    show bg violettespunishment_reversecowgirl_16_2
    $ renpy.pause(0.4,hard=True)
    show bg violettespunishment_reversecowgirl_16_3
    $ renpy.pause(0.4,hard=True)
    show bg violettespunishment_reversecowgirl_16_4
    $ renpy.pause(0.4,hard=True)
    show bg violettespunishment_reversecowgirl_16_5
    $ renpy.pause()

    menu:
        "Arched Doggy" if violettespunishment_archeddoggy == 0:
            jump lbl_violettes_punishment_archeddoggy
        "Mating Press" if violettespunishment_matingpress == 0:
            jump lbl_violettes_punishment_matingpress
        "End":
            jump lbl_violettes_punishment_end
