## A Cool Creek
label lbl_a_cool_creek_hscene_revisit:
    scene img_acoolcreek_1
    with fade
    $ renpy.pause()
    show img_acoolcreek_2
    $ renpy.pause()
    show img_acoolcreek_3
    $ renpy.pause()
    show white
    with dissolve
    $ renpy.pause(2,hard=True)
    show bg acoolcreek_cum
    with dissolve
    $ renpy.pause()
    
    scene black
    with fade

    jump lbl_vrheadset_character_selection

image img_acoolcreek_1:
    "bg acoolcreek_1"
    pause 0.3
    "bg acoolcreek_2"
    pause 0.1
    "bg acoolcreek_3"
    pause 0.1
    "bg acoolcreek_4"
    pause 0.2
    "bg acoolcreek_5"
    pause 0.2
    repeat

image img_acoolcreek_2:
    "bg acoolcreek_1"
    pause 0.3
    "bg acoolcreek_3"
    pause 0.1
    "bg acoolcreek_4"
    pause 0.2
    "bg acoolcreek_5"
    pause 0.2
    repeat

image img_acoolcreek_3:
    "bg acoolcreek_1"
    pause 0.2
    "bg acoolcreek_4"
    pause 0.1
    "bg acoolcreek_5"
    pause 0.2
    repeat

    