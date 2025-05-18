## Mom x Sister x MC 69 Doggy
####################
## START
label lbl_momxsisterxmc_69doggy_revisit_0:
    scene bg momxsisterxmc_69doggy_1
    with fade

    jump lbl_momxsisterxmc_69doggy_revisit_1

####################
## Stage 1
label lbl_momxsisterxmc_69doggy_revisit_1:
    scene img_momxsisterxmc_69doggy_revisit_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_1

image img_momxsisterxmc_69doggy_revisit_stage_1:
    "bg momxsisterxmc_69doggy_1"
    pause 0.3
    "bg momxsisterxmc_69doggy_2"
    pause 0.3
    "bg momxsisterxmc_69doggy_3"
    pause 0.3
    "bg momxsisterxmc_69doggy_4"
    pause 0.3
    "bg momxsisterxmc_69doggy_2"
    pause 0.3
    repeat

####################
## Stage 2
label lbl_momxsisterxmc_69doggy_revisit_2:
    scene img_momxsisterxmc_69doggy_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_2

image img_momxsisterxmc_69doggy_revisit_stage_2:
    "bg momxsisterxmc_69doggy_1"
    pause 0.2
    "bg momxsisterxmc_69doggy_2"
    pause 0.2
    "bg momxsisterxmc_69doggy_3"
    pause 0.2
    "bg momxsisterxmc_69doggy_4"
    pause 0.2
    "bg momxsisterxmc_69doggy_2"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_momxsisterxmc_69doggy_revisit_3:
    scene img_momxsisterxmc_69doggy_revisit_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_69doggy_revisit_3

image img_momxsisterxmc_69doggy_revisit_stage_3:
    "bg momxsisterxmc_69doggy_1"
    pause 0.1
    "bg momxsisterxmc_69doggy_2"
    pause 0.1
    "bg momxsisterxmc_69doggy_3"
    pause 0.1
    "bg momxsisterxmc_69doggy_4"
    pause 0.1
    "bg momxsisterxmc_69doggy_2"
    pause 0.1
    repeat

####################
## CUM
label lbl_momxsisterxmc_69doggy_revisit_cum:
    call screen scr_momxsisterxmc_69doggy_revisit_cum

screen scr_momxsisterxmc_69doggy_revisit_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_69doggy_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_69doggy_revisit_cum1")

####################
## CUM
label lbl_momxsisterxmc_69doggy_revisit_cum1:
    scene img_momxsisterxmc_69doggy_revisit_stage_3
    pov "I-"
    pov "I'm.."
    pov "I'm gonna cum-"
    mum "Yes, baby- let it out inside [sister]."
    sis "D-do it! *Huff huff* Just do it!"
    show bg momxsisterxmc_69doggy_4
    with hpunch
    $ renpy.pause(2,hard=True)
    mum "That's my boy. Good boy."
    pov "Oh fuck... take it all, [sister]."
    sis "Arrghh!."
    sis "It's sooo fucking- hot..."
    mum "{i}*Giggles*{/i}"
    mum "I love how close you two are."
    pov "*Huff* Do you want some, [missus]?"
    mum "No, it's okay, honey. I've got some chores to do around the house."

    $ townmap_enabled = 1

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
