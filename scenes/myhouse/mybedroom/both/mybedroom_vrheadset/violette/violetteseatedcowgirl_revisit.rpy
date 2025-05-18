## Violette Seated Cowgirl
label lbl_violette_seated_cowgirl_revisit_0:
    $ violette_seated_cowgirl_counter = 0
    if hscene_xray == 0:
        jump lbl_violette_seated_cowgirl_revisit_1
    else:
        jump lbl_violette_seated_cowgirl_revisit_1_0

####################
## Stage 1
label lbl_violette_seated_cowgirl_revisit_1:
    $ violette_seated_cowgirl_counter += 1
    scene img_violette_seated_cowgirl_stage_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_1

image img_violette_seated_cowgirl_stage_1:
    "bg violetteseatedcowgirl_1"
    pause 0.2
    "bg violetteseatedcowgirl_2"
    pause 0.2
    "bg violetteseatedcowgirl_3"
    pause 0.2
    "bg violetteseatedcowgirl_4"
    pause 0.2
    "bg violetteseatedcowgirl_2"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_violette_seated_cowgirl_revisit_1_0:
    $ violette_seated_cowgirl_counter += 1
    scene img_violette_seated_cowgirl_stage_1_0

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_1_0

image img_violette_seated_cowgirl_stage_1_0:
    "bg violetteseatedcowgirl_1_0"
    pause 0.2
    "bg violetteseatedcowgirl_2_0"
    pause 0.2
    "bg violetteseatedcowgirl_3_0"
    pause 0.2
    "bg violetteseatedcowgirl_4_0"
    pause 0.2
    "bg violetteseatedcowgirl_2_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_violette_seated_cowgirl_revisit_2:
    $ violette_seated_cowgirl_counter += 1
    scene img_violette_seated_cowgirl_stage_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_2

image img_violette_seated_cowgirl_stage_2:
    "bg violetteseatedcowgirl_1"
    pause 0.2
    "bg violetteseatedcowgirl_2"
    pause 0.1
    "bg violetteseatedcowgirl_4"
    pause 0.2
    "bg violetteseatedcowgirl_2"
    pause 0.2
    repeat
####################
## Stage 2 XRAY
label lbl_violette_seated_cowgirl_revisit_2_0:
    $ violette_seated_cowgirl_counter += 1
    scene img_violette_seated_cowgirl_stage_2_0

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_2_0

image img_violette_seated_cowgirl_stage_2_0:
    "bg violetteseatedcowgirl_1_0"
    pause 0.2
    "bg violetteseatedcowgirl_2_0"
    pause 0.1
    "bg violetteseatedcowgirl_4_0"
    pause 0.2
    "bg violetteseatedcowgirl_2_0"
    pause 0.2
    repeat
####################
## Stage 3
label lbl_violette_seated_cowgirl_revisit_3:
    $ violette_seated_cowgirl_counter += 1

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_3

image img_violette_seated_cowgirl_stage_3:
    "bg violetteseatedcowgirl_1"
    pause 0.2
    "bg violetteseatedcowgirl_3"
    pause 0.1
    "bg violetteseatedcowgirl_2"
    pause 0.2
    repeat
####################
## Stage 3 XRAY
label lbl_violette_seated_cowgirl_revisit_3_0:
    $ violette_seated_cowgirl_counter += 1

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_revisit_3_0

image img_violette_seated_cowgirl_stage_3_0:
    "bg violetteseatedcowgirl_1_0"
    pause 0.2
    "bg violetteseatedcowgirl_3_0"
    pause 0.1
    "bg violetteseatedcowgirl_2_0"
    pause 0.2
    repeat
####################
## Cum
label lbl_violette_seated_cowgirl_revisit_cum:
    jump lbl_violette_seated_cowgirl_revisit_cum_2

label lbl_violette_seated_cowgirl_revisit_cum_2:

    call screen scr_violette_seated_cowgirl_revisit_cum_2

screen scr_violette_seated_cowgirl_revisit_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violette_seated_cowgirl_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violette_seated_cowgirl_revisit_cumchoice")


label lbl_violette_seated_cowgirl_revisit_cumchoice:
    menu:
        "Cum inside":
            pov "Vi- I'm gonna cum in you."
            vio "Do it, [povname]."
            if hscene_xray == 0:
                jump lbl_violette_seated_cowgirl_revisit_cumin
            else:
                jump lbl_violette_seated_cowgirl_revisit_cumin_0
        "Cum on her":
            pov "Vi- I'm cumming..."
            pov "Quick pull out-"
            vio "No! No littering on my beach!"
            vio "Keep it inside."
            pov "Eughh-"
            if hscene_xray == 0:
                jump lbl_violette_seated_cowgirl_revisit_cumin
            else:
                jump lbl_violette_seated_cowgirl_revisit_cumin_0

####################
## Cum In
label lbl_violette_seated_cowgirl_revisit_cumin:
    scene bg violetteseatedcowgirl_2
    $ renpy.pause(0.2,hard=True)
    show bg violetteseatedcowgirl_3
    $ renpy.pause(0.2,hard=True)
    show bg violetteseatedcowgirl_4
    $ renpy.pause(1.5,hard=True)
    show bg violetteseatedcowgirl_6_1
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_6_2
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_6_3
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_6_4
    $ renpy.pause(0.8,hard=True)

    jump lbl_violette_seated_cowgirl_revisit_end

####################
## Cum In XRAY
label lbl_violette_seated_cowgirl_revisit_cumin_0:
    scene bg violetteseatedcowgirl_2_0
    $ renpy.pause(0.2,hard=True)
    show bg violetteseatedcowgirl_3_0
    $ renpy.pause(0.2,hard=True)
    show bg violetteseatedcowgirl_4_0
    $ renpy.pause(0.2,hard=True)
    show bg violetteseatedcowgirl_5_1
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_2
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_3
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_4
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_5
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_6
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_7
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_8
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_9
    $ renpy.pause(0.3,hard=True)
    show bg violetteseatedcowgirl_5_10
    $ renpy.pause(0.8,hard=True)

    jump lbl_violette_seated_cowgirl_revisit_end

label lbl_violette_seated_cowgirl_revisit_end:
    vio "Ahh~ That feels great."
    pov "{i}*Pants*{/i}"
    pov "I- agree..."
    vio "Hey, you didn't make {i}too{/i} much of a mess at least."
    vio "Got most of it inside me."
    pov "You're alright with that?"
    vio "As long as it's not all over my nice sand."
    pov "You.. have strange priorities."
    vio "Save Earth, don't dump your trash just anywhere."
    pov "I prefer it if you didn't call my cum 'trash'."
    vio "Haha, sorry. Anyway, I gotta get back to duty. Thanks for the much needed break."
    pov "Thanks for letting me up here."
    pov "It was a... nice view."
    vio "Right?!"
    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
