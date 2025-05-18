###############
## Setup
## Story Path
label lbl_park_night_setup:
    ## MAIN STORY
    ## Pre Game
    if main_story == 0:
        "WTF are you doing here?"
        jump lbl_townmap_setup
    ## The Mysterious Figure
    elif main_story == 23:
        call lbl_randomevent_park_violette_1
        scene bg themysteriousfigure_1_1
        with fade
        jump lbl_the_mysterious_figure
    ## Taken For Sacrifice
    elif main_story == 35:
        jump lbl_taken_for_sacrifice
    ## Don't Be Too Hasty
    elif main_story == 124:
        jump lbl_dont_be_too_hasty
    # ## Second Safer Ceremony
    # elif main_story == 135:
    #     jump lbl_second_safer_ceremony
    # ## Let the Ceremony Begin
    # elif main_story == 136:
    #     jump lbl_let_the_ceremony_begin
    # ## Ceremonial Orgy
    # elif main_story == 137:
    #     jump lbl_ceremonial_orgy
    # ## Post Ceremonial Orgy
    # elif main_story == 138:
    #     jump lbl_post_ceremonial_orgy
    # ## Park Party Mirroring
    # elif main_story == 139:
    #     jump lbl_park_party_mirroring

    ## SIDE STORIES
    ## Mom at the Park
    if mum_path == 21:
        scene bg park_night
        with fade
        jump lbl_mom_at_the_park
    ## Allaway Private Talk
    if missallaway_path == 21:
        jump lbl_allaway_private_talk
    ## Effie Breaks Down
    if effie_path == 19:
        jump lbl_effie_breaks_down
    else:
        ## Violette Night Run
        #if violette_path >= 1:
        #    if date == 2 and (month == 0 or month == 4 or month == 5 or month == 6 or month == 9 or month == 10) and randomencounter == 0:
        #        $ randomencounter = 1
        #        scene bg park_night
        #        with fade

        #        jump lbl_randomevent_park_violette_1
        #else:
        jump lbl_park_night

###############
## Room Navigation
## This is the map for park during the night.
label lbl_park_night:

    scene bg park_night
    if effie_path > 1 and effie_funlater == 0 and insexworld == 0 and not 25 <= main_story <= 33:
        show btn_park_night_effie_idle2
    call screen scr_park_night

screen scr_park_night():
    imagebutton auto "btn park_night_path_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_park_night_path")
    imagebutton auto "btn park_night_bench_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_park_night_bench")
    # mom on bench
    #if main_story <= 12 or mum_path == 21 or (main_story >= 14 and effie_path == 1) or 25 <= main_story <= 33:
    #    pass
    #else:
        ## Invite to sex
    #    if main_story == 11 or effie_funlater == 1:
    #        pass
        ## Otherwise
    #    else:
    #        imagebutton auto "btn park_night_effie_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_park_night_effie")
    if effie_path > 1 and effie_funlater == 0 and insexworld == 0 and not 25 <= main_story <= 33:
        imagebutton auto "btn park_night_effie_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_park_night_effie")
    use hud_overlay

###############
## Labels
## Locations
label lbl_park_night_path:
    scene bg park_night
    if effie_path > 1 and effie_funlater == 0 and insexworld == 0 and not 25 <= main_story <= 33:#and main_story != 11
        show btn_park_night_effie_idle2
    pov "{i}I can increase my stamina during the day here.{/i}"
    call screen scr_park_night

label lbl_park_night_bench:
    scene bg park_night
    if effie_path > 1 and effie_funlater == 0 and insexworld == 0 and not 25 <= main_story <= 33:#and main_story != 11
        show btn_park_night_effie_idle2
    pov "{i}Lovely seat. 10/10 would sit again.{/i}"
    call screen scr_park_night
