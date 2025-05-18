## Director Office Chair Sex
label lbl_principal_office_chair_sex_revisit_0:
    if hscene_xray == 0:
        jump lbl_principal_office_chair_sex_revisit_1
    else:
        jump lbl_principal_office_chair_sex_revisit_1_0

####################
## Stage 1
label lbl_principal_office_chair_sex_revisit_1:
    scene img_principal_office_chair_sex_revisit_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_principal_office_chair_sex_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_revisit_1

image img_principal_office_chair_sex_revisit_stage_1:
    "bg principalofficechairsex_1"
    pause 0.2
    "bg principalofficechairsex_2"
    pause 0.2
    "bg principalofficechairsex_3"
    pause 0.2
    "bg principalofficechairsex_4"
    pause 0.2
    "bg principalofficechairsex_5"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_principal_office_chair_sex_revisit_1_0:
    scene img_principal_office_chair_sex_revisit_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_principal_office_chair_sex_revisit_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_revisit_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_revisit_1_0

image img_principal_office_chair_sex_revisit_stage_1_0:
    "bg principalofficechairsex_anal_1_0"
    pause 0.2
    "bg principalofficechairsex_anal_2_0"
    pause 0.2
    "bg principalofficechairsex_anal_3_0"
    pause 0.2
    "bg principalofficechairsex_anal_4_0"
    pause 0.2
    "bg principalofficechairsex_anal_5_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_principal_office_chair_sex_revisit_2:
    scene img_principal_office_chair_sex_revisit_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_principal_office_chair_sex_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_revisit_2

image img_principal_office_chair_sex_revisit_stage_2:
    "bg principalofficechairsex_6"
    pause 0.2
    "bg principalofficechairsex_7"
    pause 0.2
    "bg principalofficechairsex_8"
    pause 0.2
    "bg principalofficechairsex_9"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_principal_office_chair_sex_revisit_2_0:
    scene img_principal_office_chair_sex_revisit_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_principal_office_chair_sex_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_revisit_2_0

image img_principal_office_chair_sex_revisit_stage_2_0:
    "bg principalofficechairsex_anal_6_0"
    pause 0.2
    "bg principalofficechairsex_anal_7_0"
    pause 0.2
    "bg principalofficechairsex_anal_8_0"
    pause 0.2
    "bg principalofficechairsex_anal_9_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_principal_office_chair_sex_revisit_3:
    scene img_principal_office_chair_sex_revisit_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_revisit_3

image img_principal_office_chair_sex_revisit_stage_3:
    "bg principalofficechairsex_10"
    pause 0.2
    "bg principalofficechairsex_11"
    pause 0.1
    "bg principalofficechairsex_12"
    pause 0.1
    "bg principalofficechairsex_13"
    pause 0.1
    repeat

####################
## Stage 3 XRAY
label lbl_principal_office_chair_sex_revisit_3_0:
    scene img_principal_office_chair_sex_revisit_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_revisit_3_0

image img_principal_office_chair_sex_revisit_stage_3_0:
    "bg principalofficechairsex_anal_10_0"
    pause 0.2
    "bg principalofficechairsex_anal_11_0"
    pause 0.1
    "bg principalofficechairsex_anal_12_0"
    pause 0.1
    "bg principalofficechairsex_anal_13_0"
    pause 0.1
    repeat

####################
## Missionary Cum
label lbl_principal_office_chair_sex_revisit_cum:
    jump lbl_principal_office_chair_sex_revisit_cum_2

label lbl_principal_office_chair_sex_revisit_cum_2:
    call screen scr_principal_office_chair_sex_revisit_cum_2

screen scr_principal_office_chair_sex_revisit_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_principal_office_chair_sex_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_principal_office_chair_sex_revisit_cumchoice")

label lbl_principal_office_chair_sex_revisit_cumchoice:
    if hscene_xray == 0:
        jump lbl_principal_office_chair_sex_revisit_cumin
    else:
        jump lbl_principal_office_chair_sex_revisit_cumin_0

