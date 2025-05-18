## Stairs ##
label lbl_allaway_after_school_sex_stairs_revisit:
    if hscene_xray == 0:
        scene bg allawayposthscene_stairs_3
        with fade
    else:
        scene bg allawayposthscene_stairs_3_0
        with fade
    jump lbl_allaway_after_school_sex_stairs_revisit_pussy
####################
## Stairs Pussy Pre
label lbl_allaway_after_school_sex_stairs_revisit_pussy:
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

    jump lbl_allaway_after_school_sex_stairs_revisit_pussy_0

label lbl_allaway_after_school_sex_stairs_revisit_pussy_0:
    $ vrheadset_revisitcounter = 0
    if hscene_xray == 0:
        jump lbl_allaway_after_school_sex_stairs_revisit_pussy_1
    else:
        jump lbl_allaway_after_school_sex_stairs_revisit_pussy_1_0

####################
## Stairs Stage 1
label lbl_allaway_after_school_sex_stairs_revisit_pussy_1:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_stairs_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_2
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_stairs_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_3b
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_4
    $ renpy.pause(0.3,hard=True)
    jump lbl_allaway_after_school_sex_stairs_revisit_pussy_counter

####################
## Stairs Stage 1 XRAY
label lbl_allaway_after_school_sex_stairs_revisit_pussy_1_0:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_stairs_1_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_2_0
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_stairs_3_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_3b_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayposthscene_stairs_4_0
    $ renpy.pause(0.3,hard=True)
    jump lbl_allaway_after_school_sex_stairs_revisit_pussy_counter_xray


####################
## Stairs Stage 2
label lbl_allaway_after_school_sex_stairs_revisit_pussy_2:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_stairs_5
    $ renpy.pause(0.2,hard=True)
    show bg allawayposthscene_stairs_6
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_stairs_7
    $ renpy.pause(0.2,hard=True)
    show bg allawayposthscene_stairs_6
    $ renpy.pause(0.2,hard=True)
    jump lbl_allaway_after_school_sex_stairs_revisit_pussy_counter


####################
## Stairs Stage 2 XRAY
label lbl_allaway_after_school_sex_stairs_revisit_pussy_2_0:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_stairs_5_0
    $ renpy.pause(0.2,hard=True)
    show bg allawayposthscene_stairs_6_0
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_stairs_7_0
    $ renpy.pause(0.2,hard=True)
    show bg allawayposthscene_stairs_6_0
    $ renpy.pause(0.2,hard=True)
    jump lbl_allaway_after_school_sex_stairs_revisit_pussy_counter_xray


####################
## Stairs Stage 3
label lbl_allaway_after_school_sex_stairs_revisit_pussy_3:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_stairs_8
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_stairs_10
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_stairs_9
    $ renpy.pause(0.1,hard=True)
    jump lbl_allaway_after_school_sex_stairs_revisit_pussy_counter


####################
## Stairs Stage 3 XRAY
label lbl_allaway_after_school_sex_stairs_revisit_pussy_3_0:
    $ vrheadset_revisitcounter += 1
    show bg allawayposthscene_stairs_8_0
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_stairs_10_0
    $ renpy.pause(0.1,hard=True)
    show bg allawayposthscene_stairs_9_0
    $ renpy.pause(0.1,hard=True)
    jump lbl_allaway_after_school_sex_stairs_revisit_pussy_counter_xray

label lbl_allaway_after_school_sex_stairs_revisit_pussy_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_allaway_after_school_sex_stairs_revisit_pussy_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_allaway_after_school_sex_stairs_revisit_pussy_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_allaway_after_school_sex_stairs_pussy_cum_revisit
    else:
        jump lbl_allaway_after_school_sex_stairs_revisit_pussy_1

label lbl_allaway_after_school_sex_stairs_revisit_pussy_counter_xray:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_allaway_after_school_sex_stairs_revisit_pussy_2_0
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_allaway_after_school_sex_stairs_revisit_pussy_3_0
    elif vrheadset_revisitcounter >= 90:
        call screen scr_allaway_after_school_sex_stairs_pussy_cum_revisit
    else:
        jump lbl_allaway_after_school_sex_stairs_revisit_pussy_1_0



screen scr_allaway_after_school_sex_stairs_pussy_cum_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_stairs_revisit_pussy_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_after_school_sex_stairs_revisit_pussy_cumchoice")


label lbl_allaway_after_school_sex_stairs_revisit_pussy_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_allaway_after_school_sex_stairs_revisit_pussy_cumin
            else:
                jump lbl_allaway_after_school_sex_stairs_revisit_pussy_cumin_0
        "Cum outside":
            jump lbl_allaway_after_school_sex_stairs_revisit_pussy_cumout

####################
## Stairs Cum In
label lbl_allaway_after_school_sex_stairs_revisit_pussy_cumin:
    show bg allawayposthscene_stairs_12_0
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

    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## Stairs Cum In XRAY
label lbl_allaway_after_school_sex_stairs_revisit_pussy_cumin_0:
    show bg allawayposthscene_stairs_11_0
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

    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## Stairs Cum Out
label lbl_allaway_after_school_sex_stairs_revisit_pussy_cumout:
    show bg allawayposthscene_stairs_13_0
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

    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
