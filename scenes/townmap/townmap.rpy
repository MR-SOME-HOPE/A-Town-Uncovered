###############
## TOWN MAP ##
## Time Decider
label lbl_townmap_setup:
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    $ renpy.music.set_volume(0.4, delay=0, channel='ambience')
    play sound "audio/sfx/mapopen.mp3"
    call lbl_in_sex_world
    if main_story == 33:
        if (sexaroundtowncafe and sexaroundtownbeach and sexaroundtownstreet and sexaroundtownpark and sexaroundtownretailstore) == 1:
            if (sexaroundtownhazel and sexaroundtownalanna and sexaroundtowngrundlesam and sexaroundtownprincipallashley) == 1:
                $ main_story = 33.5
                if winc == 0:
                    $ renpy.notify("New Objective: Get Back Home and Talk to [missus]")
                else:
                    $ renpy.notify("New Objective: Get Back Home and Talk to Mom")
    elif main_story == 84 and not 0 in (investigations_grundlesam, investigations_violette, investigations_effie, investigations_edward) and investigations_complete == 0:
        default investigations_complete = 0
        pov "I think I have enough info. I could keep looking or go back home and go over things."
        $ renpy.notify("New Objective: Get Back Home and go over investigation.")
        $ investigations_complete = 1
    elif hitomi_path == 11:
        $ map_blocking = True
    if gtime <= 1:
        play ambience 'audio/ambience/quietexteriorday_ambience.ogg' fadein 2.0
        jump lbl_townmap_day
    else:
        stop music fadeout 2.0
        play ambience 'audio/ambience/quietexteriornight_ambience.ogg' fadein 2.0
        jump lbl_townmap_night

###############
## Room Navigation
## This is the town map during the day.
label lbl_townmap_day:

    scene bg townmap_day
    with fade
    call screen scr_townmap_day

