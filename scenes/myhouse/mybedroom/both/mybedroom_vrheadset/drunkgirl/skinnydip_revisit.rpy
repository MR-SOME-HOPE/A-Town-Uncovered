## RANDOM EVENT - Skinny Dipping with Drunk Girl ##
label lbl_randomevent_beach_skinnydipping_revisit_1:
    scene bg skinnydipping_1 with fade
    drug "Hey! You!"
    drug "Yes you!"
    drug "Coooooommmmeee-"
    drug "Fuck MEHH!!"
    scene bg skinnydipping_2

    menu:
        "Fuck her":
            jump lbl_randomevent_beach_skinnydipping_revisit_2
        "Ignore her":
            jump lbl_beachmain_night_setup

label lbl_randomevent_beach_skinnydipping_revisit_2:

    scene bg skinnydipping_3
    $ renpy.pause ()
    show bg skinnydipping_4
    $ renpy.pause ()
    if 11 <= skill_luc <= 16:
        jump lbl_randomevent_beach_skinnydipping_revisit_2_pass
    else:
        jump lbl_randomevent_beach_skinnydipping_revisit_2_fail

label lbl_randomevent_beach_skinnydipping_revisit_2_fail:
    $ beachchangeroom_fishbite = 1
    $ skinnydipping_fishbite = 1
    if skill_luc <= 10:
        $ renpy.notify("You don't have enough luck with that girl.")
    elif skill_luc >= 16:
        $ renpy.notify("You have too much luck with that fish.")

    scene bg skinnydipping_5
    $ renpy.pause ()
    show bg skinnydipping_6
    $ renpy.pause(1,hard=True)
    show bg skinnydipping_7
    $ renpy.pause(1,hard=True)
    if cheat_on == 2 and skill_luc == 19 and violette_path == 0:
        show bg skinnydipping_8_2
        $ renpy.pause(1,hard=True)
    else:
        show bg skinnydipping_8
        $ renpy.pause(1,hard=True)
    show bg skinnydipping_9
    pov "Aaaahhhhhouchhh!"

    jump lbl_beachmain_night_setup

label lbl_randomevent_beach_skinnydipping_revisit_2_pass:

    scene bg skinnydipping_5
    $ renpy.pause ()
    show bg skinnydipping_10
    drug "Come. And. Stick. It. Innn. Hehehe."
    #$ skinnydipping_thrust = 0
    if hscene_xray == 0:
        jump lbl_randomevent_beach_skinnydipping_revisit_3
    else:
        jump lbl_randomevent_beach_skinnydipping_revisit_3_xray

label lbl_randomevent_beach_skinnydipping_revisit_3:
    scene img_beach_skinnydipping_revisit_3
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_beach_skinnydipping_revisit_cumchoice
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_randomevent_beach_skinnydipping_revisit_3_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_randomevent_beach_skinnydipping_revisit_3_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_randomevent_beach_skinnydipping_revisit_3

image img_beach_skinnydipping_revisit_3:
    "bg skinnydipping_11"
    pause 0.5
    "bg skinnydipping_12"
    pause 0.5
    "bg skinnydipping_13"
    pause 0.5
    "bg skinnydipping_14"
    pause 0.5
    repeat

label lbl_randomevent_beach_skinnydipping_revisit_3_2:
    scene img_beach_skinnydipping_revisit_3_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_beach_skinnydipping_revisit_cumchoice

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_beach_skinnydipping_revisit_cumchoice

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_randomevent_beach_skinnydipping_revisit_3_2

image img_beach_skinnydipping_revisit_3_2:
    "bg skinnydipping_11"
    pause 0.2
    "bg skinnydipping_12"
    pause 0.2
    "bg skinnydipping_13"
    pause 0.2
    "bg skinnydipping_14"
    pause 0.2
    repeat

label lbl_randomevent_beach_skinnydipping_revisit_3_xray:
    scene img_beach_skinnydipping_revisit_3_xray
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_beach_skinnydipping_revisit_cumchoice_xray
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_randomevent_beach_skinnydipping_revisit_3_2_xray

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_randomevent_beach_skinnydipping_revisit_3_2_xray

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_randomevent_beach_skinnydipping_revisit_3_xray

