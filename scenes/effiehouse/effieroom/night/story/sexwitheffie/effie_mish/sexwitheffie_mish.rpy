## MISSIONARY (MISH) ##
label lbl_effie_mish_1:
    if hscene_xray == 0:
        scene bg hscene_effie_mish_1
        with fade
        $ renpy.pause()
        show bg hscene_effie_mish_2
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3
        eff "Fuck that's deep."
        show bg hscene_effie_mish_4
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1
        $ renpy.pause ()
        show bg hscene_effie_mish_2
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3
        eff "Right there..."
        show bg hscene_effie_mish_4
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1
        $ renpy.pause ()
        show bg hscene_effie_mish_2
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3
        eff "Don't stop.."
    else:
        scene bg hscene_effie_mish_1_0
        with fade
        $ renpy.pause()
        show bg hscene_effie_mish_2_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3_0
        eff "Fuck that's deep."
        show bg hscene_effie_mish_4_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1_0
        $ renpy.pause ()
        show bg hscene_effie_mish_2_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3_0
        eff "Right there..."
        show bg hscene_effie_mish_4_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1_0
        $ renpy.pause ()
        show bg hscene_effie_mish_2_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_3_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_4_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_5_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_6_0
        $ renpy.pause(0.2, hard=True)
        show bg hscene_effie_mish_1_0
        eff "Don't stop.."

    jump lbl_effie_mish_continue

label lbl_effie_mish_continue:

## Set Mish Counter
    $ effie_mish = 0
    if hscene_xray == 0:
        jump lbl_effie_mish_2
    else:
        jump lbl_effie_mish_2_0

####################
## Mish Stage 1
# label lbl_effie_mish_2:
#     $ effie_mish += 1
#     show bg hscene_effie_mish_1
#     $ renpy.pause(0.3,hard=True)
#     show bg hscene_effie_mish_2
#     $ renpy.pause(0.1,hard=True)
#     show bg hscene_effie_mish_3
#     $ renpy.pause(0.3,hard=True)
#     show bg hscene_effie_mish_4
#     $ renpy.pause(0.3,hard=True)
#     show bg hscene_effie_mish_5
#     $ renpy.pause(0.3,hard=True)
#     show bg hscene_effie_mish_6
#     $ renpy.pause(0.1,hard=True)
#     if skill_sta <= 7 and effie_mish == 4:
#         jump lbl_effie_mish_cum
#     elif skill_sta <= 14 and effie_mish == 6:
#         jump lbl_effie_mish_3
#     elif skill_sta <= 20 and effie_mish == 8:
#         jump lbl_effie_mish_3
#     else:
#         jump lbl_effie_mish_2

label lbl_effie_mish_2:
    $ effie_mish += 1
    scene img_effie_mish_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_mish_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_mish_3
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_mish_3
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_mish_2

image img_effie_mish_stage_1:
    "bg hscene_effie_mish_1"
    pause 0.3
    "bg hscene_effie_mish_2"
    pause 0.1
    "bg hscene_effie_mish_3"
    pause 0.3
    "bg hscene_effie_mish_4"
    pause 0.3
    "bg hscene_effie_mish_5"
    pause 0.3
    "bg hscene_effie_mish_6"
    pause 0.1
    repeat

####################
## Mish Stage 1 XRAY
# label lbl_effie_mish_2_0:
#     $ effie_mish += 1
#     show bg hscene_effie_mish_1_0
#     $ renpy.pause(0.3,hard=True)
#     show bg hscene_effie_mish_2_0
#     $ renpy.pause(0.1,hard=True)
#     show bg hscene_effie_mish_3_0
#     $ renpy.pause(0.3,hard=True)
#     show bg hscene_effie_mish_4_0
#     $ renpy.pause(0.3,hard=True)
#     show bg hscene_effie_mish_5_0
#     $ renpy.pause(0.3,hard=True)
#     show bg hscene_effie_mish_6_0
#     $ renpy.pause(0.1,hard=True)
#     if skill_sta <= 7 and effie_mish == 4:
#         jump lbl_effie_mish_cum
#     elif skill_sta <= 14 and effie_mish == 6:
#         jump lbl_effie_mish_3_0
#     elif skill_sta <= 20 and effie_mish == 8:
#         jump lbl_effie_mish_3_0
#     else:
#         jump lbl_effie_mish_2_0

label lbl_effie_mish_2_0:
    $ effie_mish += 1
    scene img_effie_mish_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_mish_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_mish_3_0
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_mish_3_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_mish_2_0

