###############
## Setup
## Story Path
label lbl_schoolyard_night_setup:
    ## INTRO
    if main_story == 1:
        pov "{i}Tomorrow's my first day of universty. I should get home and get some sleep. From what I remember, my house has a red roof.{/i}"
        jump lbl_townmap_setup
    ## Miss Allaway Watching Gym
    elif main_story >= 16 and missallaway_path == 0.5:
        jump lbl_miss_allaway_watching_gym
    ## Post Miss Allaway Watching Gym
    elif missallaway_path == 1.5:
        pov "{i}I'll come back tomorrow night, Miss Allaway might still be there lurking around.{/i}"
        jump lbl_townmap_setup
    ## Allaway Wants A Warrior
    elif missallaway_path == 11.5:
        jump lbl_allaway_want_a_warrior
    ## I Become The Warriror
    elif missallaway_path == 12.5:
        jump lbl_i_become_the_warrior
    ## NO EVENT
    else:
        jump lbl_schoolyard_night

###############
## Room Navigation
## This is the map for school yard during the night.
label lbl_schoolyard_night:

    scene bg schoolyard_night
    call screen scr_schoolyard_night

screen scr_schoolyard_night():
    imagebutton auto "btn schoolyard_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolyard_night_door")
    imagebutton auto "btn schoolyard_night_gym_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_schoolgym_night_setup")
    use hud_overlay

###############
## Labels
## Locations
label lbl_schoolyard_night_door:
    ## Drunk & Frisky
    if principallashley_path == 14:
        jump lbl_drunk_and_frisky
    ## Post Drunk & Frisky
    elif principallashley_path == 14.1:
        pov "{i}I should leave her alone and go home tonight.{/i}"
        jump lbl_schoolyard_night_setup
    ## NO EVENT
    else:
        pov "{i}The university isn't open at night.{/i}"
    jump lbl_schoolyard_night_setup
