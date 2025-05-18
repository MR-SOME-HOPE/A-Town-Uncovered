## Mom in my Bed ##
label lbl_mom_in_my_bed_revist:
    scene black
    with fade
    scene bg strippingformom_1
    with fade
    $ renpy.pause()
    show bg strippingformom_2
    $ renpy.pause()
    show bg strippingformom_3
    $ renpy.pause()
    scene bg strippingformom_4
    with fade
    $ renpy.pause()
    show bg strippingformom_5
    $ renpy.pause()
    show bg strippingformom_6
    $ renpy.pause()
    $ vrheadset_revistcounter = 0
    if winc == 0:
        jump lbl_mom_in_my_bed_revist_2_winc0
    else:
        jump lbl_mom_in_my_bed_revist_2

label lbl_mom_in_my_bed_revist_0:
    $ vrheadset_revistcounter = 0
    jump lbl_mom_in_my_bed_revist_3


label lbl_mom_in_my_bed_revist_2:
    scene black
    with fade
    scene bg mominmybed_1
    with fade
    $ renpy.pause()
    show bg mominmybed_2
    with dissolve
    mum "Goodnight, [povname]..."
    show bg mominmybed_3
    pov "Goodnight.. Mom.."
    show bg mominmybed_4
    mum "Hmm? What's wrong?"
    show bg mominmybed_5
    pov "Hm? Nothing."
    show bg mominmybed_6
    mum "No, tell me. We can still talk if you want."
    show bg mominmybed_7
    mum "We can gossip and braid each other's hair."
    mum "Hehehe."
    show bg mominmybed_8
    pov "..."
    show bg mominmybed_9
    mum "Naww, c'mon, sweetie. I'm just trying to lighten the mood. I can feel you're a little... tense.."
    show bg mominmybed_10
    mum "That's it, isn't it?"
    show bg mominmybed_11
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_12
    mum "My baby's a little tense?"
    show bg mominmybed_13
    mum "Oh... wow... you have a lot of girth on this thing..."
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_16
    mum "Do me a favour and avoid making a mess tonight. Washing day isn't until next week."
    show bg mominmybed_17
    pov "...I- I'll try."

    jump lbl_mom_in_my_bed_revist_3

label lbl_mom_in_my_bed_revist_3:
    $ vrheadset_revistcounter += 1
    show bg mominmybed_18
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_19
    $ renpy.pause(0.5, hard=True)

    jump lbl_mom_in_my_bed_revist_counter

label lbl_mom_in_my_bed_revist_3_2:
    $ vrheadset_revistcounter += 1
    show bg mominmybed_18
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_19
    $ renpy.pause(0.3, hard=True)

    jump lbl_mom_in_my_bed_revist_counter

label lbl_mom_in_my_bed_revist_3_3:
    $ vrheadset_revistcounter += 1
    show bg mominmybed_18
    $ renpy.pause(0.2, hard=True)
    show bg mominmybed_19
    $ renpy.pause(0.2, hard=True)

    jump lbl_mom_in_my_bed_revist_counter

label lbl_mom_in_my_bed_revist_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_mom_in_my_bed_revist_3_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_mom_in_my_bed_revist_3_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_mom_bedroom_hscene_after_mishanal_revisit
    else:
        jump lbl_mom_in_my_bed_revist_3

screen scr_mom_in_my_bed_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_in_my_bed_revist_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_in_my_bed_revist_cumcheck")

label lbl_mom_in_my_bed_revist_cumcheck:
    if winc == 0:
        jump lbl_mom_in_my_bed_revist_cumshot_winc0
    else:
        jump lbl_mom_in_my_bed_revist_cumshot

label lbl_mom_in_my_bed_revist_cumshot:
    show bg mominmybed_20
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_21
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_22
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_23
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_24
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_25
    $ renpy.pause()
    show bg mominmybed_26
    mum "You're an idiot."
    show bg mominmybed_27
    pov "Screw you, Mom... you're such a tease."
    show bg mominmybed_28
    mum "Hehehe."
    show bg mominmybed_29
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_28
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_29
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_28
    $ renpy.pause(0.5, hard=True)
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection



label lbl_mom_in_my_bed_revist_2_winc0:

    scene black
    with fade
    scene bg mominmybed_1
    with fade
    $ renpy.pause()
    show bg mominmybed_2
    with dissolve
    $ vrheadset_revistcounter = 0
    mum "Goodnight, [povname]..."
    show bg mominmybed_3
    pov "Goodnight.. [missus].."
    show bg mominmybed_4
    mum "Hmm? What's wrong?"
    show bg mominmybed_5
    pov "Hm? Nothing."
    show bg mominmybed_6
    mum "No, tell me. We can still talk if you want."
    show bg mominmybed_7
    mum "We can gossip and braid each other's hair."
    mum "Hehehe."
    show bg mominmybed_8
    pov "..."
    show bg mominmybed_9
    mum "Naww, c'mon, sweetie. I'm just trying to lighten the mood. I can feel you're a little... tense.."
    show bg mominmybed_10
    mum "That's it, isn't it?"
    show bg mominmybed_11
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_12
    mum "My baby's a little tense?"
    show bg mominmybed_13
    mum "Oh... wow... you have a lot of girth on this thing..."
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_14
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_15
    $ renpy.pause(0.8, hard=True)
    show bg mominmybed_16
    mum "Do me a favour and avoid making a mess tonight. Washing day isn't until next week."
    show bg mominmybed_17
    pov "...I- I'll try."
    jump lbl_mom_in_my_bed_revist_3

label lbl_mom_in_my_bed_revist_cumshot_winc0:
    show bg mominmybed_20
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_21
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_22
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_23
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_24
    $ renpy.pause(0.3, hard=True)
    show bg mominmybed_25
    $ renpy.pause()
    show bg mominmybed_26
    mum "You're an idiot."
    show bg mominmybed_27
    pov "Screw you, [missus]... you're such a tease."
    show bg mominmybed_28
    mum "Hehehe."
    show bg mominmybed_29
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_28
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_29
    $ renpy.pause(0.5, hard=True)
    show bg mominmybed_28
    $ renpy.pause(0.5, hard=True)
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