image img_effie_mish_stage_1_0:
    "bg hscene_effie_mish_1_0"
    pause 0.3
    "bg hscene_effie_mish_2_0"
    pause 0.1
    "bg hscene_effie_mish_3_0"
    pause 0.3
    "bg hscene_effie_mish_4_0"
    pause 0.3
    "bg hscene_effie_mish_5_0"
    pause 0.3
    "bg hscene_effie_mish_6_0"
    pause 0.1
    repeat

####################
## Mish Stage 2
# label lbl_effie_mish_3:
#     $ effie_mish += 1
#     show bg hscene_effie_mish_7
#     $ renpy.pause(0.2,hard=True)
#     show bg hscene_effie_mish_8
#     $ renpy.pause(0.1,hard=True)
#     show bg hscene_effie_mish_9
#     $ renpy.pause(0.2,hard=True)
#     show bg hscene_effie_mish_10
#     $ renpy.pause(0.2,hard=True)
#     if skill_sta <= 14 and effie_mish == 14:
#         jump lbl_effie_mish_cum
#     elif skill_sta <= 20 and effie_mish == 16:
#         jump lbl_effie_mish_4
#     else:
#         jump lbl_effie_mish_3

label lbl_effie_mish_3:
    $ effie_mish += 1
    scene img_effie_mish_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_mish_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_mish_4
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_mish_3

image img_effie_mish_stage_2:
    "bg hscene_effie_mish_7"
    pause 0.2
    "bg hscene_effie_mish_8"
    pause 0.1
    "bg hscene_effie_mish_9"
    pause 0.2
    "bg hscene_effie_mish_10"
    pause 0.2
    repeat

####################
## Mish Stage 2 XRAY
# label lbl_effie_mish_3_0:
#     $ effie_mish += 1
#     show bg hscene_effie_mish_7_0
#     $ renpy.pause(0.2,hard=True)
#     show bg hscene_effie_mish_8_0
#     $ renpy.pause(0.1,hard=True)
#     show bg hscene_effie_mish_9_0
#     $ renpy.pause(0.2,hard=True)
#     show bg hscene_effie_mish_10_0
#     $ renpy.pause(0.2,hard=True)
#     if skill_sta <= 14 and effie_mish == 14:
#         jump lbl_effie_mish_cum
#     elif skill_sta <= 20 and effie_mish == 16:
#         jump lbl_effie_mish_4_0
#     else:
#         jump lbl_effie_mish_3_0

label lbl_effie_mish_3_0:
    $ effie_mish += 1
    scene img_effie_mish_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_mish_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_mish_4_0
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_mish_3_0

image img_effie_mish_stage_2_0:
    "bg hscene_effie_mish_7_0"
    pause 0.2
    "bg hscene_effie_mish_8_0"
    pause 0.1
    "bg hscene_effie_mish_9_0"
    pause 0.2
    "bg hscene_effie_mish_10_0"
    pause 0.2
    repeat

image img_effie_mish_stage_2:
    "bg hscene_effie_mish_7"
    pause 0.2
    "bg hscene_effie_mish_8"
    pause 0.1
    "bg hscene_effie_mish_9"
    pause 0.2
    "bg hscene_effie_mish_10"
    pause 0.2
    repeat

####################
## Mish Stage 3
# label lbl_effie_mish_4:
#     $ effie_mish += 1
#     show bg hscene_effie_mish_11
#     $ renpy.pause(0.1,hard=True)
#     show bg hscene_effie_mish_12
#     $ renpy.pause(0.1,hard=True)
#     show bg hscene_effie_mish_13
#     $ renpy.pause(0.1,hard=True)
#     if skill_sta <= 20 and effie_mish == 24:
#         jump lbl_effie_mish_cum
#     else:
#         jump lbl_effie_mish_4

label lbl_effie_mish_4:
    $ effie_mish += 1
    scene img_effie_mish_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_effie_mish_cum

image img_effie_mish_stage_3:
    "bg hscene_effie_mish_11"
    pause 0.1
    "bg hscene_effie_mish_12"
    pause 0.1
    "bg hscene_effie_mish_13"
    pause 0.1
    repeat

