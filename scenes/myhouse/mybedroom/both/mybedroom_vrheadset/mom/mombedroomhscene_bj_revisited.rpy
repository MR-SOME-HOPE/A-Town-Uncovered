####################
## BJ
label lbl_mom_bedroom_hscene_after_bj_revisit:
    $ vrheadset_revisitcounter = 0
    scene bg mombedroomhscene_bj_24
    with fade
    mum "Hard already?"
    show bg mombedroomhscene_bj_25
    pov "It's been this way ever since we got home."
    show bg mombedroomhscene_bj_24
    mum "Couldn't wait, could you?"
    show bg mombedroomhscene_bj_26
    pov "To be honest with you..."
    show bg mombedroomhscene_bj_1
    pov "{i}*Inhale*{/i} I was wondering if we would end up doing this."

    jump lbl_mom_bedroom_hscene_after_bj_revisit_0

label lbl_mom_bedroom_hscene_after_bj_revisit_0:
    $ vrheadset_revisitcounter = 0
    jump lbl_mom_bedroom_hscene_after_bj_revisit_1

####################
## BJ Stage 1
label lbl_mom_bedroom_hscene_after_bj_revisit_1:
    $ vrheadset_revisitcounter += 1
    show bg mombedroomhscene_bj_1
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_bj_2
    $ renpy.pause(0.1,hard=True)
    show bg mombedroomhscene_bj_3
    $ renpy.pause(0.1,hard=True)
    show bg mombedroomhscene_bj_4
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_bj_5
    $ renpy.pause(0.3,hard=True)
    jump lbl_mom_bedroom_hscene_after_bj_revisit_counter


####################
## BJ Stage 2
label lbl_mom_bedroom_hscene_after_bj_revisit_2:
    $ vrheadset_revisitcounter += 1
    show bg mombedroomhscene_bj_1
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_bj_3
    $ renpy.pause(0.1,hard=True)
    show bg mombedroomhscene_bj_4
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_5
    $ renpy.pause(0.2,hard=True)
    jump lbl_mom_bedroom_hscene_after_bj_revisit_counter


####################
## BJ Stage 3
label lbl_mom_bedroom_hscene_after_bj_revisit_3:
    $ vrheadset_revisitcounter += 1
    show bg mombedroomhscene_bj_1
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_3
    $ renpy.pause(0.1,hard=True)
    show bg mombedroomhscene_bj_5
    $ renpy.pause(0.2,hard=True)
    jump lbl_mom_bedroom_hscene_after_bj_revisit_counter

label lbl_mom_bedroom_hscene_after_bj_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_mom_bedroom_hscene_after_bj_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_mom_bedroom_hscene_after_bj_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_mom_bedroom_hscene_after_bj_cum_revisit
    else:
        jump lbl_mom_bedroom_hscene_after_bj_revisit_1



screen scr_mom_bedroom_hscene_after_bj_cum_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_bj_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_bj_revisit_cumchoice")


label lbl_mom_bedroom_hscene_after_bj_revisit_cumchoice:

    menu:
        "Cum inside mouth":
            jump lbl_mom_bedroom_hscene_after_bj_revisit_cumin
        "Cum outside on face":
            jump lbl_mom_bedroom_hscene_after_bj_revisit_cumout

####################
## BJ Cum in
label lbl_mom_bedroom_hscene_after_bj_revisit_cumin:
    show bg mombedroomhscene_bj_2
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_bj_3
    $ renpy.pause(1,hard=True)
    show bg mombedroomhscene_bj_6
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_7
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_8
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_9
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_10
    $ renpy.pause()
    show bg mombedroomhscene_bj_11
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_12
    $ renpy.pause(0.5,hard=True)
    show bg mombedroomhscene_bj_13
    mum "Wow.. you nearly drowned me, honey."
    show bg mombedroomhscene_bj_14
    if winc == 0:
        pov "Sorry, [missus]. I can't help it."
    else:
        pov "Sorry, Mom. I can't help it."
    show bg mombedroomhscene_bj_13
    mum "Never be sorry, you're a godsend."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection

####################
## BJ Cum Out
label lbl_mom_bedroom_hscene_after_bj_revisit_cumout:
    show bg mombedroomhscene_bj_15
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_16
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_17
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_18
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_19
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_20
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_bj_21
    $ renpy.pause()
    show bg mombedroomhscene_bj_22
    mum "Damnit, honey. I can't breath through my nose!"
    show bg mombedroomhscene_bj_23
    if winc == 0:
        pov "Sorry, [missus]. I can't help it."
    else:
        pov "Sorry, Mom. I can't help it."
    pov "You look great though."
    show bg mombedroomhscene_bj_22
    mum "Very funny, [povname]."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
