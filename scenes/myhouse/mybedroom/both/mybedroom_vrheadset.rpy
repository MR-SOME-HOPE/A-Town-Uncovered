## VR Headset
label lbl_vrheadset_startup:
    if gtime <= 1:
        scene bg vrstartup_1
        with fade
        $ renpy.pause(0.5,hard=True)
        show bg vrstartup_2
        $ renpy.pause(0.5,hard=True)
        show bg vrstartup_3
        $ renpy.pause(0.4,hard=True)
        show bg vrstartup_4
        $ renpy.pause(0.4,hard=True)
        show bg vrstartup_5
        $ renpy.pause(0.3,hard=True)
        show black
        with dissolve
        $ renpy.pause(1,hard=True)
    else:
        scene bg vrstartup_6
        with fade
        $ renpy.pause(0.5,hard=True)
        show bg vrstartup_7
        $ renpy.pause(0.5,hard=True)
        show bg vrstartup_8
        $ renpy.pause(0.4,hard=True)
        show bg vrstartup_9
        $ renpy.pause(0.4,hard=True)
        show bg vrstartup_10
        $ renpy.pause(0.3,hard=True)
        show black
        with dissolve
        $ renpy.pause(1,hard=True)

    jump lbl_vrheadset_character_selection


label lbl_vrheadset_character_selection:
    scene bg vrheadset_0
    with fade
    call screen scr_vrheadset_charselection_pg1

##############################################################
## PAGE 1
screen scr_vrheadset_charselection_pg1():
    imagebutton auto "btn vrheadset_mother_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_mom"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_sister_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_sis"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_missallaway_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_allaway"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_effie_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_effie"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_lashley_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_lashley"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_hitomi_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_hitomi"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_violette_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_violette"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_zariah_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_zariah"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_teghan_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_teghan"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_hazel_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_hazel"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_mina_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_mina"), Hide("scr_vrheadset_charselection_pg1")
    imagebutton auto "btn vrheadset_luna_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_luna"), Hide("scr_vrheadset_charselection_pg1")
    
    imagebutton auto "btn vrheadset_next_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_charselection_pg1")
    if gtime >= 2:
        imagebutton auto "btn vrheadset_quit_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_charselection_pg1"), Jump("lbl_mybedroom_night_setup")
    else:
        imagebutton auto "btn vrheadset_quit_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_charselection_pg1"), Jump("lbl_mybedroom_day_setup")

## PAGE 2
screen scr_vrheadset_charselection_pg2():
    imagebutton auto "btn vrheadset_nursehollick_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_nursehollick"), Hide("scr_vrheadset_charselection_pg2")
    imagebutton auto "btn vrheadset_lailah_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_lailah"), Hide("scr_vrheadset_charselection_pg2")
    imagebutton auto "btn vrheadset_meghan_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_meghan"), Hide("scr_vrheadset_charselection_pg2")
    imagebutton auto "btn vrheadset_alanna_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_alanna"), Hide("scr_vrheadset_charselection_pg2")
    imagebutton auto "btn vrheadset_xina_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_xina"), Hide("scr_vrheadset_charselection_pg2")
    imagebutton auto "btn vrheadset_janae_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_janae"), Hide("scr_vrheadset_charselection_pg2")
    imagebutton auto "btn vrheadset_drunkgirl_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_drunkgirl"), Hide("scr_vrheadset_charselection_pg2")
    
    imagebutton auto "btn vrheadset_prev_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_charselection_pg2")
    if gtime >= 2:
        imagebutton auto "btn vrheadset_quit_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_charselection_pg2"), Jump("lbl_mybedroom_night_setup")
    else:
        imagebutton auto "btn vrheadset_quit_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_charselection_pg2"), Jump("lbl_mybedroom_day_setup")

