## NIGHT ##
label lbl_uptownmap_night_church: ######################################
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    ## Funky Teas  - moved trigger to church interior
    #elif principallashley_path == 17:
    #    jump lbl_funky_teas
    ## Post-Funky Teas
    elif principallashley_path == 17.5:
        pov "{i}I should just head home. Tonight's been really weird.{/i}"
        jump lbl_uptownmap_setup
    ## NO EVENT
    else:
        jump lbl_churchoutside_night_setup

label lbl_uptownmap_night_cliff:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    else:
        jump lbl_cliff_night_setup

label lbl_uptownmap_night_forest:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    ## NO EVENT
    else:
        jump lbl_forest_night_setup

label lbl_uptownmap_night_graveyard: ######################################
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    scene bg graveyard_night ###
    with fade
    # show img inconstruction # Fixed
    with hpunch
    $ renpy.pause()
    jump lbl_uptownmap_night

label lbl_uptownmap_night_lashleymanor: ######################################
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup

    jump lbl_lashleymanorfront_night

label lbl_uptownmap_night_mayorsestate: ######################################
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup

    jump lbl_mayorsestatefront_night_setup

label lbl_uptownmap_night_mineentrance:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    ## NO EVENT
    else:
        jump lbl_mineentrance_night_setup

label lbl_uptownmap_night_motel: ######################################
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup

    jump lbl_motelfront_night_setup

label lbl_uptownmap_night_restaurant:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    ## NO EVENT
    else:
        jump lbl_restaurant_night_setup

label lbl_uptownmap_night_townhouses: ######################################
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    scene bg townhousefront_night ###
    with fade
    pov "{i}Just some townhouses.{/i}"
    # show img inconstruction
    # with hpunch
    # $ renpy.pause()
    jump lbl_uptownmap_night

label lbl_uptownmap_night_trainstation: ######################################
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    else:
        pov "{i}Don't need to go anywhere.{/i}"
    # show img inconstruction
    # with hpunch
    # $ renpy.pause()
    jump lbl_uptownmap_night

label lbl_uptownmap_night_downtown:
    jump lbl_townmap_setup
