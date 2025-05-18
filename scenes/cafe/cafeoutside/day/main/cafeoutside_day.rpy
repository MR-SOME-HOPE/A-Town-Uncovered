###############
## Setup
## Story Path
label lbl_cafeoutside_day_setup:
    ## First Day of School
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## Milkshake for Two
    elif main_story == 10:
        jump lbl_effie_date
    ## In Trouble By Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_allaway == 0:
        jump lbl_investigations_allaway
    ## School in Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## Nothing
    else:
        jump lbl_cafeoutside_day

###############
## Room Navigation
## This is the map for cafe outside during the day
label lbl_cafeoutside_day:

    scene bg cafeoutside_day
    call screen scr_cafeoutside_day

screen scr_cafeoutside_day():
    imagebutton auto "btn cafeoutside_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeinside_day_setup")
    if missallaway_path == 7:
        pass
    elif missallaway_path >= 8 and day >= 5:
        imagebutton auto "btn cafeoutside_day_missallaway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeoutside_day_missallaway")
    elif main_story == 84:
        imagebutton auto "btn cafeoutside_day_missallaway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cafeoutside_day_missallaway")

    # imagebutton auto "btn cafeoutside_day_cornerstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_cornerstoreoutside_day_setup")

    use hud_overlay

###############
## Labels
