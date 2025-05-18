## Mom x Sister x MC Double BJ
####################
## BJ
label lbl_momxsisterxmc_doublebj_revisit_0:
    scene bg momxsisterxmc_doublebj_1
    #$ momxsisterxmc_doublebj_counter = 0

    jump lbl_momxsisterxmc_doublebj_revisit_1

####################
## BJ Stage 1
label lbl_momxsisterxmc_doublebj_revisit_1:
    scene img_momxsisterxmc_doublebj_revisit_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_1

image img_momxsisterxmc_doublebj_revisit_stage_1:
    "bg momxsisterxmc_doublebj_1"
    pause 0.3
    "bg momxsisterxmc_doublebj_2"
    pause 0.3
    "bg momxsisterxmc_doublebj_3"
    pause 0.3
    "bg momxsisterxmc_doublebj_4"
    pause 0.3
    "bg momxsisterxmc_doublebj_5"
    pause 0.3
    repeat

####################
## BJ Stage 2
label lbl_momxsisterxmc_doublebj_revisit_2:
    scene img_momxsisterxmc_doublebj_revisit_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_2

image img_momxsisterxmc_doublebj_revisit_stage_2:
    "bg momxsisterxmc_doublebj_1"
    pause 0.2
    "bg momxsisterxmc_doublebj_2"
    pause 0.2
    "bg momxsisterxmc_doublebj_3"
    pause 0.2
    "bg momxsisterxmc_doublebj_4"
    pause 0.2
    "bg momxsisterxmc_doublebj_5"
    pause 0.2
    repeat

####################
## BJ Stage 3
label lbl_momxsisterxmc_doublebj_revisit_3:
    scene img_momxsisterxmc_doublebj_revisit_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_doublebj_revisit_3

image img_momxsisterxmc_doublebj_revisit_stage_3:
    "bg momxsisterxmc_doublebj_1"
    pause 0.1
    "bg momxsisterxmc_doublebj_2"
    pause 0.1
    "bg momxsisterxmc_doublebj_3"
    pause 0.1
    "bg momxsisterxmc_doublebj_4"
    pause 0.1
    "bg momxsisterxmc_doublebj_5"
    pause 0.1
    repeat

####################
## BJ Cum
label lbl_momxsisterxmc_doublebj_revisit_cum:

    call screen scr_momxsisterxmc_doublebj_revisit_cum

screen scr_momxsisterxmc_doublebj_revisit_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_doublebj_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_doublebj_revisit_cumchoice")

label lbl_momxsisterxmc_doublebj_revisit_cumchoice:

    menu:
        "Cum inside Mom's mouth" if winc == 1:
            jump lbl_momxsisterxmc_doublebj_revisit_cummom
        "Cum inside [missus]'s mouth" if winc == 0:
            jump lbl_momxsisterxmc_doublebj_revisit_cummom
        "Cum inside [sister]'s mouth":
            jump lbl_momxsisterxmc_doublebj_revisit_cumsis

####################
## BJ Cum in Mom's Mouth
label lbl_momxsisterxmc_doublebj_revisit_cummom:
    scene bg momxsisterxmc_doublebj_1
    pov "I-"
    show bg momxsisterxmc_doublebj_2
    pov "I'm.."
    show bg momxsisterxmc_doublebj_6
    pov "I'm gonna cum-"
    show bg momxsisterxmc_doublebj_6
    with hpunch
    mum "No! Not the carpet!"
    show bg momxsisterxmc_doublebj_13
    with hpunch
    $ renpy.pause(2,hard=True)
    show bg momxsisterxmc_doublebj_14
    mum "{i}*Gulp*{/i}"
    pov "Oh fuck, [missus]... you're sucking me so hard."
    show bg momxsisterxmc_doublebj_15
    sis "Wow, [missus]. Taking it like a champ."
    sis "For a second, I thought you were gonna make me do it, hehe~"
    show bg momxsisterxmc_doublebj_14
    mum "{i}*Gulp gulp*{/i}"
    show bg momxsisterxmc_doublebj_16
    mum "{i}*Exhales*{/i} Mmhmm.."
    pov "You really sucked every last drop, [missus]."
    pov "And as a bonus, you saved the carpet. Hehehe~"

    $ townmap_enabled = 1

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## BJ Cum in Sister's Mouth
label lbl_momxsisterxmc_doublebj_revisit_cumsis:
    scene bg momxsisterxmc_doublebj_1
    pov "I-"
    show bg momxsisterxmc_doublebj_2
    pov "I'm.."
    show bg momxsisterxmc_doublebj_6
    pov "I'm gonna cum-"
    show bg momxsisterxmc_doublebj_7
    with hpunch
    mum "No! Not the carpet!"
    show bg momxsisterxmc_doublebj_8
    mum "[sister]! Open your mouth now!"
    sis "Ahwww..."
    show bg momxsisterxmc_doublebj_9
    with hpunch
    $ renpy.pause(2,hard=True)
    pov "Fuck... [missus], she's sucking it all out of me."
    show bg momxsisterxmc_doublebj_11
    mum "I always tell you both not to waste your food."
    show bg momxsisterxmc_doublebj_10
    pov "Mm.. shit.."
    sis "{i}*Gulp*{/i}"
    show bg momxsisterxmc_doublebj_11
    mum "Thanks for taking one for the team, sweetiecakes. I'm so proud of you."
    show bg momxsisterxmc_doublebj_10
    sis "{i}*Gulp* Mmmph..{/i}"
    show bg momxsisterxmc_doublebj_12
    sis "{i}*Exhales*{/i} Mrhmmm..."
    pov "What's with that look, [sister]?"
    pov "Don't tell me you want more..."

    $ townmap_enabled = 1

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
