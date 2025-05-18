## DAY ##
label lbl_uptownmap_day_church:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    ## Funky Teas SETUP - moved trigger to church interior
    #elif principallashley_path == 17:
    #    pov "{i}It's too early to go there. I should come back at night.{/i}"
    #    jump lbl_uptownmap_setup
    ## NO EVENT
    else:
        jump lbl_churchoutside_day_setup

label lbl_uptownmap_day_cliff:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    else:
        jump lbl_cliff_day_setup

label lbl_uptownmap_day_forest:
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
        jump lbl_forest_day_setup

label lbl_uptownmap_day_graveyard:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    scene bg graveyard_day ###
    with fade
    # show img inconstruction # Fixed
    with hpunch
    $ renpy.pause()
    jump lbl_uptownmap_day

label lbl_uptownmap_day_lashleymanor:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup

    jump lbl_lashleymanorfront_day_setup

label lbl_uptownmap_day_mayorsestate:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup

    jump lbl_mayorsestatefront_day_setup

label lbl_uptownmap_day_mineentrance:
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
        jump lbl_mineentrance_day_setup

label lbl_uptownmap_day_motel: ######################################
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup

    jump lbl_motelfront_day_setup

label lbl_uptownmap_day_restaurant:
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
        jump lbl_restaurant_day_setup

label lbl_uptownmap_day_townhouses:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_uptownmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_uptownmap_setup
    scene bg townhousefront_day
    with fade
    pov "{i}These are some nice town houses. No one I know lives here though.{/i}"
    jump lbl_uptownmap_day

label lbl_uptownmap_day_trainstation:
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
        jump lbl_trainstation_day_setup

label lbl_uptownmap_day_downtown:
    jump lbl_townmap_setup
