## Violettes Punishment Mating PRess
label lbl_violettes_punishment_matingpress_revisit:
    $ violettespunishment_matingpress = 1

    scene bg violettespunishment_matingpress_1
    with fade

label lbl_violettes_punishment_matingpress_revisit_1:
    scene img_violettes_punishment_matingpress_revisit_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_1

image img_violettes_punishment_matingpress_revisit_1:
    "bg violettespunishment_matingpress_1"
    pause 0.3
    "bg violettespunishment_matingpress_2"
    pause 0.1
    "bg violettespunishment_matingpress_3"
    pause 0.1
    "bg violettespunishment_matingpress_4"
    pause 0.2
    "bg violettespunishment_matingpress_5"
    pause 0.2
    repeat

label lbl_violettes_punishment_matingpress_revisit_2:
    scene img_violettes_punishment_matingpress_revisit_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_2

image img_violettes_punishment_matingpress_revisit_2:
    "bg violettespunishment_matingpress_1"
    pause 0.3
    "bg violettespunishment_matingpress_3"
    pause 0.1
    "bg violettespunishment_matingpress_4"
    pause 0.2
    "bg violettespunishment_matingpress_5"
    pause 0.2
    repeat

label lbl_violettes_punishment_matingpress_revisit_3:
    scene img_violettes_punishment_matingpress_revisit_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violettes_punishment_matingpress_revisit_3

image img_violettes_punishment_matingpress_revisit_3:
    "bg violettespunishment_matingpress_1"
    pause 0.2
    "bg violettespunishment_matingpress_4"
    pause 0.1
    "bg violettespunishment_matingpress_5"
    pause 0.2
    repeat

label lbl_violettes_punishment_matingpress_revisit_cum:
    call screen scr_violettes_punishment_matingpress_revisit_cum

screen scr_violettes_punishment_matingpress_revisit_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violettes_punishment_matingpress_revisit_1")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violettes_punishment_matingpress_revisit_cumming")
    else:
        pass

label lbl_violettes_punishment_matingpress_revisit_cumming:
    scene bg violettespunishment_matingpress_6_0
    $ renpy.pause(1,hard=True)
    show bg violettespunishment_matingpress_6_1
    $ renpy.pause(0.4,hard=True)
    show bg violettespunishment_matingpress_6_2
    $ renpy.pause(0.4,hard=True)
    show bg violettespunishment_matingpress_6_3
    $ renpy.pause(0.4,hard=True)
    show bg violettespunishment_matingpress_6_4
    $ renpy.pause(0.4,hard=True)
    show bg violettespunishment_matingpress_6_5
    $ renpy.pause()

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
