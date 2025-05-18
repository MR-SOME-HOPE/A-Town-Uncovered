## Lailah Lying Doggy
label lbl_lailah_lying_doggy:
    ## PRE STORY

label lbl_lailah_lying_doggy_0:
    if hscene_xray == 0:
        jump lbl_lailah_lying_doggy_1
    else:
        jump lbl_lailah_lying_doggy_1_0

####################
## Doggy Stage 1
label lbl_lailah_lying_doggy_1:
    scene img_lailah_lying_doggy_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_lailah_lying_doggy_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lailah_lying_doggy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lailah_lying_doggy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lailah_lying_doggy_1

image img_lailah_lying_doggy_stage_1:
    "bg lailahlyingdoggy_1"
    pause 0.2
    "bg lailahlyingdoggy_2"
    pause 0.2
    "bg lailahlyingdoggy_3"
    pause 0.2
    "bg lailahlyingdoggy_4"
    pause 0.2
    "bg lailahlyingdoggy_5"
    pause 0.2
    repeat

####################
## Doggy Stage 1 XRAY
label lbl_lailah_lying_doggy_1_0:
    scene img_lailah_lying_doggy_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_lailah_lying_doggy_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lailah_lying_doggy_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lailah_lying_doggy_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lailah_lying_doggy_1_0

image img_lailah_lying_doggy_stage_1_0:
    "bg lailahlyingdoggy_1_0"
    pause 0.2
    "bg lailahlyingdoggy_2_0"
    pause 0.2
    "bg lailahlyingdoggy_3_0"
    pause 0.2
    "bg lailahlyingdoggy_4_0"
    pause 0.2
    "bg lailahlyingdoggy_5_0"
    pause 0.2
    repeat
####################
## Doggy Stage 2
label lbl_lailah_lying_doggy_2:
    scene img_lailah_lying_doggy_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lailah_lying_doggy_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lailah_lying_doggy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lailah_lying_doggy_2

image img_lailah_lying_doggy_stage_2:
    "bg lailahlyingdoggy_6"
    pause 0.2
    "bg lailahlyingdoggy_8"
    pause 0.2
    "bg lailahlyingdoggy_9"
    pause 0.2
    "bg lailahlyingdoggy_10"
    pause 0.2
    repeat
####################
## Doggy Stage 2 XRAY
label lbl_lailah_lying_doggy_2_0:
    scene img_lailah_lying_doggy_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lailah_lying_doggy_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lailah_lying_doggy_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lailah_lying_doggy_2_0

image img_lailah_lying_doggy_stage_2_0:
    "bg lailahlyingdoggy_6_0"
    pause 0.2
    "bg lailahlyingdoggy_8_0"
    pause 0.2
    "bg lailahlyingdoggy_9_0"
    pause 0.2
    "bg lailahlyingdoggy_10_0"
    pause 0.2
    repeat

####################
## Doggy Stage 3
label lbl_lailah_lying_doggy_3:
    scene img_lailah_lying_doggy_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lailah_lying_doggy_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lailah_lying_doggy_3

image img_lailah_lying_doggy_stage_3:
    "bg lailahlyingdoggy_11"
    pause 0.2
    "bg lailahlyingdoggy_14"
    pause 0.2
    "bg lailahlyingdoggy_15"
    pause 0.2
    repeat

####################
## Doggy Stage 3 XRAY
label lbl_lailah_lying_doggy_3_0:
    scene img_lailah_lying_doggy_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lailah_lying_doggy_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lailah_lying_doggy_3_0

image img_lailah_lying_doggy_stage_3_0:
    "bg lailahlyingdoggy_11_0"
    pause 0.2
    "bg lailahlyingdoggy_14_0"
    pause 0.2
    "bg lailahlyingdoggy_15_0"
    pause 0.2
    repeat

####################
## Doggy Cum
label lbl_lailah_lying_doggy_menu:
    call screen scr_lailah_lying_doggy_menu

screen scr_lailah_lying_doggy_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lailah_lying_doggy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lailah_lying_doggy_cum")

label lbl_lailah_lying_doggy_cum:
    lai "Just come inside me!"
    lai "I want it inside me!"
    lai "It's okay, [povname]!"

    if hscene_xray == 0:
        jump lbl_lailah_lying_doggy_cumin
    else:
        jump lbl_lailah_lying_doggy_cumin_0

####################
## Doggy Cum In
label lbl_lailah_lying_doggy_cumin:
    scene bg lailahlyingdoggy_14
    $ renpy.pause(1.5,hard=True)
    show bg lailahlyingdoggy_16_1
    $ renpy.pause(0.4,hard=True)
    show bg lailahlyingdoggy_16_2
    $ renpy.pause()
    lai "Ahhh~ Yesss~!"
    pov "{i}*Pants*{/i}"
    pov "Shit, that was so good-"
    lai "You have just as much of a potty mouth as Jacob does."
    pov "Oh- sorry."
    lai "I'm just kidding."
    lai "I don't fucking care."
    lai "Look at us."
    pov "This was fun, Lailah."
    lai "It was~ I haven't been fucked like this in so long."
    lai "I should be thanking you, handsome."
    lai "Don't pull out yet, it's gonna stain the bed."
    lai "We'll- have to sorta, carefully maneuver our way over to the bathroom without pulling out."
    pov "I can carry you."
    lai "Oh- that would be perfect~ So strong"
    scene black
    with fade
    $ renpy.pause()
    "After cleaning up..."
    scene bg mylivingroom_day
    with fade

    jump lbl_mylivingroom_day_setup

####################
## Doggy Cum In XRAY
label lbl_lailah_lying_doggy_cumin_0:
    scene bg lailahlyingdoggy_14
    $ renpy.pause(1.5,hard=True)
    show bg lailahlyingdoggy_17_1
    $ renpy.pause(0.3,hard=True)
    show bg lailahlyingdoggy_17_2
    $ renpy.pause(0.3,hard=True)
    show bg lailahlyingdoggy_17_3
    $ renpy.pause(0.3,hard=True)
    show bg lailahlyingdoggy_17_4
    $ renpy.pause(0.3,hard=True)
    show bg lailahlyingdoggy_17_5
    $ renpy.pause(0.3,hard=True)
    show bg lailahlyingdoggy_17_6
    $ renpy.pause(0.3,hard=True)
    show bg lailahlyingdoggy_17_7
    $ renpy.pause(0.3,hard=True)
    show bg lailahlyingdoggy_17_8
    $ renpy.pause(0.3,hard=True)
    show bg lailahlyingdoggy_17_9
    $ renpy.pause()
    lai "Ahhh~ Yesss~!"
    pov "{i}*Pants*{/i}"
    pov "Shit, that was so good-"
    lai "You have just as much of a potty mouth as Jacob does."
    pov "Oh- sorry."
    lai "I'm just kidding."
    lai "I don't fucking care."
    lai "Look at us."
    pov "This was fun, Lailah."
    lai "It was~ I haven't been fucked like this in so long."
    lai "I should be thanking you, handsome."
    lai "Don't pull out yet, it's gonna stain the bed."
    lai "We'll- have to sorta, carefully maneuver our way over to the bathroom without pulling out."
    pov "I can carry you."
    lai "Oh- that would be perfect~ So strong"
    scene black
    with fade
    $ renpy.pause()
    "After cleaning up..."
    scene bg mylivingroom_day
    with fade

    jump lbl_jacobhouseoutside_day
