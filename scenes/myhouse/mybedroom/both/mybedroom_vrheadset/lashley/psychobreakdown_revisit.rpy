label lbl_psychobreakdown_hscene_revisit_continue:
    $ psychobreakdown_hscene = 1
    if hscene_xray == 1:
        jump lbl_psychobreakdown_hscene_revisit_1_0
    else:
        jump lbl_psychobreakdown_hscene_revisit_1

####################
## Stage 1
label lbl_psychobreakdown_hscene_revisit_1:
    $ psychobreakdown_hscene += 1
    scene img_psychobreakdown_hscene_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_menu

image img_psychobreakdown_hscene_revisit_stage_1:
    "bg psychobreakdown_hscene_1"
    pause 0.3
    "bg psychobreakdown_hscene_2"
    pause 0.1
    "bg psychobreakdown_hscene_3"
    pause 0.1
    "bg psychobreakdown_hscene_4"
    pause 0.3
    "bg psychobreakdown_hscene_5"
    pause 0.3
    repeat

####################
## Stage 1 XRAY
label lbl_psychobreakdown_hscene_revisit_1_0:
    $ psychobreakdown_hscene += 1
    scene img_psychobreakdown_hscene_revisit_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_2_0
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_2_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_menu

image img_psychobreakdown_hscene_revisit_stage_1_0:
    "bg psychobreakdown_hscene_1_0"
    pause 0.3
    "bg psychobreakdown_hscene_2_0"
    pause 0.1
    "bg psychobreakdown_hscene_3_0"
    pause 0.1
    "bg psychobreakdown_hscene_4_0"
    pause 0.3
    "bg psychobreakdown_hscene_5_0"
    pause 0.3
    repeat

####################
## Stage 2
label lbl_psychobreakdown_hscene_revisit_2:
    $ psychobreakdown_hscene += 1
    scene img_psychobreakdown_hscene_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_menu
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_menu

image img_psychobreakdown_hscene_revisit_stage_2:
    "bg psychobreakdown_hscene_1"
    pause 0.3
    "bg psychobreakdown_hscene_2"
    pause 0.1
    "bg psychobreakdown_hscene_4"
    pause 0.2
    "bg psychobreakdown_hscene_5"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_psychobreakdown_hscene_revisit_2_0:
    $ psychobreakdown_hscene += 1
    scene img_psychobreakdown_hscene_revisit_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_menu
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_3_0
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_psychobreakdown_hscene_revisit_menu

image img_psychobreakdown_hscene_revisit_stage_2_0:
    "bg psychobreakdown_hscene_1_0"
    pause 0.3
    "bg psychobreakdown_hscene_2_0"
    pause 0.1
    "bg psychobreakdown_hscene_4_0"
    pause 0.2
    "bg psychobreakdown_hscene_5_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_psychobreakdown_hscene_revisit_3:
    $ psychobreakdown_hscene += 1
    scene img_psychobreakdown_hscene_revisit_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_psychobreakdown_hscene_revisit_menu

image img_psychobreakdown_hscene_revisit_stage_3:
    "bg psychobreakdown_hscene_1"
    pause 0.2
    "bg psychobreakdown_hscene_4"
    pause 0.1
    "bg psychobreakdown_hscene_5"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_psychobreakdown_hscene_revisit_3_0:
    $ psychobreakdown_hscene += 1
    scene img_psychobreakdown_hscene_revisit_stage_3_0
    $ renpy.pause(20,hard=True)
    jump lbl_psychobreakdown_hscene_revisit_menu

image img_psychobreakdown_hscene_revisit_stage_3_0:
    "bg psychobreakdown_hscene_1_0"
    pause 0.2
    "bg psychobreakdown_hscene_4_0"
    pause 0.1
    "bg psychobreakdown_hscene_5_0"
    pause 0.2
    repeat

####################
## Menu
label lbl_psychobreakdown_hscene_revisit_menu:
    call screen scr_psychobreakdown_hscene_revisit_menu

screen scr_psychobreakdown_hscene_revisit_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_psychobreakdown_hscene_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_psychobreakdown_hscene_revisit_cum")

####################
## Cum
label lbl_psychobreakdown_hscene_revisit_cum:
    pov "I- I- I'm gonna-"

    pri "What's that, [povname]? I can't hear you from all the sloppy noises we're making-"

    pov "Stop- I'm- gonna cum-"

    if hscene_xray == 1:
        scene bg psychobreakdown_hscene_4_0
        with vpunch
    else:
        scene bg psychobreakdown_hscene_4
        with vpunch
    #-Once sex scene is done, Lashley is resting on the MC both of them out of breath-

    pri "Ah- nooooo~ No, you're not my impatient one."
    pri "We're just gonna sit here for a bit while you catch your breath."
    pri "You're not allowed to cum, I'm gonna be using you all night."

    pov "{i}*Huff* *Huff*...{/i}"
    pov "B-but…"

    pri "Shhh.. just breathe, deary."

    pov "I don’t think I’ve ever been ridden that hard before, holy crap…"

    pri "{i}*Pants*{/i} You've got 10 seconds."

    pov "Wait- what?"

    #-Lashley brings her head up to look at the Mc with the same deranged in lust look on her face-
    if hscene_xray == 1:
        scene img_psychobreakdown_hscene_revisit_stage_1_0
    else:
        scene img_psychobreakdown_hscene_revisit_stage_1
    pri "{i}*Chuckles*{/i}"
    pri "I. WANT. MORE!"

    pov "Gah!"
    pov "How- how are you still going-?"

    pri "I told you, didn't I?"
    pri "I’M RIDING THAT DICK UNTIL IT FALLS OFF!"

    pov "I-I think I need an adult."

    pri "I AM AN ADULT!"
    pri "NOW HOLD TIGHT, I'M GOING FOR IT!"
    if hscene_xray == 1:
        scene img_psychobreakdown_hscene_revisit_stage_3_0
    else:
        scene img_psychobreakdown_hscene_revisit_stage_3
    pri "{i}*Chuckles*{/i}"
    $ renpy.pause(5,hard=True)

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
