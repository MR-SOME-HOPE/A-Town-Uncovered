## Mom x Sister x MC Box Fort
label lbl_momxsisterxmc_boxfort:
    scene bg mybasement_lightson
    with fade
    show povne neutral at left
    show sis confused at Position(xpos=1300)
    show mum shocked at right
    with dissolve
    sis "..."
    show povne smirk at left
    show sis smirk at Position(xpos=1300)
    show mum angry_talk at right
    mum "When did you get the time to take your clothes off?!"
    show povne smirk_talk at left
    show mum confused at right
    pov "On the way down here?"
    show povne confused_talk at left
    show sis neutral at Position(xpos=1300)
    pov "Didn't you notice?"
    show povne bored at left
    show sis smirk at Position(xpos=1300)
    show mum bored_talk at right
    mum "You better pick up your clothes on the way back-"
    hide mum
    with dissolve
    show povne confused at left
    show sis smirk_talk at Position(xpos=1300)
    sis "How are you already hard?"
    show povne smirk_talk at left
    show sis smirk at Position(xpos=1300)
    pov "I was hard for like 3 hours already."
    show povne neutral at left
    show sis neutral_talk at Position(xpos=1300)
    show mumn neutral at right
    sis "Well, better not keep him waiting then."
    hide sis
    show povne smirk at left
    show mumn neutral_talk at right
    mum "Ready, honey?"
    show mumn neutral at right
    sis "Hold on-"
    show povne neutral at left
    show sisn neutral_talk at Position(xpos=1300)
    with dissolve
    show mumn neutral at right
    sis "Ready!"
    show povne smirk_talk at left
    show sisn neutral at Position(xpos=1300)
    show mumn neutral at right
    pov "Let's do this thing!"

    jump lbl_momxsisterxmc_boxfort_0

####################
## INTRO
label lbl_momxsisterxmc_boxfort_0:
    if hscene_xray == 1:
        scene bg momxsisterxmc_fort_1_0

        jump lbl_momxsisterxmc_boxfort_1_0
    else:
        scene bg momxsisterxmc_fort_1

        jump lbl_momxsisterxmc_boxfort_1

####################
## Stage 1
label lbl_momxsisterxmc_boxfort_1:
    scene img_momxsisterxmc_boxfort_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_boxfort_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_boxfort_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_boxfort_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_boxfort_1

image img_momxsisterxmc_boxfort_stage_1:
    "bg momxsisterxmc_fort_1"
    pause 0.3
    "bg momxsisterxmc_fort_2"
    pause 0.3
    "bg momxsisterxmc_fort_3"
    pause 0.3
    "bg momxsisterxmc_fort_4"
    pause 0.3
    "bg momxsisterxmc_fort_2"
    pause 0.3
    repeat

####################
## Stage 1 XRAY
label lbl_momxsisterxmc_boxfort_1_0:
    scene img_momxsisterxmc_boxfort_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_boxfort_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_boxfort_2_0
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_boxfort_2_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_boxfort_1_0

image img_momxsisterxmc_boxfort_stage_1_0:
    "bg momxsisterxmc_fort_1_0"
    pause 0.3
    "bg momxsisterxmc_fort_2_0"
    pause 0.3
    "bg momxsisterxmc_fort_3_0"
    pause 0.3
    "bg momxsisterxmc_fort_4_0"
    pause 0.3
    "bg momxsisterxmc_fort_2_0"
    pause 0.3
    repeat

####################
## Stage 2
label lbl_momxsisterxmc_boxfort_2:
    scene img_momxsisterxmc_boxfort_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_boxfort_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_boxfort_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_boxfort_2

image img_momxsisterxmc_boxfort_stage_2:
    "bg momxsisterxmc_fort_1"
    pause 0.2
    "bg momxsisterxmc_fort_2"
    pause 0.2
    "bg momxsisterxmc_fort_4"
    pause 0.2
    "bg momxsisterxmc_fort_2"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_momxsisterxmc_boxfort_2_0:
    scene img_momxsisterxmc_boxfort_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_boxfort_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_boxfort_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_boxfort_2_0

image img_momxsisterxmc_boxfort_stage_2_0:
    "bg momxsisterxmc_fort_1_0"
    pause 0.2
    "bg momxsisterxmc_fort_2_0"
    pause 0.2
    "bg momxsisterxmc_fort_4_0"
    pause 0.2
    "bg momxsisterxmc_fort_2_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_momxsisterxmc_boxfort_3:
    scene img_momxsisterxmc_boxfort_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_boxfort_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_boxfort_3

