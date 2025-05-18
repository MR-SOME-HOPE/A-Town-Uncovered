####################
## Mom Under Table Trio
label lbl_mom_under_table_trio_revisit_0:
    jump lbl_mom_under_table_trio_revisit_1


####################
## Stage 1
label lbl_mom_under_table_trio_revisit_1:
    scene img_mom_under_table_trio_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_under_table_trio_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_under_table_trio_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_under_table_trio_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_under_table_trio_revisit_1

image img_mom_under_table_trio_revisit_stage_1:
    "bg momundertabletrio_1"
    pause 0.2
    "bg momundertabletrio_2"
    pause 0.2
    "bg momundertabletrio_3"
    pause 0.2
    "bg momundertabletrio_4"
    pause 0.2
    "bg momundertabletrio_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_mom_under_table_trio_revisit_2:
    scene img_mom_under_table_trio_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_under_table_trio_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_under_table_trio_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_under_table_trio_revisit_2

image img_mom_under_table_trio_revisit_stage_2:
    "bg momundertabletrio_1"
    pause 0.2
    "bg momundertabletrio_3"
    pause 0.2
    "bg momundertabletrio_4"
    pause 0.2
    "bg momundertabletrio_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_mom_under_table_trio_revisit_3:
    scene img_mom_under_table_trio_revisit_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_under_table_trio_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_under_table_trio_revisit_3

image img_mom_under_table_trio_revisit_stage_3:
    "bg momundertabletrio_1"
    pause 0.2
    "bg momundertabletrio_3"
    pause 0.1
    "bg momundertabletrio_4"
    pause 0.1
    "bg momundertabletrio_5"
    pause 0.2
    repeat

####################
## Cum
label lbl_mom_under_table_trio_revisit_menu:
    jump lbl_mom_under_table_trio_revisit_menu_2

label lbl_mom_under_table_trio_revisit_menu_2:
    call screen scr_mom_under_table_trio_revisit_cum

screen scr_mom_under_table_trio_revisit_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_under_table_trio_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_under_table_trio_revisit_cumchoice")

label lbl_mom_under_table_trio_revisit_cumchoice:
    jump lbl_mom_under_table_trio_revisit_cumin


####################
## Cum In
label lbl_mom_under_table_trio_revisit_cumin:
    if winc == 1:
        pov "M-mom..."
        pov "I'm gonna-"
        pov "I'm gonna cum.."
        mum "..."
        pov "Mom!"
    else:
        pov "[missus]..."
        pov "I'm gonna-"
        pov "I'm gonna cum.."
        mum "..."
        pov "[missus]!"
    mum "..."
    sis "Just let it all out, [povname]."
    sis "{i}*Pants*{/i}"
    sis "She's busy."
    pov "Mffrmm-"
    show white
    $ renpy.pause(1.5,hard=True)
    hide white with dissolve
    pov "Fuu-u--u-uuck-"
    if winc == 1:
        pov "Moo-oooo-oom..."
        mum "{i}*Slurp slurp*{/i}"
        sis "Alright- it's my turn, c'mon, mom."
    else:
        pov "[missus]..."
        mum "{i}*Slurp slurp*{/i}"
        sis "Alright- it's my turn, c'mon, [missus]."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
