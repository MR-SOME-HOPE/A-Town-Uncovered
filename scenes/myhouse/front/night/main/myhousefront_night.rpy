###############
## Setup
label lbl_myhousefront_night_setup:
    ## Help Build a Fort
    if sister_path == 10:
        pov "{i}[sister] is waiting for me in the basement.{/i}"

        jump lbl_mylivingroom_night_setup
    ## Sister 20Question
    elif sister_path == 16:
        pov "{i}I have to wait for [sister] in the basement.{/i}"

        jump lbl_mylivingroom_night_setup
    else:
        jump lbl_myhousefront_night

###############
## Room Navigation
label lbl_myhousefront_night:

    scene bg myhousefront_night
    call screen scr_myhousefront_night

screen scr_myhousefront_night():
    use hud_overlay
    imagebutton auto "btn myhousefront_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mylivingroom_night_setup")
    imagebutton auto "btn myhousefront_night_gate_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_night_setup")
    imagebutton auto "btn myhousefront_night_mailbox_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhouse_night_mailbox")

###############
## Labels
label lbl_myhouse_night_mailbox:
    pov "{i}I should check this tomorrow morning.{/i}"

    jump lbl_myhousefront_night
