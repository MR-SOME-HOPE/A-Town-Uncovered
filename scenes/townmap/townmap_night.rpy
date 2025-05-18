## NIGHT ##
label lbl_townmap_night_abandonedlot:
    jump lbl_abandonedlot_night_setup

label lbl_townmap_night_apartments:
    jump lbl_apartmentsoutside_night_setup

label lbl_townmap_night_beach:
    $ beach_naked = 0
    $ beachchangeroom_fishbite = 0

    jump lbl_beachmain_night_setup

label lbl_townmap_night_cafe:
    jump lbl_cafeoutside_night_setup

label lbl_townmap_night_cinema:
    jump lbl_cinema_night_setup

label lbl_townmap_night_cornerstore:
    jump lbl_cornerstoreoutside_night_setup

label lbl_townmap_night_effiehouse:
    jump lbl_effiehouseoutside_night_setup

label lbl_townmap_night_hospital:
    jump lbl_hospitaloutside_night_setup

label lbl_townmap_night_jacobhouse:
    jump lbl_jacobhouseoutside_night_setup

label lbl_townmap_night_mall:
    jump lbl_malloutside_night_setup

label lbl_townmap_night_myhouse:
    call screen scr_townmap_night_myhouse_navigation

label lbl_townmap_night_neighbour1: ######################################
    scene bg neighbour1front_night
    with fade
    pov "{i}Just my neighbours."
    # show img inconstruction # Fixed
    # with hpunch
    # $ renpy.pause()
    jump lbl_townmap_night

label lbl_townmap_night_neighbour2: ######################################
    scene bg neighbour2front_night
    with fade
    pov "{i}Just my neighbours."
    # show img inconstruction # Fixed
    # with hpunch
    # $ renpy.pause()
    jump lbl_townmap_night

label lbl_townmap_night_office:
    jump lbl_officeoutside_night_setup

label lbl_townmap_night_park:
    if main_story == 1:
        pov "{i}I just came from the park, I don't want to go back there, at least not tonight. From what I remember, my house has a red roof, that's where I should be heading.{/i}"

        jump lbl_townmap_setup
    else:
        jump lbl_park_night_setup

label lbl_townmap_night_policestation:
    jump lbl_policestationoutside_night_setup

label lbl_townmap_night_school:
    jump lbl_schoolyard_night_setup

label lbl_townmap_night_street:
    jump lbl_street_night_setup

label lbl_townmap_night_uptown:
    if main_story == 1:
        pov "{i}This really isn't the time to be exploring uptown. From what I remember, my house has a red roof. I should be getting back.{/i}"
        jump lbl_townmap_setup

    jump lbl_uptownmap_setup

## My House Navigation Choice
screen scr_townmap_night_myhouse_navigation():
    if mum_path == 19:
        add "btn townmap_night_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_night_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action Jump("lbl_myhousefront_night_setup")
    elif mum_path == 7:
        imagebutton auto "btn townmap_night_myhousebedroom_%s" xpos 500 ypos 200 focus_mask True action Jump("lbl_mybedroom_night_setup")
        add "btn townmap_night_myhousefrontyard_disabled" xpos 500 ypos 600
    elif sister_path == 36.1:
        add "btn townmap_night_myhousebedroom_disabled" xpos 500 ypos 200
        imagebutton auto "btn townmap_night_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action Jump("lbl_myhousefront_night_setup")
    else:
        imagebutton auto "btn townmap_night_myhousebedroom_%s" xpos 500 ypos 200 focus_mask True action Jump("lbl_mybedroom_night_setup")
        imagebutton auto "btn townmap_night_myhousefrontyard_%s" xpos 500 ypos 600 focus_mask True action Jump("lbl_myhousefront_night_setup")
    use hud_overlay
