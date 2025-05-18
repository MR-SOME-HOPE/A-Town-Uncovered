####################
## Desk Rimjob
label lbl_mom_bedroom_hscene_after_desk_rimjob:

    scene bg mombedroomhscene_desk_rimjob_1
    with dissolve
    mum "Oh... Mmm..."
    show bg mombedroomhscene_desk_rimjob_2
    mum "Eat me up, [povname].."

    jump lbl_mom_bedroom_hscene_after_desk_rimjob_0

label lbl_mom_bedroom_hscene_after_desk_rimjob_0:
    #$ mom_bedroom_hscene_desk_rimjob_counter = 0

    jump lbl_mom_bedroom_hscene_after_desk_rimjob_1

####################
## Desk Rimjob Stage 1
label lbl_mom_bedroom_hscene_after_desk_rimjob_1:
    scene img_mom_bedroom_hscene_after_desk_rimjob_stage_1
    #$ mom_bedroom_hscene_desk_rimjob_counter += 1
    #show bg mombedroomhscene_desk_rimjob_1
    #$ renpy.pause(0.4,hard=True)
    #show bg mombedroomhscene_desk_rimjob_2
    #$ renpy.pause(0.4,hard=True)
    #show bg mombedroomhscene_desk_rimjob_3
    #$ renpy.pause(0.4,hard=True)
    #if skill_sta <= 7 and mom_bedroom_hscene_desk_rimjob_counter == 6:
    #    jump lbl_mom_bedroom_hscene_after_desk_rimjob_next
    #elif skill_sta <= 14 and mom_bedroom_hscene_desk_rimjob_counter == 8:
    #    jump lbl_mom_bedroom_hscene_after_desk_rimjob_next
    #elif skill_sta <= 20 and mom_bedroom_hscene_desk_rimjob_counter == 10:
    #    jump lbl_mom_bedroom_hscene_after_desk_rimjob_next
    #else:
    #    jump lbl_mom_bedroom_hscene_after_desk_rimjob_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_rimjob_next
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_rimjob_next

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_rimjob_next

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_bedroom_hscene_after_desk_rimjob_1

image img_mom_bedroom_hscene_after_desk_rimjob_stage_1:
    "bg mombedroomhscene_desk_rimjob_1"
    pause 0.2
    "bg mombedroomhscene_desk_rimjob_2"
    pause 0.2
    "bg mombedroomhscene_desk_rimjob_3"
    pause 0.2
    repeat

####################
## Desk Rimjob Next
label lbl_mom_bedroom_hscene_after_desk_rimjob_next:

    #scene bg mombedroomhscene_desk_rimjob_1
    call screen scr_mom_bedroom_hscene_after_desk_rimjob_next

screen scr_mom_bedroom_hscene_after_desk_rimjob_next():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_scenechoice_desk_rimjob")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_bedroom_hscene_after_desk_rimjob_0")

####################
## Desk Rimjob Next 2
label lbl_mom_bedroom_hscene_after_desk_rimjob_next_2:
    stop sex_sounds
    scene bg mombedroomhscene_desk_1
    with dissolve
    if winc == 0:
        pov "Let's move to the bed, [missus]."
    else:
        pov "Let's move to the bed, Mom."

    jump lbl_mom_bedroom_hscene_after_mish
