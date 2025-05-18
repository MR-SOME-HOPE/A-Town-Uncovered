###############
## Setup
## Story Path
label lbl_street_day_setup:
    ## First Day of university
    if main_story <= 5:
        pov "{i}I can't go there yet, I have to get to university.{/i}"
        jump lbl_townmap_setup
    ## In Trouble by Mom
    elif main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Before Jacob Invites You to the Comic Book Store
    elif main_story <= 17:
        pov "{i}I don't think I should go there, it looks like a dangerous area.{/i}"
        jump lbl_townmap_setup
    ## First Day in the Sex World
    elif insexworld == 1 and main_story <= 32:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## Sex Around Town
    elif insexworld == 1 and main_story == 33:
        if sexaroundtownstreet == 0:
            scene bg street_daysexworld
            show btn street_day_jack_idle
            with fade
            jump lbl_sex_around_town_street
        else:
            scene bg street_daysexworld
            jump lbl_street_day
    ## NOT IN SEX WORLD
    if insexworld == 0:
        ## Sister in the Streets
        if sister_path == 17 and ((gtime == 0 and day in (0,3)) or (gtime == 1 and day == 4)):
            jump lbl_sister_in_the_streets
        elif hitomi_path == 13.5:
            jump lbl_modelling_requests_part1
        ## NO EVENTS
        else:
            jump lbl_street_day
    ## NO EVENTS
    else:
        jump lbl_street_day

###############
## Room Navigation
## This is the map for street during the day
label lbl_street_day:
    if main_story == 33:
        scene bg street_daysexworld
    else:
        scene bg street_day
    call screen scr_street_day

screen scr_street_day():
    imagebutton auto "btn street_day_comicbookstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_comicbookstore_day_setup")
    imagebutton auto "btn street_day_alleyway_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_streetalleyway_day_setup")
    imagebutton auto "btn street_day_adultstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_adultstore_day_setup")
    imagebutton auto "btn street_day_club_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_day_club")
    imagebutton auto "btn street_day_abandonedlot_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_abandonedlot_day_setup")

    ## Beat the Shit Out of Jack
    if missallaway_path == 19:
        pass

    ## Normal
    else:
        imagebutton auto "btn street_day_jack_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_street_day_jack")
    use hud_overlay

###############
## Labels
## Conversations
label lbl_sex_around_town_street:
    pov "{i}That... is a hobo with his dick stuck in a bottle.{/i}"
    pov "{i}Nothing unusual there.{/i}"
    $ sexaroundtownstreet += 1

    jump lbl_street_day

## Locations
label lbl_street_day_club:
    if not missallaway_path == 19:
        show btn street_day_jack_idle

    pov "{i}This place is not open during the day.{/i}"

    if principallashley_path == 23 and day == 5:
        pov "{i}I need to come back tonight for Zariah's party.{/i}"

    jump lbl_street_day
