## Stairs ##
label lbl_allaway_after_school_sex_stairs:
    if hscene_xray == 0:
        scene bg allawayposthscene_stairs_3
        with fade
    else:
        scene bg allawayposthscene_stairs_3_0
        with fade

label lbl_allaway_after_school_sex_stairs_choice:
    jump lbl_allaway_after_school_sex_stairs_pussy

####################
## Stairs Pussy Pre
label lbl_allaway_after_school_sex_stairs_pussy:
    if hscene_xray == 0:
        show bg allawayposthscene_stairs_3b
        pov "Go on deeper, Miss Allaway."
        show bg allawayposthscene_stairs_3
        mis "Shhh, you're too fucking big... Lemme ease into it..."
        show bg allawayposthscene_stairs_3b
        mis "{i}*Moan*{/i}"
    else:
        show bg allawayposthscene_stairs_3b_0
        pov "Go on deeper, Miss Allaway."
        show bg allawayposthscene_stairs_3_0
        mis "Shhh, you're too fucking big... Lemme ease into it..."
        show bg allawayposthscene_stairs_3b_0
        mis "{i}*Moan*{/i}"
    if hscene_xray == 0:
        show bg allawayposthscene_stairs_2
        $ renpy.pause(0.7,hard=True)
        show bg allawayposthscene_stairs_1
        $ renpy.pause(0.7,hard=True)
    else:
        show bg allawayposthscene_stairs_2_0
        $ renpy.pause(0.7,hard=True)
        show bg allawayposthscene_stairs_1_0
        $ renpy.pause(0.7,hard=True)
    pov "Oh- God..."
    mis "Are you oka-?"
    pov "Keep going, Miss. You feel amazing."

    jump lbl_allaway_after_school_sex_stairs_pussy_0

label lbl_allaway_after_school_sex_stairs_pussy_0:
    #$ allaway_after_school_sex_stairs_counter = 0
    if hscene_xray == 0:
        jump lbl_allaway_after_school_sex_stairs_pussy_1
    else:
        jump lbl_allaway_after_school_sex_stairs_pussy_1_0

####################
## Stairs Stage 1
label lbl_allaway_after_school_sex_stairs_pussy_1:
    scene img_allaway_after_school_sex_stairs_pussy_stage_1
    #$ allaway_after_school_sex_stairs_counter += 1
    #show bg allawayposthscene_stairs_1
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_stairs_2
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_stairs_3
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_stairs_3b
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_stairs_4
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and allaway_after_school_sex_stairs_counter == 4:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_cum
    #elif skill_sta <= 14 and allaway_after_school_sex_stairs_counter == 6:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_2
    #elif skill_sta <= 20 and allaway_after_school_sex_stairs_counter == 8:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_2
    #else:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_1

image img_allaway_after_school_sex_stairs_pussy_stage_1:
    "bg allawayposthscene_stairs_1"
    pause 0.3
    "bg allawayposthscene_stairs_2"
    pause 0.1
    "bg allawayposthscene_stairs_3"
    pause 0.3
    "bg allawayposthscene_stairs_3b"
    pause 0.3
    "bg allawayposthscene_stairs_4"
    pause 0.3
    repeat

####################
## Stairs Stage 1 XRAY
label lbl_allaway_after_school_sex_stairs_pussy_1_0:
    scene img_allaway_after_school_sex_stairs_pussy_stage_1_0
    #$ allaway_after_school_sex_stairs_counter += 1
    #show bg allawayposthscene_stairs_1_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_stairs_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_stairs_3_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_stairs_3b_0
    #$ renpy.pause(0.3,hard=True)
    #show bg allawayposthscene_stairs_4_0
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and allaway_after_school_sex_stairs_counter == 4:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_cum
    #elif skill_sta <= 14 and allaway_after_school_sex_stairs_counter == 6:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_2_0
    #elif skill_sta <= 20 and allaway_after_school_sex_stairs_counter == 8:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_2_0
    #else:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_1_0

image img_allaway_after_school_sex_stairs_pussy_stage_1_0:
    "bg allawayposthscene_stairs_1_0"
    pause 0.3
    "bg allawayposthscene_stairs_2_0"
    pause 0.1
    "bg allawayposthscene_stairs_3_0"
    pause 0.3
    "bg allawayposthscene_stairs_3b_0"
    pause 0.3
    "bg allawayposthscene_stairs_4_0"
    pause 0.3
    repeat

