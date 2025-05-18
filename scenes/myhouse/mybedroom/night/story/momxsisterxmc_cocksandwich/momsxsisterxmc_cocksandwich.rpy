## Mom x Sister x MC Cock Sandwich
label lbl_momxsisterxmc_cocksandwich:
    scene bg parentsbedroom_nightlightson
    show pov sad_talk at left
    show mum confused at right
    with dissolve
    pov "[missus]... Can you help tuck me in bed? My mind is racing but my body is exhausted."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "Need a little help clearing your mind?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "Mhmm- yeaah..."
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "Perhaps, [sister] can help me with that."
    show mum neutral_talk at right
    mum "Go get ready for bed and we'll meet you there, okay?"

    scene black
    with fade
    $ renpy.pause()
    "In your bed..."

    jump lbl_momxsisterxmc_cocksandwich_0

####################
## START
label lbl_momxsisterxmc_cocksandwich_0:
    scene bg momxsisterxmc_cocksandwich_1
    with fade

    jump lbl_momxsisterxmc_cocksandwich_1

####################
## Stage 1
label lbl_momxsisterxmc_cocksandwich_1:
    scene img_momxsisterxmc_cocksandwich_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_1

image img_momxsisterxmc_cocksandwich_stage_1:
    "bg momxsisterxmc_cocksandwich_1"
    pause 0.3
    "bg momxsisterxmc_cocksandwich_2"
    pause 0.3
    "bg momxsisterxmc_cocksandwich_3"
    pause 0.3
    "bg momxsisterxmc_cocksandwich_4"
    pause 0.3
    "bg momxsisterxmc_cocksandwich_5"
    pause 0.3
    repeat

####################
## Stage 2
label lbl_momxsisterxmc_cocksandwich_2:
    scene img_momxsisterxmc_cocksandwich_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_2

image img_momxsisterxmc_cocksandwich_stage_2:
    "bg momxsisterxmc_cocksandwich_1"
    pause 0.2
    "bg momxsisterxmc_cocksandwich_2"
    pause 0.2
    "bg momxsisterxmc_cocksandwich_3"
    pause 0.2
    "bg momxsisterxmc_cocksandwich_4"
    pause 0.2
    "bg momxsisterxmc_cocksandwich_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_momxsisterxmc_cocksandwich_3:
    scene img_momxsisterxmc_cocksandwich_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_momxsisterxmc_cocksandwich_3

image img_momxsisterxmc_cocksandwich_stage_3:
    "bg momxsisterxmc_cocksandwich_1"
    pause 0.1
    "bg momxsisterxmc_cocksandwich_2"
    pause 0.1
    "bg momxsisterxmc_cocksandwich_3"
    pause 0.1
    "bg momxsisterxmc_cocksandwich_4"
    pause 0.1
    "bg momxsisterxmc_cocksandwich_5"
    pause 0.1
    repeat

####################
## CUM
label lbl_momxsisterxmc_cocksandwich_cum:
    call screen scr_momxsisterxmc_cocksandwich_cum

screen scr_momxsisterxmc_cocksandwich_cum():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_cocksandwich_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momxsisterxmc_cocksandwich_cum1")

####################
## CUM
label lbl_momxsisterxmc_cocksandwich_cum1:
    scene img_momxsisterxmc_cocksandwich_stage_3
    pov "I-"
    pov "I'm.."
    pov "I'm gonna cum-"
    sis "Oooh yes!!"
    sis "Just what I've been waiting for!"
    mum "C'mon, baby- cover all of us in your beautiful cum."
    sis "C'mon, dude-"
    pov "Mmmmmpph!!"
    show bg momxsisterxmc_cocksandwich_cum
    with hpunch
    $ renpy.pause(2,hard=True)
    sis "Jesus Christ!"
    sis "I knew you came a lot but fuckk-"
    sis "It's literally like a blanket of it."
    mum "I'm so proud of you, [povname]."
    mum "I love how much you give to the both of us."
    pov "*Huff huff* All thanks to the both of you, of course."
    pov "I just wanna show how much I appreciate you tending to me."

    $ townmap_enabled = 1

    $ gtime = 3

    scene bg mybedroom_night
    with fade

    jump lbl_mybedroom_night_setup
