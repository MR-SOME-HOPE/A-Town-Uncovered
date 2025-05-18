label lbl_start_game_load_mumxsis:
    if winc == 1:
        "Where do you want to leave off from with mom & [sister]?"
        menu:
            "[sister] Passed out" if mum_path >= 1 and sister_path >= 5:
                $ mumsis_path = 1
            "Mom Coddling [sister]" if mum_path >= 3 and sister_path >= 11:
                $ mumsis_path = 3
            "Mom & [sister] Bathing Together" if mum_path >= 17.5 and sister_path >= 18:
                $ mumsis_path = 5
            "[sister] Eating Mom for Breakfast" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 8
            "Snuggled Awake" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 11
            "Mom & [sister] Movie Night" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 13
            "Mom & [sister] Camping Trip Day 1" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 15
                $ mumsiscamp_path = 0
            "Mom & [sister] Camping Trip Day 2" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 15
                $ mumsiscamp_path = 8

    else:
        "Where do you want to leave off from with [missus] & [sister]?"
        menu:
            "[sister] Passed out" if mum_path >= 1 and sister_path >= 5:
                $ mumsis_path = 1
            "[missus] Coddling [sister]" if mum_path >= 3 and sister_path >= 11:
                $ mumsis_path = 3
            "[missus] & [sister] Bathing Together" if mum_path >= 17.5 and sister_path >= 18:
                $ mumsis_path = 5
            "[sister] Eating [missus] for Breakfast" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 8
            "Snuggled Awake" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 11
            "[missus] & [sister] Movie Night" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 13
            "[missus] & [sister] Camping Trip Day 1" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 15
                $ mumsiscamp_path = 0
            "[missus] & [sister] Camping Trip Day 2" if mum_path >= 22 and sister_path >= 22:
                $ mumsis_path = 15
                $ mumsiscamp_path = 8
                

    return
