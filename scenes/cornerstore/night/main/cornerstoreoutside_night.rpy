###############
## Setup
## Story Path
label lbl_cornerstoreoutside_night_setup:
    ## First Day of university
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Before Jacob Invites You to the Comic Book Store
    #elif main_story <= 17:
    #    pov "{i}I don't think I should go there, it looks like a dangerous area.{/i}"
    #    jump lbl_townmap_setup
    ## First Day in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## NO EVENTS
    else:
        jump lbl_cornerstoreoutside_night

###############
## Room Navigation
## This is the map for cornerstore oustide during the night
label lbl_cornerstoreoutside_night:
    scene bg cornerstoreoutside_night
    call screen scr_cornerstoreoutside_night

screen scr_cornerstoreoutside_night():
    imagebutton auto "btn cornerstoreoutside_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cornerstoreoutside_night_door")
    imagebutton auto "btn cornerstoreoutside_night_cafe_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeoutside_night_setup")

    use hud_overlay

###############
## Labels
## Conversations
label lbl_cornerstoreoutside_night_door:
    # show img inconstruction # Fixed
    with hpunch
    $ renpy.pause()

    jump lbl_cornerstoreoutside_night
