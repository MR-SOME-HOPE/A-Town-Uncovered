label lbl_momaftersunset_suck_revisit:
    $ vrheadset_revisitcounter = 0
    scene bg momaftersunset_suck_2
    with fade
    $ renpy.pause()
    show bg momaftersunset_suck_3
    mum "Enjoy it, [povname]. You deserve it."
    show bg momaftersunset_suck_6
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_4
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_5
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_6
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_4
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_5
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_6
    $ renpy.pause(0.3,hard=True)
    mum "Ahmm.. not too rough with the teeth, baby..."
    show bg momaftersunset_suck_7
    pov "Mhmm.."
    show bg momaftersunset_suck_8
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_9
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_8
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_9
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_8
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_9
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_10
    mum "I'll let you suck on them as much as you want, in exchange, we do this every single night."
    show bg momaftersunset_suck_11
    if winc == 0:
        mum "Remember, our time starts when the sun sets and the rest of the house sleeps."
    else:
        mum "Remember, our time starts when the sun sets and the rest of the family sleeps."

    jump lbl_momaftersunset_suck_revisit_0

label lbl_momaftersunset_suck_revisit_0:
    $ vrheadset_revisitcounter = 0
    jump lbl_momaftersunset_suck_revisit_1

label lbl_momaftersunset_suck_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_momaftersunset_suck_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_momaftersunset_suck_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_momaftersunset_suck_revisit
    else:
        jump lbl_momaftersunset_suck_revisit_1


label lbl_momaftersunset_suck_revisit_1: #Lick
    $ vrheadset_revisitcounter += 1
    show bg momaftersunset_suck_12
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_13
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_14
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_12
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_13
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_14
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_8
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_9
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_8
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_9
    $ renpy.pause(0.3,hard=True)

    jump lbl_momaftersunset_suck_revisit_counter



label lbl_momaftersunset_suck_revisit_2: #Tug
    $ vrheadset_revisitcounter += 1
    show bg momaftersunset_suck_6
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_4
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_5
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_6
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_4
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_5
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_6
    $ renpy.pause(0.3,hard=True)
    show bg momaftersunset_suck_15
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_16
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_17
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_15
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_16
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_17
    $ renpy.pause(0.50,hard=True)

    jump lbl_momaftersunset_suck_revisit_counter


label lbl_momaftersunset_suck_revisit_3: #Suck
    $ vrheadset_revisitcounter += 1
    show bg momaftersunset_suck_18
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_19
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_18
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_19
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_20
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_21
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_22
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_20
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_21
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_22
    $ renpy.pause(0.50,hard=True)

    jump lbl_momaftersunset_suck_revisit_counter

screen scr_momaftersunset_suck_revisit():
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momaftersunset_suck_revisit_7")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_momaftersunset_suck_revisit_0")

label lbl_momaftersunset_suck_revisit_7:
    show bg momaftersunset_suck_23
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_24
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_25
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_23
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_24
    $ renpy.pause(0.50,hard=True)
    show bg momaftersunset_suck_25
    $ renpy.pause(0.50,hard=True)
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
