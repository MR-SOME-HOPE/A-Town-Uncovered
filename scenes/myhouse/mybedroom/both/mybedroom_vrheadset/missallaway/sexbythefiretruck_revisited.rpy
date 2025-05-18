## Sex By The Fire Truck ##
label lbl_sex_by_the_fire_truck_revisit:
    scene black
    with fade
    mis "Is it just me or is this night really heating up?"
    pov "I feel it too, Miss Allaway."
    pov "Do you... wanna..."
    mis "Strip off our clothes and fuck each other silly?"
    pov "You are such a goddamn romantic."
    if hscene_xray == 0:
        scene bg sexbythefiretruck_1
        with fade
        mis "Mmmm... that feels a lot better."
        show bg sexbythefiretruck_2
        $ renpy.pause(0.1,hard=True)
        show bg sexbythefiretruck_3
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_4
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_2
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_1
        mis "Ahh- that feels sooo good."
        show bg sexbythefiretruck_2
        $ renpy.pause(0.1,hard=True)
        show bg sexbythefiretruck_3
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_4
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_2
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_1
        pov "Ah yeah... Definitely feels a lot warmer."
        show bg sexbythefiretruck_2
        $ renpy.pause(0.1,hard=True)
        show bg sexbythefiretruck_3
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_4
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_2
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_1
        mis "Well, I want it steaming hot."
        pov "Then let's see if we can start a fire this way."
    else:
        scene bg sexbythefiretruck_1_0
        with fade
        mis "Mmmm... that feels a lot better."
        show bg sexbythefiretruck_2_0
        $ renpy.pause(0.1,hard=True)
        show bg sexbythefiretruck_3_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_4_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_2_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_1_0
        mis "Ahh- that feels sooo good."
        show bg sexbythefiretruck_2_0
        $ renpy.pause(0.1,hard=True)
        show bg sexbythefiretruck_3_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_4_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_2_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_1_0
        pov "Ah yeah... Definitely feels a lot warmer."
        show bg sexbythefiretruck_2_0
        $ renpy.pause(0.1,hard=True)
        show bg sexbythefiretruck_3_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_4_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_2_0
        $ renpy.pause(0.3,hard=True)
        show bg sexbythefiretruck_1_0
        mis "Well, I want it steaming hot."
        pov "Then let's see if we can start a fire this way."

label lbl_sex_by_the_fire_truck_revisit_0:
    $ vrheadset_revisitcounter = 0
    if hscene_xray == 0:
        jump lbl_sex_by_the_fire_truck_revisit_1
    else:
        jump lbl_sex_by_the_fire_truck_revisit_1_0

####################
## Stage 1
label lbl_sex_by_the_fire_truck_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg sexbythefiretruck_1
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_2
    $ renpy.pause(0.1,hard=True)
    show bg sexbythefiretruck_3
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_4
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_2
    $ renpy.pause(0.3,hard=True)
    jump lbl_sex_by_the_fire_truck_revisit_counter

####################
## Stage 1 XRAY
label lbl_sex_by_the_fire_truck_revisit_1_0:
    $ vrheadset_revisitcounter += 1
    show bg sexbythefiretruck_1_0
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_2_0
    $ renpy.pause(0.1,hard=True)
    show bg sexbythefiretruck_3_0
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_4_0
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_2_0
    $ renpy.pause(0.3,hard=True)
    jump lbl_sex_by_the_fire_truck_revisit_counter_xray

####################
## Stage 2
label lbl_sex_by_the_fire_truck_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg sexbythefiretruck_1
    $ renpy.pause(0.2,hard=True)
    show bg sexbythefiretruck_2
    $ renpy.pause(0.1,hard=True)
    show bg sexbythefiretruck_3
    $ renpy.pause(0.2,hard=True)
    show bg sexbythefiretruck_2
    $ renpy.pause(0.2,hard=True)
    jump lbl_sex_by_the_fire_truck_revisit_counter

####################
## Stage 2 XRAY
label lbl_sex_by_the_fire_truck_revisit_2_0:
    $ vrheadset_revisitcounter += 1
    show bg sexbythefiretruck_1_0
    $ renpy.pause(0.2,hard=True)
    show bg sexbythefiretruck_2_0
    $ renpy.pause(0.1,hard=True)
    show bg sexbythefiretruck_3_0
    $ renpy.pause(0.2,hard=True)
    show bg sexbythefiretruck_2_0
    $ renpy.pause(0.2,hard=True)
    jump lbl_sex_by_the_fire_truck_revisit_counter_xray

