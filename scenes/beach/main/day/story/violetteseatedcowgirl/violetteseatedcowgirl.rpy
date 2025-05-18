## Violette Seated Cowgirl
label lbl_violette_seated_cowgirl:
    #default violette_seated_cowgirl_counter = 0
    scene bg beachmain_day
    show povn neutral_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "Hey, Vi."
    show povn neutral_talk at left
    show vio confused at right
    pov "Wondering if I can have a turn up there."
    show povn neutral at left
    show vio neutral_talk at right
    vio "Sure, I could use a break."
    show vio smirk_talk at right
    vio "Can't say no to-"
    show povn confused at left
    vio "-to that..."
    show povn confused_talk at left
    show vio smirk at right
    pov "Are you looking at my dick?"
    show povn bored at left
    show vio smirk_talk at right
    vio "You still don't have a name for him?"

    scene black
    with fade
    "Violette got off and allowed you to climb on..."

    jump lbl_violette_seated_cowgirl_pre

####################
## Pre Dialogue
label lbl_violette_seated_cowgirl_pre:
    if hscene_xray == 0:
        scene bg violetteseatedcowgirl_4
        with fade
        scene bg violetteseatedcowgirl_4
        with hpunch
    else:
        scene bg violetteseatedcowgirl_4_0
        with fade
        scene bg violetteseatedcowgirl_4_0
        with hpunch
    vio "Ah- yeah- that's big."
    pov "I thought you said you wanted a break!"
    vio "And I thought you wanted a turn on the lifeguard's chair."
    vio "What did you think that implied?"
    pov "Well-"
    vio "Don't play dumb, [povname]. Just behave."
    vio "This is still my beach."

    jump lbl_violette_seated_cowgirl_0

label lbl_violette_seated_cowgirl_0:
    $ violette_seated_cowgirl_counter = 0
    if hscene_xray == 0:
        jump lbl_violette_seated_cowgirl_1
    else:
        jump lbl_violette_seated_cowgirl_1_0

####################
## Stage 1
label lbl_violette_seated_cowgirl_1:
    $ violette_seated_cowgirl_counter += 1
    scene img_violette_seated_cowgirl_stage_1
    #show bg violetteseatedcowgirl_1
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_2
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_3
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_4
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and violette_seated_cowgirl_counter == 4:
    #    jump lbl_violette_seated_cowgirl_cum
    #elif skill_sta <= 14 and violette_seated_cowgirl_counter == 6:
    #    jump lbl_violette_seated_cowgirl_2
    #elif skill_sta <= 20 and violette_seated_cowgirl_counter == 8:
    #    jump lbl_violette_seated_cowgirl_2
    #else:
    #    jump lbl_violette_seated_cowgirl_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violette_seated_cowgirl_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_1

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
label lbl_violette_seated_cowgirl_1_0:
    $ violette_seated_cowgirl_counter += 1
    scene img_violette_seated_cowgirl_stage_1_0
    #show bg violetteseatedcowgirl_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_2_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and violette_seated_cowgirl_counter == 4:
    #    jump lbl_violette_seated_cowgirl_cum
    #elif skill_sta <= 14 and violette_seated_cowgirl_counter == 6:
    #    jump lbl_violette_seated_cowgirl_2_0
    #elif skill_sta <= 20 and violette_seated_cowgirl_counter == 8:
    #    jump lbl_violette_seated_cowgirl_2_0
    #else:
    #    jump lbl_violette_seated_cowgirl_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violette_seated_cowgirl_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_1_0

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
label lbl_violette_seated_cowgirl_2:
    $ violette_seated_cowgirl_counter += 1
    scene img_violette_seated_cowgirl_stage_2
    #show bg violetteseatedcowgirl_1
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_2
    #$ renpy.pause(0.1,hard=True)
    #show bg violetteseatedcowgirl_4
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and violette_seated_cowgirl_counter == 14:
    #    jump lbl_violette_seated_cowgirl_cum
    #elif skill_sta <= 20 and violette_seated_cowgirl_counter == 16:
    #    jump lbl_violette_seated_cowgirl_3
    #else:
    #    jump lbl_violette_seated_cowgirl_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violette_seated_cowgirl_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_2

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
label lbl_violette_seated_cowgirl_2_0:
    $ violette_seated_cowgirl_counter += 1
    scene img_violette_seated_cowgirl_stage_2_0
    #show bg violetteseatedcowgirl_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg violetteseatedcowgirl_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_2_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and violette_seated_cowgirl_counter == 14:
    #    jump lbl_violette_seated_cowgirl_cum
    #elif skill_sta <= 20 and violette_seated_cowgirl_counter == 16:
    #    jump lbl_violette_seated_cowgirl_3_0
    #else:
    #    jump lbl_violette_seated_cowgirl_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_violette_seated_cowgirl_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_2_0

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
label lbl_violette_seated_cowgirl_3:
    $ violette_seated_cowgirl_counter += 1
    #show bg violetteseatedcowgirl_1
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_3
    #$ renpy.pause(0.1,hard=True)
    #show bg violetteseatedcowgirl_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and violette_seated_cowgirl_counter == 24:
    #    jump lbl_violette_seated_cowgirl_cum
    #else:
    #    jump lbl_violette_seated_cowgirl_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_3

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
label lbl_violette_seated_cowgirl_3_0:
    $ violette_seated_cowgirl_counter += 1
    #show bg violetteseatedcowgirl_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg violetteseatedcowgirl_3_0
    #$ renpy.pause(0.1,hard=True)
    #show bg violetteseatedcowgirl_2_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and violette_seated_cowgirl_counter == 24:
    #    jump lbl_violette_seated_cowgirl_cum
    #else:
    #    jump lbl_violette_seated_cowgirl_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_violette_seated_cowgirl_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_violette_seated_cowgirl_3_0

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
label lbl_violette_seated_cowgirl_cum:
    jump lbl_violette_seated_cowgirl_cum_2

