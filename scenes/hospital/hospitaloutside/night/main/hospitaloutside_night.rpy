###############
## Setup
## Story Path
label lbl_hospitaloutside_night_setup:
    if main_story == 1:
        pov "{i}That's the hospital, hopefully I don't need to go there anytime soon. From what I remember, my house has a red roof.{/i}"
    elif violette_path == 7.9:
        pov "{i}I should let Violette get some rest tonight.{/i}"
    else:
        scene bg hospitaloutside_night
        pov "{i}I don't need to visit anyone here at the moment, hopefully I won't have to.{/i}"

    jump lbl_townmap_setup

###############
## Room Navigation
## This is the map for office outside during the night
#label lbl_hospitaloutside_night:
#    scene bg hospitaloutside_night
#    call screen scr_hospitaloutside_night
#
#screen scr_mall_day:
#    imagebutton auto "btn mall_night_icecreamstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_icecreamstore")
#    imagebutton auto "btn mall_night_retailstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_setup_1")
#
#    use hud_overlay

###############
## Labels
