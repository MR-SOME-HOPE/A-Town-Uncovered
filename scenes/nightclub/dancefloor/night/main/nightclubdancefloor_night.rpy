###############
## Setup
## Story Path
label lbl_nightclubdancefloor_night_setup:
    ## NO EVENT
    jump lbl_nightclubdancefloor_night

###############
## Room Navigation
## This is the map for nightclub dance floor during the night.
label lbl_nightclubdancefloor_night:

    scene bg nightclubdancefloor_night
    call screen scr_nightclubdancefloor_night

screen scr_nightclubdancefloor_night():
    imagebutton auto "btn nightclubdancefloor_night_mainarea_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclub_night_setup")
    imagebutton auto "btn nightclubdancefloor_night_zariah_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclubdancefloor_night_zariah")
    use hud_overlay

###############
## Labels
label lbl_dancefloor_counter_check:
    if store_counter == 1:
        show counter dancefloor at right
        with dissolve
    else:
        pass
    return

label lbl_nightclubdancefloor_night_zariah:
    if zariah_path >= 1:
        pov "Hey, it's Zariah from uni!"
        pov "It's really loud so it's gonna be hard for us to talk properly."
        pov "Plus she's in the middle of a set."
        menu:
            "Talk":
                jump lbl_nightclubdancefloor_night_zariah_temp
            "Have fun":
                jump lbl_zariah_stage_reverse_cowgirl
            "Dance to the music":
                jump lbl_nightclub_night_dancefloor
            "Leave":
                jump lbl_nightclubdancefloor_night
    #else:
    #    pov "She seems really cool, wonder who she is."

    #jump lbl_nightclub_night_dancefloor

label lbl_nightclubdancefloor_night_zariah_temp:
    show pov neutral_talk at left
    show zar neutral at right
    call lbl_dancefloor_counter_check
    pov "Hey, Z!"
    show pov neutral at left
    show zar neutral_talk at right
    zar "Yo! What's up?"
    show pov neutral_talk at left
    show zar confused at right
    pov "Just wanted to talk to you."
    show pov confused at left
    show zar shocked_talk at right
    zar "Sorry, dude! I don't take requests!"
    show pov confused_talk at left
    show zar neutral at right
    pov "I'm not here for requests!"
    show pov confused at left
    show zar smirk_talk at right
    zar "Thanks, man! I appreciate my fans!"
    show pov confused_talk at left
    show zar smirk at right
    pov "What?"
    show pov bored at left
    show zar neutral_talk at right
    zar "Okay! Cool seeing you too, man!"
    show zar neutral at right
    pov "..."

    jump lbl_nightclubdancefloor_night


## Locations
