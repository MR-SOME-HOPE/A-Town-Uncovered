## MC CHOOSE ##
label lbl_drunk_and_frisky_mc_choose:
    pri "A-AHHHHH!"
    pri "O-Oh sweet lord in heaven!"

    pov "W-Woah, easy there!"
    pov "Are you okay?"

    pri "B-Bhetter than ever…"
    pri "It was… Better than what I…"
    pri "Imagined it to be..."

    pov "Well, Glad you enjoyed yourself, now I really yould-"

    pri "It’sh your turn now."

    pov "What?"

    pri "you’ve done so much for meh…"
    pri "L-Let me do shomething for you now."

    pov "Lashley, that’s-"

    pri "Shhhh…"
    pri "I want to, [povname]."
    pri "I-I wan’t to see it… To tashte it…"
    pri "But…"

    pov "But?"

    pri "I know young mhen have thing for… fucking breasts, so…"
    pri "Would you like my mouth… Or my breasts?"

label lbl_drunk_and_frisky_mc_choose_menu:
    menu:
        "BJ":
            pov "T-The mouth please…"

            pri "Good answer~"
            pri "I-I’m new to thish so…"
            pri "Let meh know if I’m doing it right, the videos and magazines made it seem simple enough…"

            jump lbl_drunk_and_frisky_bj
        "Titjob":
            pov "T-The tits, please…"

            pri "{i}*Giggle*{/i}"
            pri "S-Seems like those articles were right, huh?"
            pri "Okay…"
            pri "I’m new to this so… L-Let me know if I’m doing it right…"
            pri "The online guides made it seem simple."

            jump lbl_drunk_and_frisky_titjob

#######################################################
## BJ ##
label lbl_drunk_and_frisky_bj:
    scene bg drunkandfrisky_bj_1
    with fade

    jump lbl_drunk_and_frisky_bj_continue

label lbl_drunk_and_frisky_bj_continue:
## Set Finder Counter
    $ drunkandfrisky_bj = 0
    jump lbl_drunk_and_frisky_bj_1

####################
## BJ Stage 1
label lbl_drunk_and_frisky_bj_1:
    $ drunkandfrisky_bj += 1
    scene img_drunk_and_frisky_bj_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_bj_next
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_bj_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_bj_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_bj_2

image img_drunk_and_frisky_bj_stage_1:
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
label lbl_drunk_and_frisky_bj_2:
    $ drunkandfrisky_bj += 1
    scene img_drunk_and_frisky_bj_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_bj_next
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_bj_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_bj_3

image img_drunk_and_frisky_bj_stage_2:
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
label lbl_drunk_and_frisky_bj_3:
    $ drunkandfrisky_bj += 1
    scene img_drunk_and_frisky_bj_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_drunk_and_frisky_bj_next

image img_drunk_and_frisky_bj_stage_3:
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
label lbl_drunk_and_frisky_bj_next:
    if principallashley_points >= 6:
        call screen scr_drunk_and_frisky_bj_menu_1
    else:
        call screen scr_drunk_and_frisky_bj_menu_0

screen scr_drunk_and_frisky_bj_menu_0():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_cum")

screen scr_drunk_and_frisky_bj_menu_1():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj_cum")

####################
## BJ Cum
label lbl_drunk_and_frisky_bj_cum:
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

    jump lbl_drunk_and_frisky_2

#######################################################
## Titjob ##
label lbl_drunk_and_frisky_titjob:
    scene bg drunkandfrisky_titjob_1
    with fade

    jump lbl_drunk_and_frisky_titjob_continue

label lbl_drunk_and_frisky_titjob_continue:
## Set Finder Counter
    $ drunkandfrisky_titjob = 0
    jump lbl_drunk_and_frisky_titjob_1

####################
## Titjob Stage 1
label lbl_drunk_and_frisky_titjob_1:
    $ drunkandfrisky_titjob += 1
    scene img_drunk_and_frisky_titjob_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_titjob_next
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_titjob_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_titjob_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_drunk_and_frisky_titjob_2

image img_drunk_and_frisky_titjob_stage_1:
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
label lbl_drunk_and_frisky_titjob_2:
    $ drunkandfrisky_titjob += 1
    scene img_drunk_and_frisky_titjob_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_titjob_next
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_drunk_and_frisky_titjob_3
    else:
        $ renpy.pause(15,hard=True)
        jump lbl_drunk_and_frisky_titjob_3

image img_drunk_and_frisky_titjob_stage_2:
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
label lbl_drunk_and_frisky_titjob_3:
    $ drunkandfrisky_titjob += 1
    scene img_drunk_and_frisky_titjob_stage_3
    $ renpy.pause(20,hard=True)
    jump lbl_drunk_and_frisky_titjob_next

image img_drunk_and_frisky_titjob_stage_3:
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
label lbl_drunk_and_frisky_titjob_next:
    if principallashley_points >= 6:
        call screen scr_drunk_and_frisky_titjob_menu_1
    else:
        call screen scr_drunk_and_frisky_titjob_menu_0

screen scr_drunk_and_frisky_titjob_menu_0():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_cum")

screen scr_drunk_and_frisky_titjob_menu_1():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_bj")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_continue")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_drunk_and_frisky_titjob_cum")

####################
## Titjob Cum
label lbl_drunk_and_frisky_titjob_cum:
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
    "After cleaning up..."

    jump lbl_drunk_and_frisky_2