##############################################################
## MOM
screen scr_vrheadset_mom():
    if renpy.seen_label("lbl_momaftersunset_massage"):
        imagebutton auto "btn vrheadset_mother1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_momaftersunset_massage_revisit")
    if renpy.seen_label("lbl_momaftersunset_suck"):
        imagebutton auto "btn vrheadset_mother2_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_momaftersunset_suck_revisit")
    if renpy.seen_label("lbl_mom_in_my_bed") or renpy.seen_label("lbl_mom_in_my_bed_winc0"):
        imagebutton auto "btn vrheadset_mother3_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_mom_in_my_bed_revist")
    if renpy.seen_label("lbl_bath_with_mom_1"):
        imagebutton auto "btn vrheadset_mother4_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_bath_with_mom_3_revisit")
    if renpy.seen_label("lbl_mom_at_the_park_bj"):
        imagebutton auto "btn vrheadset_mother5_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_mom_at_the_park_revisit_bj")
    if renpy.seen_label("lbl_incest_porno_with_mom_0"):
        imagebutton auto "btn vrheadset_mother6_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_incest_porno_with_mom_revisit_angle1")
    if renpy.seen_label("lbl_incest_porno_with_mom_0"):
        imagebutton auto "btn vrheadset_mother7_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_incest_porno_with_mom_revisit_angle2")
    if renpy.seen_label("lbl_incest_porno_with_mom_0"):
        imagebutton auto "btn vrheadset_mother8_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_incest_porno_with_mom_revisit_angle3")
    if renpy.seen_label("lbl_mom_midnight_fun_bj"):
        imagebutton auto "btn vrheadset_mother9_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_mom_midnight_fun_bj_revisit")
    if renpy.seen_label("lbl_mom_midnight_fun_grind"):
        imagebutton auto "btn vrheadset_mother10_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_mom_midnight_fun_grind_revisit")
    if renpy.seen_label("lbl_mom_bedroom_hscene_after_bj"):
        imagebutton auto "btn vrheadset_mother11_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_mom_bedroom_hscene_after_bj_revisit")
    if renpy.seen_label("lbl_mom_bedroom_hscene_after_mish"):
        imagebutton auto "btn vrheadset_mother12_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("menu_vrheadset_mom_missionary_choice")
    if renpy.seen_label("lbl_mom_bedroom_hscene_after_desk_rimjob"):
        imagebutton auto "btn vrheadset_mother13_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("lbl_mom_bedroom_hscene_after_desk_rimjob_revist")
    if renpy.seen_label("lbl_mom_bedroom_hscene_after_desk_pussy") or renpy.seen_label("lbl_mom_bedroom_hscene_after_desk_anal"):
        imagebutton auto "btn vrheadset_mother14_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mom"), Jump("menu_vrheadset_mom_desk_choice")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_mom")

##############################################################
## SISTER
screen scr_vrheadset_sis():
    if renpy.seen_label("lbl_second_camgurl_stream"):
        imagebutton auto "btn vrheadset_sister1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_sis"), Jump("lbl_second_camgurl_stream_revisit")
    if renpy.seen_label("lbl_whos_the_better_sibling_1"):
        imagebutton auto "btn vrheadset_sister2_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_sis"), Jump("lbl_whos_the_better_sibling_revisit_1")
    if renpy.seen_label("lbl_sibling_jail_time_2"):
        imagebutton auto "btn vrheadset_sister3_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_sis"), Jump("lbl_sibling_jail_time_revisit")
    if renpy.seen_label("lbl_third_camgurl_stream"):
        imagebutton auto "btn vrheadset_sister4_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_sis"), Jump("lbl_third_camgurl_stream_revist")
    if renpy.seen_label("lbl_breakinginfortrebuild_bj_pre"):
        imagebutton auto "btn vrheadset_sister5_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_sis"), Jump("lbl_breakinginfortrebuild_bj_revisit_pre")
    if renpy.seen_label("lbl_sisters_nightmare"):
        imagebutton auto "btn vrheadset_sister6_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_sis"), Jump("lbl_sisters_nightmare_revisit")
    if renpy.seen_label("lbl_stargazing_fun"):
        imagebutton auto "btn vrheadset_sister7_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_sis"), Jump("lbl_stargazing_fun_revisit")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_sis")

