label lbl_start_game_load_effie:
    "Where do you want to leave off from with Effie?"
    menu:
        "Start of her Story":
            $ effie_path = 0
            $ effie_points = 0
        "Pouring Rain":
            $ effie_path = 4
            $ effie_points = 1
        "Artistic Expression":
            $ effie_path = 7
            $ effie_points = 2
        "Dateish Night":
            $ effie_path = 9
            $ effie_points = 3
        "Effie Calling":
            $ effie_path = 11
            $ effie_points = 4
        "There is No Webflix":
            $ effie_path = 14
            $ effie_points = 5
        "Before The Beach Party":
            $ effie_path = 16
            $ effie_points = 6
        "Effie Breaks Down":
            $ effie_path = 19
            $ effie_points = 7

    return
