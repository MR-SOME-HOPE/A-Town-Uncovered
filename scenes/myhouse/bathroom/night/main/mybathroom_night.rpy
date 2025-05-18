###############
## Setup
## Story Path
label lbl_mybathroom_night_setup:

## Show my bathroom during the night.
    jump lbl_mybathroom_night

###############
## Room Navigation
## This is the map for my bedroom during the night with the door closed.

label lbl_mybathroom_night:

    scene bg mybathroom_night_open
    call screen scr_mybathroom_night

screen scr_mybathroom_night():
    imagebutton auto "btn mybathroom_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybathroom_night_dooropen")
    imagebutton auto "btn mybathroom_night_wall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_night_setup")
    if mum_path == 28 or sister_path == 10:
        pass
    else:
        use hud_overlay

## This is the map for my bedroom during the night with the door open
label lbl_mybathroom_night_1:

    scene bg mybathroom_night_open
    call screen scr_mybathroom_night_1

screen scr_mybathroom_night_1():
    imagebutton auto "btn mybathroom_night_wall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_night_setup")
    use hud_overlay

###############
## Labels
label lbl_mybathroom_night_dooropen:
    pov "{i}There seems to be no one here.{/i}"

    jump lbl_mybathroom_night_1
