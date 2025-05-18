

label lbl_allaway_school_sex_facefuck:
    #default allaway_school_sex_facefuck_counter = 0

    scene bg schoolsexfacefuck_0
    with fade
    mis "Shove it in already, [povname]."
    mis "I know how much you wanna feel my throat."

    jump lbl_allaway_school_sex_facefuck_0

label lbl_allaway_school_sex_facefuck_0:
    #$ allaway_school_sex_facefuck_counter = 0
    jump lbl_allaway_school_sex_facefuck_1

label lbl_allaway_school_sex_facefuck_1:
    scene img_allaway_school_sex_facefuck_stage_1
    #$ allaway_school_sex_facefuck_counter += 1
    #show bg schoolsexfacefuck_1
    #$ renpy.pause(0.3,hard=True)
    #show bg schoolsexfacefuck_2
    #$ renpy.pause(0.1,hard=True)
    #show bg schoolsexfacefuck_3
    #$ renpy.pause(0.1,hard=True)
    #show bg schoolsexfacefuck_4
    #$ renpy.pause(0.3,hard=True)
    #show bg schoolsexfacefuck_3
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and allaway_school_sex_facefuck_counter == 4:
    #    jump lbl_allaway_school_sex_facefuck_cum
    #elif skill_sta <= 14 and allaway_school_sex_facefuck_counter == 6:
    #    jump lbl_allaway_school_sex_facefuck_2
    #elif skill_sta <= 20 and allaway_school_sex_facefuck_counter == 8:
    #    jump lbl_allaway_school_sex_facefuck_2
    #else:
    #    jump lbl_allaway_school_sex_facefuck_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_school_sex_facefuck_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_school_sex_facefuck_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_school_sex_facefuck_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_school_sex_facefuck_1

image img_allaway_school_sex_facefuck_stage_1:
    "bg schoolsexfacefuck_1"
    pause 0.3
    "bg schoolsexfacefuck_2"
    pause 0.1
    "bg schoolsexfacefuck_3"
    pause 0.1
    "bg schoolsexfacefuck_4"
    pause 0.3
    "bg schoolsexfacefuck_3"
    pause 0.3
    repeat

label lbl_allaway_school_sex_facefuck_2:
    scene img_allaway_school_sex_facefuck_stage_2
    #$ allaway_school_sex_facefuck_counter += 1
    #show bg schoolsexfacefuck_5
    #$ renpy.pause(0.3,hard=True)
    #show bg schoolsexfacefuck_6
    #$ renpy.pause(0.1,hard=True)
    #show bg schoolsexfacefuck_7
    #$ renpy.pause(0.2,hard=True)
    #show bg schoolsexfacefuck_6
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_school_sex_facefuck_counter == 14:
    #    jump lbl_allaway_school_sex_facefuck_cum
    #elif skill_sta <= 20 and allaway_school_sex_facefuck_counter == 16:
    #    jump lbl_allaway_school_sex_facefuck_3
    #else:
    #    jump lbl_allaway_school_sex_facefuck_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_school_sex_facefuck_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_school_sex_facefuck_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_school_sex_facefuck_2

image img_allaway_school_sex_facefuck_stage_2:
    "bg schoolsexfacefuck_5"
    pause 0.3
    "bg schoolsexfacefuck_6"
    pause 0.1
    "bg schoolsexfacefuck_7"
    pause 0.2
    "bg schoolsexfacefuck_6"
    pause 0.2
    repeat

label lbl_allaway_school_sex_facefuck_3:
    scene img_allaway_school_sex_facefuck_stage_3
    #$ allaway_school_sex_facefuck_counter += 1
    #show bg schoolsexfacefuck_8
    #$ renpy.pause(0.2,hard=True)
    #show bg schoolsexfacefuck_9
    #$ renpy.pause(0.1,hard=True)
    #show bg schoolsexfacefuck_10
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and allaway_school_sex_facefuck_counter == 24:
    #    jump lbl_allaway_school_sex_facefuck_cum
    #else:
    #    jump lbl_allaway_school_sex_facefuck_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_school_sex_facefuck_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_school_sex_facefuck_3

image img_allaway_school_sex_facefuck_stage_3:
    "bg schoolsexfacefuck_8"
    pause 0.2
    "bg schoolsexfacefuck_9"
    pause 0.1
    "bg schoolsexfacefuck_10"
    pause 0.2
    repeat

label lbl_allaway_school_sex_facefuck_cum:
    if missallaway_points <= 4:
        jump lbl_allaway_school_sex_facefuck_cum_2
    else:
        jump lbl_allaway_school_sex_facefuck_cum_3

