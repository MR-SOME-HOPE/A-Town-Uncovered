###############
## TOWN MAP ##
## Time Decider
label lbl_uptownmap_setup:
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
        pov "I think I have enough info. I could keep looking or go back home and go over things."
        $ renpy.notify("New Objective: Get Back Home and go over investigation.")
        $ investigations_complete = 1
    if gtime <= 1:
        play ambience 'audio/ambience/quietexteriorday_ambience.ogg' fadein 2.0
        jump lbl_uptownmap_day
    else:
        stop music fadeout 2.0
        play ambience 'audio/ambience/quietexteriornight_ambience.ogg' fadein 2.0
        jump lbl_uptownmap_night

###############
## Room Navigation
## This is the town map during the day.
label lbl_uptownmap_day:

    scene bg uptownmap_day
    with fade
    call screen scr_uptownmap_day

screen scr_uptownmap_day():
    ## Top Row
    imagebutton auto "btn uptownmap_day_trainstation_%s" xpos 12 ypos 147 focus_mask True action Jump("lbl_uptownmap_day_trainstation") ####
    imagebutton auto "btn uptownmap_day_forest_%s" xpos 561 ypos 12 focus_mask True action Jump("lbl_uptownmap_day_forest")
    imagebutton auto "btn uptownmap_day_lashleymanor_%s" xpos 1310 ypos 132 focus_mask True action Jump("lbl_uptownmap_day_lashleymanor") ####
    imagebutton auto "btn uptownmap_day_cliff_%s" xpos 1649 ypos 12 focus_mask True action Jump("lbl_uptownmap_day_cliff")
    imagebutton auto "btn uptownmap_day_mineentrance_%s" xpos 1806 ypos 218 focus_mask True action Jump("lbl_uptownmap_day_mineentrance")
    ## Middle Row
    imagebutton auto "btn uptownmap_day_mayorsestate_%s" xpos 1021 ypos 369 focus_mask True action Jump("lbl_uptownmap_day_mayorsestate") ####
    imagebutton auto "btn uptownmap_day_church_%s" xpos 1444 ypos 446 focus_mask True action Jump("lbl_uptownmap_day_church")
    add "btn uptownmap_day_graveyard_idle" xpos 1553 ypos 393
    ## Bottom Row
    imagebutton auto "btn uptownmap_day_townhouses_%s" xpos 687 ypos 658 focus_mask True action Jump("lbl_uptownmap_day_townhouses") ####
    imagebutton auto "btn uptownmap_day_restaurant_%s" xpos 1010 ypos 675 focus_mask True action Jump("lbl_uptownmap_day_restaurant")
    imagebutton auto "btn uptownmap_day_motel_%s" xpos 1303 ypos 677 focus_mask True action Jump("lbl_uptownmap_day_motel") ####
    ## Downtown
    imagebutton auto "btn uptownmap_day_downtown_%s" xpos 1662 ypos 903 focus_mask True action Jump("lbl_townmap_day") #########################################

    use hud_overlay2

## This is the town map during the night.
label lbl_uptownmap_night:
    scene bg uptownmap_night
    with fade
    call screen scr_uptownmap_night

screen scr_uptownmap_night():
    ## Top Row
    imagebutton auto "btn uptownmap_night_trainstation_%s" xpos 12 ypos 147 focus_mask True action Jump("lbl_uptownmap_night_trainstation") ####
    imagebutton auto "btn uptownmap_night_forest_%s" xpos 561 ypos 12 focus_mask True action Jump("lbl_uptownmap_night_forest")
    imagebutton auto "btn uptownmap_night_lashleymanor_%s" xpos 1310 ypos 132 focus_mask True action Jump("lbl_uptownmap_night_lashleymanor") ####
    imagebutton auto "btn uptownmap_night_cliff_%s" xpos 1649 ypos 12 focus_mask True action Jump("lbl_uptownmap_night_cliff")
    imagebutton auto "btn uptownmap_night_mineentrance_%s" xpos 1806 ypos 218 focus_mask True action Jump("lbl_uptownmap_night_mineentrance")
    ## Middle Row
    imagebutton auto "btn uptownmap_night_mayorsestate_%s" xpos 1021 ypos 369 focus_mask True action Jump("lbl_uptownmap_night_mayorsestate") ####
    imagebutton auto "btn uptownmap_night_church_%s" xpos 1444 ypos 446 focus_mask True action Jump("lbl_uptownmap_night_church")
    add "btn uptownmap_night_graveyard_idle" xpos 1553 ypos 393
    ## Bottom Row
    imagebutton auto "btn uptownmap_night_townhouses_%s" xpos 687 ypos 658 focus_mask True action Jump("lbl_uptownmap_night_townhouses") ####
    imagebutton auto "btn uptownmap_night_restaurant_%s" xpos 1010 ypos 675 focus_mask True action Jump("lbl_uptownmap_night_restaurant")
    imagebutton auto "btn uptownmap_night_motel_%s" xpos 1303 ypos 677 focus_mask True action Jump("lbl_uptownmap_night_motel") ####
    ## Downtown
    imagebutton auto "btn uptownmap_night_downtown_%s" xpos 1662 ypos 903 focus_mask True action Jump("lbl_townmap_night") #########################################

    use hud_overlay2

###############
## Labels
