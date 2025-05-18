################################################################################
label lbl_previous_gamever_preset_public:
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

    "Where do you want to leave off from in the main story?"
    menu:
        "The Beginning":
            $ main_story = 2

            $ inventory.money = 50
            $ skill_luc = 0
            $ skill_str = 0
            $ skill_sta = 0
            $ skill_int = 0
            $ skill_cha = 0

        "Before going into the Sex World":
            $ main_story = 22

            $ inventory.money = 250
            $ skill_luc = 4
            $ skill_str = 4
            $ skill_sta = 4
            $ skill_int = 4
            $ skill_cha = 4
            $ skill_lucmax = 7
            $ skill_strmax = 7
            $ skill_stamax = 7
            $ skill_intmax = 7
            $ skill_chamax = 7

            "Note: Not all characters have been met and you need to talk to them first before going into the sexworld."

        "Arriving back from the Sex World":
            $ main_story = 36

            $ inventory.money = 500
            $ skill_luc = 7
            $ skill_str = 7
            $ skill_sta = 7
            $ skill_int = 7
            $ skill_cha = 7
            $ skill_lucmax = 10
            $ skill_strmax = 10
            $ skill_stamax = 10
            $ skill_intmax = 10
            $ skill_chamax = 10

            call lbl_setcharacterpathto1

            jump lbl_back_to_safety

        "Something is following you":
            $ main_story = 45.5

            $ inventory.money = 600
            $ skill_luc = 7
            $ skill_str = 7
            $ skill_sta = 7
            $ skill_int = 7
            $ skill_cha = 7
            $ skill_lucmax = 12
            $ skill_strmax = 12
            $ skill_stamax = 12
            $ skill_intmax = 12
            $ skill_chamax = 12

            call lbl_setcharacterpathto1

            jump lbl_something_is_following_you

        "Stumbling on the Crime Scene":
            $ main_story = 51

            $ inventory.money = 700
            $ skill_luc = 10
            $ skill_str = 10
            $ skill_sta = 10
            $ skill_int = 10
            $ skill_cha = 10
            $ skill_lucmax = 16
            $ skill_strmax = 16
            $ skill_stamax = 16
            $ skill_intmax = 16
            $ skill_chamax = 16

            call lbl_setcharacterpathto1

            jump lbl_mybedroom_day_setup

        "Finding a Trashed School":
            $ main_story = 58

            $ inventory.money = 1000
            $ skill_luc = 12
            $ skill_str = 12
            $ skill_sta = 12
            $ skill_int = 12
            $ skill_cha = 12
            $ skill_lucmax = 16
            $ skill_strmax = 16
            $ skill_stamax = 16
            $ skill_intmax = 16
            $ skill_chamax = 16

            call lbl_setcharacterpathto1

            jump lbl_mybedroom_day_setup

        "Morning of the Polaroid":
            $ main_story = 68

            $ inventory.money = 1000
            $ skill_luc = 12
            $ skill_str = 12
            $ skill_sta = 12
            $ skill_int = 12
            $ skill_cha = 12
            $ skill_lucmax = 16
            $ skill_strmax = 16
            $ skill_stamax = 16
            $ skill_intmax = 16
            $ skill_chamax = 16

            call lbl_setcharacterpathto1

            jump lbl_the_morning_headache

        "Mall with Friends":
            $ main_story = 76

            $ inventory.money = 1200
            $ skill_luc = 12
            $ skill_str = 12
            $ skill_sta = 12
            $ skill_int = 12
            $ skill_cha = 12
            $ skill_lucmax = 16
            $ skill_strmax = 16
            $ skill_stamax = 16
            $ skill_intmax = 16
            $ skill_chamax = 16

            call lbl_setcharacterpathto1

            jump lbl_mall_with_friends

    jump lbl_mybedroom_day_setup
