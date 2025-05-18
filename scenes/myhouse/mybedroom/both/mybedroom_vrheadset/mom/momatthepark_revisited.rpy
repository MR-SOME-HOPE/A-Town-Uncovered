label lbl_mom_at_the_park_revisit_bj:
    $ vrheadset_revisitcounter = 0
    scene bg momattheparkbj_1
    with fade
    mum "You'll have to release it all in my mouth, we can't make a mess out here."
    mum "We also have to be quick in case someone {i}does{/i} come."
    show bg momattheparkbj_2
    pov "In case {i}I{/i} cum?"
    show bg momattheparkbj_3
    mum "Hush up."
    jump lbl_mom_at_the_park_revisit_bj_1

label lbl_mom_at_the_park_revisit_bj_0:
    $ vrheadset_revisitcounter = 0
    jump lbl_mom_at_the_park_revisit_bj_1

label lbl_mom_at_the_park_revisit_bj_1:
    $ vrheadset_revisitcounter += 1
    show bg momattheparkbj_4
    $ renpy.pause(0.3,hard=True)
    show bg momattheparkbj_5
    $ renpy.pause(0.1,hard=True)
    show bg momattheparkbj_6
    $ renpy.pause(0.1,hard=True)
    show bg momattheparkbj_7
    $ renpy.pause(0.2,hard=True)
    show bg momattheparkbj_8
    $ renpy.pause(0.2,hard=True)
    jump lbl_mom_at_the_park_revisit_bj_counter

label lbl_mom_at_the_park_revisit_bj_2:
    $ vrheadset_revisitcounter += 1
    show bg momattheparkbj_4
    $ renpy.pause(0.3,hard=True)
    show bg momattheparkbj_6
    $ renpy.pause(0.1,hard=True)
    show bg momattheparkbj_7
    $ renpy.pause(0.2,hard=True)
    show bg momattheparkbj_8
    $ renpy.pause(0.2,hard=True)
    jump lbl_mom_at_the_park_revisit_bj_counter

label lbl_mom_at_the_park_revisit_bj_3:
    $ vrheadset_revisitcounter += 1
    show bg momattheparkbj_4
    $ renpy.pause(0.2,hard=True)
    show bg momattheparkbj_6
    $ renpy.pause(0.1,hard=True)
    show bg momattheparkbj_8
    $ renpy.pause(0.2,hard=True)
    jump lbl_mom_at_the_park_revisit_bj_counter

label lbl_mom_at_the_park_revisit_bj_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_mom_at_the_park_revisit_bj_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_mom_at_the_park_revisit_bj_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_mom_at_the_park_bj_revist
    else:
        jump lbl_mom_at_the_park_revisit_bj_1

screen scr_mom_at_the_park_bj_revist():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_at_the_park_revisit_bj_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_at_the_park_revisit_bj_cumming")

label lbl_mom_at_the_park_revisit_bj_cumming:
    show bg momattheparkbj_4
    $ renpy.pause(0.3,hard=True)
    show bg momattheparkbj_6
    $ renpy.pause(0.1,hard=True)
    show bg momattheparkbj_7
    $ renpy.pause(2,hard=True)
    show bg momattheparkbj_9
    $ renpy.pause(1,hard=True)
    show bg momattheparkbj_10
    $ renpy.pause(1,hard=True)
    show bg momattheparkbj_11
    $ renpy.pause(1,hard=True)
    show bg momattheparkbj_12
    $ renpy.pause(1.5,hard=True)
    show bg momattheparkbj_13
    $ renpy.pause(1,hard=True)
    show bg momattheparkbj_14
    mum "You big baby. You nearly drowned me."
    if winc == 0:
        pov "Sorry, [missus]. Your mouth was asking for it."
    else:
        pov "Sorry, Mom. Your mouth was asking for it."
    show bg momattheparkbj_15
    mum "I know, I did this to myself..."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