label lbl_allaway_school_sex_facefuck_cum_2:

    #scene bg schoolsexfacefuck_1
    call screen scr_allaway_school_sex_facefuck_cum_2

screen scr_allaway_school_sex_facefuck_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_school_sex_facefuck_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_school_sex_facefuck_cumchoice")

label lbl_allaway_school_sex_facefuck_cum_3:

    #scene bg schoolsexfacefuck_1
    call screen scr_allaway_school_sex_facefuck_cum_3

screen scr_allaway_school_sex_facefuck_cum_3():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_school_sex_facefuck_next")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_school_sex_facefuck_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_school_sex_facefuck_cumchoice")

label lbl_allaway_school_sex_facefuck_cumchoice:

    menu:
        "Cum inside mouth":
            jump lbl_allaway_school_sex_facefuck_cumin
        "Cum outside on face":
            jump lbl_allaway_school_sex_facefuck_cumout

label lbl_allaway_school_sex_facefuck_cumin:
    scene bg schoolsexfacefuck_3
    $ renpy.pause(0.3,hard=True)
    show bg schoolsexfacefuck_11_0
    $ renpy.pause(2,hard=True)
    show bg schoolsexfacefuck_11_1
    $ renpy.pause(0.4,hard=True)
    show bg schoolsexfacefuck_11_2
    $ renpy.pause(0.4,hard=True)
    show bg schoolsexfacefuck_11_3
    $ renpy.pause(0.6,hard=True)
    show bg schoolsexfacefuck_11_4
    $ renpy.pause(0.6,hard=True)
    show bg schoolsexfacefuck_11_5
    $ renpy.pause()
    show bg schoolsexfacefuck_11_6
    $ renpy.pause(0.8,hard=True)
    show bg schoolsexfacefuck_11_7
    $ renpy.pause(0.8,hard=True)
    show bg schoolsexfacefuck_11_8
    $ renpy.pause(0.8,hard=True)
    show bg schoolsexfacefuck_20
    mis "..."
    show bg schoolsexfacefuck_21
    mis "Are you done?"
    show bg schoolsexfacefuck_20
    pov "Well, I just came..."
    show bg schoolsexfacefuck_21
    mis "Well, I guess you aren't up for round 2..."
    mis "Or 3..."
    show bg schoolsexfacefuck_22
    mis "Or even 4..."
    mis "Who know how long we'll be up tonight."
    show bg schoolsexfacefuck_20
    pov "N-no no! I'm up, my little buddy's up. We're both ready to go."
    show bg schoolsexfacefuck_22
    mis "Fantastic. Let's go wild, shall we?"

    jump lbl_allaway_school_sex_farshots

label lbl_allaway_school_sex_facefuck_cumout:
    scene bg schoolsexfacefuck_12_0
    $ renpy.pause(0.6,hard=True)
    show bg schoolsexfacefuck_12_1
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_12_2
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_12_3
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_12_4
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_12_5
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_12_6
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_12_7
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_12_8
    $ renpy.pause()
    show bg schoolsexfacefuck_13
    mis "..."
    show bg schoolsexfacefuck_14
    mis "Are you done?"
    show bg schoolsexfacefuck_16
    pov "Well, I just came..."
    show bg schoolsexfacefuck_14
    mis "Well, I guess you aren't up for round 2..."
    mis "Or 3..."
    show bg schoolsexfacefuck_15
    mis "Or even 4..."
    mis "Who know how long we'll be up tonight."
    show bg schoolsexfacefuck_16
    pov "N-no no! I'm up, my little buddy's up. We're both ready to go."
    show bg schoolsexfacefuck_15
    mis "Fantastic. Let's go wild, shall we?"

    jump lbl_allaway_school_sex_farshots

label lbl_allaway_school_sex_facefuck_next:
    scene bg schoolsexfacefuck_18
    mis "...?"
    show bg schoolsexfacefuck_17
    mis "Hmm?"
    show bg schoolsexfacefuck_18
    mis "Why aren't you moving me?"
    show bg schoolsexfacefuck_17
    pov "Well, I don't want to cum just yet."
    show bg schoolsexfacefuck_18
    mis "Well... when {i}do{/i} you wanna cum?"
    show bg schoolsexfacefuck_19
    mis "Isn't my throat warm enough for you?"
    show bg schoolsexfacefuck_17
    pov "It's just... your pussy felt even warmer."
    show bg schoolsexfacefuck_19
    mis "Oh, I see where you're going with this."
    mis "Well, as you kids say, 'yolo'!"
    show bg schoolsexfacefuck_18
    mis "You all still say 'yolo', right?"

    jump lbl_allaway_school_sex_farshots
