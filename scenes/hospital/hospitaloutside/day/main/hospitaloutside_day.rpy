###############
## Setup
## Story Path
label lbl_hospitaloutside_day_setup:

    ## MAIN STORY
    # ## Inquire Nurse Hollick About Erica
    # if main_story == 167:
    #     scene bg hospitaloutside_day
    #     with fade
    #     "Text Effie and Cole to talk to Erica?"
    #     menu:
    #         "Meet up together":
    #             jump lbl_inquire_nurse_hollick_about_erica
    #         "Nevermind":
    #             pass
    if violette_path == 8:
        pov "{i}Violette should be back at the beach now. I should check there first.{/i}"
    ## NO EVENT
    else:
        scene bg hospitaloutside_day
        pov "{i}I don't need to visit anyone here at the moment, hopefully I won't have to.{/i}"

    jump lbl_townmap_setup

###############
## Room Navigation
## This is the map for office outside during the day
#label lbl_hospitaloutside_day:
#    scene bg hospitaloutside_day
#    call screen scr_hospitaloutside_day
#
#screen scr_mall_day:
#    imagebutton auto "btn mall_night_icecreamstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_icecreamstore")
#    imagebutton auto "btn mall_night_retailstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_setup_1")
#
#    use hud_overlay

###############
## Labels