##############################################################
## ALLAWAY
screen scr_vrheadset_allaway():
    if renpy.seen_label("lbl_trapped_and_teased_1"):
        imagebutton auto "btn vrheadset_missallaway1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_allaway"), Jump("lbl_trapped_and_teased_revisit")
    if renpy.seen_label("lbl_allaway_under_the_desk"):
        imagebutton auto "btn vrheadset_missallaway3_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_allaway"), Jump("lbl_allaway_under_the_desk_revisit")
    if renpy.seen_label("lbl_allaway_school_sex_facefuck"):
        imagebutton auto "btn vrheadset_missallaway4_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_allaway"), Jump("lbl_allaway_school_sex_facefuck_revisit")
    if renpy.seen_label("lbl_sex_by_the_fire_truck"):
        imagebutton auto "btn vrheadset_missallaway5_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_allaway"), Jump("lbl_sex_by_the_fire_truck_revisit")
    if renpy.seen_label("lbl_allaway_after_school_sex_desk"):
        imagebutton auto "btn vrheadset_missallaway6_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_allaway"), Jump("lbl_allaway_after_school_sex_desk_revisit")
    if renpy.seen_label("lbl_allaway_after_school_sex_stairs"):
        imagebutton auto "btn vrheadset_missallaway7_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_allaway"), Jump("lbl_allaway_after_school_sex_stairs_revisit")
    if renpy.seen_label("lbl_allaway_after_school_sex_cowgirl"):
        imagebutton auto "btn vrheadset_missallaway8_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_allaway"), Jump("lbl_allaway_after_school_sex_cowgirl_revisit")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_allaway")

##############################################################
## EFFIE
screen scr_vrheadset_effie():
    if renpy.seen_label("lbl_effie_bj_1"):
        imagebutton auto "btn vrheadset_effie1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effie"), Jump("lbl_effie_bj_revisit_1")
    if renpy.seen_label("lbl_effie_exib_1"):
        imagebutton auto "btn vrheadset_effie2_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effie"), Jump("lbl_effie_exib_revisit_1")
    if renpy.seen_label("lbl_effie_mish_1"):
        imagebutton auto "btn vrheadset_effie3_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effie"), Jump("lbl_effie_mish_revisit_1")
    if renpy.seen_label("lbl_a_predictable_realization_handjob"):
        imagebutton auto "btn vrheadset_effie4_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effie"), Jump("lbl_a_predictable_realization_handjob_revisit")
    if renpy.seen_label("lbl_dateish_night_room_sex"):
        imagebutton auto "btn vrheadset_effie5_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effie"), Jump("lbl_dateish_night_room_sex_revisit")
    if renpy.seen_label("lbl_effie_couch_on_phone_0"):
        imagebutton auto "btn vrheadset_effie6_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effie"), Jump("lbl_effie_couch_on_phone_revisit_0")
    if renpy.seen_label("lbl_there_is_no_webflix_sex"):
        imagebutton auto "btn vrheadset_effie7_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effie"), Jump("lbl_there_is_no_webflix_sex_revisit")
    if renpy.seen_label("lbl_there_is_no_webflix_sex"):
        imagebutton auto "btn vrheadset_effie8_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effie"), Jump("lbl_there_is_no_webflix_sex_revisit")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_effie")

##############################################################
## LASHLEY
screen scr_vrheadset_lashley():
    if renpy.seen_label("lbl_drunk_and_frisky_titjob"):
        imagebutton auto "btn vrheadset_lashley1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_drunk_and_frisky_titjob_revisit")
    if renpy.seen_label("lbl_drunk_and_frisky_bj"):
        imagebutton auto "btn vrheadset_lashley2_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_drunk_and_frisky_bj_revisit")
    if renpy.seen_label("lbl_drunk_and_frisky_finger"):
        imagebutton auto "btn vrheadset_lashley3_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_drunk_and_frisky_finger_revisit")
    if renpy.seen_label("lbl_drunk_and_frisky_oral"):
        imagebutton auto "btn vrheadset_lashley4_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_drunk_and_frisky_oral_revisit")
    if renpy.seen_label("lbl_lashley_ribbon_mating_press_0"):
        imagebutton auto "btn vrheadset_lashley5_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_lashley_ribbon_mating_press_revisit_0")
    if renpy.seen_label("lbl_lashley_bent_over_desk_0"):
        imagebutton auto "btn vrheadset_lashley6_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_lashley_bent_over_desk_revisit_0")
    if renpy.seen_label("lbl_lashley_cafeteria_doggy"):
        imagebutton auto "btn vrheadset_lashley7_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_lashley_cafeteria_doggy_revisit")
    if renpy.seen_label("lbl_principal_office_chair_sex_0"):
        imagebutton auto "btn vrheadset_lashley9_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_principal_office_chair_sex_revisit_0")
    if renpy.seen_label("lbl_lashleyshunger_hscene_0"):
        imagebutton auto "btn vrheadset_lashley8_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_lashleyshunger_hscene_revisit_0")
    if renpy.seen_label("lbl_psychobreakdown_hscene_continue"):
        imagebutton auto "btn vrheadset_lashley10_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lashley"), Jump("lbl_psychobreakdown_hscene_revisit_continue")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_lashley")

