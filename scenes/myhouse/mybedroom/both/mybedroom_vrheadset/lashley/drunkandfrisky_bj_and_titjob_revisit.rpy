#######################################################
## BJ ##
label lbl_drunk_and_frisky_bj_revisit:
    scene bg drunkandfrisky_bj_1
    with fade

    jump lbl_drunk_and_frisky_bj_revisit_continue

label lbl_drunk_and_frisky_bj_revisit_continue:
## Set Finder Counter
    $ drunkandfrisky_bj = 0
    jump lbl_drunk_and_frisky_bj_revisit_1

####################
## BJ Stage 1
label lbl_drunk_and_frisky_bj_revisit_1:
    $ drunkandfrisky_bj += 1
    scene img_drunk_and_frisky_bj_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_bj_revisit_next
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_bj_revisit_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_bj_revisit_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_bj_revisit_2

image img_drunk_and_frisky_bj_revisit_stage_1:
    "bg drunkandfrisky_bj_1"
    pause 0.3
    "bg drunkandfrisky_bj_2"
    pause 0.3
    "bg drunkandfrisky_bj_3"
    pause 0.3
    "bg drunkandfrisky_bj_4"
    pause 0.4
    "bg drunkandfrisky_bj_2"
    pause 0.4
    repeat

####################
## BJ Stage 2
label lbl_drunk_and_frisky_bj_revisit_2:
    $ drunkandfrisky_bj += 1
    scene img_drunk_and_frisky_bj_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_bj_revisit_next
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_bj_revisit_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_bj_revisit_3

image img_drunk_and_frisky_bj_revisit_stage_2:
    "bg drunkandfrisky_bj_5"
    pause 0.2
    "bg drunkandfrisky_bj_6"
    pause 0.2
    "bg drunkandfrisky_bj_7"
    pause 0.2
    "bg drunkandfrisky_bj_8"
    pause 0.3
    "bg drunkandfrisky_bj_6"
    pause 0.3
    repeat

####################
## BJ Stage 3
label lbl_drunk_and_frisky_bj_revisit_3:
    $ drunkandfrisky_bj += 1
    scene img_drunk_and_frisky_bj_revisit_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_drunk_and_frisky_bj_revisit_next

image img_drunk_and_frisky_bj_revisit_stage_3:
    "bg drunkandfrisky_bj_9"
    pause 0.1
    "bg drunkandfrisky_bj_10"
    pause 0.1
    "bg drunkandfrisky_bj_11"
    pause 0.1
    "bg drunkandfrisky_bj_12"
    pause 0.2
    "bg drunkandfrisky_bj_10"
    pause 0.2
    repeat

####################
## BJ Menu
label lbl_drunk_and_frisky_bj_revisit_next:
    if principallashley_points >= 6:
        call screen scr_drunk_and_frisky_bj_revisit_menu_1
    else:
        call screen scr_drunk_and_frisky_bj_revisit_menu_0

screen scr_drunk_and_frisky_bj_revisit_menu_0():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_revisit_cum")

screen scr_drunk_and_frisky_bj_revisit_menu_1():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_revisit")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_revisit_cum")

####################
## BJ Cum
label lbl_drunk_and_frisky_bj_revisit_cum:
    scene bg drunkandfrisky_bj_13_1
    with dissolve
    $ renpy.pause(1.5,hard=True)
    show bg drunkandfrisky_bj_13_2
    $ renpy.pause(1.5,hard=True)
    show bg drunkandfrisky_bj_13_3
    $ renpy.pause(1.5,hard=True)
    show bg drunkandfrisky_bj_13_4
    $ renpy.pause(1.5,hard=True)
    show bg drunkandfrisky_bj_13_5
    $ renpy.pause(1,hard=True)
    show bg drunkandfrisky_bj_13_6
    $ renpy.pause(1,hard=True)
    show bg drunkandfrisky_bj_13_7
    $ renpy.pause(1,hard=True)
    show bg drunkandfrisky_bj_13_10
    pri "{i}*Gulp*{/i}"
    show bg drunkandfrisky_bj_13_9
    pri "T-anks for -ot making a mesh on ny mice carpet, [povname]."
    show bg drunkandfrisky_bj_13_8
    pov "Well, it wasn't like I had much of a say."
    show bg drunkandfrisky_bj_13_11
    pri "I feel full-"
    show bg drunkandfrisky_bj_13_10
    pov "Why don't you sit down, you deserve a break."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

