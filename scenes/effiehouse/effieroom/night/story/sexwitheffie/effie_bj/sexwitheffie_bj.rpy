## BJ
label lbl_effie_bj_1:
    $ sexwitheffie_bj = 1

    scene bg hsceneeffiebj_1
    with fade
    show bg hsceneeffiebj_1
    $ renpy.pause ()
    show bg hsceneeffiebj_2
    $ renpy.pause ()
    show bg hsceneeffiebj_3
    eff "Can I put this in my mouth? I love feeling it grow hard in my throat."
    show bg hsceneeffiebj_2
    pov "Go ahead."
    show bg hsceneeffiebj_4
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_4_1
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_5
    $ renpy.pause (1.5,hard=True)
    show bg hsceneeffiebj_5_1
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_5_2
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_6_1
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffiebj_6
    $ renpy.pause ()

    jump lbl_effie_bj_continue

label lbl_effie_bj_continue:
    $ effie_bj = 0

####################
## BJ Stage 1
# label lbl_effie_bj_1_1:
#     $ effie_bj += 1
#     show bg hsceneeffiebj_10
#     $ renpy.pause(0.3,hard=True)
#     show bg hsceneeffiebj_10_1
#     $ renpy.pause(0.1,hard=True)
#     show bg hsceneeffiebj_11
#     $ renpy.pause(0.1,hard=True)
#     show bg hsceneeffiebj_11_1
#     $ renpy.pause(0.3,hard=True)
#     show bg hsceneeffiebj_10_1
#     $ renpy.pause(0.3,hard=True)
#     if skill_sta <= 7 and effie_bj == 4:
#         jump lbl_effie_bj_menu
#     elif skill_sta <= 14 and effie_bj == 6:
#         jump lbl_effie_bj_2
#     elif skill_sta <= 20 and effie_bj == 8:
#         jump lbl_effie_bj_2
#     else:
#         jump lbl_effie_bj_1_1

label lbl_effie_bj_1_1:
    $ effie_bj += 1
    scene img_effie_bg_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_bj_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_bj_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_bj_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_bj_menu

image img_effie_bg_stage_1:
    "bg hsceneeffiebj_10"
    pause 0.3
    "bg hsceneeffiebj_10_1"
    pause 0.1
    "bg hsceneeffiebj_11"
    pause 0.1
    "bg hsceneeffiebj_11_1"
    pause 0.3
    "bg hsceneeffiebj_10_1"
    pause 0.3
    repeat

####################
## BJ Stage 2
# label lbl_effie_bj_2:
#     $ effie_bj += 1
#     show bg hsceneeffiebj_10
#     $ renpy.pause(0.3,hard=True)
#     show bg hsceneeffiebj_11
#     $ renpy.pause(0.1,hard=True)
#     show bg hsceneeffiebj_11_1
#     $ renpy.pause(0.2,hard=True)
#     show bg hsceneeffiebj_10_1
#     $ renpy.pause(0.2,hard=True)
#     if skill_sta <= 14 and effie_bj == 14:
#         jump lbl_effie_bj_menu
#     elif skill_sta <= 20 and effie_bj == 16:
#         jump lbl_effie_bj_3
#     else:
#         jump lbl_effie_bj_2

label lbl_effie_bj_2:
    $ effie_bj += 1
    scene img_effie_bg_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_bj_menu
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_bj_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_bj_menu

image img_effie_bg_stage_2:
    "bg hsceneeffiebj_10"
    pause 0.3
    "bg hsceneeffiebj_11"
    pause 0.1
    "bg hsceneeffiebj_11_1"
    pause 0.2
    "bg hsceneeffiebj_10_1"
    pause 0.2
    repeat

####################
## BJ Stage 3
# label lbl_effie_bj_3:
#     $ effie_bj += 1
#     show bg hsceneeffiebj_10
#     $ renpy.pause(0.2,hard=True)
#     show bg hsceneeffiebj_11
#     $ renpy.pause(0.1,hard=True)
#     show bg hsceneeffiebj_10_1
#     $ renpy.pause(0.2,hard=True)
#     if skill_sta <= 20 and effie_bj == 24:
#         jump lbl_effie_bj_menu
#     else:
#         jump lbl_effie_bj_3

label lbl_effie_bj_3:
    $ effie_bj += 1
    scene img_effie_bg_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_effie_bj_menu

image img_effie_bg_stage_3:
    "bg hsceneeffiebj_10"
    pause 0.2
    "bg hsceneeffiebj_11"
    pause 0.1
    "bg hsceneeffiebj_10_1"
    pause 0.2
    repeat

####################
## BJ Menu
label lbl_effie_bj_menu:
    if effie_points >= 6:
        call screen scr_effie_bj_5_1
    else:
        call screen scr_effie_bj_5_0

screen scr_effie_bj_5_0():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_bj_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_bj_cum")

screen scr_effie_bj_5_1():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_bj_next")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_bj_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_bj_cum")

####################
## BJ Cum
label lbl_effie_bj_cum:
    scene bg hsceneeffiebj_11
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_1
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_2
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_3
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_4
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_5
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_6
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_12_7
    $ renpy.pause (0.3,hard=True)
    show bg hsceneeffiebj_13
    $ renpy.pause (1,hard=True)
    show bg hsceneeffiebj_14
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_15
    $ renpy.pause (0.7,hard=True)
    show bg hsceneeffiebj_16
    $ renpy.pause ()
    show bg hsceneeffiebj_20
    eff "I haven't had a dick like that in a long time."
    show bg hsceneeffiebj_22
    effdad "Effie? Are you home?"
    show bg hsceneeffiebj_21
    eff "Oh, shit.. hold on."
    eff "Don't come in! I'm changing!"
    show bg hsceneeffiebj_22
    effdad "Alright. I'm just checking up on you. How's work and university?"
    show bg hsceneeffiebj_21
    eff "It's good. Nothing new!"
    show bg hsceneeffiebj_22
    effdad "Alright. Well, I've got company with me tonight so, goodnight!"
    show bg hsceneeffiebj_21
    eff "G'night, Dad!"
    if main_story == 12:
        $ main_story = 13
    elif main_story >= 14:
        $ effie_funlater = 0
        $ effie_path = 2

    jump lbl_effieroom_night_setup

####################
## BJ Next
label lbl_effie_bj_next:
    scene bg hsceneeffiebj_10
    $ renpy.pause (0.5,hard=True)
    show bg hsceneeffiebj_6
    $ renpy.pause ()
    show bg hsceneeffiebj_23
    eff "Hey dude, you wanna get naked?"

    menu:
        "Fuck yeah!":
            jump lbl_effie_exib_1
        "Nah, it's okay":
            jump lbl_effie_bj_rejection

label lbl_effie_bj_rejection:
    scene bg hsceneeffiebj_24
    eff "Bleh, you selfish bore."
    if main_story == 12:
        $ main_story = 13
    elif main_story >= 14:
        $ effie_funlater = 0

    jump lbl_effieroom_night_setup
