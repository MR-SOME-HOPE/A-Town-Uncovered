
label lbl_allaway_school_sex_facefuck_revisit:
    scene bg schoolsexfacefuck_0
    with fade
    mis "Shove it in already, [povname]."
    mis "I know how much you wanna feel my throat."
    jump lbl_allaway_school_sex_facefuck_revisit_0

label lbl_allaway_school_sex_facefuck_revisit_0:
    $ vrheadset_revisitcounter = 0
    jump lbl_allaway_school_sex_facefuck_revisit_1

label lbl_allaway_school_sex_facefuck_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg schoolsexfacefuck_1
    $ renpy.pause(0.3,hard=True)
    show bg schoolsexfacefuck_2
    $ renpy.pause(0.1,hard=True)
    show bg schoolsexfacefuck_3
    $ renpy.pause(0.1,hard=True)
    show bg schoolsexfacefuck_4
    $ renpy.pause(0.3,hard=True)
    show bg schoolsexfacefuck_3
    $ renpy.pause(0.3,hard=True)
    jump lbl_allaway_school_sex_facefuck_revisit_counter

label lbl_allaway_school_sex_facefuck_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg schoolsexfacefuck_5
    $ renpy.pause(0.3,hard=True)
    show bg schoolsexfacefuck_6
    $ renpy.pause(0.1,hard=True)
    show bg schoolsexfacefuck_7
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_6
    $ renpy.pause(0.2,hard=True)
    jump lbl_allaway_school_sex_facefuck_revisit_counter


label lbl_allaway_school_sex_facefuck_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg schoolsexfacefuck_8
    $ renpy.pause(0.2,hard=True)
    show bg schoolsexfacefuck_9
    $ renpy.pause(0.1,hard=True)
    show bg schoolsexfacefuck_10
    $ renpy.pause(0.2,hard=True)
    jump lbl_allaway_school_sex_facefuck_revisit_counter

label lbl_allaway_school_sex_facefuck_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_allaway_school_sex_facefuck_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_allaway_school_sex_facefuck_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_allaway_school_sex_facefuck_cum_revisit
    else:
        jump lbl_allaway_school_sex_facefuck_revisit_1


screen scr_allaway_school_sex_facefuck_cum_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_school_sex_facefuck_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_school_sex_facefuck_revisit_cumchoice")

label lbl_allaway_school_sex_facefuck_revisit_cumchoice:

    menu:
        "Cum inside mouth":
            jump lbl_allaway_school_sex_facefuck_revisit_cumin
        "Cum outside on face":
            jump lbl_allaway_school_sex_facefuck_revisit_cumout

label lbl_allaway_school_sex_facefuck_revisit_cumin:
    show bg schoolsexfacefuck_3
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
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

label lbl_allaway_school_sex_facefuck_revisit_cumout:
    show bg schoolsexfacefuck_12_0
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
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
