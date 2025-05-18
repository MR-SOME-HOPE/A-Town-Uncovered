####################
## Desk Rimjob
label lbl_mom_bedroom_hscene_after_desk_rimjob_revist:
    $ vrheadset_revisitcounter = 0
    scene bg mombedroomhscene_desk_rimjob_1
    with dissolve
    mum "Oh... Mmm..."
    show bg mombedroomhscene_desk_rimjob_2
    mum "Eat me up, [povname].."

    jump lbl_mom_bedroom_hscene_after_desk_rimjob_revist_0

label lbl_mom_bedroom_hscene_after_desk_rimjob_revist_0:
    $ vrheadset_revistcounter = 0

    jump lbl_mom_bedroom_hscene_after_desk_rimjob_revist_1

####################
## Desk Rimjob Stage 1
label lbl_mom_bedroom_hscene_after_desk_rimjob_revist_1:
    $ vrheadset_revistcounter += 1
    show bg mombedroomhscene_desk_rimjob_1
    $ renpy.pause(0.4,hard=True)
    show bg mombedroomhscene_desk_rimjob_2
    $ renpy.pause(0.4,hard=True)
    show bg mombedroomhscene_desk_rimjob_3
    $ renpy.pause(0.4,hard=True)
    jump lbl_mom_bedroom_hscene_after_desk_rimjob_revist_counter

label lbl_mom_bedroom_hscene_after_desk_rimjob_revist_2:
    $ vrheadset_revistcounter += 1
    show bg mombedroomhscene_desk_rimjob_1
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_rimjob_2
    $ renpy.pause(0.3,hard=True)
    show bg mombedroomhscene_desk_rimjob_3
    $ renpy.pause(0.3,hard=True)
    jump lbl_mom_bedroom_hscene_after_desk_rimjob_revist_counter

label lbl_mom_bedroom_hscene_after_desk_rimjob_revist_3:
    $ vrheadset_revistcounter += 1
    show bg mombedroomhscene_desk_rimjob_1
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_desk_rimjob_2
    $ renpy.pause(0.2,hard=True)
    show bg mombedroomhscene_desk_rimjob_3
    $ renpy.pause(0.2,hard=True)
    jump lbl_mom_bedroom_hscene_after_desk_rimjob_revist_counter

label lbl_mom_bedroom_hscene_after_desk_rimjob_revist_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_mom_bedroom_hscene_after_desk_rimjob_revist_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_mom_bedroom_hscene_after_desk_rimjob_revist_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_mom_bedroom_hscene_after_desk_rimjob_revist
    else:
        jump lbl_mom_bedroom_hscene_after_desk_rimjob_revist_1


screen scr_mom_bedroom_hscene_after_desk_rimjob_revist():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_rimjob_revist_end")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_rimjob_revist_0")

####################
## Desk Rimjob Next 2
label lbl_mom_bedroom_hscene_after_desk_rimjob_revist_end:
    show bg mombedroomhscene_desk_1
    with dissolve
    if winc == 0:
        pov "Let's move to the bed, [missus]."
    else:
        pov "Let's move to the bed, Mom."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