####################
## Stage 3
label lbl_sex_by_the_fire_truck_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg sexbythefiretruck_1
    $ renpy.pause(0.1,hard=True)
    show bg sexbythefiretruck_3
    $ renpy.pause(0.1,hard=True)
    show bg sexbythefiretruck_2
    $ renpy.pause(0.1,hard=True)
    jump lbl_sex_by_the_fire_truck_revisit_counter

####################
## Stage 3 XRAY
label lbl_sex_by_the_fire_truck_revisit_3_0:
    $ vrheadset_revisitcounter += 1
    show bg sexbythefiretruck_1_0
    $ renpy.pause(0.1,hard=True)
    show bg sexbythefiretruck_3_0
    $ renpy.pause(0.1,hard=True)
    show bg sexbythefiretruck_2_0
    $ renpy.pause(0.1,hard=True)
    jump lbl_sex_by_the_fire_truck_revisit_counter_xray

label lbl_sex_by_the_fire_truck_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_sex_by_the_fire_truck_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_sex_by_the_fire_truck_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_sex_by_the_fire_truck_cum_revisit
    else:
        jump lbl_sex_by_the_fire_truck_revisit_1

label lbl_sex_by_the_fire_truck_revisit_counter_xray:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_sex_by_the_fire_truck_revisit_2_0
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_sex_by_the_fire_truck_revisit_3_0
    elif vrheadset_revisitcounter >= 90:
        call screen scr_sex_by_the_fire_truck_cum_revisit
    else:
        jump lbl_sex_by_the_fire_truck_revisit_1_0

screen scr_sex_by_the_fire_truck_cum_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sex_by_the_fire_truck_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sex_by_the_fire_truck_revisit_cumchoice")

label lbl_sex_by_the_fire_truck_revisit_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_sex_by_the_fire_truck_revisit_cumin
            else:
                jump lbl_sex_by_the_fire_truck_revisit_cumin_0
        "Cum outside":
            jump lbl_sex_by_the_fire_truck_revisit_cumout

####################
## Cum In
label lbl_sex_by_the_fire_truck_revisit_cumin:
    show bg sexbythefiretruck_3
    $ renpy.pause(2,hard=True)
    show bg sexbythefiretruck_6_1
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_6_2
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_6_3
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_6_4
    $ renpy.pause()
    pov "Fucckk..."
    pov "Sorry, Miss..."
    mis "N-no- {i}*pants*{/i} It's alright."
    mis "I've been on the pill for a while..."
    mis "{i}*Pants*{/i}"
    pov "Oh- in that case..."
    pov "That felt fucking amazing."
    mis "You fucking said it..."

    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## Cum In XRAY
label lbl_sex_by_the_fire_truck_revisit_cumin_0:
    show bg sexbythefiretruck_4_0
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_1
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_2
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_3
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_4
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_5
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_6
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_7
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_8
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_9
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_5_10
    $ renpy.pause()
    pov "Fucckk..."
    pov "Sorry, Miss..."
    mis "N-no- {i}*pants*{/i} It's alright."
    mis "I've been on the pill for a while..."
    mis "{i}*Pants*{/i}"
    pov "Oh- in that case..."
    pov "That felt fucking amazing."
    mis "You fucking said it..."

    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## Cum Out
label lbl_sex_by_the_fire_truck_revisit_cumout:
    show bg sexbythefiretruck_7_0
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_1
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_2
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_3
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_4
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_5
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_6
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_7
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_8
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_9
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_10
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_11
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_12
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_13
    $ renpy.pause(0.3,hard=True)
    show bg sexbythefiretruck_7_14
    $ renpy.pause()
    pov "Fucckk..."
    pov "Oh, God... that felt like a lot..."
    mis "You're quivering a lot for sure."
    pov "I can feel it all over my thighs."
    mis "Can't feel any on me, which I'm somewhat thankful for."
    pov "..."
    pov "I don't know if this is the right time but I think I've fertilized the land."
    mis "Lines like these are what gets you laid."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
