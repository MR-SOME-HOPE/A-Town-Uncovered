label lbl_start_game_load_sister:
    "Where do you want to leave off from with [sister]?"
    menu:
        "Talk about Effie with her":
            $ sister_path = 0
            $ sister_points = 0
        "First Camgurl Stream":
            $ sister_path = 5
            $ sister_points = 1
        "Help Build a Fort":
            $ sister_path = 9
            $ sister_points = 2
        "Second Camgurl Stream":
            $ sister_path = 14
            $ sister_points = 3
        "Sister in the Streets":
            $ sister_path = 17
            $ sister_points = 4
        "Third Camgurl Stream":
            $ sister_path = 23
            $ sister_points = 5
        "Collecting Boxes for New Fort":
            $ sister_path = 29
            $ sister_points = 6
        "Plan to Rebuild Fort":
            $ sister_path = 29
            $ sister_points = 7
        "Rebuild the New Boxfort":
            $ fursuitforboxjob_boxes = 50
            $ sister_path = 32
            $ sister_points = 8

    return
