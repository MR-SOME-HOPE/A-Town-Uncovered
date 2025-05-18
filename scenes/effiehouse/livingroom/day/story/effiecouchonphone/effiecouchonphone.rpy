## Effie Couch On Phone
label lbl_effie_couch_on_phone:
    ## PRE STORY
    scene black
    with fade
    "..."
    eff "Dad- you don't need a list, just get stuff that you think we need."
    eff "..."
    eff "I don't know- just stuff that's run out or about to run out."
    eff "..."
    eff "Why didn't you take the list on your way out, it was on counter."
    eff "..."
    if hscene_xray == 0:
        scene bg effiecouchonphone_1
    else:
        scene bg effiecouchonphone_1_0
    with fade
    eff "I swear it was on the counter."
    eff "...Alright, hang on- lemme go get it."
    show bg effiecouchonphone_1
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_3
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_4
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    eff ".."
    show bg effiecouchonphone_1
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_3
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_4
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_1
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_3
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_4
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    eff "..."
    show bg effiecouchonphone_1
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_3
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_4
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_1
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_3
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_4
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_1
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_3
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_4
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    eff "...."
    eff "Nah- I can't find it."
    show bg effiecouchonphone_1
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_3
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_4
    $ renpy.pause(0.2,hard=True)
    show bg effiecouchonphone_2
    $ renpy.pause(0.2,hard=True)
    eff "..."
    eff "{i}*Sigh*{/i} Yes, dad. We need more garlic powder."
    eff "..."
    eff "It's in the spice isle- I don't know where exactly. You just have to use your eyes."
    eff "..."
    eff "Fine, I'll wait."
    eff "{i}*Whisper*{/i}Go on-"

    jump lbl_effie_couch_on_phone_0

label lbl_effie_couch_on_phone_0:
    if hscene_xray == 0:
        scene bg effiecouchonphone_1
        with fade
        jump lbl_effie_couch_on_phone_1
    else:
        scene bg effiecouchonphone_1_0
        with fade
        jump lbl_effie_couch_on_phone_1_0

####################
## Stage 1
label lbl_effie_couch_on_phone_1:
    scene img_effie_couch_on_phone_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_couch_on_phone_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_couch_on_phone_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_couch_on_phone_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_couch_on_phone_1

image img_effie_couch_on_phone_stage_1:
    "bg effiecouchonphone_1"
    pause 0.2
    "bg effiecouchonphone_2"
    pause 0.2
    "bg effiecouchonphone_3"
    pause 0.2
    "bg effiecouchonphone_4"
    pause 0.2
    "bg effiecouchonphone_2"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_effie_couch_on_phone_1_0:
    scene img_effie_couch_on_phone_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_couch_on_phone_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_couch_on_phone_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_couch_on_phone_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_couch_on_phone_1_0

image img_effie_couch_on_phone_stage_1_0:
    "bg effiecouchonphone_1_0"
    pause 0.2
    "bg effiecouchonphone_2_0"
    pause 0.2
    "bg effiecouchonphone_3_0"
    pause 0.2
    "bg effiecouchonphone_4_0"
    pause 0.2
    "bg effiecouchonphone_2_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_effie_couch_on_phone_2:
    scene img_effie_couch_on_phone_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_couch_on_phone_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_couch_on_phone_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_couch_on_phone_2

image img_effie_couch_on_phone_stage_2:
    "bg effiecouchonphone_5"
    pause 0.2
    "bg effiecouchonphone_7"
    pause 0.1
    "bg effiecouchonphone_8"
    pause 0.2
    "bg effiecouchonphone_6"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_effie_couch_on_phone_2_0:
    scene img_effie_couch_on_phone_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_couch_on_phone_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_couch_on_phone_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_couch_on_phone_2_0