image img_momxsisterxmc_boxfort_stage_3:
    "bg momxsisterxmc_fort_1"
    pause 0.2
    "bg momxsisterxmc_fort_4"
    pause 0.1
    "bg momxsisterxmc_fort_2"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_momxsisterxmc_boxfort_3_0:
    scene img_momxsisterxmc_boxfort_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_boxfort_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_boxfort_3_0

image img_momxsisterxmc_boxfort_stage_3_0:
    "bg momxsisterxmc_fort_1_0"
    pause 0.1
    "bg momxsisterxmc_fort_2_0"
    pause 0.1
    "bg momxsisterxmc_fort_3_0"
    pause 0.1
    "bg momxsisterxmc_fort_4_0"
    pause 0.1
    "bg momxsisterxmc_fort_2_0"
    pause 0.1
    repeat

####################
## MENU
label lbl_momxsisterxmc_boxfort_menu:
    call screen scr_momxsisterxmc_boxfort_menu

screen scr_momxsisterxmc_boxfort_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_boxfort_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_boxfort_cum")

####################
## CUM
label lbl_momxsisterxmc_boxfort_cum:
    scene img_momxsisterxmc_boxfort_stage_1
    pov "{i}*Muffles*{/i}"
    sis "{i}*Pants*{/i}"
    mum "{i}*Moans*{/i}"
    pov "{i}*Panic muffles*{/i}"
    sis "Hmmmhmm? Whatcha say, dude?"
    mum "Hm?"
    pov "{i}*More panic muffles*{/i}"
    mum "{i}*Moans*{/i} Honey, don't talk with you mouth full-"
    sis "So fuckin rude, [povname]."
    mum "Ah-!"
    sis "Mm-?"
    if hscene_xray == 1:
        scene bg momxsisterxmc_fort_4_0
        with hpunch
        $ renpy.pause(0.5,hard=True)
        show bg momxsisterxmc_fort_5_1
        $ renpy.pause(0.3,hard=True)
        show bg momxsisterxmc_fort_5_2
        $ renpy.pause(0.3,hard=True)
        show bg momxsisterxmc_fort_5_3
        $ renpy.pause(0.3,hard=True)
        show bg momxsisterxmc_fort_5_4
        $ renpy.pause(0.3,hard=True)
        show bg momxsisterxmc_fort_5_5
        $ renpy.pause(0.3,hard=True)
        show bg momxsisterxmc_fort_5_6
        $ renpy.pause(0.3,hard=True)
        show bg momxsisterxmc_fort_5_7
        $ renpy.pause()
    else:
        scene bg momxsisterxmc_fort_4
        with hpunch
        $ renpy.pause(0.5,hard=True)
        scene bg momxsisterxmc_fort_3
        $ renpy.pause(0.3,hard=True)
        scene bg momxsisterxmc_fort_4
        $ renpy.pause(0.7,hard=True)
        scene bg momxsisterxmc_fort_3
        $ renpy.pause(0.3,hard=True)
        scene bg momxsisterxmc_fort_4
        $ renpy.pause()
    mum "Oh- sweetie, he just came in me."
    sis "[povname]!"
    sis "{i}*Exhales*{/i} You could have warned us-"
    pov "{i}*Muffled sigh*{/i}"
    if winc == 1:
        mum "{i}*Pants and moans*{/i} Honeycake, you just made a mess in mommy."
    else:
        mum "{i}*Pants and moans*{/i} Honeycake, you just made a mess in me."
    mum "Couldn't you have held it in a little longer?"
    sis "I wanna keep going- I don't know about you."
    if winc == 1:
        mum "You can keep going, sweetie. I'll keep your brother from moving around."
        mum "Show mommy how you move those hips~"
        sis "Mhmm~ Okay-"
        pov "{i}*Muffles*{/i}"
        mum "Hush, sweetie. You've said enough. You're staying in me until your sister has soaked us completely."
    else:
        mum "You can keep going, sweetie. I'll keep [povname] from moving around."
        mum "Show me how you move those hips~"
        sis "Mhmm~ Okay-"
        pov "{i}*Muffles*{/i}"
        mum "Hush, sweetie. You've said enough. You're staying in me until your [sisrole] has soaked us completely."
    pov "{i}*Defeated muffles*{/i}"

    scene black
    with fade
    $ renpy.pause()
    "After being drenched and cleaning up afterwards..."

    $ gtime = 3

    jump lbl_mybasement_night
