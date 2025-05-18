## DAY ##
label lbl_townmap_day_abandonedlot: ######################################
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    ## No Event
    else:
        jump lbl_abandonedlot_day_setup

label lbl_townmap_day_apartments:
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    ## NO EVENT
    else:
        jump lbl_apartmentsoutside_day_setup

label lbl_townmap_day_beach:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    $ beach_naked = 0
    $ beachchangeroom_visit = 0
    $ beachgloryhole_visit = 0

    jump lbl_beachmain_day_setup

label lbl_townmap_day_cafe:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking and bought_coffee_run_drinks:
        pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        jump lbl_townmap_setup
    jump lbl_cafeoutside_day_setup

label lbl_townmap_day_cinema:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_cinema_day_setup

label lbl_townmap_day_cornerstore:
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    ## Investigations
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking and bought_coffee_run_drinks:
        pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        jump lbl_townmap_setup
    ## NO EVENT
    else:
        jump lbl_cornerstoreoutside_day_setup

label lbl_townmap_day_effiehouse:
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_effiehouseoutside_day_setup

label lbl_townmap_day_hospital:
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_hospitaloutside_day_setup

label lbl_townmap_day_jacobhouse:
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_jacobhouseoutside_day_setup

label lbl_townmap_day_mall:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_mall_day_setup

label lbl_townmap_day_myhouse:
    if main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    call screen scr_townmap_day_myhouse_navigation

label lbl_townmap_day_neighbour1: ######################################
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    scene bg neighbour1front_day
    with fade
    pov "{i}Just my neighbours."
    # show img inconstruction # Fixed
    # with hpunch
    # $ renpy.pause()
    jump lbl_townmap_day

label lbl_townmap_day_neighbour2: ######################################
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    scene bg neighbour2front_day
    with fade
    pov "{i}Just my neighbours."
    # show img inconstruction # Fixed
    # with hpunch
    # $ renpy.pause()
    jump lbl_townmap_day

label lbl_townmap_day_office:
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking and not bought_coffee_run_drinks:
        pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_officeoutside_day_setup

label lbl_townmap_day_park:
    ## Naked Man of the Hour
    if main_story == 16:
        pov "{i}I don't think I'll find a job at the park. I could be wrong.{/i}"
        jump lbl_townmap_setup
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_park_day_setup

label lbl_townmap_day_policestation:
    ## In Trouble by Mom
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    ## Naked Man of the Hour
    elif main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_policestationoutside_day_setup

label lbl_townmap_day_school:
    if main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_schoolyard_day_setup

label lbl_townmap_day_street:
    ## Naked Man of the Hour
    if main_story == 41 and day <= 4:
        pov "{i}I should just head to university and face the music.{/i}"
        jump lbl_townmap_setup
    elif main_story == 84 and investigations_grundlesam == 0:
        pov "{i}I need to check out the mall before anywhere else.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_street_day_setup

label lbl_townmap_day_uptown:
    if main_story == 15:
        pov "{i}I should get home before I get into more trouble than I already am.{/i}"
        jump lbl_townmap_setup
    elif main_story in (97,101,102,103) and on_coffee_run_blocking:
        if bought_coffee_run_drinks:
            pov "{i}I have the coffees. I'd better get straight back to the office now.{/i}"
        else:
            pov "{i}I'd better get straight to the coffee shop and get back with the coffee as soon as possible.{/i}"
        jump lbl_townmap_setup
    jump lbl_uptownmap_setup

## My House Navigation Choice
screen scr_townmap_day_myhouse_navigation():

    ## In Trouble with Mom
    if main_story == 15:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## In Trouble with Mom
    elif 18 <= main_story <= 20:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## Found a Job
    elif main_story == 20:
        if nextday_ajob == 1:
            if gtime == 1:
                add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
                imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action  [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]
            else:
                imagebutton auto "btn townmap_day_myhousebedroom_%s" xpos 500 ypos 200 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"), Jump("lbl_mybedroom_day_setup")]
                imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]
        else:
            imagebutton auto "btn townmap_day_myhousebedroom_%s" xpos 500 ypos 200 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"), Jump("lbl_mybedroom_day_setup")]
            imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## The Town is Crazy
    elif main_story == 33.5:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## Something is Following You
    elif main_story == 45.5:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## Home Early
    elif main_story == 63.3:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## Girls' Upstairs
    elif main_story == 77:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## Investigations
    elif main_story == 84 and investigations_complete == 1:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    # ## Modern Day Parental Punishment
    # elif main_story == 141:
    #     add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
    #     imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## The Town is Crazy
    elif missallaway_path == 9:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## Meet Allaway For Sex in your Bedroom
    elif allawaybedroomsex_sneakherin == 1:
        add "btn townmap_day_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]

    ## Take Hitomi to your Bedoom for modeling
    elif hitomi_path == 11:
        imagebutton auto "btn townmap_day_myhousebedroom_%s" xpos 500 ypos 200 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"), Jump("lbl_mybedroom_day_setup")]
        add "btn townmap_day_myhousefrontyard_disabled" xpos 500 ypos 600

    ## Normal
    else:
        imagebutton auto "btn townmap_day_myhousebedroom_%s" xpos 500 ypos 200 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"), Jump("lbl_mybedroom_day_setup")]
        imagebutton auto "btn townmap_day_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action [Play("music", "audio/music/a_family_home.ogg"),Jump("lbl_myhousefront_day_setup")]
    use hud_overlay
