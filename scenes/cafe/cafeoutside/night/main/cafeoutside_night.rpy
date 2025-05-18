###############
## Setup
## Story Path
label lbl_cafeoutside_night_setup:
    if main_story == 1:
        pov "{i}That's the local cafe. I doubt they're open at this hour. From what I remember, my house has a red roof, that's where I should be heading.{/i}"

        jump lbl_townmap_setup
    else:
        jump lbl_cafeoutside_night

###############
## Room Navigation
## This is the map for cafe outside during the night.
label lbl_cafeoutside_night:

    scene bg cafeoutside_night
    call screen scr_cafeoutside_night

screen scr_cafeoutside_night():
    imagebutton auto "btn cafeoutside_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeoutside_night_door")
    # imagebutton auto "btn cafeoutside_night_cornerstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cornerstoreoutside_night_setup")

    use hud_overlay

###############
## Labels
## Locations
label lbl_cafeoutside_night_door:
    pov "{i}The cafe isn't open at night... yet... maybe. I don't know the timetable yet.{/i}"

    jump lbl_cafeoutside_night_setup
