###############
## Setup
## Story Path
label lbl_officeoutside_day_setup:
    if main_story <= 5:
        pov "{i}I can't go there yet. I have to get to university.{/i}"
    elif main_story == 90:
        scene bg officeoutside_day
        if gtime == 1:
            jump lbl_prelude_of_the_first_day
        else:
            pov "{i}I need to be here in the afternoon, in order to be onboarded with the company.{/i}"
            jump lbl_officeoutside_day
    elif main_story > 90:
        jump lbl_officeoutside_day
    else:
        scene bg officeoutside_day
        pov "{i}I don't work here. Why am I here?{/i}"

    play music "<loop 1.777>audio/music/out_and_about.ogg"
    jump lbl_townmap_setup

###############
## Room Navigation
## This is the map for office outside during the day
label lbl_officeoutside_day:
    scene bg officeoutside_day

    call screen scr_officeoutside_day

screen scr_officeoutside_day():
    imagebutton auto "btn officeoutside_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officelobby_day_setup")

    use hud_overlay

###############
## Labels
