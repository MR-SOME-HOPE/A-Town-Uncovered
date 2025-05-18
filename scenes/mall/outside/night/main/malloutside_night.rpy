###############
## Setup
## Story Path
label lbl_malloutside_night_setup:
    if main_story == 1:
        pov "{i}That's the mall. It's closed right now. From what I remember, my house has a red roof, that's where I should be heading.{/i}"
    else:
        scene bg malloutside_night
        pov "{i}The mall isn't open at night. I'll come back tomorrow.{/i}"

    jump lbl_townmap_setup

###############
## Room Navigation
## This is the map for mall during the night
#label lbl_mall_night:
#    scene bg mall_night
#    call screen scr_mall_night
#
#screen scr_mall_day:
#    imagebutton auto "btn mall_night_icecreamstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_icecreamstore")
#    imagebutton auto "btn mall_night_retailstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_setup_1")
#
#    use hud_overlay

###############
## Labels