####################
## Cum In
label lbl_principal_office_chair_sex_revisit_cumin:
    scene bg principalofficechairsex_14_0
    $ renpy.pause(1.5,hard=True)
    show bg principalofficechairsex_14_1
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_14_2
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_14_3
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_14_4
    $ renpy.pause(1,hard=True)
    pri "{i}*Pants*{/i}"
    pov "Mmm.. fuckk..."
    pri "Ah!"
    pri "[povname]!"
    pri "I can't believe you just said that!"
    pov "Oop- {i}*Exhale*{/i} sorry... I just-"
    pov "That felt so good."
    pri "{i}*Pants*{/i} O- of course, [povname]."
    pri "Why'd you think God made us like this."
    pri "Do you think he'd make it so... pleasurable if it was a sin...?"
    pov "No, of course not. He knows what he's doing."
    pri "{i}*Pants*{/i} Dear... Lord, thank you for this blessed day."
    pri "Thank you for- {i}*pants*{/i} [povname]- and reaching out to him in his dream."
    pri "Bless him with more pleasant dreams, I know you will. Amen."
    pov "Yeah, thanks Big G."
    pri "Let's... clean ourselves up and-"
    pri "[povname]? Let's keep this between us, okay?"
    pri "This is no one else's business except yours, mine, and the-"
    pri "Almighty."
    pov "I won't tell another soul, don't worry."
    pov "Who do you think I am."
    
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Cum In XRAY
label lbl_principal_office_chair_sex_revisit_cumin_0:
    scene bg principalofficechairsex_anal_14_0
    $ renpy.pause(1.5,hard=True)
    show bg principalofficechairsex_anal_14_1
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_2
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_3
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_4
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_5
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_6
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_7
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_8
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_9
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_10
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_11
    $ renpy.pause(1,hard=True)
    pri "{i}*Pants*{/i}"
    pov "Mmm.. fuckk..."
    pri "Ah!"
    pri "[povname]!"
    pri "I can't believe you just said that!"
    pov "Oop- {i}*Exhale*{/i} sorry... I just-"
    pov "That felt so good."
    pri "{i}*Pants*{/i} O- of course, [povname]."
    pri "Why'd you think God made us like this."
    pri "Do you think he'd make it so... pleasurable if it was a sin...?"
    pov "No, of course not. He knows what he's doing."
    pri "{i}*Pants*{/i} Dear... Lord, thank you for this blessed day."
    pri "Thank you for- {i}*pants*{/i} [povname]- and reaching out to him in his dream."
    pri "Bless him with more pleasant dreams, I know you will. Amen."
    pov "Yeah, thanks Big G."
    pri "Let's... clean ourselves up and-"
    pri "[povname]? Let's keep this between us, okay?"
    pri "This is no one else's business except yours, mine, and the-"
    pri "Almighty."
    pov "I won't tell another soul, don't worry."
    pov "Who do you think I am."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Cum Out
label lbl_principal_office_chair_sex_revisit_cumout:
    show bg allawaybedroommish_5_0#NOTE make scene not show when replacing this line
    $ renpy.pause(0.6,hard=True)
    show bg allawaybedroommish_5_1
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_2
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_3
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_4
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_5
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_6
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_7
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_8
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_9
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_10
    $ renpy.pause(0.8,hard=True)
    mis "Jesus Christ, [povname]. {i}*Pants*{/i} Look at the frikkin' mess you made."
    pov "I know, {i}*pants*{/i} I call it art."
    mis "Am I a canvas now?"
    pov "You're part of my masterpiece."
    mis "{i}*Pants*{/i} It's so.. hot..."
    mis "And sticky..."
    pov "{i}*Pants*{/i} Am I in trouble?"
    mis "If I give you detention, I'm afraid what I'll do with you."
    pov "Is that a threat or a proposal?"
    mis "Hehehe~ {i}*pants*{/i} Maybe both?"
    mis "Now... get off me and get me some towels. I think 5 big ones will suffice."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
