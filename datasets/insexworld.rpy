label lbl_in_sex_world:
    if main_story <= 22:
        $ insexworld = 0
    elif 23 <= main_story <= 35:
        $ insexworld = 1
    elif main_story >= 36:
        $ insexworld = 0
