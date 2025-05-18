###############
## Setup
## Story Path
label lbl_nightclub_night_setup:
    stop ambience fadeout 2.0
    play music 'audio/music/nightclub_music.ogg' fadein 2.0

    if zariah_path == 0:
        scene bg street_night
        show btn street_night_cole_idle
        pov "I don't know anybody that goes here. I'll leave it just now."
        pov "{i}That white-haired girl at school seems like someone who knows about this place.{/i}"
        jump lbl_street_night_setup
    ## Make sure Stamina doesn't go over 20
    if skill_chamax >= 20:
        $ skill_chamax = 20

    ## Underaged Drinking
    if sister_path == 19:
        jump lbl_underaged_drinking
    elif principallashley_path == 23 and day == 5:
        jump lbl_zariahs_party_pt1
    elif principallashley_path == 23.9:
        scene bg street_night
        pov "That's enough partying for one night."
        jump lbl_street_night_setup
    elif hitomi_path == 27:
        jump lbl_nightclub_hookups
    jump lbl_nightclub_night

###############
## Room Navigation
## This is the map for nightclub during the night.
label lbl_nightclub_night:

    scene bg nightclub_night
    call screen scr_nightclub_night

screen scr_nightclub_night():
    imagebutton auto "btn nightclub_night_dancefloor_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclubdancefloor_night_setup")
    imagebutton auto "btn nightclub_night_vip_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclub_night_vip")
    imagebutton auto "btn nightclub_night_bar_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclub_night_steve")
    imagebutton auto "btn nightclub_night_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_night_setup")
    use hud_overlay

###############
## Labels
## Locations
label lbl_nightclub_night_vip:
    show btn nightclub_night_bar_idle
    pov "{i}I can't go in there yet. I'm not a VIP.{/i}"

    jump lbl_nightclub_night_setup

label lbl_nightclub_counter_check:
    if store_counter == 1:
        show counter nightclub at right
        with dissolve
    else:
        pass
    return
