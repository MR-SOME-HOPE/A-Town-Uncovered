## A Shared Dream 69
label lbl_a_shared_dream_69:
    scene bg ashareddream69_1
    with fade

label lbl_a_shared_dream_69_1:
    scene img_a_shared_dream_69_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_a_shared_dream_69_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_a_shared_dream_69_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_a_shared_dream_69_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_a_shared_dream_69_1

image img_a_shared_dream_69_1:
    "bg ashareddream69_1"
    pause 0.3
    "bg ashareddream69_2"
    pause 0.1
    "bg ashareddream69_3"
    pause 0.1
    "bg ashareddream69_4"
    pause 0.2
    "bg ashareddream69_2"
    pause 0.2
    repeat

label lbl_a_shared_dream_69_2:
    scene img_a_shared_dream_69_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_a_shared_dream_69_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_a_shared_dream_69_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_a_shared_dream_69_2

image img_a_shared_dream_69_2:
    "bg ashareddream69_1"
    pause 0.3
    "bg ashareddream69_3"
    pause 0.1
    "bg ashareddream69_4"
    pause 0.2
    "bg ashareddream69_2"
    pause 0.2
    repeat

label lbl_a_shared_dream_69_3:
    scene img_a_shared_dream_69_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_a_shared_dream_69_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_a_shared_dream_69_3

image img_a_shared_dream_69_3:
    "bg ashareddream69_1"
    pause 0.2
    "bg ashareddream69_4"
    pause 0.1
    "bg ashareddream69_2"
    pause 0.2
    repeat

label lbl_a_shared_dream_69_cum:
    call screen scr_a_shared_dream_69_cum

screen scr_a_shared_dream_69_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_a_shared_dream_69_1")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_a_shared_dream_69_cumming")
    else:
        pass

label lbl_a_shared_dream_69_cumming:
    scene bg ashareddream69_4
    $ renpy.pause(1,hard=True)
    show bg ashareddream69_5_1
    $ renpy.pause(0.4,hard=True)
    show bg ashareddream69_5_2
    $ renpy.pause(0.4,hard=True)
    show bg ashareddream69_5_3
    $ renpy.pause(0.4,hard=True)
    show bg ashareddream69_5_4
    $ renpy.pause(0.4,hard=True)
    show bg ashareddream69_5_5
    $ renpy.pause()

    jump lbl_a_shared_dream_end
