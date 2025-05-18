label lbl_start_game_load_mainstory:
    "Where do you want to leave off from in the main story?"

    jump lbl_start_game_load_mainstory_1

label lbl_start_game_load_mainstory_1:
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

            $ gtime = 0

            jump lbl_mybedroom_day_setup

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

            jump lbl_mall_with_friends

        "NEXT":
            jump lbl_start_game_load_mainstory_2

label lbl_start_game_load_mainstory_2:
    menu:
        "An Awkward Dinner Situation":
            $ main_story = 85

            $ inventory.money = 1300
            $ skill_luc = 14
            $ skill_str = 14
            $ skill_sta = 14
            $ skill_int = 14
            $ skill_cha = 14
            $ skill_lucmax = 17
            $ skill_strmax = 17
            $ skill_stamax = 17
            $ skill_intmax = 17
            $ skill_chamax = 17

            jump lbl_an_awkward_dinner_situation

        "First Day At the Office":
            play music "audio/music/office_music.ogg"
            $ main_story = 90

            $ inventory.money = 1300
            $ skill_luc = 14
            $ skill_str = 14
            $ skill_sta = 14
            $ skill_int = 14
            $ skill_cha = 14
            $ skill_lucmax = 17
            $ skill_strmax = 17
            $ skill_stamax = 17
            $ skill_intmax = 17
            $ skill_chamax = 17

            jump lbl_prelude_of_the_first_day

        "First Shift at the Office":
            play music "audio/music/office_music.ogg"
            $ main_story = 96

            $ inventory.money = 1300
            $ skill_luc = 15
            $ skill_str = 15
            $ skill_sta = 15
            $ skill_int = 15
            $ skill_cha = 15
            $ skill_lucmax = 18
            $ skill_strmax = 18
            $ skill_stamax = 18
            $ skill_intmax = 18
            $ skill_chamax = 18

            jump lbl_our_first_shift

        "Daily Grind at the Office":
            play music "audio/music/office_music.ogg"
            $ main_story = 101

            $ inventory.money = 1300
            $ skill_luc = 15
            $ skill_str = 15
            $ skill_sta = 15
            $ skill_int = 15
            $ skill_cha = 15
            $ skill_lucmax = 18
            $ skill_strmax = 18
            $ skill_stamax = 18
            $ skill_intmax = 18
            $ skill_chamax = 18

            $ gtime = 0

            jump lbl_daily_grind_part1

        "Eloise Gives You a Tour":
            play music "audio/music/office_music.ogg"
            $ main_story = 104

            $ inventory.money = 1300
            $ skill_luc = 15
            $ skill_str = 15
            $ skill_sta = 15
            $ skill_int = 15
            $ skill_cha = 15
            $ skill_lucmax = 18
            $ skill_strmax = 18
            $ skill_stamax = 18
            $ skill_intmax = 18
            $ skill_chamax = 18

            $ gtime = 2

            jump lbl_meeting_with_eloise

        "Meeting Jacob and Effie Behind Rocks":
            $ main_story = 108

            $ inventory.money = 1300
            $ skill_luc = 15
            $ skill_str = 15
            $ skill_sta = 15
            $ skill_int = 15
            $ skill_cha = 15
            $ skill_lucmax = 18
            $ skill_strmax = 18
            $ skill_stamax = 18
            $ skill_intmax = 18
            $ skill_chamax = 18

            $ gtime = 2

            jump lbl_knockout_news

        "Discuss plans with team in Forest Safehouse":
            $ main_story = 113

            $ inventory.money = 1500
            $ skill_luc = 15
            $ skill_str = 15
            $ skill_sta = 15
            $ skill_int = 15
            $ skill_cha = 15
            $ skill_lucmax = 18
            $ skill_strmax = 18
            $ skill_stamax = 18
            $ skill_intmax = 18
            $ skill_chamax = 18

            $ gtime = 2


            jump lbl_friends_in_high_places

        "NEXT":
            jump lbl_start_game_load_mainstory_3

        "BACK":
            jump lbl_start_game_load_mainstory_1


