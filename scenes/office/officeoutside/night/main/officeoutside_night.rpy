###############
## Setup
## Story Path
label lbl_officeoutside_night_setup:
    if main_story == 1:
        pov "{i}That's an office building. From what I remember, my house has a red roof, that's where I should be heading.{/i}"
    elif main_story >= 90:
        scene bg officeoutside_night
        if main_story == 90:
            pov "{i}I need to be here in the afternoon, in order to be onboarded with the company.{/i}"
        jump lbl_officeoutside_night
    else:
        scene bg officeoutside_night
        pov "{i}The office isn't open at night. Even so, I don't even work here.{/i}"

    play music "<loop 1.777>audio/music/out_and_about.ogg"
    jump lbl_townmap_setup

###############
## Room Navigation
## This is the map for office outside during the night
label lbl_officeoutside_night:
    scene bg officeoutside_night
    call screen scr_officeoutside_night

screen scr_officeoutside_night():
    imagebutton auto "btn officeoutside_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_officelobby_night_setup")

    use hud_overlay

###############
## Labels
