################################################################################
label lbl_start_game_load:
    ## Set Date and Time
    $ month = 5
    $ date = 9
    $ day = 0
    $ gtime = 0

    ## Misc Sets
    $ nextday_ajob = 1

    # menu:
    #     "Public Version":
    #         jump lbl_previous_gamever_preset_public
    #     "Alpha 0.52":
    #         jump lbl_previous_gamever_preset_49
    #     "Alpha 0.53":
    #         jump lbl_previous_gamever_preset_49
    #     "Alpha 0.54":
    #         jump lbl_previous_gamever_preset_49
    #     "Alpha 0.55":
    jump lbl_previous_gamever_preset_49
        #"Alpha Test":
        #    jump lbl_previous_gamever_preset_test

## Previous Game Version Preset
################################################################################
# label lbl_previous_gamever_preset_48:
#     call lbl_setcharacterpathto1

#     call lbl_unlockvrheadset

#     call lbl_start_game_load_mum

#     call lbl_start_game_load_sister

#     call lbl_start_game_load_allaway

#     call lbl_start_game_load_lashley

#     call lbl_start_game_load_effie

#     call lbl_start_game_load_mumxsis

#     call lbl_start_game_load_mainstory

#     jump lbl_mybedroom_day_setup

################################################################################
label lbl_previous_gamever_preset_49:
    call lbl_setcharacterpathto1

    call lbl_unlockvrheadset

    call lbl_start_game_load_mum

    call lbl_start_game_load_sister

    call lbl_start_game_load_allaway

    call lbl_start_game_load_lashley

    call lbl_start_game_load_effie

    call lbl_start_game_load_violette

    call lbl_start_game_load_mumxsis

    call lbl_start_game_load_mainstory

    menu:
        "Go to new content":
            $ mumsis_path = 15
            $ mumsiscamp_path = 8
            jump lbl_naked_yoga
        "Continue game":
            pass

    jump lbl_mybedroom_day_setup

################################################################################
label lbl_previous_gamever_preset_test:
    "Do you want to leave off after the bath scene with mom or after your homerun with mom?"
    menu:
        "After Bath with Mom":
            $ mum_path = 17
        "After Homerun with Mom":
            $ mum_path = 31
        "Incest Porno with Mom":
            $ mum_path = 22
            $ day = 4
        "Unlocked Door with Sister":
            $ mum_path = 31
            $ sister_path = 8.5

    $ main_story = 36
    #$ sister_path = 4
    $ missallaway_path = 4

    $ gtime = 0

    $ mum_points = 8
    $ sister_points = 2
    $ missallaway_points = 2

    $ inventory.money = 300
    $ skill_luc = 10
    $ skill_str = 10
    $ skill_sta = 10
    $ skill_int = 10
    $ skill_cha = 10

    "Note: Characters such as Hitomi, Violette, Brock, Jack, Alanna, and Janae will start from the beginning."

    jump lbl_mybedroom_day_setup

##########################################################################
label lbl_setcharacterpathto1:
    $ violette_path = 1
    $ jack_path = 1
    $ lordkevlamin_path = 1
    $ hitomi_path = 1
    $ effie_path = 1
    $ effiesdad_path = 1
    $ jacob_path = 1
    $ jacobsdad_path = 1
    $ lailah_path = 1
    $ dad_path = 1
    $ brock_path = 1
    $ alanna_path = 1
    $ janae_path = 1
    $ principallashley_path = 1
    $ steve_path = 1
    $ hazel_path = 1
    $ mina_path = 1
    $ grundlesam_path = 1
    $ phil_path = 1
    $ meghan_path = 1
    $ chieghan_path = 1
    $ cole_path = 1
    $ jaiden_path = 1
    $ eloise_path = 1
    $ edward_path = 1
    $ teghan_path = 1
    $ zariah_path = 1
    $ luna_path = 1
    $ xina_path = 1

    return

label lbl_unlockvrheadset:
    $ inventory.add(Items.vrheadsetmod)
    $ vrheadset_chest = 1
    $ edward_vr_path = 6

    return
