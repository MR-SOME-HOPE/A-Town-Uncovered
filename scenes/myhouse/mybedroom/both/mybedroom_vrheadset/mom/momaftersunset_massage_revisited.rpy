label lbl_momaftersunset_massage_revisit:
    $ vrheadset_revisitcounter = 0
    show bg momaftersunset_63
    pov "It'll be my pleasure."
    show bg momaftersunset_massage_1
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_2
    mum "I'm ready, baby."
    show bg momaftersunset_massage_3
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_4
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_5
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_3
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_4
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_5
    $ renpy.pause(1,hard=True)
    show bg momaftersunset_massage_6
    mum "Mmm... yeah, like that, baby."
    show bg momaftersunset_massage_7
    mum "Do they feel good?"
    show bg momaftersunset_massage_5
    pov "They feel amazing..."
    show bg momaftersunset_massage_6
    mum "I'll let you play with them as much as you want..."
    show bg momaftersunset_massage_7
    mum "In exchange, we do this every single night."
    show bg momaftersunset_massage_8
    if winc == 0:
        mum "Remember, our time starts when the sun sets and the rest of the house sleeps."
    else:
        mum "Remember, our time starts when the sun sets and the rest of the family sleeps."

    jump lbl_momaftersunset_massage_revisit_1

label lbl_momaftersunset_massage_revisit_0:
    $ vrheadset_revisitcounter = 0
    jump lbl_momaftersunset_massage_revisit_1

label lbl_momaftersunset_massage_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg momaftersunset_massage_3
    $ renpy.pause(0.333,hard=True)
    show bg momaftersunset_massage_4
    $ renpy.pause(0.333,hard=True)
    show bg momaftersunset_massage_5
    $ renpy.pause(0.333,hard=True)

    jump lbl_momaftersunset_massage_revisit_counter

label lbl_momaftersunset_massage_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg momaftersunset_massage_9
    $ renpy.pause(0.266,hard=True)
    show bg momaftersunset_massage_10
    $ renpy.pause(0.266,hard=True)
    show bg momaftersunset_massage_11
    $ renpy.pause(0.266,hard=True)

    jump lbl_momaftersunset_massage_revisit_counter

label lbl_momaftersunset_massage_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg momaftersunset_massage_12
    $ renpy.pause(0.2,hard=True)
    show bg momaftersunset_massage_13
    $ renpy.pause(0.2,hard=True)
    show bg momaftersunset_massage_14
    $ renpy.pause(0.2,hard=True)

    jump lbl_momaftersunset_massage_revisit_counter

label lbl_momaftersunset_massage_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_momaftersunset_massage_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_momaftersunset_massage_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_momaftersunset_massage_revisit
    else:
        jump lbl_momaftersunset_massage_revisit_1

label lbl_momaftersunset_massage_revisit_end:


screen scr_momaftersunset_massage_revisit():
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momaftersunset_massage_revisit_4")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momaftersunset_massage_revisit_0")

label lbl_momaftersunset_massage_revisit_4:
    show bg momaftersunset_massage_15
    $ renpy.pause(0.333,hard=True)
    show bg momaftersunset_massage_16
    $ renpy.pause(0.333,hard=True)
    show bg momaftersunset_massage_17
    $ renpy.pause(0.333,hard=True)
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
