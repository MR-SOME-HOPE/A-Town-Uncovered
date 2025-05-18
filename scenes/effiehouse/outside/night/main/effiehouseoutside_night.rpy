###############
## Setup
## Story Path
label lbl_effiehouseoutside_night_setup:
    ## MAIN ###############################
    ## Beginning
    if main_story == 1:
        pov "{i}That is indeed a house, but not mine. From what I remember, my house has a red roof.{/i}"
        jump lbl_townmap_setup
    ## Before Meeting Effie
    elif main_story <= 10:
        scene bg effiehouseoutside_night
        pov "I don't know who lives here, I should go."
        jump lbl_townmap_setup
    ## Outside Effie's House
    elif main_story == 11:
        scene bg effiehouseoutside_night
        with fade
        jump lbl_outside_effies_house
    ## Outside Effie's House (Have Fun)
    elif main_story >= 14 and effie_funlater == 1:
        scene bg effiehouseoutside_night
        with fade
        jump lbl_outside_effies_house_again

    ## EFFIE ###############################
    ## Daddy Ain't Happy
    if effie_path == 13:
        jump lbl_daddy_aint_happy



    ## NO EVENT
    else:
        jump lbl_effiehouseoutside_night

###############
## Room Navigation
## This is the map for effie house outside during the day
label lbl_effiehouseoutside_night:

    scene bg effiehouseoutside_night
    call screen scr_effiehouseoutside_night

screen scr_effiehouseoutside_night():
    imagebutton auto "btn effiehouseoutside_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effiehouseoutside_night_door")
    use hud_overlay

###############
## Labels
## Locations
label lbl_effiehouseoutside_night_door:
    if gtime == 2:
        pov "{i}I shouldn't knock on her door at this hour.{/i}"
        "Knock anyway?"

        menu:
            "Yes":
                ## Effie Story Start
                if effie_path == 1 and main_story >= 14:
                    scene black with fade
                    $ renpy.pause()
                    "You and Effie spent the night together having some fun..."
                    jump lbl_a_hectic_wakeup_call
                ## Dateish Night
                if effie_path == 9:
                    jump lbl_dateish_night
                ## NO EVENT
                else:
                    jump lbl_throwaway_effiesdad_effiehouseoutside_night
            "No":
                jump lbl_effiehouseoutside_night_setup
    else:
        pov "{i}I really seriously should not knock on their door at this late-late hour.{/i}"

    jump lbl_effiehouseoutside_night
