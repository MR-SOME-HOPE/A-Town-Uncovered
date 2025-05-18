label lbl_lashleyshunger_hscene_revisit_0:
    $ lashleyshunger_hscene = 1
    scene img_lashleyshunger_hscene_revisit_stage_1
    with fade

    jump lbl_lashleyshunger_hscene_revisit_continue

label lbl_lashleyshunger_hscene_revisit_continue:
    $ lashleyshunger_hscene = 0

## STAGE 1
label lbl_lashleyshunger_hscene_revisit_1:
    $ lashleyshunger_hscene += 1
    scene img_lashleyshunger_hscene_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_lashleyshunger_hscene_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashleyshunger_hscene_revisit_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashleyshunger_hscene_revisit_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashleyshunger_hscene_revisit_menu

image img_lashleyshunger_hscene_revisit_stage_1:
    "bg lashleyshunger_hscene_1"
    pause 0.3
    "bg lashleyshunger_hscene_2"
    pause 0.1
    "bg lashleyshunger_hscene_3"
    pause 0.1
    "bg lashleyshunger_hscene_4"
    pause 0.3
    "bg lashleyshunger_hscene_2"
    pause 0.3
    repeat

## STAGE 2
label lbl_lashleyshunger_hscene_revisit_2:
    $ lashleyshunger_hscene += 1
    scene img_lashleyshunger_hscene_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashleyshunger_hscene_revisit_menu
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashleyshunger_hscene_revisit_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_lashleyshunger_hscene_revisit_menu

image img_lashleyshunger_hscene_revisit_stage_2:
    "bg lashleyshunger_hscene_1"
    pause 0.3
    "bg lashleyshunger_hscene_3"
    pause 0.1
    "bg lashleyshunger_hscene_4"
    pause 0.2
    "bg lashleyshunger_hscene_2"
    pause 0.2
    repeat

## STAGE 3
label lbl_lashleyshunger_hscene_revisit_3:
    $ lashleyshunger_hscene += 1
    scene img_lashleyshunger_hscene_revisit_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_lashleyshunger_hscene_revisit_menu

image img_lashleyshunger_hscene_revisit_stage_3:
    "bg lashleyshunger_hscene_1"
    pause 0.2
    "bg lashleyshunger_hscene_4"
    pause 0.1
    "bg lashleyshunger_hscene_2"
    pause 0.2
    repeat

####################
## Menu
label lbl_lashleyshunger_hscene_revisit_menu:
    call screen scr_lashleyshunger_hscene_revisit_menu

screen scr_lashleyshunger_hscene_revisit_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashleyshunger_hscene_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashleyshunger_hscene_revisit_cum")

####################
## CUM
label lbl_lashleyshunger_hscene_revisit_cum: ###############################################################
    scene bg lashleyshunger_hscene_5_1
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_2
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_3
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_4
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_5
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_6
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_7
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_8
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_9
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_10
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_11
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_12
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_13
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_14
    $ renpy.pause (0.3,hard=True)
    show bg lashleyshunger_hscene_5_15
    $ renpy.pause (0.5,hard=True)
    show bg lashleyshunger_hscene_5_16
    $ renpy.pause ()
    pri "{i}*Huff*{/i}"
    pri "M-My god… [povname]... A-Are men supposed to cum this much?"
    pri "It’s significant… more than what I’ve seen in..."
    pri "-those videos..."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
