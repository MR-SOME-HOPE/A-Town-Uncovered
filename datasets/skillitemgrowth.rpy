label lbl_skill_items:
    ## Wolf - CHA
    ## Owl - INT
    ## Rabbit - LUC
    ## Elk - STA
    ## Bear - STR

    ## +1 WOOD
    ## +2 BRONZE
    ## +3 SILVER
    ## +4 GOLD
    ## +5 METEOR

    ## Scarf - CHA
    ## Monocle - INT
    ## 4 Leaf Clover - LUC
    ## Sweatdrop - STA
    ## Heavy Weight Belt - STR

    ## +1 = $10
    ## +2 = $20
    ## +3 = $40
    ## +4 = $80
    ## +5 = $160
    if inventory.has_item(Items.skillitem1):
        $ skill_cha += 1
        $ skill_int += 1
        $ skill_luc += 1
        $ skill_sta += 1
        $ skill_str += 1
    elif inventory.has_item(Items.skillitem2):
        $ skill_cha += 2
        $ skill_int += 1
        $ skill_luc += 1
        $ skill_sta += 1
        $ skill_str += 1
    elif inventory.has_item(Items.skillitem3):
        $ skill_cha += 1
        $ skill_int += 2
        $ skill_luc += 1
        $ skill_sta += 1
        $ skill_str += 1
    elif inventory.has_item(Items.skillitem4):
        $ skill_cha += 1
        $ skill_int += 1
        $ skill_luc += 2
        $ skill_sta += 1
        $ skill_str += 1
    elif inventory.has_item(Items.skillitem5):
        $ skill_cha += 1
        $ skill_int += 1
        $ skill_luc += 1
        $ skill_sta += 2
        $ skill_str += 2
    elif inventory.has_item(Items.skillitem6):
        $ skill_cha += 3
        $ skill_int += 3
        $ skill_luc += 3
        $ skill_sta += 3
        $ skill_str += 3
    elif inventory.has_item(Items.skillitem7):
        $ skill_cha += 5
        $ skill_int += 3
        $ skill_luc += 5
        $ skill_sta += 3
        $ skill_str += 5
    elif inventory.has_item(Items.skillitem8):
        $ skill_cha += 3
        $ skill_int += 5
        $ skill_luc += 3
        $ skill_sta += 5
        $ skill_str += 5
    elif inventory.has_item(Items.skillitem9):
        $ skill_cha += 5
        $ skill_int += 5
        $ skill_luc += 3
        $ skill_sta += 5
        $ skill_str += 3
    elif inventory.has_item(Items.skillitem10):
        $ skill_cha += 5
        $ skill_int += 5
        $ skill_luc += 5
        $ skill_sta += 5
        $ skill_str += 5
    if skill_cha > skill_chamax:
        $ skill_cha = skill_chamax
    elif skill_cha >= 20:
        $ skill_cha = 20
    elif skill_cha <= 0:
        $ skill_cha = 0
    if skill_int > skill_intmax:
        $ skill_int = skill_intmax
    elif skill_int >= 20:
        $ skill_int = 20
    elif skill_int <= 0:
        $ skill_int = 0
    if skill_luc > skill_lucmax:
        $ skill_luc = skill_lucmax
    elif skill_luc >= 20:
        $ skill_luc = 20
    elif skill_luc <= 0:
        $ skill_luc = 0
    if skill_sta > skill_stamax:
        $ skill_sta = skill_stamax
    elif skill_sta >= 20:
        $ skill_sta = 20
    elif skill_sta <= 0:
        $ skill_sta = 0
    if skill_str > skill_strmax:
        $ skill_str = skill_strmax
    elif skill_str >= 20:
        $ skill_str = 20
    elif skill_str <= 0:
        $ skill_str = 0
    return
