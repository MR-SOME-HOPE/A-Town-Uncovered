###############
## Setup
## Story Path
label lbl_beachbehindrocks_night_setup:
    ## Knockout News
    if main_story == 108:
        jump lbl_knockout_news

    if violette_path == 4:
        jump lbl_beach_sparks_after_dark
    elif violette_path == 11:
        jump lbl_a_shared_dream
    elif violette_path == 14:
        jump lbl_violettes_punishment
        
    jump lbl_beachbehindrocks_night

###############
## Room Navigation
## This is the map for the beach behind the rocks during the night
label lbl_beachbehindrocks_night:

    scene bg beachbehindrocks_night
    call screen scr_beachbehindrocks_night

screen scr_beachbehindrocks_night():
    if gtime == 2 and edward_path != 0:
        imagebutton auto "btn beachbehindrocks_night_edward_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_night_edward")
    imagebutton auto "btn beachbehindrocks_night_rocks_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_night_setup")
    use hud_overlay

###############
## Label
label lbl_beachmain_night_edward:
    show btn beachbehindrocks_night_edward_idle
    $ renpy.pause(0.001)

    show pov confused_talk at left
    with dissolve
    hide btn beachbehindrocks_night_edward_idle
    show edw shocked at right
    with dissolve
    pov "Edward? What are you doing here."
    show pov confused at left
    show edw confused_talk at right
    edw "I could say the same thing for you."
    show edw neutral_talk at right
    edw "My radar is off the charts, there has been high amounts of ghost activity around here."
    show pov embarrassed at left
    show edw confused_talk at right
    edw "I'm just trying to figure out where it all leads too."

    jump lbl_beachbehindrocks_night
