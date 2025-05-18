label lbl_start_game_load_mum:
    if winc == 1:
        "Where do you want to leave off from with mom?"
        menu:
            "Watching TV with Mom":
                $ mum_path = 1
                $ mum_points = 0
            "Hanging out with Mom Everyday":
                $ mum_path = 6
                $ mum_points = 4
            "Cheer Up Mom":
                $ mum_path = 11
                $ mum_points = 4
            "After Bath with Mom":
                $ mum_path = 17
                $ mum_points = 6
            "Mom At the Park":
                $ mum_path = 21
                $ mum_points = 6
            "Dinner with Mom":
                $ mum_path = 25
                $ momhasdonebj = 1
                $ mum_points = 8
            "After Homerun with Mom":
                $ mum_path = 31
                $ momhasdonebj = 1
                $ mum_points = 8

    else:
        "Where do you want to leave off from with [missus]?"
        menu:
            "Watching TV with [missus]":
                $ mum_path = 1
                $ mum_points = 0
            "Hanging out with [missus] Everyday":
                $ mum_path = 6
                $ mum_points = 4
            "Cheer Up [missus]":
                $ mum_path = 11
                $ mum_points = 4
            "After Bath with [missus]":
                $ mum_path = 17
                $ mum_points = 5
            "[missus] At the Park":
                $ mum_path = 21
                $ mum_points = 6
            "Dinner with [missus]":
                $ mum_path = 25
                $ momhasdonebj = 1
                $ mum_points = 8
            "After Homerun with [missus]":
                $ mum_path = 31
                $ momhasdonebj = 1
                $ mum_points = 9

    return
