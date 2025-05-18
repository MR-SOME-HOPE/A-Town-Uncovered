###############
## Setup
## Story Path
label lbl_street_night_setup:
    play music 'audio/music/nightclub_muffled_music.ogg' fadein 2.0

    ## Start of Game
    if main_story == 1:
        pov "{i}That street looks very shady and dangerous, I should just get home. From what I remember, my house has a red roof.{/i}"
        jump lbl_townmap_setup
    ## Before Jacob Invites You to the Comic Book Store
    elif main_story <= 19:
        pov "{i}I don't think I should go there, it looks like a dangerous area.{/i}"
        jump lbl_townmap_setup
    ## Green Eyed Jacob
    elif hitomi_path == 16.5:
        jump lbl_green_eyed_jacob
    ## No EVENT
    else:
        jump lbl_street_night

###############
## Room Navigation
## This is the map for street during the night
label lbl_street_night:

    scene bg street_night
    call screen scr_street_night

screen scr_street_night():
    imagebutton auto "btn street_night_comicbookstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_night_comicbookstore")
    imagebutton auto "btn street_night_alleyway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_streetalleyway_night_setup")
    imagebutton auto "btn street_night_adultstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_night_adultstore")
    imagebutton auto "btn street_night_club_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclub_night_setup")
    imagebutton auto "btn street_night_cole_%s" xpos 0 ypos 0 focus_mask True action If(cole_path > 0, Jump("lbl_street_night_cole"), Jump("lbl_street_night_not_met_cole"))
    imagebutton auto "btn street_night_abandonedlot_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_abandonedlot_night_setup")
    use hud_overlay

###############
## Labels

## Locations
label lbl_street_night_comicbookstore:
    show btn street_night_cole_idle
    pov "{i}This place is not open at the moment.{/i}"

    jump lbl_street_night

label lbl_street_night_adultstore:
    show btn street_night_cole_idle
    pov "{i}This place is not open at the moment.{/i}"

    jump lbl_street_night

label lbl_street_night_not_met_cole:
    show btn street_night_cole_idle
    pov "{i}I shouldn't bother people I don't know.{/i}"

    jump lbl_street_night
