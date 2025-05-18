## Hitomi Beach Accident
label lbl_hitomi_beach_accident_revisit_0:
    $ hitomi_beach_accident_revisit_counter = 0
    if hscene_xray == 0:
        jump lbl_hitomi_beach_accident_revisit_1
    else:
        jump lbl_hitomi_beach_accident_revisit_1_0

####################
## Stage 1
label lbl_hitomi_beach_accident_revisit_1:
    $ hitomi_beach_accident_revisit_counter += 1
    scene img_hitomi_beach_accident_revisit_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_beach_accident_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_revisit_1

image img_hitomi_beach_accident_revisit_stage_1:
    "bg hitomibeachaccident_1"
    pause 0.2
    "bg hitomibeachaccident_2"
    pause 0.2
    "bg hitomibeachaccident_3"
    pause 0.2
    "bg hitomibeachaccident_4"
    pause 0.2
    "bg hitomibeachaccident_2"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_hitomi_beach_accident_revisit_1_0:
    $ hitomi_beach_accident_revisit_counter += 1
    scene img_hitomi_beach_accident_revisit_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_beach_accident_revisit_2_0
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_revisit_2_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_revisit_cum

image img_hitomi_beach_accident_revisit_stage_1_0:
    "bg hitomibeachaccident_1_0"
    pause 0.2
    "bg hitomibeachaccident_2_0"
    pause 0.2
    "bg hitomibeachaccident_3_0"
    pause 0.2
    "bg hitomibeachaccident_4_0"
    pause 0.2
    "bg hitomibeachaccident_2_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_hitomi_beach_accident_revisit_2:
    $ hitomi_beach_accident_revisit_counter += 1
    scene img_hitomi_beach_accident_revisit_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_beach_accident_revisit_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_revisit_3
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_revisit_2

image img_hitomi_beach_accident_revisit_stage_2:
    "bg hitomibeachaccident_5"
    pause 0.2
    "bg hitomibeachaccident_6"
    pause 0.1
    "bg hitomibeachaccident_7"
    pause 0.2
    "bg hitomibeachaccident_6"
    pause 0.2
    repeat
####################
## Stage 2 XRAY
label lbl_hitomi_beach_accident_revisit_2_0:
    $ hitomi_beach_accident_revisit_counter += 1
    scene img_hitomi_beach_accident_revisit_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_hitomi_beach_accident_revisit_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_revisit_3_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_revisit_2_0

image img_hitomi_beach_accident_revisit_stage_2_0:
    "bg hitomibeachaccident_5_0"
    pause 0.2
    "bg hitomibeachaccident_6_0"
    pause 0.1
    "bg hitomibeachaccident_7_0"
    pause 0.2
    "bg hitomibeachaccident_6_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_hitomi_beach_accident_revisit_3:
    $ hitomi_beach_accident_revisit_counter += 1
    scene img_hitomi_beach_accident_revisit_stage_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_revisit_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_revisit_3
image img_hitomi_beach_accident_revisit_stage_3:
    "bg hitomibeachaccident_8"
    pause 0.2
    "bg hitomibeachaccident_9"
    pause 0.1
    "bg hitomibeachaccident_10"
    pause 0.2

    repeat
####################
## Stage 3 XRAY
label lbl_hitomi_beach_accident_revisit_3_0:
    $ hitomi_beach_accident_revisit_counter += 1
    scene img_hitomi_beach_accident_revisit_stage_3_0

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_hitomi_beach_accident_revisit_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_hitomi_beach_accident_revisit_3_0

image img_hitomi_beach_accident_revisit_stage_3_0:
    "bg hitomibeachaccident_8_0"
    pause 0.2
    "bg hitomibeachaccident_9_0"
    pause 0.1
    "bg hitomibeachaccident_10_0"
    pause 0.2
    repeat

####################
## Cum
label lbl_hitomi_beach_accident_revisit_cum:
    if hitomi_points <= 8:
        jump lbl_hitomi_beach_accident_revisit_cum_2
    else:
        jump lbl_hitomi_beach_accident_revisit_cum_2
        #jump lbl_hitomi_beach_accident_revisit_cum_3