####################
## Stairs Stage 2
label lbl_allaway_after_school_sex_stairs_pussy_2:
    scene img_allaway_after_school_sex_stairs_pussy_stage_2
    #$ allaway_after_school_sex_stairs_counter += 1
    #show bg allawayposthscene_stairs_5
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_stairs_6
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_stairs_7
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_stairs_6
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_after_school_sex_stairs_counter == 18:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_cum
    #elif skill_sta <= 20 and allaway_after_school_sex_stairs_counter == 20:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_3
    #else:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_2

image img_allaway_after_school_sex_stairs_pussy_stage_2:
    "bg allawayposthscene_stairs_5"
    pause 0.2
    "bg allawayposthscene_stairs_6"
    pause 0.1
    "bg allawayposthscene_stairs_7"
    pause 0.2
    "bg allawayposthscene_stairs_6"
    pause 0.2
    repeat

####################
## Stairs Stage 2 XRAY
label lbl_allaway_after_school_sex_stairs_pussy_2_0:
    scene img_allaway_after_school_sex_stairs_pussy_stage_2_0
    #$ allaway_after_school_sex_stairs_counter += 1
    #show bg allawayposthscene_stairs_5_0
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_stairs_6_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_stairs_7_0
    #$ renpy.pause(0.2,hard=True)
    #show bg allawayposthscene_stairs_6_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_after_school_sex_stairs_counter == 18:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_cum
    #elif skill_sta <= 20 and allaway_after_school_sex_stairs_counter == 20:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_3_0
    #else:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_2_0

image img_allaway_after_school_sex_stairs_pussy_stage_2_0:
    "bg allawayposthscene_stairs_5_0"
    pause 0.2
    "bg allawayposthscene_stairs_6_0"
    pause 0.1
    "bg allawayposthscene_stairs_7_0"
    pause 0.2
    "bg allawayposthscene_stairs_6_0"
    pause 0.2
    repeat

####################
## Stairs Stage 3
label lbl_allaway_after_school_sex_stairs_pussy_3:
    scene img_allaway_after_school_sex_stairs_pussy_stage_3
    #$ allaway_after_school_sex_stairs_counter += 1
    #show bg allawayposthscene_stairs_8
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_stairs_10
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_stairs_9
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and allaway_after_school_sex_stairs_counter == 36:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_cum
    #else:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_3

image img_allaway_after_school_sex_stairs_pussy_stage_3:
    "bg allawayposthscene_stairs_8"
    pause 0.1
    "bg allawayposthscene_stairs_10"
    pause 0.1
    "bg allawayposthscene_stairs_9"
    pause 0.1
    repeat

####################
## Stairs Stage 3 XRAY
label lbl_allaway_after_school_sex_stairs_pussy_3_0:
    scene img_allaway_after_school_sex_stairs_pussy_stage_3_0
    #$ allaway_after_school_sex_stairs_counter += 1
    #show bg allawayposthscene_stairs_8_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_stairs_10_0
    #$ renpy.pause(0.1,hard=True)
    #show bg allawayposthscene_stairs_9_0
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and allaway_after_school_sex_stairs_counter == 36:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_cum
    #else:
    #    jump lbl_allaway_after_school_sex_stairs_pussy_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_after_school_sex_stairs_pussy_3_0

image img_allaway_after_school_sex_stairs_pussy_stage_3_0:
    "bg allawayposthscene_stairs_8_0"
    pause 0.1
    "bg allawayposthscene_stairs_10_0"
    pause 0.1
    "bg allawayposthscene_stairs_9_0"
    pause 0.1
    repeat

####################
## Stairs Cum
label lbl_allaway_after_school_sex_stairs_pussy_cum:
    if missallaway_points <= 6:
        jump lbl_allaway_after_school_sex_stairs_pussy_cum_2
    else:
        jump lbl_allaway_after_school_sex_stairs_pussy_cum_3

label lbl_allaway_after_school_sex_stairs_pussy_cum_2:
    #if hscene_xray == 0:
    #    scene bg allawayposthscene_stairs_3
    #else:
    #    scene bg allawayposthscene_stairs_3_0
    call screen scr_allaway_after_school_sex_stairs_pussy_cum_2

