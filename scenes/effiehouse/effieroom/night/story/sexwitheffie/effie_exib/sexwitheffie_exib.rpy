## MUTUAL MASTURBATION (EXIB - EXHIBITION) ##
label lbl_effie_exib_1:
    scene bg hsceneeffieexib_1
    with fade
    show bg hsceneeffieexib_1
    eff "No touching okay? You're only allowed to watch me play with myself."
    eff "Got it?"
    pov "Yeah."

label lbl_effie_exib_continue:
    $ effie_exib = 0
    jump lbl_effie_exib_2

####################
## Exib Stage 1
# label lbl_effie_exib_1_1:
#     $ effie_exib += 1
#     show bg hsceneeffieexib_2
#     $ renpy.pause(0.4,hard=True)
#     show bg hsceneeffieexib_3
#     $ renpy.pause(0.4,hard=True)
#     if skill_sta <= 7 and effie_exib == 8:
#         jump lbl_effie_exib_menu
#     elif skill_sta <= 14 and effie_exib == 12:
#         jump lbl_effie_exib_2
#     elif skill_sta <= 20 and effie_exib == 16:
#         jump lbl_effie_exib_2
#     else:
#         jump lbl_effie_exib_1_1

label lbl_effie_exib_1_1:
    $ effie_exib += 1
    scene img_effie_exib_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_exib_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_exib_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_exib_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_effie_exib_menu

image img_effie_exib_stage_1:
    "bg hsceneeffieexib_2"
    pause 0.4
    "bg hsceneeffieexib_3"
    pause 0.4
    repeat

####################
## Exib Stage 2
# label lbl_effie_exib_2:
#     $ effie_exib += 1
#     show bg hsceneeffieexib_2
#     $ renpy.pause(0.2,hard=True)
#     show bg hsceneeffieexib_3
#     $ renpy.pause(0.2,hard=True)
#     if skill_sta <= 14 and effie_exib == 28:
#         jump lbl_effie_exib_menu
#     elif skill_sta <= 20 and effie_exib == 32:
#         jump lbl_effie_exib_3
#     else:
#         jump lbl_effie_exib_2

label lbl_effie_exib_2:
    $ effie_exib += 1
    scene img_effie_exib_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_exib_menu
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_effie_exib_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_effie_exib_2

image img_effie_exib_stage_2:
    "bg hsceneeffieexib_2"
    pause 0.2
    "bg hsceneeffieexib_3"
    pause 0.2
    repeat

####################
## Exib Stage 3
# label lbl_effie_exib_3:
#     $ effie_exib += 1
#     show bg hsceneeffieexib_4
#     $ renpy.pause(0.1,hard=True)
#     show bg hsceneeffieexib_5
#     $ renpy.pause(0.1,hard=True)
#     if skill_sta <= 20 and effie_exib == 48:
#         jump lbl_effie_exib_menu
#     else:
#         jump lbl_effie_exib_3

label lbl_effie_exib_3:
    $ effie_exib += 1
    scene img_effie_exib_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_effie_exib_menu

image img_effie_exib_stage_3:
    "bg hsceneeffieexib_4"
    pause 0.1
    "bg hsceneeffieexib_5"
    pause 0.1
    repeat

####################
## Exib Menu
label lbl_effie_exib_menu:
    if effie_points >= 3:
        jump lbl_effie_exib_menu_1
    else:
        jump lbl_effie_exib_menu_0

label lbl_effie_exib_menu_0:

    # scene bg hsceneeffieexib_5
    call screen scr_effie_exib_5_0
    screen scr_effie_exib_5_0():
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_exib_continue")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_exib_cum")

label lbl_effie_exib_menu_1:

    # scene bg hsceneeffieexib_5
    call screen scr_effie_exib_5_1
    screen scr_effie_exib_5_1():
        imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_exib_next")
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_exib_continue")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effie_exib_cum")

####################
## Exib Cum
label lbl_effie_exib_cum:
    scene bg hsceneeffieexib_6
    show bg hsceneeffieexib_6
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_7
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_8
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_9
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_10
    $ renpy.pause (0.2,hard=True)
    show bg hsceneeffieexib_11
    $ renpy.pause ()
    eff "Fuck that's a lot of cum."
    show bg hsceneeffieexib_12
    effdad "Effie? Are you home?"
    show bg hsceneeffieexib_11
    eff "Oh, shit.. hold on."
    show bg hsceneeffieexib_12
    eff "Don't come in! I'm changing!"
    show bg hsceneeffieexib_13
    effdad "Alright. I'm just checking up on you. How's work and university?"
    show bg hsceneeffieexib_12
    eff "It's good. Nothing new!"
    show bg hsceneeffieexib_13
    effdad "Alright. Well, I've got company with me tonight so, goodnight!"
    show bg hsceneeffieexib_12
    eff "G'night, Dad!"
    if main_story == 12:
        $ main_story = 13
    elif main_story >= 14:
        $ effie_funlater = 0
        $ effie_path = 2

    jump lbl_effieroom_night_setup

####################
## Exib Next
label lbl_effie_exib_next:
    scene bg hsceneeffieexib_6
    eff "Fuck it, I want you so bad, [povname]."
    eff "Hurry up and shove that fat cock inside me."

    menu:
        "Shove it in":
            jump lbl_effie_mish_1
        "I don't think that's a good idea.":
            jump lbl_effie_exib_rejection

label lbl_effie_exib_rejection:
    scene bg hsceneeffieexib_14
    eff "What the fuck? Are you fucking kidding me? Are you gay or something? Jesus. Fine. Get off me."
    if main_story == 12:
        $ main_story = 13
    elif main_story >= 14:
        $ effie_funlater = 0

    jump lbl_effieroom_night_setup
