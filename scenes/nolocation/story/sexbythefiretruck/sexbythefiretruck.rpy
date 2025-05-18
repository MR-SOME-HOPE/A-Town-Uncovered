## Sex By The Fire Truck ##
label lbl_sex_by_the_fire_truck:
    #default sex_by_the_fire_truck_counter = 0

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

label lbl_sex_by_the_fire_truck_0:
    #$ sex_by_the_fire_truck_counter = 0
    if hscene_xray == 0:
        jump lbl_sex_by_the_fire_truck_1
    else:
        jump lbl_sex_by_the_fire_truck_1_0

####################
## Stage 1
label lbl_sex_by_the_fire_truck_1:
    scene img_sex_by_the_fire_truck_stage_1
    #$ sex_by_the_fire_truck_counter += 1
    #show bg sexbythefiretruck_1
    #$ renpy.pause(0.3,hard=True)
    #show bg sexbythefiretruck_2
    #$ renpy.pause(0.1,hard=True)
    #show bg sexbythefiretruck_3
    #$ renpy.pause(0.3,hard=True)
    #show bg sexbythefiretruck_4
    #$ renpy.pause(0.3,hard=True)
    #show bg sexbythefiretruck_2
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and sex_by_the_fire_truck_counter == 4:
    #    jump lbl_sex_by_the_fire_truck_cum
    #elif skill_sta <= 14 and sex_by_the_fire_truck_counter == 6:
    #    jump lbl_sex_by_the_fire_truck_2
    #elif skill_sta <= 20 and sex_by_the_fire_truck_counter == 8:
    #    jump lbl_sex_by_the_fire_truck_2
    #else:
    #    jump lbl_sex_by_the_fire_truck_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_sex_by_the_fire_truck_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_sex_by_the_fire_truck_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sex_by_the_fire_truck_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sex_by_the_fire_truck_1

image img_sex_by_the_fire_truck_stage_1:
    "bg sexbythefiretruck_1"
    pause 0.3
    "bg sexbythefiretruck_2"
    pause 0.1
    "bg sexbythefiretruck_3"
    pause 0.3
    "bg sexbythefiretruck_4"
    pause 0.3
    "bg sexbythefiretruck_2"
    pause 0.3
    repeat

####################
## Stage 1 XRAY
label lbl_sex_by_the_fire_truck_1_0:
    scene img_sex_by_the_fire_truck_stage_1_0
    #$ sex_by_the_fire_truck_counter += 1
    #show bg sexbythefiretruck_1_0
    #$ renpy.pause(0.3,hard=True)
    #show bg sexbythefiretruck_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg sexbythefiretruck_3_0
    #$ renpy.pause(0.3,hard=True)
    #show bg sexbythefiretruck_4_0
    #$ renpy.pause(0.3,hard=True)
    #show bg sexbythefiretruck_2_0
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and sex_by_the_fire_truck_counter == 4:
    #    jump lbl_sex_by_the_fire_truck_cum
    #elif skill_sta <= 14 and sex_by_the_fire_truck_counter == 6:
    #    jump lbl_sex_by_the_fire_truck_2_0
    #elif skill_sta <= 20 and sex_by_the_fire_truck_counter == 8:
    #    jump lbl_sex_by_the_fire_truck_2_0
    #else:
    #    jump lbl_sex_by_the_fire_truck_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_sex_by_the_fire_truck_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_sex_by_the_fire_truck_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sex_by_the_fire_truck_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sex_by_the_fire_truck_1_0

image img_sex_by_the_fire_truck_stage_1_0:
    "bg sexbythefiretruck_1_0"
    pause 0.3
    "bg sexbythefiretruck_2_0"
    pause 0.1
    "bg sexbythefiretruck_3_0"
    pause 0.3
    "bg sexbythefiretruck_4_0"
    pause 0.3
    "bg sexbythefiretruck_2_0"
    pause 0.3
    repeat

####################
## Stage 2
label lbl_sex_by_the_fire_truck_2:
    scene img_sex_by_the_fire_truck_stage_2
    #$ sex_by_the_fire_truck_counter += 1
    #show bg sexbythefiretruck_1
    #$ renpy.pause(0.2,hard=True)
    #show bg sexbythefiretruck_2
    #$ renpy.pause(0.1,hard=True)
    #show bg sexbythefiretruck_3
    #$ renpy.pause(0.2,hard=True)
    #show bg sexbythefiretruck_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and sex_by_the_fire_truck_counter == 14:
    #    jump lbl_sex_by_the_fire_truck_cum
    #elif skill_sta <= 20 and sex_by_the_fire_truck_counter == 16:
    #    jump lbl_sex_by_the_fire_truck_3
    #else:
    #    jump lbl_sex_by_the_fire_truck_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_sex_by_the_fire_truck_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sex_by_the_fire_truck_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sex_by_the_fire_truck_2