image img_beach_skinnydipping_revisit_3_xray:
    "bg skinnydipping_11_1"
    pause 0.5
    "bg skinnydipping_12_1"
    pause 0.5
    "bg skinnydipping_13_1"
    pause 0.5
    "bg skinnydipping_14_1"
    pause 0.5
    repeat

label lbl_randomevent_beach_skinnydipping_revisit_3_2_xray:
    scene img_beach_skinnydipping_revisit_3_2_xray
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_beach_skinnydipping_revisit_cumchoice_xray

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_beach_skinnydipping_revisit_cumchoice_xray

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_randomevent_beach_skinnydipping_revisit_3_2_xray

image img_beach_skinnydipping_revisit_3_2_xray:
    "bg skinnydipping_11_1"
    pause 0.2
    "bg skinnydipping_12_1"
    pause 0.2
    "bg skinnydipping_13_1"
    pause 0.2
    "bg skinnydipping_14_1"
    pause 0.2
    repeat


label lbl_beach_skinnydipping_revisit_cumchoice_xray:
    menu:
        "Cum Inside":
            jump lbl_randomevent_beach_skinnydipping_revisit_5_xray
        "Cum Outside":
            jump lbl_randomevent_beach_skinnydipping_revisit_4

label lbl_beach_skinnydipping_revisit_cumchoice:
    menu:
        "Cum Inside":
            jump lbl_randomevent_beach_skinnydipping_revisit_5
        "Cum Outside":
            jump lbl_randomevent_beach_skinnydipping_revisit_4

label lbl_randomevent_beach_skinnydipping_revisit_4:

    scene bg skinnydipping_15
    $ renpy.pause (0.2,hard=True)
    show bg skinnydipping_16
    $ renpy.pause (0.2,hard=True)
    show bg skinnydipping_17
    $ renpy.pause (0.3,hard=True)
    show bg skinnydipping_18
    $ renpy.pause (0.4,hard=True)
    show bg skinnydipping_19
    $ renpy.pause (0.5,hard=True)
    show bg skinnydipping_20
    $ renpy.pause (0.6,hard=True)
    show bg skinnydipping_21
    $ renpy.pause (0.7,hard=True)
    show bg skinnydipping_22
    $ renpy.pause ()

    jump lbl_randomevent_beach_skinnydipping_revisit_end

label lbl_randomevent_beach_skinnydipping_revisit_5:

    scene bg skinnydipping_11
    $ renpy.pause (1.2,hard=True)

    scene bg skinnydipping_30
    $ renpy.pause (0.5,hard=True)

    scene bg skinnydipping_31
    $ renpy.pause (0.5,hard=True)

    scene bg skinnydipping_32
    $ renpy.pause ()

    jump lbl_randomevent_beach_skinnydipping_revisit_end

label lbl_randomevent_beach_skinnydipping_revisit_5_xray:

    scene bg skinnydipping_23
    $ renpy.pause (0.3,hard=True)
    scene bg skinnydipping_24
    $ renpy.pause (0.3,hard=True)
    scene bg skinnydipping_25
    $ renpy.pause (0.3,hard=True)
    scene bg skinnydipping_26
    $ renpy.pause (0.3,hard=True)
    scene bg skinnydipping_27
    $ renpy.pause (0.5,hard=True)
    scene bg skinnydipping_28
    $ renpy.pause (0.5,hard=True)
    scene bg skinnydipping_29
    $ renpy.pause ()

    jump lbl_randomevent_beach_skinnydipping_revisit_end

label lbl_randomevent_beach_skinnydipping_revisit_end:
    drug "Oh, fuck... that felt so good..."
    drug "I'm so glad you came by at just the right time."
    drug "Maybe it's destiny.."
    drug "..."
    drug "Will you marry me?"

    menu:
        "Yes.":
            pov "Yes, I will."
            drug "Sweet."
        "No.":
            pov "I don't think so."
            drug "Bummer."

    scene black
    with fade
    $ renpy.pause (1,hard=True)

    jump lbl_vrheadset_character_selection