##############################################################
## HITOMI
screen scr_vrheadset_hitomi():
    if renpy.seen_label("lbl_caught_in_4k_bj"):
        imagebutton auto "btn vrheadset_hitomi1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_caught_in_4k_bj_revisit")
    if renpy.seen_label("lbl_caught_in_4k_cunnilingus"):
        imagebutton auto "btn vrheadset_hitomi2_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_caught_in_4k_cunnilingus_revisit")
    if renpy.seen_label("lbl_caught_in_4k_spooning"):
        imagebutton auto "btn vrheadset_hitomi3_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_caught_in_4k_spooning_revisit")
    if renpy.seen_label("lbl_hitomi_backroom_matingpress"):
        imagebutton auto "btn vrheadset_hitomi4_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_hitomi_backroom_matingpress_revisit")
    if renpy.seen_label("lbl_hitomi_backroom_cunnilingus"):
        imagebutton auto "btn vrheadset_hitomi5_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_hitomi_backroom_cunnilingus_revisit")
    if renpy.seen_label("lbl_hitomi_entrance_doggy"):
        imagebutton auto "btn vrheadset_hitomi6_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_hitomi_entrance_doggy_revisit")
    if renpy.seen_label("lbl_hitomi_beach_accident_0"):
        imagebutton auto "btn vrheadset_hitomi7_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_hitomi_beach_accident_revisit_0")
    if renpy.seen_label("lbl_hitomi_livingroom_doggy_0"):
        imagebutton auto "btn vrheadset_hitomi8_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_hitomi_livingroom_doggy_revisit_0")
    if renpy.seen_label("lbl_vip_heart_to_heart_hscene_0"):
        imagebutton auto "btn vrheadset_hitomi9_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hitomi"), Jump("lbl_vip_heart_to_heart_hscene_revisit_0")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_hitomi")

##############################################################
## VIOLETTE
screen scr_vrheadset_violette():
    if renpy.seen_label("lbl_violette_seated_cowgirl_0"):
        imagebutton auto "btn vrheadset_violette1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_violette"), Jump("lbl_violette_seated_cowgirl_revisit_0")
    if renpy.seen_label("lbl_a_shared_dream_69"):
        imagebutton auto "btn vrheadset_violette2_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_violette"), Jump("lbl_a_shared_dream_69_revisit")
    if renpy.seen_label("lbl_beach_sparks_after_dark_bj"):
        imagebutton auto "btn vrheadset_violette3_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_violette"), Jump("lbl_beach_sparks_after_dark_bj_revisit")
    if renpy.seen_label("lbl_violettes_punishment_archeddoggy"):
        imagebutton auto "btn vrheadset_violette4_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_violette"), Jump("lbl_violettes_punishment_archeddoggy_revisit")
    if renpy.seen_label("lbl_violettes_punishment_matingpress"):
        imagebutton auto "btn vrheadset_violette5_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_violette"), Jump("lbl_violettes_punishment_matingpress_revisit")
    if renpy.seen_label("lbl_violettes_punishment_reversecowgirl"):
        imagebutton auto "btn vrheadset_violette6_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_violette"), Jump("lbl_violettes_punishment_reversecowgirl_revisit")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_violette")

##############################################################
## ZARIAH
screen scr_vrheadset_zariah():
    if renpy.seen_label("lbl_zariah_stage_reverse_cowgirl_0"):
        imagebutton auto "btn vrheadset_zariah1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_zariah"), Jump("lbl_zariah_stage_reverse_cowgirl_revisit_0")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_zariah")