image img_sex_by_the_fire_truck_stage_2:
    "bg sexbythefiretruck_1"
    pause 0.2
    "bg sexbythefiretruck_2"
    pause 0.1
    "bg sexbythefiretruck_3"
    pause 0.2
    "bg sexbythefiretruck_2"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_sex_by_the_fire_truck_2_0:
    scene img_sex_by_the_fire_truck_stage_2_0
    #$ sex_by_the_fire_truck_counter += 1
    #show bg sexbythefiretruck_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg sexbythefiretruck_2_0
    #$ renpy.pause(0.1,hard=True)
    #show bg sexbythefiretruck_3_0
    #$ renpy.pase(#0.2,hard=True)
    #show bg sexbythefiretruck_2_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and sex_by_the_fire_truck_counter == 14:
    #    jump lbl_sex_by_the_fire_truck_cum
    #elif skill_sta <= 20 and sex_by_the_fire_truck_counter == 16:
    #    jump lbl_sex_by_the_fire_truck_3_0
    #else:
    #    jump lbl_sex_by_the_fire_truck_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_sex_by_the_fire_truck_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sex_by_the_fire_truck_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sex_by_the_fire_truck_2_0

image img_sex_by_the_fire_truck_stage_2_0:
    "bg sexbythefiretruck_1_0"
    pause 0.2
    "bg sexbythefiretruck_2_0"
    pause 0.1
    "bg sexbythefiretruck_3_0"
    pause 0.2
    "bg sexbythefiretruck_2_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_sex_by_the_fire_truck_3:
    scene img_sex_by_the_fire_truck_stage_3
    #$ sex_by_the_fire_truck_counter += 1
    #show bg sexbythefiretruck_1
    #$ renpy.pause(0.1,hard=True)
    #show bg sexbythefiretruck_3
    #$ renpy.pause(0.1,hard=True)
    #show bg sexbythefiretruck_2
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and sex_by_the_fire_truck_counter == 24:
    #    jump lbl_sex_by_the_fire_truck_cum
    #else:
    #    jump lbl_sex_by_the_fire_truck_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sex_by_the_fire_truck_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sex_by_the_fire_truck_3

image img_sex_by_the_fire_truck_stage_3:
    "bg sexbythefiretruck_1"
    pause 0.1
    "bg sexbythefiretruck_3"
    pause 0.1
    "bg sexbythefiretruck_2"
    pause 0.1
    repeat

####################
## Stage 3 XRAY
label lbl_sex_by_the_fire_truck_3_0:
    scene img_sex_by_the_fire_truck_stage_3_0
    #$ sex_by_the_fire_truck_counter += 1
    #show bg sexbythefiretruck_1_0
    #$ renpy.pause(0.1,hard=True)
    #show bg sexbythefiretruck_3_0
    #$ renpy.pause(0.1,hard=True)
    #show bg sexbythefiretruck_2_0
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and sex_by_the_fire_truck_counter == 24:
    #    jump lbl_sex_by_the_fire_truck_cum
    #else:
    #    jump lbl_sex_by_the_fire_truck_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_sex_by_the_fire_truck_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_sex_by_the_fire_truck_3_0

image img_sex_by_the_fire_truck_stage_3_0:
    "bg sexbythefiretruck_1_0"
    pause 0.1
    "bg sexbythefiretruck_3_0"
    pause 0.1
    "bg sexbythefiretruck_2_0"
    pause 0.1
    repeat

####################
## Cum Choice

label lbl_sex_by_the_fire_truck_cum:
    #if hscene_xray == 0:
    #    scene bg sexbythefiretruck_3
    #else:
    #    scene bg sexbythefiretruck_3_0
    call screen scr_sex_by_the_fire_truck_cum_2

screen scr_sex_by_the_fire_truck_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sex_by_the_fire_truck_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_sex_by_the_fire_truck_cumchoice")

label lbl_sex_by_the_fire_truck_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_sex_by_the_fire_truck_cumin
            else:
                jump lbl_sex_by_the_fire_truck_cumin_0
        "Cum outside":
            jump lbl_sex_by_the_fire_truck_cumout

####################
## Cum In
label lbl_sex_by_the_fire_truck_cumin:
    scene bg sexbythefiretruck_3
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

    jump lbl_sex_by_the_fire_truck_end

####################
## Cum In XRAY
label lbl_sex_by_the_fire_truck_cumin_0:
    scene bg sexbythefiretruck_4_0
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

    jump lbl_sex_by_the_fire_truck_end

####################
## Cum Out
label lbl_sex_by_the_fire_truck_cumout:
    scene bg sexbythefiretruck_7_0
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

    jump lbl_sex_by_the_fire_truck_end

####################
## End

label lbl_sex_by_the_fire_truck_end:
    pov "..."
    pov "How the hell are we gonna get back home..."
    mis "We can figure that out after a few more rounds."

    scene black
    with fade
    $ renpy.pause(1.5)
    "After a few hours of exhaustedly walking back into town..."

    scene bg myhousefront_night
    with fade
    $ renpy.pause(1.5)
    if skill_sta >= 12:
        $ skill_sta -= 12
    else:
        $ skill_sta = 0
    $ renpy.notify("You lost 12 Stamina Points")
    pov "{i}Home... sweet... home...{/i}"
    pov "{i}Fuck my legs hurt...{/i}"
    pov "{i}My dick feels numb as well...{/i}"
    pov "{i}Y'know what?{/i}"
    pov "{i}Still worth it.{/i}"
    $ gtime = 3
    $ missallaway_path = 24

    jump lbl_myhousefront_night_setup
