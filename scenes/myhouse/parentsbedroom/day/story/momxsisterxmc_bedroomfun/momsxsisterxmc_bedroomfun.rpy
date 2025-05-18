## Mom x Sister x MC Bedroom Fun
label lbl_momxsisterxmc_bedroomfun:
    scene bg mykitchen_day
    show pov smirk_talk at left
    with dissolve
    show mum confused at right
    with dissolve
    pov "Hey, did you get a chance to get off this morning, [missus]?"
    show pov smirk at left
    show mum confused_talk at right
    mum "Hey, [povname]. Unfortunately not... I wasn't really in the mood."
    show pov smirk_talk at left
    show mum shocked at right
    pov "Are you in the mood now? You can use us."
    show pov smirk at left
    show mum smirk_talk at right
    mum "Us?"
    show pov smirk_talk at left
    show mum smirk at right
    pov "[sister] and I, of course. Who else?"
    show pov smirk at left
    show mum smirk_talk at right
    mum "Hmmm~ I can't say no to that."
    show pov neutral at left
    show mum smirk_talk at right
    mum "Let's go to my room, go grab [sister]."
    
    scene black
    with fade
    $ renpy.pause()
    "Up in the bedroom..."

    jump lbl_momxsisterxmc_bedroomfun_0

####################
## Bedroom Fun
label lbl_momxsisterxmc_bedroomfun_0:
    scene bg momxsisterxmc_bedroomfun_1
    with fade

    jump lbl_momxsisterxmc_bedroomfun_1

####################
## Stage 1
label lbl_momxsisterxmc_bedroomfun_1:
    scene img_momxsisterxmc_bedroomfun_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_1

image img_momxsisterxmc_bedroomfun_stage_1:
    "bg momxsisterxmc_bedroomfun_1"
    pause 0.3
    "bg momxsisterxmc_bedroomfun_2"
    pause 0.3
    "bg momxsisterxmc_bedroomfun_3"
    pause 0.3
    "bg momxsisterxmc_bedroomfun_4"
    pause 0.3
    "bg momxsisterxmc_bedroomfun_5"
    pause 0.3
    repeat

####################
## Stage 2
label lbl_momxsisterxmc_bedroomfun_2:
    scene img_momxsisterxmc_bedroomfun_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_2

image img_momxsisterxmc_bedroomfun_stage_2:
    "bg momxsisterxmc_bedroomfun_1"
    pause 0.2
    "bg momxsisterxmc_bedroomfun_2"
    pause 0.2
    "bg momxsisterxmc_bedroomfun_3"
    pause 0.2
    "bg momxsisterxmc_bedroomfun_4"
    pause 0.2
    "bg momxsisterxmc_bedroomfun_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_momxsisterxmc_bedroomfun_3:
    scene img_momxsisterxmc_bedroomfun_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_bedroomfun_3

image img_momxsisterxmc_bedroomfun_stage_3:
    "bg momxsisterxmc_bedroomfun_1"
    pause 0.1
    "bg momxsisterxmc_bedroomfun_2"
    pause 0.1
    "bg momxsisterxmc_bedroomfun_3"
    pause 0.1
    "bg momxsisterxmc_bedroomfun_4"
    pause 0.1
    "bg momxsisterxmc_bedroomfun_5"
    pause 0.1
    repeat

####################
## CUM
label lbl_momxsisterxmc_bedroomfun_cum:
    call screen scr_momxsisterxmc_bedroomfun_cum

screen scr_momxsisterxmc_bedroomfun_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_bedroomfun_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_bedroomfun_cum1")

# label lbl_momxsisterxmc_bedroomfun_cumchoice:

#     menu:
#         "Cum inside Mom's mouth" if winc == 1:
#             jump lbl_momxsisterxmc_bedroomfun_cummom
#         "Cum inside [missus]'s mouth" if winc == 0:
#             jump lbl_momxsisterxmc_bedroomfun_cummom
#         "Cum inside [sister]'s mouth":
#             jump lbl_momxsisterxmc_bedroomfun_cumsis

####################
## CUM
label lbl_momxsisterxmc_bedroomfun_cum1:
    scene img_momxsisterxmc_bedroomfun_stage_3
    pov "I-"
    pov "I'm.."
    pov "I'm gonna cum-"
    mum "*Muffled* *Murrmurrr*"
    sis "Cum inside her, [povname]. I know she wants it. She wants you so bad."
    show bg momxsisterxmc_bedroomfun_cum
    with hpunch
    $ renpy.pause(2,hard=True)
    mum "*Muffleedd* *Murr murr*"
    pov "*Huff huff* Wh- what was that?"
    sis "*Pants* She said, that felt amazing-"
    pov "How can you understand her?"
    sis "She's communicating in tongue."
    pov "*Chuckles* I'll go clean us up. I hope you enjoyed that, [missus]."
    mum "Mhmmpph! Mmhm-"

    $ townmap_enabled = 1

    scene bg myhallway_day 
    with fade
    
    jump lbl_myhallway_day_setup