#######################################################
## Titjob ##
label lbl_drunk_and_frisky_titjob_revisit:
    scene bg drunkandfrisky_titjob_1
    with fade

    jump lbl_drunk_and_frisky_titjob_revisit_continue

label lbl_drunk_and_frisky_titjob_revisit_continue:
## Set Finder Counter
    $ drunkandfrisky_titjob = 0
    jump lbl_drunk_and_frisky_titjob_revisit_1

####################
## Titjob Stage 1
label lbl_drunk_and_frisky_titjob_revisit_1:
    $ drunkandfrisky_titjob += 1
    scene img_drunk_and_frisky_titjob_revisit_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_titjob_revisit_next
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_titjob_revisit_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_titjob_revisit_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_titjob_revisit_2

image img_drunk_and_frisky_titjob_revisit_stage_1:
    "bg drunkandfrisky_titjob_1"
    pause 0.3
    "bg drunkandfrisky_titjob_2"
    pause 0.3
    "bg drunkandfrisky_titjob_3"
    pause 0.3
    "bg drunkandfrisky_titjob_4"
    pause 0.4
    "bg drunkandfrisky_titjob_5"
    pause 0.4
    repeat

####################
## Titjob Stage 2
label lbl_drunk_and_frisky_titjob_revisit_2:
    $ drunkandfrisky_titjob += 1
    scene img_drunk_and_frisky_titjob_revisit_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_titjob_revisit_next
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_titjob_revisit_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_titjob_revisit_3

image img_drunk_and_frisky_titjob_revisit_stage_2:
    "bg drunkandfrisky_titjob_6"
    pause 0.2
    "bg drunkandfrisky_titjob_7"
    pause 0.2
    "bg drunkandfrisky_titjob_8"
    pause 0.2
    "bg drunkandfrisky_titjob_9"
    pause 0.3
    "bg drunkandfrisky_titjob_10"
    pause 0.3
    repeat

####################
## Titjob Stage 3
label lbl_drunk_and_frisky_titjob_revisit_3:
    $ drunkandfrisky_titjob += 1
    scene img_drunk_and_frisky_titjob_revisit_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_drunk_and_frisky_titjob_revisit_next

image img_drunk_and_frisky_titjob_revisit_stage_3:
    "bg drunkandfrisky_titjob_11"
    pause 0.1
    "bg drunkandfrisky_titjob_12"
    pause 0.1
    "bg drunkandfrisky_titjob_13"
    pause 0.1
    "bg drunkandfrisky_titjob_14"
    pause 0.2
    "bg drunkandfrisky_titjob_15"
    pause 0.2
    repeat

####################
## Titjob Menu
label lbl_drunk_and_frisky_titjob_revisit_next:
    if principallashley_points >= 6:
        call screen scr_drunk_and_frisky_titjob_revisit_menu_1
    else:
        call screen scr_drunk_and_frisky_titjob_revisit_menu_0

screen scr_drunk_and_frisky_titjob_revisit_menu_0():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_revisit_cum")

screen scr_drunk_and_frisky_titjob_revisit_menu_1():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_revisit")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_revisit_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_revisit_cum")

####################
## Titjob Cum
label lbl_drunk_and_frisky_titjob_revisit_cum:
    scene bg drunkandfrisky_titjob_16_0
    with dissolve
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_0
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_1
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_2
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_3
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_4
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_5
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_6
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_7
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_8
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_9
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_10
    $ renpy.pause(0.3,hard=True)
    show bg drunkandfrisky_titjob_16_11
    $ renpy.pause()
    show bg drunkandfrisky_titjob_16_12
    pri "D-ishu"
    show bg drunkandfrisky_titjob_16_11
    pov "What?"
    show bg drunkandfrisky_titjob_16_12
    pri "Dh-eeshoe"
    show bg drunkandfrisky_titjob_16_11
    pov "Dishoe? Oh tissue!"
    pov "Uhh- hold tight, lemme find something."
    pri "{i}*Grubble*{/i}"

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
