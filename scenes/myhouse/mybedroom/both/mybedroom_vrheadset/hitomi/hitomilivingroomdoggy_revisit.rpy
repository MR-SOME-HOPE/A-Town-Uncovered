####################
## Doggy (Mish)
label lbl_hitomi_livingroom_doggy_revisit_0:
    #$ hitomi_livingroom_doggy_revisit_counter = 0
    if hscene_xray == 0:
        jump lbl_hitomi_livingroom_doggy_revisit_1
    else:
        jump lbl_hitomi_livingroom_doggy_revisit_1_0

####################
## Stage 1
label lbl_hitomi_livingroom_doggy_revisit_1:
    scene img_hitomi_livingroom_doggy_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_1

image img_hitomi_livingroom_doggy_revisit_stage_1:
    "bg hitomilivingroomdoggy_1"
    pause 0.2
    "bg hitomilivingroomdoggy_2"
    pause 0.2
    "bg hitomilivingroomdoggy_3"
    pause 0.2
    "bg hitomilivingroomdoggy_4"
    pause 0.2
    "bg hitomilivingroomdoggy_5"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_hitomi_livingroom_doggy_revisit_1_0:
    scene img_hitomi_livingroom_doggy_revisit_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_1_0

image img_hitomi_livingroom_doggy_revisit_stage_1_0:
    "bg hitomilivingroomdoggy_1_0"
    pause 0.2
    "bg hitomilivingroomdoggy_2_0"
    pause 0.2
    "bg hitomilivingroomdoggy_3_0"
    pause 0.2
    "bg hitomilivingroomdoggy_4_0"
    pause 0.2
    "bg hitomilivingroomdoggy_5_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_hitomi_livingroom_doggy_revisit_2:
    scene img_hitomi_livingroom_doggy_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_2

image img_hitomi_livingroom_doggy_revisit_stage_2:
    "bg hitomilivingroomdoggy_6"
    pause 0.2
    "bg hitomilivingroomdoggy_7"
    pause 0.2
    "bg hitomilivingroomdoggy_8"
    pause 0.2
    "bg hitomilivingroomdoggy_9"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_hitomi_livingroom_doggy_revisit_2_0:
    scene img_hitomi_livingroom_doggy_revisit_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_2_0

image img_hitomi_livingroom_doggy_revisit_stage_2_0:
    "bg hitomilivingroomdoggy_6_0"
    pause 0.2
    "bg hitomilivingroomdoggy_7_0"
    pause 0.2
    "bg hitomilivingroomdoggy_8_0"
    pause 0.2
    "bg hitomilivingroomdoggy_9_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_hitomi_livingroom_doggy_revisit_3:
    scene img_hitomi_livingroom_doggy_revisit_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_3

image img_hitomi_livingroom_doggy_revisit_stage_3:
    "bg hitomilivingroomdoggy_10"
    pause 0.2
    "bg hitomilivingroomdoggy_11"
    pause 0.2
    "bg hitomilivingroomdoggy_12"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_hitomi_livingroom_doggy_revisit_3_0:
    scene img_hitomi_livingroom_doggy_revisit_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_livingroom_doggy_revisit_3_0

image img_hitomi_livingroom_doggy_revisit_stage_3_0:
    "bg hitomilivingroomdoggy_10_0"
    pause 0.2
    "bg hitomilivingroomdoggy_11_0"
    pause 0.2
    "bg hitomilivingroomdoggy_12_0"
    pause 0.2
    repeat

####################
## Cum
label lbl_hitomi_livingroom_doggy_revisit_menu:
    call screen scr_hitomi_livingroom_doggy_revisit_menu

screen scr_hitomi_livingroom_doggy_revisit_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_livingroom_doggy_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_livingroom_doggy_revisit_cumchoice")

label lbl_hitomi_livingroom_doggy_revisit_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_hitomi_livingroom_doggy_revisit_cumin
            else:
                jump lbl_hitomi_livingroom_doggy_revisit_cumin_0
        "Cum on her":
            jump lbl_hitomi_livingroom_doggy_revisit_cumout

####################
## Cum In
label lbl_hitomi_livingroom_doggy_revisit_cumin:
    scene bg hitomilivingroomdoggy_14_0
    $ renpy.pause(1.5,hard=True)
    show bg hitomilivingroomdoggy_14_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_14_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_14_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_14_4
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_14_5
    hit "Oh wow- {i}*pants*{/i}"
    hit "You really just came inside, huh?"
    pov "Sorry, I couldn't help myself."
    pov "{i}*pants*{/i} Your pussy was just too fucking good, Hitomi."
    hit "Mmm... {i}*exhale*{/i} I know, [povname]."
    hit "Likewise with that massive cock of yours."
    hit "I better get back to work..."
    hit "I can't leave the store with those idiots for too long."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Cum In XRAY
label lbl_hitomi_livingroom_doggy_revisit_cumin_0:
    scene bg hitomilivingroomdoggy_13_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_4
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_5
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_6
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_7
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_8
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_9
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_10
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_11
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_13_12
    $ renpy.pause()
    hit "Oh wow- {i}*pants*{/i}"
    hit "You really just came inside, huh?"
    pov "Sorry, I couldn't help myself."
    pov "{i}*pants*{/i} Your pussy was just too fucking good, Hitomi."
    hit "Mmm... {i}*exhale*{/i} I know, [povname]."
    hit "Likewise with that massive cock of yours."
    hit "I better get back to work..."
    hit "I can't leave the store with those idiots for too long."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Doggy Cum Out
label lbl_hitomi_livingroom_doggy_revisit_cumout:
    scene bg hitomilivingroomdoggy_15_0
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_4
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_5
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_6
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_7
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_8
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_9
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_10
    $ renpy.pause(0.3,hard=True)
    show bg hitomilivingroomdoggy_15_11
    hit "Fuck that's hot-"
    hit "{i}*Chuckles*{/i} Like literally... it actually feels kinda nice."
    hit "As if you're about to give me a full body Swedish massage."
    pov "{i}*Pants*{/i} Hahaha! I can if you want."
    pov "I hear sperm is great for the skin."
    hit "I don't know what kinda person told you that."
    hit "Everyone knows it's a great teeth whitener."
    hit "Ugh- anyway. I gotta head back to the store, I can't leave those idiots in charge for too long."
    hit "Be an angel and grab me a towel."
    pov "It's the least I can do for you."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
