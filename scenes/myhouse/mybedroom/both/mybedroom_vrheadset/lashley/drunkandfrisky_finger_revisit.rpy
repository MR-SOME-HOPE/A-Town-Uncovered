## FINGER ##
label lbl_drunk_and_frisky_finger_revisit:
    scene bg drunkandfrisky_finger_1
    with fade

    jump lbl_drunk_and_frisky_finger_revisit_continue

label lbl_drunk_and_frisky_finger_revisit_continue:
## Set Finder Counter
    $ drunkandfrisky_finger = 0
    jump lbl_drunk_and_frisky_finger_revisit_1

####################
## Finger Stage 1
label lbl_drunk_and_frisky_finger_revisit_1:
    $ drunkandfrisky_finger += 1
    scene img_drunk_and_frisky_finger_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_finger_revisit_next
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_finger_revisit_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_finger_revisit_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_finger_revisit_2

image img_drunk_and_frisky_finger_revisit_stage_1:
    "bg drunkandfrisky_finger_1"
    pause 0.3
    "bg drunkandfrisky_finger_2"
    pause 0.3
    "bg drunkandfrisky_finger_3"
    pause 0.3
    "bg drunkandfrisky_finger_4"
    pause 0.4
    repeat

####################
## Finger Stage 2
label lbl_drunk_and_frisky_finger_revisit_2:
    $ drunkandfrisky_finger += 1
    scene img_drunk_and_frisky_finger_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_finger_revisit_next
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_finger_revisit_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_finger_revisit_3

image img_drunk_and_frisky_finger_revisit_stage_2:
    "bg drunkandfrisky_finger_1"
    pause 0.2
    "bg drunkandfrisky_finger_2"
    pause 0.2
    "bg drunkandfrisky_finger_3"
    pause 0.2
    "bg drunkandfrisky_finger_4"
    pause 0.3
    repeat

####################
## Finger Stage 3
label lbl_drunk_and_frisky_finger_revisit_3:
    $ drunkandfrisky_finger += 1
    scene img_drunk_and_frisky_finger_revisit_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_drunk_and_frisky_finger_revisit_next

image img_drunk_and_frisky_finger_revisit_stage_3:
    "bg drunkandfrisky_finger_1"
    pause 0.1
    "bg drunkandfrisky_finger_2"
    pause 0.1
    "bg drunkandfrisky_finger_3"
    pause 0.1
    "bg drunkandfrisky_finger_4"
    pause 0.1
    repeat

####################
## Finger Menu
label lbl_drunk_and_frisky_finger_revisit_next:
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

#     call screen scr_drunk_and_frisky_finger_revisit_next

# screen scr_drunk_and_frisky_finger_revisit_next():
#     imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj")
#     imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_finger_revisit_continue")