label lbl_violette_seated_cowgirl_cum_2:
    #if hscene_xray == 0:
    #    scene bg violetteseatedcowgirl_1
    #else:
    #    scene bg violetteseatedcowgirl_1_0
    call screen scr_violette_seated_cowgirl_cum_2

screen scr_violette_seated_cowgirl_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violette_seated_cowgirl_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violette_seated_cowgirl_cumchoice")

# label lbl_violette_seated_cowgirl_cum_3:
#     if hscene_xray == 0:
#         scene bg violetteseatedcowgirl_1
#     else:
#         scene bg violetteseatedcowgirl_1_0
#     call screen scr_violette_seated_cowgirl_cum_3
#
# screen scr_violette_seated_cowgirl_cum_3():
#     imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violette_seated_cowgirl_scenechoice_mish")
#     imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violette_seated_cowgirl_mish_0")
#     imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_violette_seated_cowgirl_cumchoice")

label lbl_violette_seated_cowgirl_cumchoice:
    menu:
        "Cum inside":
            pov "Vi- I'm gonna cum in you."
            vio "Do it, [povname]."
            if hscene_xray == 0:
                jump lbl_violette_seated_cowgirl_cumin
            else:
                jump lbl_violette_seated_cowgirl_cumin_0
        "Cum on her":
            pov "Vi- I'm cumming..."
            pov "Quick pull out-"
            vio "No! No littering on my beach!"
            vio "Keep it inside."
            pov "Eughh-"
            if hscene_xray == 0:
                jump lbl_violette_seated_cowgirl_cumin
            else:
                jump lbl_violette_seated_cowgirl_cumin_0

####################
## Cum In
label lbl_violette_seated_cowgirl_cumin: ##################################
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

    jump lbl_violette_seated_cowgirl_end

####################
## Cum In XRAY
label lbl_violette_seated_cowgirl_cumin_0:
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

    jump lbl_violette_seated_cowgirl_end

label lbl_violette_seated_cowgirl_end:
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
    if violette_points < 10:
        $ violette_points += 1
        $ renpy.notify("Your relationship with Violette has increased")
    $ renpy.pause()
    "After getting down..."
    scene bg beachmain_day
    with fade

    jump lbl_beachmain_day
