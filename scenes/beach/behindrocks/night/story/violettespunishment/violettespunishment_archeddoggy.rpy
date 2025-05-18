## Violettes Punishment Arched Doggy
label lbl_violettes_punishment_archeddoggy:
    $ violettespunishment_archeddoggy = 1

    scene bg violettespunishment_archeddoggy_1
    with fade

label lbl_violettes_punishment_archeddoggy_1:
    scene img_violettes_punishment_archeddoggy_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_archeddoggy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violettes_punishment_archeddoggy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_archeddoggy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_archeddoggy_1

image img_violettes_punishment_archeddoggy_1:
    "bg violettespunishment_archeddoggy_1"
    pause 0.3
    "bg violettespunishment_archeddoggy_2"
    pause 0.1
    "bg violettespunishment_archeddoggy_3"
    pause 0.1
    "bg violettespunishment_archeddoggy_4"
    pause 0.2
    "bg violettespunishment_archeddoggy_5"
    pause 0.2
    repeat

label lbl_violettes_punishment_archeddoggy_2:
    scene img_violettes_punishment_archeddoggy_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violettes_punishment_archeddoggy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_archeddoggy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_archeddoggy_2

image img_violettes_punishment_archeddoggy_2:
    "bg violettespunishment_archeddoggy_6"
    pause 0.3
    "bg violettespunishment_archeddoggy_8"
    pause 0.1
    "bg violettespunishment_archeddoggy_9"
    pause 0.2
    "bg violettespunishment_archeddoggy_10"
    pause 0.2
    repeat

label lbl_violettes_punishment_archeddoggy_3:
    scene img_violettes_punishment_archeddoggy_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_archeddoggy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_archeddoggy_3

image img_violettes_punishment_archeddoggy_3:
    "bg violettespunishment_archeddoggy_11"
    pause 0.2
    "bg violettespunishment_archeddoggy_14"
    pause 0.1
    "bg violettespunishment_archeddoggy_15"
    pause 0.2
    repeat

label lbl_violettes_punishment_archeddoggy_cum:
    call screen scr_violettes_punishment_archeddoggy_cum

screen scr_violettes_punishment_archeddoggy_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violettes_punishment_archeddoggy_1")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violettes_punishment_archeddoggy_cumming")
    else:
        pass

label lbl_violettes_punishment_archeddoggy_cumming:
    scene bg violettespunishment_archeddoggy_16
    $ renpy.pause(4,hard=True)
    $ renpy.pause()

    menu:
        "Reverse Cowgirl" if violettespunishment_reversecowgirl == 0:
            jump lbl_violettes_punishment_reversecowgirl
        "Mating Press" if violettespunishment_matingpress == 0:
            jump lbl_violettes_punishment_matingpress
        "End":
            jump lbl_violettes_punishment_end