####################
## Mish Stage 3 XRAY
# label lbl_effie_mish_4_0:
#     $ effie_mish += 1
#     show bg hscene_effie_mish_11_0
#     $ renpy.pause(0.1,hard=True)
#     show bg hscene_effie_mish_12_0
#     $ renpy.pause(0.1,hard=True)
#     show bg hscene_effie_mish_13_0
#     $ renpy.pause(0.1,hard=True)
#     if skill_sta <= 20 and effie_mish == 24:
#         jump lbl_effie_mish_cum
#     else:
#         jump lbl_effie_mish_4_0

label lbl_effie_mish_4_0:
    $ effie_mish += 1
    scene img_effie_mish_stage_3_0
    $ renpy.pause(20,hard=True)
    jump lbl_effie_mish_cum

image img_effie_mish_stage_3_0:
    "bg hscene_effie_mish_11_0"
    pause 0.1
    "bg hscene_effie_mish_12_0"
    pause 0.1
    "bg hscene_effie_mish_13_0"
    pause 0.1
    repeat

####################
## Missionary Cum
label lbl_effie_mish_cum:
    screen scr_effie_mish_5_1():
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_mish_continue")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_mish_cumchoice")

label lbl_effie_mish_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_effie_mish_cumin
            else:
                jump lbl_effie_mish_cumin_0
        "Cum on her":
            jump lbl_effie_mish_cumout

label lbl_effie_mish_cumin:
    scene bg hscene_effie_mish_cumin_1
    $ renpy.pause (1.8,hard=True)
    show bg hscene_effie_mish_cumin_6
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_7
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_8
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_9
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_10
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_11
    $ renpy.pause ()
    show bg hscene_effie_mish_cumin_12
    effdad "Effie? Are you home?"
    show bg hscene_effie_mish_cumin_14
    eff "Oh, shit.. hold on."
    show bg hscene_effie_mish_cumin_12
    eff "Don't come in! I'm changing!"
    show bg hscene_effie_mish_cumin_13
    effdad "Alright. I'm just checking up on you. How's work and university?"
    show bg hscene_effie_mish_cumin_12
    eff "It's good. Nothing new!"
    show bg hscene_effie_mish_cumin_13
    effdad "Alright. Well, I've got company with me tonight so, goodnight!"
    show bg hscene_effie_mish_cumin_12
    eff "G'night, Dad!"

    jump lbl_effie_mish_end

label lbl_effie_mish_cumin_0:
    scene bg hscene_effie_mish_cumin_1_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_2_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_3_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_4_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_5_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_6_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_7_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_8_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_9_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_10_0
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumin_11_0
    $ renpy.pause ()
    show bg hscene_effie_mish_cumin_12_0
    effdad "Effie? Are you home?"
    show bg hscene_effie_mish_cumin_14_0
    eff "Oh, shit.. hold on."
    show bg hscene_effie_mish_cumin_12_0
    eff "Don't come in! I'm changing!"
    show bg hscene_effie_mish_cumin_13_0
    effdad "Alright. I'm just checking up on you. How's work and university?"
    show bg hscene_effie_mish_cumin_12_0
    eff "It's good. Nothing new!"
    show bg hscene_effie_mish_cumin_13_0
    effdad "Alright. Well, I've got company with me tonight so, goodnight!"
    show bg hscene_effie_mish_cumin_12_0
    eff "G'night, Dad!"

    jump lbl_effie_mish_end

label lbl_effie_mish_cumout:
    scene bg hscene_effie_mish_cumout_1
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_2
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_3
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_4
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_5
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_6
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_7
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_8
    $ renpy.pause (0.3,hard=True)
    show bg hscene_effie_mish_cumout_9
    $ renpy.pause ()
    show bg hscene_effie_mish_cumout_10
    effdad "Effie? Are you home?"
    show bg hscene_effie_mish_cumout_12
    eff "Oh, shit.. hold on."
    show bg hscene_effie_mish_cumout_10
    eff "Don't come in! I'm changing!"
    show bg hscene_effie_mish_cumout_11
    effdad "Alright. I'm just checking up on you. How's work and university?"
    show bg hscene_effie_mish_cumout_10
    eff "It's good. Nothing new!"
    show bg hscene_effie_mish_cumout_11
    effdad "Alright. Well, I've got company with me tonight so, goodnight!"
    show bg hscene_effie_mish_cumout_10
    eff "G'night, Dad!"

    jump lbl_effie_mish_end

label lbl_effie_mish_end:
    if main_story == 12:
        $ main_story = 13
    elif main_story >= 14:
        $ effie_funlater = 0
        $ effie_path = 2

    jump lbl_effieroom_night_setup