label lbl_hitomi_beach_accident_revisit_cum_2:
    call screen scr_hitomi_beach_accident_revisit_cum_2

screen scr_hitomi_beach_accident_revisit_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_revisit_cumchoice")

label lbl_hitomi_beach_accident_revisit_cum_3:
    if hscene_xray == 0:
        scene bg hitomibeachaccident_1
    else:
        scene bg hitomibeachaccident_1_0
    call screen scr_hitomi_beach_accident_revisit_cum_3

screen scr_hitomi_beach_accident_revisit_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_revisit_scenechoice_mish")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_revisit_mish_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_hitomi_beach_accident_revisit_cumchoice")

label lbl_hitomi_beach_accident_revisit_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_hitomi_beach_accident_revisit_cumin
            else:
                jump lbl_hitomi_beach_accident_revisit_cumin_0
        "Cum on her":
            jump lbl_hitomi_beach_accident_revisit_cumout

####################
## Cum In
label lbl_hitomi_beach_accident_revisit_cumin:
    scene bg hitomibeachaccident_1
    $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_2
    $ renpy.pause(1.5,hard=True)
    show bg hitomibeachaccident_11_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_11_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_11_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_11_4
    $ renpy.pause(0.8,hard=True)
    hit "Ahh- you actually came inside me!"
    pov "Sorry, didn't think you'd mind."
    hit "I need to go get a Plan B pill."
    hit "I wasn't expecting to get creampied today."
    hit "Usually guys put on a condom."
    pov "The lifeguard made it loud and clear that we must all be completely naked."
    hit "She also preaches no littering and yet you've made a mess inside of me."
    hit "{i}*Sigh*{/i} You better come by and buy some comics sometime."
    pov "Happy to see you more often."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Cum In XRAY
label lbl_hitomi_beach_accident_revisit_cumin_0:
    scene bg hitomibeachaccident_1_0
    $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_2_0
    $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_3_0
    $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_12_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_4
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_5
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_6
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_7
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_8
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_9
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_12_10
    $ renpy.pause(0.8,hard=True)
    hit "Ahh- you actually came inside me!"
    pov "Sorry, didn't think you'd mind."
    hit "I need to go get a Plan B pill."
    hit "I wasn't expecting to get creampied today."
    hit "Usually guys put on a condom."
    pov "The lifeguard made it loud and clear that we must all be completely naked."
    hit "She also preaches no littering and yet you've made a mess inside of me."
    hit "{i}*Sigh*{/i} You better come by and buy some comics sometime."
    pov "Happy to see you more often."
    
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

####################
## Missionary Cum Out
label lbl_hitomi_beach_accident_revisit_cumout:
    if hscene_xray == 0:
        scene bg hitomibeachaccident_1
        $ renpy.pause(0.2,hard=True)
    else:
        scene bg hitomibeachaccident_1_0
        $ renpy.pause(0.2,hard=True)
    show bg hitomibeachaccident_13_0
    $ renpy.pause(1.5,hard=True)
    show bg hitomibeachaccident_13_1
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_2
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_3
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_4
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_5
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_6
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_7
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_8
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_9
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_10
    $ renpy.pause(0.3,hard=True)
    show bg hitomibeachaccident_13_11
    $ renpy.pause(0.8,hard=True)
    hit "Ahh- you actually came all over me!"
    pov "Sorry, didn't think you'd mind."
    hit "This is a public beach!"
    hit "We're not supposed to be littering and making a mess."
    hit "I can't move, you're gonna have to go grab a towel or something."
    pov "Oh- uhm, I didn't bring a towel."
    hit "You came to the beach and you didn't bring a towel?"
    pov "I didn't expect to find myself in this situation-"
    hit "{i}*Sigh*{/i} Go grab mine from over there... ugh...."
    pov "Sure thing! Don't move, you stay right there."
    hit "Shut up."
    
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