label lbl_start_game_load_mainstory_3:
    menu:
        "Starting the Heist":
            $ main_story = 118

            $ inventory.money = 1500
            $ skill_luc = 15
            $ skill_str = 15
            $ skill_sta = 15
            $ skill_int = 15
            $ skill_cha = 15
            $ skill_lucmax = 18
            $ skill_strmax = 18
            $ skill_stamax = 18
            $ skill_intmax = 18
            $ skill_chamax = 18

            $ gtime = 1

            jump lbl_the_big_heist

        "Choose to Safrice Yourself or Effie":
            $ main_story = 121

            $ inventory.money = 1500
            $ skill_luc = 15
            $ skill_str = 15
            $ skill_sta = 15
            $ skill_int = 15
            $ skill_cha = 15
            $ skill_lucmax = 18
            $ skill_strmax = 18
            $ skill_stamax = 18
            $ skill_intmax = 18
            $ skill_chamax = 18

            $ gtime = 1

            jump lbl_the_big_heist

        "Ready To Head Into The Sexworld":
            $ main_story = 125

            $ inventory.money = 1500
            $ skill_luc = 15
            $ skill_str = 15
            $ skill_sta = 15
            $ skill_int = 15
            $ skill_cha = 15
            $ skill_lucmax = 18
            $ skill_strmax = 18
            $ skill_stamax = 18
            $ skill_intmax = 18
            $ skill_chamax = 18

            $ gtime = 0

            jump lbl_ready_to_go_again

        "BACK":
            jump lbl_start_game_load_mainstory_2

#         "Roam Around Freely in the Sexworld" if myversion_simplified >= 46:
#             $ main_story = 133

#             $ inventory.money = 1500
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 1

#             $ gtime = 0

#             jump lbl_mybedroom_day_setup

#         "Let the Ceremony Begin" if myversion_simplified >= 47:
#             $ main_story = 136

#             $ inventory.money = 1500
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 1

#             $ gtime = 2

#             jump lbl_let_the_ceremony_begin

#         "Back Home in the Real World" if myversion_simplified >= 47:
#             $ main_story = 140

#             $ inventory.money = 1500
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 0

#             $ gtime = 0

#             jump lbl_second_rescue_summarized_text

#         "Getting Detention" if myversion_simplified >= 47:
#             $ main_story = 143

#             $ inventory.money = 1500
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 0

#             $ gtime = 0

#             jump lbl_mixed_school_reputation

#         "NEXT":
#             jump lbl_start_game_load_mainstory_4

#         "BACK":
#             jump lbl_start_game_load_mainstory_2

# label lbl_start_game_load_mainstory_4:
#     menu:
#         "Followers of Master Buukakki Flyers" if myversion_simplified >= 47:
#             $ main_story = 146

#             $ inventory.money = 1800
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 0

#             $ gtime = 0

#             jump lbl_mall_day_setup

#         "Discussing Stolen Evidence" if myversion_simplified >= 47:
#             $ main_story = 149

#             $ inventory.money = 1800
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 0

#             $ gtime = 1

#             jump lbl_discussing_stolen_evidence

#         "Assign Roles for Operation" if myversion_simplified >= 47:
#             $ main_story = 153

#             $ inventory.money = 2000
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 0

#             $ gtime = 1

#             jump lbl_assign_roles_for_operation

#         "A Note At The Front Door" if myversion_simplified >= 47:
#             $ main_story = 156

#             $ inventory.money = 2000
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 0

#             $ gtime = 1

#             jump lbl_a_note_at_the_front_door

#         "Just put me in the world" if myversion_simplified >= 47:
#             $ main_story = 157

#             $ inventory.money = 2000
#             $ skill_luc = 15
#             $ skill_str = 15
#             $ skill_sta = 15
#             $ skill_int = 15
#             $ skill_cha = 15
#             $ skill_lucmax = 18
#             $ skill_strmax = 18
#             $ skill_stamax = 18
#             $ skill_intmax = 18
#             $ skill_chamax = 18

#             $ insexworld = 0

#             $ gtime = 1

        # # "NEXT":
        # #     jump lbl_start_game_load_mainstory_5

        # "BACK":
        #     jump lbl_start_game_load_mainstory_3
