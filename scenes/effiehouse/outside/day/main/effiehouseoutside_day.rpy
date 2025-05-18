###############
## Setup
## Story Path
label lbl_effiehouseoutside_day_setup:
    ## MAIN STORY ###############################
    ## Before Effie Invites You Over
    if main_story <= 10:
        scene bg effiehouseoutside_day
        pov "{i}I don't know who lives there yet.{/i}"
        jump lbl_townmap_setup
    ## Sex with Effie
    elif main_story == 11 or (main_story >= 14 and insexworld == 0 and effie_funlater == 1):
        scene bg effiehouseoutside_day
        "Would you like to wait for Effie?"
        menu:
            "Yes":
                if missallaway_path >= 24 and day == 5:
                    jump lbl_allawayxeffiexmc_effiebed
                else:
                    $ gtime = 2
                    jump lbl_effiehouseoutside_night_setup
            "No":
                jump lbl_effiehouseoutside_day
    ## After First Night with Effie
    elif main_story == 15:
        $ townmap_enabled = 1
    ## First Morning in the Sex World
    elif main_story <= 32 and insexworld == 1:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup

    ## No Event
    else:
        jump lbl_effiehouseoutside_day

###############
## Room Navigation
## This is the map for effie house outside during the day
label lbl_effiehouseoutside_day:
    scene bg effiehouseoutside_day
    call screen scr_effiehouseoutside_day

screen scr_effiehouseoutside_day():
    imagebutton auto "btn effiehouseoutside_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_effiehouseoutside_day_door")
    use hud_overlay

###############
## Labels
## Locations
label lbl_effiehouseoutside_day_door:

    ########## SISTER ###############################
    ## She's at my House
    if sister_path == 28:
        pov "{i}I should give her some space, it's still too early to check on her.{/i}"
        jump lbl_effiehouseoutside_day_setup
    ## How is Sister
    elif sister_path == 28.5:
        jump lbl_how_is_sister
    ## Effie is not at the Cafe
    elif 29 <= sister_path == 29.5:
        pov "{i}I should look into gathering the boxes to rebuild Twin Fortress version 2.0.{/i}"
        jump lbl_effiehouseoutside_day_setup
    ## Ask Sister Back Home
    elif sister_path == 30 and fursuitforboxjob_boxes >= 50:
        jump lbl_ask_sister_back_home

    ########### EFFIE ############################################
    ## Negotiation with Daddy
    elif effie_path == 15 and day == 0:
        jump lbl_negotiation_with_daddy
    ## Before The Beach Party
    elif effie_path == 16 and day == 4:
        jump lbl_before_the_beach_party

    ## No Side Story Event
    else:
        ## Morning
        if gtime == 0:
            if day <= 4:
                pov "{i}Effie's at university. I shouldn't knock on her door for no reason.{/i}"
                "Knock anyway?"
                menu:
                    "Yes":
                        "{i}*Knock knock*{/i}"
                        "..."
                        pov "{i}No one's home.{/i}"
                    "No":
                        pass
                jump lbl_effiehouseoutside_day_setup
            else:
                "Knock?"
                menu:
                    "Yes":
                        "{i}*Knock knock*{/i}"
                        if day != 5:
                            jump lbl_throwaway_effiesdad_effiehouseoutside_day
                        else:
                            jump lbl_effie_couch_on_phone_pre
                    "No":
                        jump lbl_effiehouseoutside_day_setup

        ## Afternoon
        elif gtime == 1:
            pov "{i}Effie's probably working at the Cafe.{/i}"
            "Knock anyway?"
            menu:
                "Yes":
                    if day <= 4:
                        "{i}*Knock knock*{/i}"
                        "..."
                        pov "{i}No one's home.{/i}"
                    else:
                        "{i}*Knock knock*{/i}"
                        jump lbl_throwaway_effiesdad_effiehouseoutside_day
                "No":
                    pass
            jump lbl_effiehouseoutside_day_setup
    jump lbl_effiehouseoutside_day_setup
