####################
## Mom Under Table Trio
default momundertabletrio = 0
default had_under_table_trio_that_day = 0

label lbl_mom_under_table_trio:
    ## PRE STORY
    if mowed_lawn == 1:
        scene bg mydiningroom_day
    else:
        scene bg mydiningroom_day_grassy
    show pov neutral at left
    show mum neutral_talk at right
    with dissolve
    mum "Good morning, [povname]."
    mum "You joining us for breakfast?"
    show pov confused_talk
    show mum neutral
    pov "Us?"
    show pov neutral
    show mum neutral_talk
    mum "Me and [sister]."
    show mum smirk_talk
    mum "I have a special treat for you since it's the weekend now."
    show pov confused_talk
    show mum smirk
    pov "I don't see any- food?"
    show pov confused
    show mum neutral_talk
    mum "I'll have it ready in a bit."
    show pov neutral
    mum "Why don't you sit down at the table and tell me about your week."
    menu:
        "Sure.":
            show pov neutral_talk
            show mum neutral
            pov "Sure thing."
            pov "Where's [sister]."
            show pov neutral
            show mum neutral_talk
            mum "She'll be here in a bit."

            scene black with fade
            $ renpy.pause()
            if winc == 1:
                "After mom makes you two breakfast..."
            else:
                "After [missus] makes you two breakfast..."

            scene img_mom_under_table_trio_stage_1 with fade

            jump lbl_mom_under_table_trio_1

        "Not today.":
            show pov embarrassed_talk
            show mum sad
            pov "Sorry, not today."
            pov "I already made plans."
            show pov embarrassed
            show mum embarrassed_talk
            mum "Oh- that's too bad."
            show mum neutral_talk
            mum "I guess it'll just be us girls."
            show pov neutral
            mum "I love you, [povname]. Have a good rest of the day, okay?"
            show pov neutral_talk
            show mum neutral
            pov "Love you too."

            jump lbl_mykitchen_day_setup

label lbl_mom_under_table_trio_0:
    jump lbl_mom_under_table_trio_1
    # if hscene_xray == 0:
    #     jump lbl_mom_under_table_trio_1
    # else:
    #     jump lbl_mom_under_table_trio_1_0

####################
## Stage 1
label lbl_mom_under_table_trio_1:
    scene img_mom_under_table_trio_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_under_table_trio_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_under_table_trio_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_under_table_trio_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_under_table_trio_1

image img_mom_under_table_trio_stage_1:
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
label lbl_mom_under_table_trio_2:
    scene img_mom_under_table_trio_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_under_table_trio_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_under_table_trio_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_under_table_trio_2

image img_mom_under_table_trio_stage_2:
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
label lbl_mom_under_table_trio_3:
    scene img_mom_under_table_trio_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_under_table_trio_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_under_table_trio_3

image img_mom_under_table_trio_stage_3:
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
label lbl_mom_under_table_trio_menu:
    jump lbl_mom_under_table_trio_menu_2

label lbl_mom_under_table_trio_menu_2:
    call screen scr_mom_under_table_trio_cum

screen scr_mom_under_table_trio_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_under_table_trio_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_under_table_trio_cumchoice")

label lbl_mom_under_table_trio_cumchoice:
    jump lbl_mom_under_table_trio_cumin
    # menu:
    #     "Cum inside":
    #         if hscene_xray == 0:
    #             jump lbl_mom_under_table_trio_cumin
    #         else:
    #             jump lbl_mom_under_table_trio_cumin_0
    #     "Cum on her":
    #         jump lbl_mom_under_table_trio_cumout

####################
## Cum In
label lbl_mom_under_table_trio_cumin:
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
    "After a hearty breakfast..."
    scene bg mydiningroom_day
    with fade

    $ momundertabletrio = 0
    $ had_under_table_trio_that_day = 1

    jump lbl_mydiningroom_day_setup