##############################################################
## TEGHAN
screen scr_vrheadset_teghan():
    if renpy.seen_label("lbl_teghan_stall_reverse_seated_cowgirl_0"):
        imagebutton auto "btn vrheadset_teghan1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_teghan"), Jump("lbl_teghan_stall_reverse_seated_cowgirl_revisit_0")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_teghan")

##############################################################
## HAZEL
screen scr_vrheadset_hazel():
    if renpy.seen_label("lbl_hazel_backroom_cowgirl_0"):
        imagebutton auto "btn vrheadset_hazel1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_hazel"), Jump("lbl_hazel_backroom_cowgirl_revisit_0")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_hazel")

##############################################################
## MINA
screen scr_vrheadset_mina():
    if renpy.seen_label("lbl_mina_standing_legup_0"):
        imagebutton auto "btn vrheadset_mina1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_mina"), Jump("lbl_effie_bj_revisit_1")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_mina")

##############################################################
## LUNA
screen scr_vrheadset_luna():
    if renpy.seen_label("lbl_luna_tied_missionary"):
        imagebutton auto "btn vrheadset_luna1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_luna"), Jump("lbl_luna_tied_missionary_revisit")
    if renpy.seen_label("lbl_luna_doggy_bedroom_0"):
        imagebutton auto "btn vrheadset_luna2_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_luna"), Jump("lbl_luna_doggy_bedroom_revisit_0")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg1"), Hide("scr_vrheadset_luna")

##############################################################
## NURSE HOLLICK
screen scr_vrheadset_nursehollick():
    if renpy.seen_label("lbl_effie_bj_1"):
        imagebutton auto "btn vrheadset_nursehollick1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_nursehollick"), Jump("lbl_your_annual_examination_revisit_5")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_nursehollick")

##############################################################
## LAILAH
screen scr_vrheadset_lailah():
    if renpy.seen_label("lbl_lailah_lying_doggy_0"):
        imagebutton auto "btn vrheadset_lailah1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_lailah"), Jump("lbl_lailah_lying_doggy_revisit_0")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_lailah")

##############################################################
## MEGHAN
screen scr_vrheadset_meghan():
    if renpy.seen_label("lbl_meghan_weed_kush_0"):
        imagebutton auto "btn vrheadset_meghan1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_meghan"), Jump("lbl_meghan_weed_kush_revisit_0")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_meghan")

##############################################################
## ALANNA
screen scr_vrheadset_alanna():
    if renpy.seen_label("lbl_alanna_cuddle_fuck"):
        imagebutton auto "btn vrheadset_alanna1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_alanna"), Jump("lbl_alanna_cuddle_fuck_revisit")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_alanna")

##############################################################
## XINA
screen scr_vrheadset_xina():
    if renpy.seen_label("lbl_taken_for_sacrifice_3"):
        imagebutton auto "btn vrheadset_xina1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_xina"), Jump("lbl_taken_for_sacrifice_revisit_4_fuck")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_xina")
    
##############################################################
## JANAE
screen scr_vrheadset_janae():
    if renpy.seen_label("lbl_effie_bj_1"):
        imagebutton auto "btn vrheadset_janae1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_janae"), Jump("lbl_janae_plowed_over_boxes_revisit")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_janae")

##############################################################
## DRUNK GIRL
screen scr_vrheadset_drunkgirl():
    if renpy.seen_label("lbl_randomevent_beach_skinnydipping_1"):
        imagebutton auto "btn vrheadset_drunkgirl1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_drunkgirl"), Jump("lbl_randomevent_beach_skinnydipping_revisit_1")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_drunkgirl")

##############################################################
## EFFIE X SISTER
screen scr_vrheadset_effiexsister():
    if renpy.seen_label("lbl_mcxsister_eating_effie"):
        imagebutton auto "btn vrheadset_effiexsister1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effiexsister"), Jump("lbl_mcxsister_eating_effie_revisit")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_effiexsister")