image img_effie_couch_on_phone_stage_2_0:
    "bg effiecouchonphone_5_0"
    pause 0.2
    "bg effiecouchonphone_7_0"
    pause 0.1
    "bg effiecouchonphone_8_0"
    pause 0.2
    "bg effiecouchonphone_6_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_effie_couch_on_phone_3:
    scene img_effie_couch_on_phone_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_couch_on_phone_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_couch_on_phone_3

image img_effie_couch_on_phone_stage_3:
    "bg effiecouchonphone_9"
    pause 0.2
    "bg effiecouchonphone_12"
    pause 0.2
    "bg effiecouchonphone_10"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_effie_couch_on_phone_3_0:
    scene img_effie_couch_on_phone_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_couch_on_phone_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_couch_on_phone_3_0

image img_effie_couch_on_phone_stage_3_0:
    "bg effiecouchonphone_9_0"
    pause 0.2
    "bg effiecouchonphone_12_0"
    pause 0.2
    "bg effiecouchonphone_10_0"
    pause 0.2
    repeat

####################
## Cum
label lbl_effie_couch_on_phone_menu:
    call screen scr_effie_couch_on_phone_menu

screen scr_effie_couch_on_phone_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_couch_on_phone_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_couch_on_phone_cumin")

# label lbl_effie_couch_on_phone_cumchoice:
#     menu:
#         "Cum inside":
#             if hscene_xray == 0:
#                 jump lbl_effie_couch_on_phone_cumin
#             else:
#                 jump lbl_effie_couch_on_phone_cumin_0
#         "Cum on her":
#             jump lbl_effie_couch_on_phone_cumout

####################
## Cum In
label lbl_effie_couch_on_phone_cumin:
    pov "Effie- I'm-"
    eff "Shhhhh!"
    eff "Yeah- dad?"
    eff "Oh- you found the garlic powder?"
    scene bg effiecouchonphone_13_1
    $ renpy.pause(1.5,hard=True)
    show bg effiecouchonphone_13_2
    $ renpy.pause(0.3,hard=True)
    show bg effiecouchonphone_13_3
    $ renpy.pause(0.3,hard=True)
    show bg effiecouchonphone_13_4
    $ renpy.pause(0.3,hard=True)
    show bg effiecouchonphone_13_5
    $ renpy.pause(0.3,hard=True)
    show bg effiecouchonphone_13_5
    $ renpy.pause()
    pov "{i}*Moan*{/i}"
    eff "Ah- ah--! Yeah, good job, dad."
    eff "Mhmm- mhmm-"
    eff "Yeah, no- I guess we should get some of that too- yeah."
    pov "{i}*Pants*{/i}"
    eff "Alright- I can cook dinner tonight."
    pov "{i}I guess I'll just clean up. She's still a little preoccupied.{/i}"

    scene black
    with fade
    $ renpy.pause()
    "After quietly cleaning up..."

    $ gtime = 1

    jump lbl_effiehouseoutside_day_setup

####################
## Cum In XRAY
label lbl_effie_couch_on_phone_cumin_0:
    pov "Effie- I'm-"
    eff "Shhhhh!"
    eff "Yeah- dad?"
    eff "Oh- you found the garlic powder?"
    scene bg effiecouchonphone_14_0
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_1
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_2
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_3
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_4
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_5
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_6
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_7
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_8
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_9
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_10
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_11
    $ renpy.pause(0.3,hard=True)
    scene bg effiecouchonphone_14_12
    $ renpy.pause()
    pov "{i}*Moan*{/i}"
    eff "Ah- ah--! Yeah, good job, dad."
    eff "Mhmm- mhmm-"
    eff "Yeah, no- I guess we should get some of that too- yeah."
    pov "{i}*Pants*{/i}"
    eff "Alright- I can cook dinner tonight."
    pov "{i}I guess I'll just clean up. She's still a little preoccupied.{/i}"

    scene black
    with fade
    $ renpy.pause()
    "After quietly cleaning up..."

    $ gtime = 1

    jump lbl_effiehouseoutside_day_setup
