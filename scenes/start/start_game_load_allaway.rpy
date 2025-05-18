label lbl_start_game_load_allaway:
    "Where do you want to leave off from with Miss Allaway?"
    menu:
        "Find her sneaking around the Fight Club":
            $ missallaway_path = 0
            $ missallaway_points = 0
        "Get Detention":
            $ missallaway_path = 4
            $ missallaway_points = 2
        "Trapped in University with Her":
            $ missallaway_path = 8
            $ missallaway_points = 3
        "Bump into her at the cinema":
            $ missallaway_path = 14
            $ missallaway_points = 4
        "Find allaway in the boys' bathroom":
            $ missallaway_path = 17
            $ missallaway_points = 5
        "Ask her for a private talk":
            $ missallaway_path = 20
            $ missallaway_points = 6
        "Do the job for Jack":
            $ missallaway_path = 23
            $ missallaway_points = 7
        "After its all over":
            $ missallaway_path = 24
            $ missallaway_points = 8

    return
