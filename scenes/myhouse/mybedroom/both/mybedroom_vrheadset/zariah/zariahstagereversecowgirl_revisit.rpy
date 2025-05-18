####################
## Zariah Stage Reverse Cowgirl
label lbl_zariah_stage_reverse_cowgirl_revisit_0:
    if hscene_xray == 0:
        scene bg zariahstagereversecowgirl_1
        with fade
        jump lbl_zariah_stage_reverse_cowgirl_revisit_1
    else:
        scene bg zariahstagereversecowgirl_1_0
        with fade
        jump lbl_zariah_stage_reverse_cowgirl_revisit_1_0

####################
## Stage 1
label lbl_zariah_stage_reverse_cowgirl_revisit_1:
    scene img_zariah_stage_reverse_cowgirl_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_1

image img_zariah_stage_reverse_cowgirl_stage_1:
    "bg zariahstagereversecowgirl_1"
    pause 0.2
    "bg zariahstagereversecowgirl_2"
    pause 0.2
    "bg zariahstagereversecowgirl_3"
    pause 0.2
    "bg zariahstagereversecowgirl_4"
    pause 0.2
    "bg zariahstagereversecowgirl_5"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_zariah_stage_reverse_cowgirl_revisit_1_0:
    scene img_zariah_stage_reverse_cowgirl_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_1_0

image img_zariah_stage_reverse_cowgirl_stage_1_0:
    "bg zariahstagereversecowgirl_1_0"
    pause 0.2
    "bg zariahstagereversecowgirl_2_0"
    pause 0.2
    "bg zariahstagereversecowgirl_3_0"
    pause 0.2
    "bg zariahstagereversecowgirl_4_0"
    pause 0.2
    "bg zariahstagereversecowgirl_5_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_zariah_stage_reverse_cowgirl_revisit_2:
    scene img_zariah_stage_reverse_cowgirl_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_2

image img_zariah_stage_reverse_cowgirl_stage_2:
    "bg zariahstagereversecowgirl_6"
    pause 0.2
    "bg zariahstagereversecowgirl_7"
    pause 0.1
    "bg zariahstagereversecowgirl_9"
    pause 0.2
    "bg zariahstagereversecowgirl_10"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_zariah_stage_reverse_cowgirl_revisit_2_0:
    scene img_zariah_stage_reverse_cowgirl_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_2_0

image img_zariah_stage_reverse_cowgirl_stage_2_0:
    "bg zariahstagereversecowgirl_6_0"
    pause 0.2
    "bg zariahstagereversecowgirl_7_0"
    pause 0.1
    "bg zariahstagereversecowgirl_9_0"
    pause 0.2
    "bg zariahstagereversecowgirl_10_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_zariah_stage_reverse_cowgirl_revisit_3:
    scene img_zariah_stage_reverse_cowgirl_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_3

image img_zariah_stage_reverse_cowgirl_stage_3:
    "bg zariahstagereversecowgirl_11"
    pause 0.2
    "bg zariahstagereversecowgirl_14"
    pause 0.2
    "bg zariahstagereversecowgirl_15"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_zariah_stage_reverse_cowgirl_revisit_3_0:
    scene img_zariah_stage_reverse_cowgirl_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_zariah_stage_reverse_cowgirl_revisit_3_0

image img_zariah_stage_reverse_cowgirl_stage_3_0:
    "bg zariahstagereversecowgirl_11_0"
    pause 0.2
    "bg zariahstagereversecowgirl_14_0"
    pause 0.2
    "bg zariahstagereversecowgirl_15_0"
    pause 0.2
    repeat

####################
## Cum
label lbl_zariah_stage_reverse_cowgirl_revisit_menu:
    call screen scr_zariah_stage_reverse_cowgirl_revisit_menu

screen scr_zariah_stage_reverse_cowgirl_revisit_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariah_stage_reverse_cowgirl_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action If(hscene_xray == 0, Jump("lbl_zariah_stage_reverse_cowgirl_revisit_cumin"), Jump("lbl_zariah_stage_reverse_cowgirl_revisit_cumin_0"))

####################
## Cum In
label lbl_zariah_stage_reverse_cowgirl_revisit_cumin:
    pov "I'm- gonna cum-"
    zar "..."
    pov "Zar-! I'm gonna cum-"
    zar "Huh-?"
    zar "I can't- what-?"
    pov "Zar!!"
    scene bg zariahstagereversecowgirl_8
    $ renpy.pause(1.5,hard=True)
    show bg zariahstagereversecowgirl_16_1
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_16_2
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_16_3
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_16_4
    zar "Oh- [povname]! Did you just-?"
    pov "{i}*Huffs*{/i} I'm sorry- I tried to warn you."
    zar "It's okay!"
    zar "I prefer it this way!"
    zar "My boss would kill me if I made a mess on the equipment!"
    pov "Are you safe?"
    zar "Yeah, I'm taking shit, don't worry about it, dude!"
    zar "Nice fuck sesh!"
    pov "Thanks, you too! Riding to the beat is a really immersive experience!"
    zar "I'm glad you think so too!"
    zar "There should be some paper rolls on the floor! Clean us up but don't make it obvious!"
    pov "Gotcha!"
    scene black
    with fade
    $ renpy.pause()
    
    jump lbl_vrheadset_character_selection

####################
## Cum In XRAY
label lbl_zariah_stage_reverse_cowgirl_revisit_cumin_0:
    pov "I'm- gonna cum-"
    zar "..."
    pov "Zar-! I'm gonna cum-"
    zar "Huh-?"
    zar "I can't- what-?"
    pov "Zar!!"
    scene bg zariahstagereversecowgirl_8_0
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_1
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_2
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_3
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_4
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_5
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_6
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_7
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_8
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_9
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_10
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_11
    $ renpy.pause(0.3,hard=True)
    show bg zariahstagereversecowgirl_17_12
    zar "Oh- [povname]! Did you just-?"
    pov "{i}*Huffs*{/i} I'm sorry- I tried to warn you."
    zar "It's okay!"
    zar "I prefer it this way!"
    zar "My boss would kill me if I made a mess on the equipment!"
    pov "Are you safe?"
    zar "Yeah, I'm taking shit, don't worry about it, dude!"
    zar "Nice fuck sesh!"
    pov "Thanks, you too! Riding to the beat is a really immersive experience!"
    zar "I'm glad you think so too!"
    zar "There should be some paper rolls on the floor! Clean us up but don't make it obvious!"
    pov "Gotcha!"
    scene black
    with fade
    $ renpy.pause()
    
    jump lbl_vrheadset_character_selection