screen scr_allaway_after_school_sex_stairs_pussy_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_stairs_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_stairs_pussy_cumchoice")

label lbl_allaway_after_school_sex_stairs_pussy_cum_3:
    #if hscene_xray == 0:
    #    scene bg allawayposthscene_stairs_3
    #else:
    #    scene bg allawayposthscene_stairs_3_0
    call screen scr_allaway_after_school_sex_stairs_pussy_cum_3

screen scr_allaway_after_school_sex_stairs_pussy_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_scenechoice_stairs")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_stairs_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_stairs_pussy_cumchoice")

label lbl_allaway_after_school_sex_stairs_pussy_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_allaway_after_school_sex_stairs_pussy_cumin
            else:
                jump lbl_allaway_after_school_sex_stairs_pussy_cumin_0
        "Cum outside":
            jump lbl_allaway_after_school_sex_stairs_pussy_cumout

####################
## Stairs Cum In
label lbl_allaway_after_school_sex_stairs_pussy_cumin:
    scene bg allawayposthscene_stairs_12_0
    $ renpy.pause(1.8,hard=True)
    show bg allawayposthscene_stairs_12_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_12_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_12_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_12_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_12_5
    $ renpy.pause()
    show bg allawayposthscene_stairs_12_6
    pov "Oh, crap... Miss Allaway? I may have accidentally..."
    show bg allawayposthscene_stairs_12_7
    mis "It's okay, [povname]. The creampie feels so amazing and hot."
    mis "I've been on the pill for a while."
    mis "{i}*Pants*{/i}"
    show bg allawayposthscene_stairs_12_6
    pov "Oh, well thank God for that."
    mis "We should... work out how to get out of this mess without spilling all your cum on the floor."
    mis "..."
    mis "It's a safety hazard."
    show bg allawayposthscene_stairs_12_7
    pov "I hear you loud and clear, teach'"

    jump lbl_allaway_after_school_sex_end

####################
## Stairs Cum In XRAY
label lbl_allaway_after_school_sex_stairs_pussy_cumin_0:
    scene bg allawayposthscene_stairs_11_0
    $ renpy.pause(0.5,hard=True)
    show bg allawayposthscene_stairs_11_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_9
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_10
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_11_11
    $ renpy.pause()
    show bg allawayposthscene_stairs_11_12
    pov "Oh, crap... Miss Allaway? I may have accidentally..."
    show bg allawayposthscene_stairs_11_13
    mis "It's okay, [povname]. The creampie feels so amazing and hot."
    mis "I've been on the pill for a while."
    mis "{i}*Pants*{/i}"
    show bg allawayposthscene_stairs_11_12
    pov "Oh, well thank God for that."
    mis "We should... work out how to get out of this mess without spilling all your cum on the floor."
    mis "..."
    mis "It's a safety hazard."
    show bg allawayposthscene_stairs_11_13
    pov "I hear you loud and clear, teach'"

    jump lbl_allaway_after_school_sex_end

####################
## Stairs Cum Out
label lbl_allaway_after_school_sex_stairs_pussy_cumout:
    scene bg allawayposthscene_stairs_13_0
    $ renpy.pause(0.6,hard=True)
    show bg allawayposthscene_stairs_13_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_9
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_10
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_11
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_12
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_13_13
    $ renpy.pause()
    mis "Hehehe, oh my God..."
    mis "You made a huge mess in the middle of the hallway."
    mis "It shot out really far."
    mis "{i}*Pants*{/i}"
    pov "Fuck... don't tell me I have to clean that up."
    show bg allawayposthscene_stairs_13_14
    mis "Best you do to avoid any trouble."
    mis "Watching you cum like this was like watching myself cum all over the place."
    mis "Honestly, that was so hot."

    jump lbl_allaway_after_school_sex_end

####################
## Stairs Next
label lbl_allaway_after_school_sex_stairs_pussy_next:
    if hscene_xray == 0:
        show bg allawayposthscene_stairs_1
        pov "C'mon, Miss. Let's get off these stairs."
    else:
        show bg allawayposthscene_stairs_1_0
        pov "C'mon, Miss. Let's get off these stairs."

    jump lbl_allaway_after_school_sex_scenechoice_stairs