screen scr_townmap_day():
    ## Uptown
    imagebutton auto "btn townmap_day_uptown_%s" xpos 1661 ypos 40 focus_mask True action If( map_blocking and MapBlockCheck("uptown"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_uptown") )
    ## Top Row
    imagebutton auto "btn townmap_day_neighbour1_%s" xpos 250 ypos 145 focus_mask True action If( map_blocking and MapBlockCheck("neighbour1"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_neighbour1") )####
    imagebutton auto "btn townmap_day_myhouse_%s" xpos 432 ypos 145 focus_mask True action If( map_blocking and MapBlockCheck("myhouse"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_myhouse") )
    imagebutton auto "btn townmap_day_neighbour2_%s" xpos 636 ypos 143 focus_mask True action If( map_blocking and MapBlockCheck("neighbour2"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_neighbour2") )####
    imagebutton auto "btn townmap_day_cafe_%s" xpos 849 ypos 161 focus_mask True action If( map_blocking and MapBlockCheck("cafe"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_cafe") )
    # imagebutton auto "btn townmap_day_cornerstore_%s" xpos 999 ypos 160 focus_mask True action If( map_blocking and MapBlockCheck("cornerstore"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_cornerstore") )
    imagebutton auto "btn townmap_day_apartments_%s" xpos 1208 ypos 139 focus_mask True action If( map_blocking and MapBlockCheck("apartments"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_apartments") )
    imagebutton auto "btn townmap_day_jacobhouse_%s" xpos 1442 ypos 146 focus_mask True action If( map_blocking and MapBlockCheck("jacobhouse"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_jacobhouse") )
    imagebutton auto "btn townmap_day_effiehouse_%s" xpos 1620 ypos 144 focus_mask True action If( map_blocking and MapBlockCheck("effiehouse"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_effiehouse") )
    ## Middle Row
    imagebutton auto "btn townmap_day_office_%s" xpos 226 ypos 414 focus_mask True action If( map_blocking and MapBlockCheck("office"), Jump("lbl_map_block_check"), [Play("music", "audio/music/office_music.ogg"), Jump("lbl_townmap_day_office")] )
    imagebutton auto "btn townmap_day_policestation_%s" xpos 506 ypos 424 focus_mask True action If( map_blocking and MapBlockCheck("policestation"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_policestation") )
    imagebutton auto "btn townmap_day_mall_%s" xpos 860 ypos 430 focus_mask True action If( map_blocking and MapBlockCheck("mall"), Jump("lbl_map_block_check"), [Play("ambience", "audio/ambience/mallinterior_ambience.ogg"), Jump("lbl_townmap_day_mall")] )
    if day <= 4:
        imagebutton auto "btn townmap_day_school_%s" xpos 1203 ypos 431 focus_mask True action If( map_blocking and MapBlockCheck("school"), Jump("lbl_map_block_check"), [Play("ambience", "audio/ambience/schoolyardweekday_ambience.ogg"), Jump("lbl_townmap_day_school")] )
    else:
        imagebutton auto "btn townmap_day_school_%s" xpos 1203 ypos 431 focus_mask True action If( map_blocking and MapBlockCheck("school"), Jump("lbl_map_block_check"), [Play("ambience", "audio/ambience/quietexteriorday_ambience.ogg"), Jump("lbl_townmap_day_school")] )
    imagebutton auto "btn townmap_day_hospital_%s" xpos 1559 ypos 442 focus_mask True action If( map_blocking and MapBlockCheck("hospital"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_hospital"))
    ## Bottom Row
    if main_story <= 5 or main_story == 15 or main_story == 29:
        imagebutton auto "btn townmap_day_beach_%s" xpos 24 ypos 705 focus_mask True action Jump("lbl_townmap_day_beach")
    else:
        imagebutton auto "btn townmap_day_beach_%s" xpos 24 ypos 705 focus_mask True action If( map_blocking and MapBlockCheck("beach"), Jump("lbl_map_block_check"), [Play("music", "audio/music/urban_nova_beach_master_tt.ogg"), Jump("lbl_townmap_day_beach")] )
    imagebutton auto "btn townmap_day_street_%s" xpos 502 ypos 796 focus_mask True action If( map_blocking and MapBlockCheck("street"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_street") )
    imagebutton auto "btn townmap_day_abandonedlot_%s" xpos 855 ypos 813 focus_mask True action If( map_blocking and MapBlockCheck("abandonedlot"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_abandonedlot") )
    imagebutton auto "btn townmap_day_cinema_%s" xpos 1066 ypos 775 focus_mask True action If( map_blocking and MapBlockCheck("cinema"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_cinema") )
    imagebutton auto "btn townmap_day_park_%s" xpos 1337 ypos 723 focus_mask True action If( map_blocking and MapBlockCheck("park"), Jump("lbl_map_block_check"), Jump("lbl_townmap_day_park") )

    use hud_overlay ## NEED TO DISABLE MAP

## This is the town map during the night.
label lbl_townmap_night:
    scene bg townmap_night
    with fade
    call screen scr_townmap_night

screen scr_townmap_night():
    ## Uptown
    imagebutton auto "btn townmap_night_uptown_%s" xpos 1661 ypos 40 focus_mask True action Jump("lbl_townmap_night_uptown")
    ## Top Row
    imagebutton auto "btn townmap_night_neighbour1_%s" xpos 250 ypos 145 focus_mask True action Jump("lbl_townmap_night_neighbour1") ####
    imagebutton auto "btn townmap_night_myhouse_%s" xpos 432 ypos 145 focus_mask True action Jump("lbl_townmap_night_myhouse")
    imagebutton auto "btn townmap_night_neighbour2_%s" xpos 636 ypos 143 focus_mask True action Jump("lbl_townmap_night_neighbour2") ####
    imagebutton auto "btn townmap_night_cafe_%s" xpos 849 ypos 161 focus_mask True action Jump("lbl_townmap_night_cafe")
    # imagebutton auto "btn townmap_night_cornerstore_%s" xpos 999 ypos 160 focus_mask True action Jump("lbl_townmap_night_cornerstore")
    imagebutton auto "btn townmap_night_apartments_%s" xpos 1208 ypos 139 focus_mask True action Jump("lbl_townmap_night_apartments")
    imagebutton auto "btn townmap_night_jacobhouse_%s" xpos 1442 ypos 146 focus_mask True action Jump("lbl_townmap_night_jacobhouse")
    imagebutton auto "btn townmap_night_effiehouse_%s" xpos 1620 ypos 144 focus_mask True action Jump("lbl_townmap_night_effiehouse")
    ## Middle Row
    imagebutton auto "btn townmap_night_office_%s" xpos 226 ypos 414 focus_mask True action [Play("music", "audio/music/office_music.ogg"), Jump("lbl_townmap_night_office")]
    imagebutton auto "btn townmap_night_policestation_%s" xpos 506 ypos 424 focus_mask True action Jump("lbl_townmap_night_policestation")
    imagebutton auto "btn townmap_night_mall_%s" xpos 860 ypos 430 focus_mask True action Jump("lbl_townmap_night_mall")
    imagebutton auto "btn townmap_night_school_%s" xpos 1203 ypos 431 focus_mask True action Jump("lbl_townmap_night_school")
    imagebutton auto "btn townmap_night_hospital_%s" xpos 1559 ypos 442 focus_mask True action Jump("lbl_townmap_night_hospital")
    ## Bottom Row
    imagebutton auto "btn townmap_night_beach_%s" xpos 24 ypos 705 focus_mask True action Jump("lbl_townmap_night_beach")
    imagebutton auto "btn townmap_night_street_%s" xpos 502 ypos 796 focus_mask True action Jump("lbl_townmap_night_street")
    imagebutton auto "btn townmap_night_abandonedlot_%s" xpos 855 ypos 813 focus_mask True action Jump("lbl_townmap_night_abandonedlot")
    imagebutton auto "btn townmap_night_cinema_%s" xpos 1066 ypos 775 focus_mask True action Jump("lbl_townmap_night_cinema")
    imagebutton auto "btn townmap_night_park_%s" xpos 1337 ypos 723 focus_mask True action Jump("lbl_townmap_night_park")

    use hud_overlay ## NEED TO DISABLE MAP


###############
## Labels
label lbl_map_block_check:
    if hitomi_path == 11:
        pov "{i}I'm with Hitomi. We should get to my room while we have the house to ourselves.{/i}"
        jump lbl_townmap_setup
    if hitomi_path == 15:
        pov "{i}Effie's with me. I should just get over to the comicbook store backroom.{/i}"
        jump lbl_townmap_setup