##############################################################
## EFFIE X MISS ALLAWAY
screen scr_vrheadset_effiexmissallaway():
    if renpy.seen_label("lbl_allawayxeffiexmc_effiebed_pre"):
        imagebutton auto "btn vrheadset_effiexmissallaway1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_effiexmissallaway"), Jump("lbl_allawayxeffiexmc_effiebed_revisit_pre")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_effiexmissallaway")

##############################################################
## MOM X SISTER
screen scr_vrheadset_momxsister():
    if renpy.seen_label("lbl_a_cool_creek_hscene"):
        imagebutton auto "btn vrheadset_momxsister1_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_a_cool_creek_hscene_revisit")
    if renpy.seen_label("lbl_first_night_camping"):
        imagebutton auto "btn vrheadset_momxsister2_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_first_night_camping_revisit")
    if renpy.seen_label("lbl_fun_ride_home_from_camp"):
        imagebutton auto "btn vrheadset_momxsister3_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_fun_ride_home_from_camp_revisit")
    if renpy.seen_label("lbl_mom_sis_movie_night_choice"):
        imagebutton auto "btn vrheadset_momxsister4_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_mom_sis_movie_night_revisit_choice")
    if renpy.seen_label("lbl_mom_under_table_trio_0"):
        imagebutton auto "btn vrheadset_momxsister5_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_mom_under_table_trio_revisit_0")
    if renpy.seen_label("lbl_momxsisterxmc_69doggy_0"):
        imagebutton auto "btn vrheadset_momxsister6_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_momxsisterxmc_69doggy_revisit_0")
    if renpy.seen_label("lbl_momxsisterxmc_bedroomfun_0"):
        imagebutton auto "btn vrheadset_momxsister7_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_momxsisterxmc_bedroomfun_revisit_0")
    if renpy.seen_label("lbl_momxsisterxmc_cocksandwich_0"):
        imagebutton auto "btn vrheadset_momxsister8_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_momxsisterxmc_cocksandwich_revisit_0")
    if renpy.seen_label("lbl_momxsisterxmc_doublebj_0"):
        imagebutton auto "btn vrheadset_momxsister9_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_momxsisterxmc_doublebj_revisit_0")
    if renpy.seen_label("lbl_momxsisterxmc_boxfort_0"):
        imagebutton auto "btn vrheadset_momxsister10_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_momxsisterxmc_boxfort_revisit_0")
    if renpy.seen_label("lbl_naked_yoga_hscene"):
        imagebutton auto "btn vrheadset_momxsister11_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_naked_yoga_hscene_revisit")
    if renpy.seen_label("lbl_second_night_camping_hscene"):
        imagebutton auto "btn vrheadset_momxsister12_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_second_night_camping_hscene_revisit")
    if renpy.seen_label("lbl_sister_eating_mom_for_breakfast"):
        imagebutton auto "btn vrheadset_momxsister13_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_sister_eating_mom_for_breakfast_revisit")
    if renpy.seen_label("lbl_snuggled_awake"):
        imagebutton auto "btn vrheadset_momxsister14_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_snuggled_awake_revisit")
    if renpy.seen_label("lbl_the_natural_spring_hscene"):
        imagebutton auto "btn vrheadset_momxsister15_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_the_natural_spring_hscene_revisit")
    if renpy.seen_label("lbl_the_purple_trail"):
        imagebutton auto "btn vrheadset_momxsister16_%s" xpos 0 ypos 0 focus_mask True action Hide("scr_vrheadset_momxsister"), Jump("lbl_the_purple_trail_revisit")
    imagebutton auto "btn vrheadset_back_%s" xpos 0 ypos 0 focus_mask True action Show("scr_vrheadset_charselection_pg2"), Hide("scr_vrheadset_momxsister")


##############################################################
## MENU
menu menu_vrheadset_mom_desk_choice:
    "Anal":
        jump lbl_mom_bedroom_hscene_after_desk_anal_revisit
    "Pussy":
        jump lbl_mom_bedroom_hscene_after_desk_pussy_revisit


menu menu_vrheadset_mom_missionary_choice:
    "Anal":
        jump lbl_mom_bedroom_hscene_after_mishanal_revisit
    "Pussy":
        jump lbl_mom_bedroom_hscene_after_mish_revisit_pussy
