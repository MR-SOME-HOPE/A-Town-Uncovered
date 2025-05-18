## ORAL ##
label lbl_drunk_and_frisky_oral:
    scene bg drunkandfrisky_oral_1
    with fade

    jump lbl_drunk_and_frisky_oral_continue

label lbl_drunk_and_frisky_oral_continue:
## Set Oral Counter
    $ drunkandfrisky_oral = 0
    jump lbl_drunk_and_frisky_oral_1

####################
## Oral Stage 1
label lbl_drunk_and_frisky_oral_1:
    $ drunkandfrisky_oral += 1
    scene img_drunk_and_frisky_oral_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_oral_next
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_oral_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_oral_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_oral_2

image img_drunk_and_frisky_oral_stage_1:
    "bg drunkandfrisky_oral_1"
    pause 0.3
    "bg drunkandfrisky_oral_2"
    pause 0.3
    "bg drunkandfrisky_oral_3"
    pause 0.3
    "bg drunkandfrisky_oral_4"
    pause 0.3
    "bg drunkandfrisky_oral_2"
    pause 0.4
    repeat

####################
## Oral Stage 2
label lbl_drunk_and_frisky_oral_2:
    $ drunkandfrisky_oral += 1
    scene img_drunk_and_frisky_oral_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_oral_next
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_oral_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_oral_3

image img_drunk_and_frisky_oral_stage_2:
    "bg drunkandfrisky_oral_1"
    pause 0.2
    "bg drunkandfrisky_oral_2"
    pause 0.2
    "bg drunkandfrisky_oral_3"
    pause 0.2
    "bg drunkandfrisky_oral_4"
    pause 0.2
    "bg drunkandfrisky_oral_2"
    pause 0.3
    repeat

####################
## Oral Stage 3
label lbl_drunk_and_frisky_oral_3:
    $ drunkandfrisky_oral += 1
    scene img_drunk_and_frisky_oral_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_drunk_and_frisky_oral_next

image img_drunk_and_frisky_oral_stage_3:
    "bg drunkandfrisky_oral_1"
    pause 0.1
    "bg drunkandfrisky_oral_2"
    pause 0.1
    "bg drunkandfrisky_oral_3"
    pause 0.1
    "bg drunkandfrisky_oral_4"
    pause 0.2
    "bg drunkandfrisky_oral_2"
    pause 0.2
    repeat

####################
## Oral Menu
label lbl_drunk_and_frisky_oral_next:
    call screen scr_drunk_and_frisky_oral_next

screen scr_drunk_and_frisky_oral_next():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_mc_choose")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_oral_continue")
