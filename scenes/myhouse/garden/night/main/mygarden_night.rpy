###############
## Setup
label lbl_mygarden_night_setup:
    jump lbl_mygarden_night

###############
## Room Navigation
label lbl_mygarden_night:
    if mowed_lawn:
        scene bg mygarden_night
    else:
        scene bg mygarden_night_grassy
    call screen scr_mygarden_night

screen scr_mygarden_night():
    use hud_overlay
    imagebutton auto "btn mygarden_night_dining_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mydiningroom_night_setup")
    imagebutton auto "btn mygarden_night_front_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhousefront_night_setup")
    if mowed_lawn:
        imagebutton auto "btn mygarden_night_shed_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_night_shed")
        imagebutton auto "btn mygarden_night_pond_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_night_pond")
    else:
        imagebutton auto "btn mygarden_night_grassy_shed_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mygarden_night_shed")

label lbl_mygarden_night_pond:
    pov "{i}It is a pond.{/i}"
    call screen scr_mygarden_night

label lbl_mygarden_night_shed:
    if mowed_lawn:
        pov "{i}It's locked.{/i}"
    else:
        pov "{i}The garden is too overgrown to get to.{/i}"
    call screen scr_mygarden_night
